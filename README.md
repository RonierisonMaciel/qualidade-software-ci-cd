# 📌 Projeto: Qualidade de Software com CI/CD e Versionamento

## 🎯 Objetivo
Este projeto tem como objetivo ensinar **Qualidade de Software** através de práticas reais de **CI/CD**, **Code Review (CR)** e **Pull Requests (PR)**, proporcionando uma experiência colaborativa utilizando **GitHub**. Os alunos terão contato com processos modernos de desenvolvimento de software, incluindo:

- **Boas práticas de versionamento de código**.
- **Revisão de Código (Code Review - CR)**.
- **Criação de Pull Requests (PRs)**.
- **Integração Contínua (CI) com testes automatizados**.
- **Entrega Contínua (CD) para publicação do software**.

---

## 🛠️ Estrutura do Projeto
O projeto consiste em uma API simples de **To-Do List** desenvolvida com **FastAPI** e testada com **pytest**.

📂 **Arquivos e Pastas:**
```
/app
  ├── main.py        # API principal
  ├── models.py      # Estruturas de dados (Pydantic)
  ├── database.py    # Simulação de um banco de dados (SQLite ou lista em memória)
  ├── services.py    # Lógica de negócio separada
/tests
  ├── test_main.py   # Testes unitários com pytest
  ├── test_api.py    # Testes de integração
.github/workflows
  ├── ci.yml         # Pipeline de CI/CD no GitHub Actions
```

---

## 🚀 Como Rodar o Projeto Localmente

### 🔧 1. Clonar o Repositório
```bash
git clone https://github.com/RonierisonMaciel/qualidade-software-ci-cd.git
cd qualidade-software-ci-cd
```

### 📦 2. Criar e Ativar um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 📥 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### ▶️ 4. Rodar a API
```bash
uvicorn app.main:app --reload
```
Acesse `http://127.0.0.1:8000/docs` para visualizar a documentação interativa do FastAPI.

---

## 🧪 Como Rodar os Testes

### ✅ 1. Rodar Todos os Testes
```bash
pytest
```

### 🔍 2. Rodar um Teste Específico
```bash
pytest tests/test_main.py
```

Se os testes passarem, a saída será semelhante a:
```
============================= test session starts =============================
collected 5 items

tests/test_main.py ....                                  [ 80%]
tests/test_api.py ..                                     [100%]

============================== 5 passed in 0.12s ==============================
```

---

## 🤝 Fluxo de Trabalho com GitHub

1. **Fork do repositório** → Clique em "Fork" no GitHub.
2. **Clonar para sua máquina** → `git clone <URL do seu fork>`.
3. **Criar uma nova branch** → `git checkout -b minha-melhoria`.
4. **Fazer alterações e commit** → `git commit -m "Adicionando melhorias"`.
5. **Enviar para seu fork** → `git push origin minha-melhoria`.
6. **Abrir um Pull Request** → No GitHub, clique em "Compare & Pull Request".
7. **Revisão de Código (CR)** → Os colegas revisam e sugerem melhorias.
8. **Merge na branch principal** → Após aprovação, o código é integrado.

---

## 🔥 CI/CD com GitHub Actions
- **Ao abrir um PR**, os **testes automatizados** serão executados automaticamente.
- Se os testes falharem, o PR **não poderá ser mesclado** até que seja corrigido.
- Caso a pipeline passe, o código poderá ser integrado na branch principal e eventualmente **implantado automaticamente**.

---

## 🎯 Desafios para os Alunos

- Corrigir **erros e bugs** propositais deixados no código.
- Melhorar **a estrutura do código** e otimizar funções.
- Escrever **novos testes unitários** para cobrir casos não testados.
- Participar de **Code Review**, analisando PRs de colegas e sugerindo melhorias.
