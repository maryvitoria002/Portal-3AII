# Setup do Portal 3AII

Este documento explica como configurar e executar o Portal da Turma 3AII.

## Estrutura do Projeto

```
portal_3aii/
├── manage.py                 # Script principal do Django
├── requirements.txt          # Dependências Python
├── .env                     # Configurações de ambiente
├── portal/                  # Configurações principais
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/                    # Apps do Django
│   ├── accounts/           # Sistema de usuários
│   ├── dashboard/          # Página principal
│   ├── notas/             # Sistema de notas
│   ├── agenda/            # Calendário e tarefas
│   ├── materiais/         # Biblioteca de materiais
│   ├── professores/       # Informações dos professores
│   └── campus/            # Vida no campus
├── templates/              # Templates HTML
├── static/                 # Arquivos estáticos (CSS, JS, imagens)
└── media/                  # Arquivos enviados pelos usuários
```

## Funcionalidades Implementadas

### 🏠 Dashboard
- Página inicial com resumo das atividades
- Mural de avisos e notícias
- Enquetes rápidas
- Cards com estatísticas
- Próximos eventos e tarefas pendentes

### 👥 Sistema de Usuários
- Cadastro e login
- Perfil personalizado
- Sistema de permissões (líder da turma)
- Fotos de perfil

### 📊 Notas e Avaliações
- Registro de notas por disciplina
- Simulador de média (normal, paralela, final)
- Calculadora "quanto falta pra passar"
- Gráficos de desempenho
- Histórico de avaliações

### 📅 Agenda e Tarefas
- Calendário unificado
- Sistema de tarefas (kanban style)
- Lembretes de prazos
- Eventos da turma
- Integração com disciplinas

### 📚 Materiais de Estudo
- Biblioteca de arquivos por professor
- Upload de PDFs, slides, links
- Sistema de busca
- Organização por disciplina
- Controle de acesso

### 👨‍🏫 Professores
- Diretório completo dos professores
- Informações de contato
- Horários de atendimento
- Métodos avaliativos
- Monitorias disponíveis

### 🏫 Vida no Campus
- Horário dinâmico das aulas
- Achados e perdidos
- Mapa do campus
- Eventos acadêmicos

## Pré-requisitos

1. **Python 3.8+**
2. **MySQL** (ou MariaDB)
3. **pip** (gerenciador de pacotes Python)

## Instalação

### 1. Configurar Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar Banco de Dados

1. Crie um banco MySQL chamado `portal_3aii`
2. Configure o arquivo `.env` com suas credenciais:

```env
DB_NAME=portal_3aii
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
```

### 4. Executar Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar Superusuário

```bash
python manage.py createsuperuser
```

### 6. Executar Servidor

```bash
python manage.py runserver
```

Acesse: http://localhost:8000

## Utilitários Acadêmicos Planejados

- **Gerador de referência ABNT**: Criar referências bibliográficas automaticamente
- **Conversor PDF→DOCX**: Converter documentos para edição
- **Compressor de PDF**: Reduzir tamanho de arquivos
- **Calculadora de médias avançada**: Simulações complexas
- **Gerador de horários**: Otimizar grade horária

## Tecnologias Utilizadas

### Backend
- **Django 4.2**: Framework web Python
- **MySQL**: Banco de dados
- **Pillow**: Processamento de imagens

### Frontend
- **Bootstrap 5**: Framework CSS responsivo
- **Font Awesome**: Ícones
- **Chart.js**: Gráficos interativos
- **JavaScript vanilla**: Funcionalidades dinâmicas

### Funcionalidades Extras
- **Sistema de notificações em tempo real**
- **API REST** para futuras integrações (mobile app)
- **Sistema de backup automático**
- **Logs de atividade dos usuários**

## Estrutura de Dados

### Principais Models

1. **User** (extends AbstractUser)
   - Informações pessoais
   - Matrícula, turma
   - Foto de perfil
   - Status de líder

2. **Disciplina**
   - Nome, código
   - Professor responsável
   - Carga horária
   - Cor para identificação

3. **Nota**
   - Relação com usuário e disciplina
   - Tipo de avaliação
   - Nota e peso
   - Data da avaliação

4. **Tarefa**
   - Título e descrição
   - Data de entrega
   - Status (pendente/concluída)
   - Prioridade

5. **Evento**
   - Título e descrição
   - Data e hora
   - Local
   - Tipo (prova, trabalho, evento)

6. **Material**
   - Arquivo ou link
   - Disciplina
   - Professor
   - Tags para busca

## Próximas Implementações

### Fase 2 - Integrações
- [ ] API do WhatsApp para lembretes
- [ ] Integração com Google Calendar
- [ ] Sistema de email automático
- [ ] Notificações push

### Fase 3 - Mobile
- [ ] App React Native
- [ ] Sincronização offline
- [ ] Câmera para scan de documentos

### Fase 4 - IA
- [ ] Chatbot para dúvidas
- [ ] Recomendação de materiais
- [ ] Análise de desempenho
- [ ] Previsão de notas

## Contribuições

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Suporte

Para dúvidas ou problemas:
- Crie uma issue no GitHub
- Entre em contato com as líderes da turma
- Documente bugs encontrados

## Licença

Este projeto é de uso interno da Turma 3AII.

---

**Desenvolvido com ❤️ para a Turma 3AII**

*"Tecnologia é para facilitar nossa vida como estudantes!"*