# DBD
Repositório para implementação do Banco de Dados Relacional PostgreSQL para a disciplina de PCS3623

### Baixando o PostgreSQL
Acesse [PostgreSQL Download](https://www.postgresql.org/download/) e baixe a versão adequada ao seu computador.
Após execução do arquivo .exe, prossiga com as instruções e defina sua **senha** - guarde bem que ela será pedida depois!
Instale tudo que ele pedir e, ao final, ele provavelmente pedirá para você instalar o *Stack Builder*, mas ele lida com coisas mais avançadas que não precisaremos para esse trabalho, então pode cancelar o que ele pede para selecionar de instalação nesse passo.
Depois disso, tá tudo certo, só procurar por *pgAdmin 4* e voilá.


### pgAdmin 4
Abrindo ele, você vai se deparar com o menu da esquerda (Object Explorer) e nele temos o Servers. Clique no Servers e conecte-se, ele vai pedir a senha criada por você lá no início.
Agora é só aprender a como criar tabelas, inserir dados nelas e fazer consultas. Lembrem das aulas de BD ou consultem os universItArios


## Como você fará as coisas no seu computador
Passo a passo no seu computador:
- Abrir pgAdmin;
- Criar um banco novo: Create --> Database (Object Explorer);
- Abre QueryTool (Clicar com botão direito no Database criado);
- Clicar em Open File ou Ctrl+O ou icone de pastinha;
- Seleciona o arquivo .sql que está na branch;
- Clica na setinha pra dar o run (Execute Script).

A partir daqui, você vai fazer tudo dentro dessa aba do Query Tool. Depois que você escrever algo e der run, ele automaticamente já roda seus comandos, então já pode apagar o que você tinha escrito e escrever as coisas novas (se você não apagar, ele dá erro pq as coisas já foram criadas e executadas, a menos que seja um comando de consulta).

Então galera, eu gosto de fazer o desenvolvimento dos trabalhos por aqui em branches e ai quando tiver td certo, mergear na main.
Não esquecer de dar git pull sempre e de fazer os commits para o coleguinha ter o trabalho att.
É isso, bjs
