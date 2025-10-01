# COMANDOS ÚTEIS - PORTAL 3AII
# Copie e cole estes comandos no terminal

# ============================================
# CONFIGURAÇÃO INICIAL (Execute uma vez)
# ============================================

# 1. Criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar banco de dados (após configurar .env)
python manage.py makemigrations
python manage.py migrate

# 4. Criar superusuário
python manage.py createsuperuser

# 5. Executar servidor
python manage.py runserver

# ============================================
# COMANDOS COTIDIANOS
# ============================================

# Ativar ambiente virtual (sempre que abrir o terminal)
venv\Scripts\activate

# Executar servidor de desenvolvimento
python manage.py runserver

# Criar nova migração após alterar models
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Acessar shell do Django
python manage.py shell

# Coletar arquivos estáticos (para produção)
python manage.py collectstatic

# ============================================
# COMANDOS DE DESENVOLVIMENTO
# ============================================

# Criar nova app
python manage.py startapp nome_da_app

# Executar testes
python manage.py test

# Limpar cache
python manage.py clearcache

# Gerar dados de exemplo (se existir fixture)
python manage.py loaddata inicial_data.json

# Fazer backup do banco
python manage.py dumpdata > backup.json

# ============================================
# COMANDOS DE PRODUÇÃO
# ============================================

# Instalar dependências de produção
pip install gunicorn

# Executar com Gunicorn
gunicorn portal.wsgi:application

# Configurar variáveis de ambiente para produção
set DEBUG=False
set ALLOWED_HOSTS=seudominio.com,www.seudominio.com

# ============================================
# COMANDOS DE MANUTENÇÃO
# ============================================

# Ver logs do Django
python manage.py runserver --verbosity=2

# Verificar problemas no projeto
python manage.py check

# Mostrar migrações aplicadas
python manage.py showmigrations

# Reverter migração específica
python manage.py migrate app_name 0001 --fake

# ============================================
# COMANDOS MYSQL (Se precisar)
# ============================================

# Conectar ao MySQL
mysql -u root -p

# Criar banco
CREATE DATABASE portal_3aii CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Criar usuário
CREATE USER 'portal_user'@'localhost' IDENTIFIED BY 'sua_senha';
GRANT ALL PRIVILEGES ON portal_3aii.* TO 'portal_user'@'localhost';
FLUSH PRIVILEGES;

# ============================================
# COMANDOS GIT (Para controle de versão)
# ============================================

# Inicializar repositório
git init

# Adicionar arquivos
git add .

# Fazer commit
git commit -m "Implementação inicial do Portal 3AII"

# Conectar com repositório remoto
git remote add origin https://github.com/seuusuario/portal-3aii.git

# Enviar para GitHub
git push -u origin main

# ============================================
# ESTRUTURA DE PASTAS FINAL
# ============================================

portal_3aii/
├── manage.py
├── requirements.txt
├── .env
├── README.md
├── setup.bat
├── demo.html
├── portal/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── __init__.py
│   ├── accounts/
│   ├── dashboard/
│   ├── notas/
│   ├── agenda/
│   ├── materiais/
│   ├── professores/
│   └── campus/
├── templates/
│   ├── base.html
│   ├── accounts/
│   └── dashboard/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── media/

# ============================================
# PROXIMOS PASSOS SUGERIDOS
# ============================================

# 1. Personalizar o arquivo .env com suas configurações
# 2. Executar as migrações
# 3. Criar alguns usuários de teste
# 4. Adicionar disciplinas e professores via admin
# 5. Testar todas as funcionalidades
# 6. Coletar feedback da turma
# 7. Implementar melhorias baseadas no feedback
# 8. Configurar backup automático
# 9. Preparar para deploy em servidor (se necessário)
# 10. Documentar processo para outros desenvolvedores

# ============================================
# DICAS DE SEGURANÇA
# ============================================

# - Nunca commitar o arquivo .env
# - Usar senhas fortes para usuários
# - Manter Django sempre atualizado
# - Configurar HTTPS em produção
# - Fazer backups regulares do banco
# - Monitorar logs de erro
# - Validar todos os inputs de usuário
# - Usar CSRF tokens em formulários

# ============================================
# CONTATOS PARA SUPORTE
# ============================================

# Líderes da Turma 3AII
# GitHub: [adicionar links dos repositórios]
# Email: [adicionar emails de contato]

# Documentação Django: https://docs.djangoproject.com/
# Documentação Bootstrap: https://getbootstrap.com/docs/