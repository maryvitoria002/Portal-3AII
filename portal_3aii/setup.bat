@echo off
echo ============================================
echo        PORTAL 3AII - SETUP AUTOMATICO
echo ============================================
echo.

echo [1/6] Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado! Instale Python 3.8+ primeiro.
    pause
    exit /b 1
)

echo.
echo [2/6] Criando ambiente virtual...
if exist venv (
    echo Ambiente virtual ja existe. Pulando...
) else (
    python -m venv venv
)

echo.
echo [3/6] Ativando ambiente virtual...
call venv\Scripts\activate

echo.
echo [4/6] Instalando dependencias...
pip install -r requirements.txt

echo.
echo [5/6] Configurando banco de dados...
echo IMPORTANTE: Configure o arquivo .env com suas credenciais do MySQL!
echo Exemplo:
echo DB_NAME=portal_3aii
echo DB_USER=root
echo DB_PASSWORD=sua_senha
echo.
pause

echo.
echo [6/6] Executando migracoes...
python manage.py makemigrations
python manage.py migrate

echo.
echo ============================================
echo            SETUP CONCLUIDO!
echo ============================================
echo.
echo Proximos passos:
echo 1. Configure o arquivo .env
echo 2. Execute: python manage.py createsuperuser
echo 3. Execute: python manage.py runserver
echo 4. Acesse: http://localhost:8000
echo.
pause