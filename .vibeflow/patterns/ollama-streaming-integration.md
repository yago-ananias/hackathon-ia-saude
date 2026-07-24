---
tags: [ollama, llm, streaming, api-integration]
modules: [app_hackathon.py]
applies_to: [services]
confidence: inferred
---
# Pattern: Integração com Ollama via Streaming

<!-- vibeflow:auto:start -->
## What
Toda chamada ao LLM local (Ollama) passa por um único consumidor de stream compartilhado,
com dois wrappers finos por endpoint (`/api/generate` para prompt único, `/api/chat` para
multi-turn) que devolvem sempre `(texto, metricas)`.

## Where
`app_hackathon.py`, funções `gerar_stream`, `chat_stream`, `_consumir_stream` (linhas 139-203).
Usado por todas as 8 abas do app.

## The Pattern

**Wrapper por tipo de chamada, montando o payload e delegando ao consumidor comum:**
```python
def gerar_stream(prompt: str, modelo: str, url_base: str, system: str = "",
                 temperatura: float = 0.7, placeholder=None, imagens: list = None):
    payload = {"model": modelo, "prompt": prompt, "stream": True,
               "options": {"temperature": temperatura}}
    if system:
        payload["system"] = system
    if imagens:
        payload["images"] = imagens
    return _consumir_stream(f"{url_base}/api/generate", payload, placeholder, "response")

def chat_stream(mensagens: list, modelo: str, url_base: str,
                temperatura: float = 0.7, placeholder=None):
    payload = {"model": modelo, "messages": mensagens, "stream": True,
               "options": {"temperature": temperatura}}
    return _consumir_stream(f"{url_base}/api/chat", payload, placeholder, "chat")
```

**Consumidor único do stream, com atualização incremental do placeholder da UI e tratamento
de erro específico por tipo de falha:**
```python
def _consumir_stream(endpoint: str, payload: dict, placeholder, modo: str):
    inicio = time.time()
    try:
        with requests.post(endpoint, json=payload, timeout=(10, 600), stream=True) as resp:
            if resp.status_code != 200:
                return f"❌ Erro HTTP {resp.status_code}: {resp.text}", ""
            texto = ""
            for linha in resp.iter_lines():
                if not linha:
                    continue
                chunk = json.loads(linha.decode("utf-8"))
                parte = chunk.get("message", {}).get("content", "") if modo == "chat" else chunk.get("response", "")
                texto += parte
                if placeholder is not None:
                    placeholder.markdown(texto + " ▌")
                if chunk.get("done"):
                    chunk_final = chunk
                    break
            ...
    except requests.exceptions.ConnectionError:
        return "❌ Nao foi possivel conectar ao Ollama...", ""
    except requests.exceptions.Timeout:
        return "⏱️ Timeout...", ""
```

**Detecção automática de modelos instalados, com fallback se Ollama estiver offline:**
```python
def listar_modelos(url_base: str):
    try:
        r = requests.get(f"{url_base}/api/tags", timeout=5)
        if r.status_code == 200:
            nomes = [m["name"] for m in r.json().get("models", [])]
            if nomes:
                return sorted(nomes, key=lambda n: (PREFERENCIA.index(n) if n in PREFERENCIA else len(PREFERENCIA), n))
    except Exception:
        pass
    return FALLBACK_MODELOS
```

## Rules
- Nunca chamar `requests.post` para Ollama diretamente de dentro de uma aba — sempre passar por
  `gerar_stream` (single-turn) ou `chat_stream` (multi-turn), que delegam a `_consumir_stream`.
- `_consumir_stream` sempre retorna a tupla `(texto: str, metricas: str)`, nunca lança exceção
  para o chamador — toda falha de rede vira uma string de erro amigável (`❌ ...`) já formatada
  para exibição direta no Streamlit.
- Timeout é sempre `(10, 600)` — 10s para conectar, 10min para o modelo responder (modelos
  locais em CPU podem ser lentos).
- Multimodal (imagens) é suportado só em `gerar_stream` via parâmetro opcional `imagens` (lista
  de base64) — `chat_stream` não aceita imagens.

## Examples from this codebase
File: app_hackathon.py:113-126 (`listar_modelos`)
File: app_hackathon.py:168-203 (`_consumir_stream`, consumidor único)
<!-- vibeflow:auto:end -->

## Anti-patterns (if found)
Nenhum encontrado.
