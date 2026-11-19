

# **The Marauder's Map Discord Bot**

> *I solemnly swear that I am up to no good.*
>
> Messrs. Moony, Wormtail, Padfoot, and Prongs  
> Purveyors of Aids to Magical Mischief-Makers  
> are proud to present...


 ---

Um bot para Discord inspirado no universo de Harry Potter, criado para trazer um pouco da atmosfera de Hogwarts para os servidores.

O bot utiliza personagens, professores e locais conhecidos da escola para gerar situações aleatórias! E quando digo aleatórias… SÃO ALEATÓRIAS MESMO! De repente, Dumbledore pode estar tentando manter a calma no meio do caos, enquanto Snape pode estar tomando um chá quente enquanto descansa! O céu é o limite!

## Funcionalidades

- `.alunos` — seleciona um aluno aleatório e gera uma situação em algum lugar de Hogwarts.
- `.professores` — escolhe um professor e descreve uma atividade aleatória.
- `.vacarosa` — acompanha as atividades suspeitas de Dolores Umbridge.
- `.users` — seleciona um membro aleatório do servidor e o coloca em uma situação.

## Tecnologias

- Python
- discord.py
- python-dotenv

## Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/vitoriariserio/Marauders_Map_Discord_Bot.git
cd Marauders_Map_Discord_Bot
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente:

**Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install discord.py python-dotenv
```

### 4. Configure o token

Crie um arquivo .env na raiz do projeto:

```
DISCORD_TOKEN=seu_token_aqui
```

O token pode ser obtido no [Discord Developer Portal](https://discord.com/developers/applications).

### 5. Execute o bot

```bash
python main.py
```

## Permissões e configurações

O bot utiliza intents específicas para acessar mensagens e membros dos servidores.

As seguintes opções precisam estar habilitadas no Discord Developer Portal:

- Server Members Intent
- Message Content Intent

As permissões necessárias para o funcionamento básico são:

- View Channels
- Send Messages
- Read Message History

## Segurança

- Os comandos possuem limite de utilização individual para evitar execuções excessivas.
- O token é armazenado em variável de ambiente.
- O arquivo .env não deve ser enviado ao repositório.



## Sobre o projeto

Este projeto foi desenvolvido como uma experiência prática de programação em Python e integração com a API do Discord.

A ideia é explorar comandos, eventos, tratamento de erros, seleção aleatória de dados e outras funcionalidades oferecidas pela biblioteca discord.py com algo que sou apaixonada: o universo de Harry Potter!

---
| Demonstração comando .professores | Demonstração comando .alunos |
|:---:|:---:|
| <img width="1458" height="683" alt="image" src="https://github.com/user-attachments/assets/59f4bc7e-b898-4dca-b1bf-6c3cf7dbbf63" /> |<img width="1591" height="698" alt="image" src="https://github.com/user-attachments/assets/0cb2fafe-9630-4691-b4aa-1cf1615ed4e1" />

---

## 🔒 | Disclaimer

Este é um projeto independente, desenvolvido por uma fã e inspirado no universo de Harry Potter, sem qualquer vínculo oficial com J.K. Rowling, Warner Bros. ou seus representantes.

Todos os personagens, nomes, lugares e demais elementos pertencentes ao universo de Harry Potter são de propriedade de seus respectivos titulares de direitos autorais e marcas registradas.

O projeto possui finalidade exclusivamente educacional e não comercial. Não há intenção de reivindicar propriedade sobre qualquer material original ou infringir direitos de terceiros.

---
> *Mischief managed.*

