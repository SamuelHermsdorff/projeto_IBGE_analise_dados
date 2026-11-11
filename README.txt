# 📊 Análise de Dados do IBGE com Python

Projeto desenvolvido com foco em Ciência e Análise de Dados utilizando **Python**, consumo da **API pública do IBGE** e uma interface web desenvolvida com **HTML, CSS e JavaScript**.

A aplicação coleta, trata e analisa dados dos municípios brasileiros e apresenta os resultados através de um **dashboard com indicadores, gráficos e tabela**.

O projeto foi desenvolvido com uma estrutura simples, organizada e de complexidade intermediária, priorizando boas práticas e clareza no código.

---

## 🎯 Objetivo

Demonstrar conhecimentos práticos em:

- Python;
- Pandas;
- Consumo de APIs;
- Tratamento e análise de dados;
- HTML;
- CSS;
- JavaScript;
- Desenvolvimento de interfaces web;
- Git e GitHub.

---

## 🛠️ Tecnologias utilizadas

### Backend

- Python
- Pandas
- Requests
- API pública do IBGE

### Frontend

- HTML5
- CSS3
- JavaScript
- Chart.js

### Controle de versão

- Git
- GitHub

---

## 🔄 Funcionamento

O funcionamento do projeto segue o seguinte fluxo:

```text
API pública do IBGE
        ↓
Coleta dos dados
        ↓
Tratamento com Python e Pandas
        ↓
Análise dos dados
        ↓
Geração do JSON
        ↓
JavaScript
        ↓
Dashboard Web

Sprint 1 — Estrutura inicial ✅

A primeira Sprint foi responsável pela criação da base do projeto.

Implementado
Estrutura inicial de pastas;
Organização do backend e frontend;
Página de apresentação;
Página da aplicação;
Estrutura inicial do HTML;
Estilização inicial com CSS;
Configuração do ambiente para desenvolvimento.

Sprint 2 — Consumo e análise dos dados do IBGE ✅

A Sprint 2 foi dedicada ao desenvolvimento do backend em Python.

Implementado
Configuração do ambiente Python;
Instalação das dependências;
Comunicação com a API pública do IBGE;
Coleta dos dados dos municípios;
Tratamento dos dados utilizando Pandas;
Tratamento de valores ausentes;
Organização dos dados;
Criação das análises;
Geração dos indicadores;
Exportação dos resultados para JSON.
Indicadores gerados
Total de municípios;
Municípios por estado;
Municípios por região;
Estado com maior quantidade de municípios;
Estado com menor quantidade de municípios.

Os resultados são exportados para:

dados/dados_ibge.json

Sprint 3 — Dashboard Web ✅

A Sprint 3 teve como objetivo conectar os dados do backend ao frontend.

Implementado
Dashboard responsivo;
Integração do JavaScript com o JSON;
Cards de indicadores;
Gráfico de municípios por estado;
Gráfico de municípios por região;
Tabela de municípios por estado;
Integração com Chart.js;
Testes de carregamento dos dados;
Correção da estrutura necessária para execução local.

O dashboard passou a consumir diretamente:

dados/dados_ibge.json

Sprint 4 — Finalização e apresentação ✅

A Sprint 4 é a etapa de finalização do projeto.

Etapa 1 — Melhoria visual da apresentação ✅

A página inicial (index.html) recebeu uma reformulação visual.

Foram aplicados:

Novo design;
Fundo moderno;
Seções de apresentação;
Cards;
Destaque das tecnologias;
Informações sobre o projeto;
Animações e transições;
Responsividade;
Melhor organização visual.

A página de apresentação passou a ter uma identidade visual mais próxima de um projeto profissional de portfólio.

Etapa 2 — revisão publicação ✅


💻 Como executar
1. Criar o ambiente virtual
python -m venv venv
2. Ativar o ambiente
.\venv\Scripts\Activate.ps1
3. Instalar as dependências
pip install -r backend/requirements.txt
4. Gerar os dados
python backend/main.py

Isso irá:

Consultar IBGE
      ↓
Tratar dados
      ↓
Gerar análises
      ↓
Exportar JSON

O arquivo será gerado em:

dados/dados_ibge.json
🌐 Executar o projeto localmente

Como o JavaScript utiliza fetch() para carregar o JSON, é necessário utilizar um servidor HTTP.

Na raiz do projeto:

python -m http.server 8000

Depois acesse:

http://localhost:8000/frontend/index.html

A página de apresentação poderá direcionar o usuário para a aplicação principal.

📌 Status do projeto
Sprint	Status
Sprint 1	✅ Concluída
Sprint 2	✅ Concluída
Sprint 3	✅ Concluída
Sprint 4	✅ Concluída