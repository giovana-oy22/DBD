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

### Primeira vez

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

### Outras vezes
Nas próximas vezes, como já tem bastante coisa configurada você só precisa fazer alguns passos:

1. Criar branch ou implementar algo em uma branch existente *Olhar tópico "Como contribuir"*
---
2. Ativar a venv novamente
* Linux / Mac:

```bash
source venv/bin/activate
```

* Windows:

```bash
venv\Scripts\activate
```
---
3. Fazer alterações no backend
- Adicionando uma nova tabela
mexer no core/models.py
mexer no core/admin.py

```bash
python manage.py makemigrations
python manage.py migrate
```
---
4. Rodar o servidor
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

1. Branches:
Criando uma branch

```bash
git checkout -b <nome_branch>
```
*Com esse comando você cria uma branch baseada na branch que você está atualmente, então cuidado*

Mudando de branch

```bash
git checkout <nome_branch>
```
Listando todas as branches

```bash
git branch 
```

2. Faça suas alterações e commit:

```bash
git add . (deixa pronto todos os arquivos que você mudou)
git add <nome_arquivo_que você quer dar commit> 
git commit -m "mensagem de commit"
```
*Esse passo dá pra fazer na área explorador também no ícone Controle de Código Fonte*

3. Envie para o GitHub:

- Primeira vez upando algo para a branch
```bash
git push -u origin minha-feature 
```
- Outras vezes:
```bash
git push 
```
4. Abra um Pull Request quando você quiser integrar sua branch com a main  🚀

5. Mantenha sempre o seu repositório local (o que tem   no seu computador) atualizado com o que tem no seu repositório remoto (site do github), para isso:

```bash
git pull
```
---

## ⚠️ Observações

* O ambiente virtual (`venv/`) não está incluído no repositório
* O banco de dados é gerado automaticamente com `migrate`
* Não é necessário configurar banco manualmente

---

## 💡 Objetivo

Este projeto foi desenvolvido para aprendizado de backend com Django, integração com banco de dados e trabalho colaborativo com Git.

---