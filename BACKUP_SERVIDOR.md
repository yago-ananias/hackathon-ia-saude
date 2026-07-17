# 🛟 Guia do Servidor Backup

> **Para:** Yago (organizador)
> **Quando usar:** Como backup no dia do hackathon, caso participantes não consigam rodar local
> **Como funciona:** Sua máquina roda Ollama + Streamlit, exposta via Cloudflare Tunnel com URL pública

---

## 🎯 O Que Você Vai Construir

```
┌─────────────────────────────────┐
│  SUA MÁQUINA (Dell Latitude)    │
│  - Ollama (porta 11434)         │
│  - Streamlit (porta 8501)       │
│  - 2 modelos (MedGemma + Gemma4)│
└─────────────┬───────────────────┘
              │ Cloudflare Tunnel
              ▼
   ┌────────────────────────────┐
   │ https://[sub].trycloudflare.com │
   └─────────────┬──────────────┘
                 │
        Participantes acessam
        de qualquer navegador
```

---

## ⚠️ Sobre Limitações

**Capacidade da sua Dell Latitude 5450 (15 GB RAM):**
- Suporta **5-10 usuários simultâneos** sem virar fila
- Cada requisição leva ~10-30s
- Com 40 pessoas ao mesmo tempo, vira fila de minutos

**Por isso este é BACKUP, não solução principal.**
Funciona bem para 1-5 pessoas que tiveram problema no setup local.

---

## 🚀 Setup do Servidor Backup

### Pré-requisitos (já feitos)
- ✅ Ollama instalado
- ✅ MedGemma 4B e Gemma 4 E4B QAT baixados
- ✅ Streamlit funcionando em localhost:8501

### Passo 1: Instalar Cloudflared (5 min)

Cloudflared cria um túnel seguro entre sua máquina e uma URL pública.

**Windows (PowerShell como Administrador):**
```powershell
winget install --id Cloudflare.cloudflared
```

Se não tiver winget, baixe manualmente:
👉 https://github.com/cloudflare/cloudflared/releases/latest
Procure por `cloudflared-windows-amd64.exe`, renomeie para `cloudflared.exe` e coloque em uma pasta no PATH.

**Verificar:**
```powershell
cloudflared --version
```

---

### Passo 2: Subir o app Streamlit (na manhã do hackathon)

Abra **2 terminais**:

**Terminal 1 — Streamlit:**
```powershell
cd C:\Users\yagoa\hackathon-ia-saude
streamlit run app_hackathon.py --server.address 0.0.0.0
```

**Terminal 2 — Cloudflare Tunnel:**
```powershell
cloudflared tunnel --url http://localhost:8501
```

Após alguns segundos, vai aparecer algo como:
```
+--------------------------------------------------------------------------------------------+
|  Your quick Tunnel has been created! Visit it at:                                          |
|  https://xyz-abc-def.trycloudflare.com                                                     |
+--------------------------------------------------------------------------------------------+
```

**⭐ Essa URL é o que você compartilha com os participantes que precisarem.**

---

### Passo 3: Testar antes do hackathon

1. Copie a URL gerada
2. Abra no **celular** (saia do Wi-Fi para garantir que funciona externamente)
3. Deve abrir a interface do hackathon
4. Teste um prompt
5. Confirme que funciona

---

## 🆘 Como Usar Durante o Hackathon

### Cenário: alguém não consegue rodar Ollama local

**Você diz:**
> "Sem problema, usa o servidor backup. Abre esse link no navegador: [URL]"

**Participante:**
- Abre URL no Chrome/Edge/Firefox
- Usa o app normalmente
- **Não precisa instalar nada**

### Cenário: vários estão com problema (>5 pessoas)

**Você diz:**
> "Pessoal, quem está com problema técnico: usem o servidor backup. URL: [URL]"

**Atenção:** se mais de 10 pessoas migrarem ao mesmo tempo, vai ficar lento. Tente resolver setup local primeiro para alguns.

---

## 🔒 Sobre Segurança

- A URL do Cloudflare Tunnel é **temporária** (sumirá quando você parar o tunnel)
- Qualquer pessoa com a URL pode acessar (não exponha em redes sociais)
- Os prompts dos participantes passam pela sua máquina
- Para o hackathon (sem dados reais de paciente), o risco é baixo

**Não é adequado para produção** — só para o evento.

---

## 🛑 Como Parar o Servidor

Após o hackathon:

**Terminal do Streamlit:** `Ctrl+C`
**Terminal do Cloudflared:** `Ctrl+C`

Pronto. A URL vai expirar automaticamente.

---

## 🧪 Comando Único (atalho)

Salve este script como `iniciar_backup.ps1` para subir tudo de uma vez:

```powershell
# iniciar_backup.ps1
Write-Host "Iniciando servidor backup do hackathon..." -ForegroundColor Cyan

# Verificar Ollama
$env:Path = "$env:LOCALAPPDATA\Programs\Ollama;" + $env:Path
ollama list | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERRO: Ollama nao esta rodando" -ForegroundColor Red
    exit 1
}

# Subir Streamlit em background
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd C:\Users\yagoa\hackathon-ia-saude; streamlit run app_hackathon.py --server.address 0.0.0.0"

# Aguardar 5 segundos para Streamlit subir
Start-Sleep -Seconds 5

# Subir tunnel
Write-Host ""
Write-Host "Aguarde a URL aparecer abaixo:" -ForegroundColor Yellow
Write-Host ""
cloudflared tunnel --url http://localhost:8501
```

Para usar:
```powershell
powershell -ExecutionPolicy Bypass -File iniciar_backup.ps1
```

---

## 📋 Checklist do Dia

- [ ] Cloudflared instalado e testado (D-2)
- [ ] Script `iniciar_backup.ps1` testado (D-1)
- [ ] URL backup testada em celular fora do Wi-Fi local (D-1)
- [ ] **No dia (1h antes):** Subir servidor backup
- [ ] **No dia (30min antes):** Confirmar URL ainda funciona
- [ ] **No dia:** URL anotada e pronta para compartilhar
- [ ] **No fim:** Parar servidor (Ctrl+C nos terminais)

---

## 🆘 Troubleshooting Backup

### "cloudflared: command not found"
- Feche e reabra PowerShell após instalar

### URL gerada não abre no celular
- Aguarde 30 segundos após gerar
- Confirme que o Streamlit está rodando (Terminal 1)
- Verifique firewall do Windows (pode pedir permissão)

### Streamlit pede para confirmar email
- Use `streamlit run app_hackathon.py --server.address 0.0.0.0 --server.headless true`

### Modelo muito lento via tunnel
- É esperado (latência adicional do Cloudflare)
- Recomende usar MedGemma 4B (mais rápido) para usuários remotos

---

*Backup tranquilo é hackathon tranquilo. Suba o tunnel logo cedo.*
