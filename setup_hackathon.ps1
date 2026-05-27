# =============================================================================
# SETUP HACKATHON IA + SAUDE DIGITAL
# Instala Ollama + Gemma e dependencias Python para o hackathon
# =============================================================================

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  SETUP HACKATHON IA + SAUDE DIGITAL" -ForegroundColor Cyan
Write-Host "  Teleconsulta Eletiva x Teleinterconsulta" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# --- 1. Verificar Python ---
Write-Host "[1/5] Verificando Python..." -ForegroundColor Yellow
$pythonPath = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $pythonPath) {
    Write-Host "ERRO: Python nao encontrado. Instale em https://python.org" -ForegroundColor Red
    exit 1
}
$pythonVersion = python --version
Write-Host "OK: $pythonVersion em $pythonPath" -ForegroundColor Green

# --- 2. Instalar dependencias Python ---
Write-Host ""
Write-Host "[2/5] Instalando dependencias Python..." -ForegroundColor Yellow
pip install streamlit requests --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Host "OK: streamlit e requests instalados" -ForegroundColor Green
} else {
    Write-Host "ERRO ao instalar dependencias" -ForegroundColor Red
    exit 1
}

# --- 3. Verificar/Instalar Ollama ---
Write-Host ""
Write-Host "[3/5] Verificando Ollama..." -ForegroundColor Yellow
$ollamaPath = (Get-Command ollama -ErrorAction SilentlyContinue).Source
if (-not $ollamaPath) {
    Write-Host "Ollama nao encontrado. Baixando instalador..." -ForegroundColor Yellow
    Write-Host ""
    Write-Host ">>> Abra o link abaixo e instale o Ollama manualmente:" -ForegroundColor Cyan
    Write-Host "    https://ollama.com/download/windows" -ForegroundColor White
    Write-Host ""
    Write-Host "Apos instalar, feche e reabra este terminal e execute o script novamente." -ForegroundColor Yellow
    exit 0
} else {
    Write-Host "OK: Ollama encontrado em $ollamaPath" -ForegroundColor Green
}

# --- 4. Baixar modelos ---
Write-Host ""
Write-Host "[4/5] Baixando modelos para o hackathon..." -ForegroundColor Yellow
Write-Host "Total aproximado: 10 GB. Pode demorar 10-20 min na 1a vez." -ForegroundColor Gray
Write-Host ""

Write-Host "  - MedGemma 4B (3.3 GB) - especializado em saude..." -ForegroundColor Cyan
ollama pull medgemma:4b
if ($LASTEXITCODE -eq 0) { Write-Host "    OK: medgemma:4b pronto" -ForegroundColor Green }

Write-Host "  - Gemma 4 E2B (7.2 GB) - modelo mais recente..." -ForegroundColor Cyan
ollama pull gemma4:e2b
if ($LASTEXITCODE -eq 0) { Write-Host "    OK: gemma4:e2b pronto" -ForegroundColor Green }

# --- 5. Testar modelo ---
Write-Host ""
Write-Host "[5/5] Testando MedGemma..." -ForegroundColor Yellow
$teste = "Responda em portugues: O que e teleconsulta? (maximo 2 frases)"
$resultado = ollama run medgemma:4b $teste 2>$null
if ($resultado) {
    Write-Host "OK: Modelo respondendo!" -ForegroundColor Green
    Write-Host "Resposta de teste: $resultado" -ForegroundColor Gray
} else {
    Write-Host "AVISO: Modelo nao respondeu no teste, mas pode estar OK. Tente rodar o app." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "  SETUP CONCLUIDO!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Para iniciar o app do hackathon, execute:" -ForegroundColor Cyan
Write-Host "  streamlit run app_hackathon.py" -ForegroundColor White
Write-Host ""
Write-Host "Acesse no navegador: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
