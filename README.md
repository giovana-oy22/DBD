# DBD
Repositório para implementação de um banco de dados para a disciplina de PCS3623

# 🚀 Projeto Django

Este é um projeto web desenvolvido com Django, utilizando banco de dados integrado e estrutura pronta para desenvolvimento em equipe.

---

## 📌 Tecnologias utilizadas

* Python 3
* Django
* SQLite (banco de dados padrão)
* Git e GitHub

---

## ⚙️ Como rodar o projeto

Siga os passos abaixo para rodar o projeto na sua máquina:

### 1. Clonar o repositório

```bash
git clone <link-do-repositorio>
cd <nome-do-repositorio>
```

---

### 2. Criar ambiente virtual

```bash
python3 -m venv venv
```

---

### 3. Ativar o ambiente virtual

* Linux / Mac:

```bash
source venv/bin/activate
```

* Windows:

```bash
venv\Scripts\activate
```

---

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 5. Aplicar migrations (criar banco de dados)

```bash
python manage.py migrate
```

---

### 6. Criar usuário administrador (opcional)

```bash
python manage.py createsuperuser
```

---

### 7. Rodar o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```
http://127.0.0.1:8000/
```

Painel admin:

```
http://127.0.0.1:8000/admin/
```

---

## 📂 Estrutura do projeto

```
├── config/        # Configurações do projeto
├── core/          # App principal
├── manage.py      # Gerenciador do Django
├── requirements.txt
```

---

## 🤝 Como contribuir

1. Crie uma branch:

```bash
git checkout -b minha-feature
```

2. Faça suas alterações e commit:

```bash
git commit -m "minha feature"
```

3. Envie para o GitHub:

```bash
git push origin minha-feature
```

4. Abra um Pull Request 🚀

---

## ⚠️ Observações

* O ambiente virtual (`venv/`) não está incluído no repositório
* O banco de dados é gerado automaticamente com `migrate`
* Não é necessário configurar banco manualmente

---

## 💡 Objetivo

Este projeto foi desenvolvido para aprendizado de backend com Django, integração com banco de dados e trabalho colaborativo com Git.

---