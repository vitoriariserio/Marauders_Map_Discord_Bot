import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=".", intents=intents)

intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True

personages_alunos = [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasley",
    "Draco Malfoy",
    "Luna Lovegood",
    "Neville Longbottom",
    "Ginny Weasley",
    "Fred Weasley",
    "George Weasley",
    "Seamus Finnigan",
    "Dean Thomas",
    "Cho Chang",
    "Pansy Parkinson",
    "Gregory Goyle",
    "Vincent Crabbe",
    "Millicent Bulstrode",
    "Blaise Zabini",
    "Colin Creevey",
    "Dennis Creevey",
    "Lee Jordan",
    "Parvati Patil",
    "Padma Patil",
    "Lavender Brown",
    "Zacharias Smith",  
    "Terry Boot",
    "Anthony Goldstein",
    "Michael Corner",
    "Marietta Edgecombe",
    "Justin Finch-Fletchley",
    "Hannah Abbott",
    "Ernie Macmillan",
    "Susan Bones",
    "Hannah Abbott",
    "inigo Montague",
    "Alicia Spinnet",
    "Angelina Johnson",
    "Katie Bell",
    "Oliver Wood",
]

personages_professores = [
    "Alvo Dumbledore",
    "Minerva McGonagall",
    "Severus Snape",
    "Rubeus Hagrid",
    "Filius Flitwick",
    "Pomona Sprout",
    "Sybill Trelawney",
    "Gilderoy Lockhart",
    "Remus Lupin",
    "Horace Slughorn",]

umbridge = [
    "está medindo a distância entre as gravatas das pessoas",
    "está praticando o famoso 'hem, hem' no espelho",
    "está retocando o laço rosa bizarro na cabeça",
    "está assinando mais um decreto educacional inútil",
    "está espalhando fotos de pratos com gatinhos falantes",
    "está tossindo de forma absurdamente falsa",
    "foi vista(o) tentando espionar os alunos atrás de um vaso",
    "está fiscalizando a postura dos quadros nas paredes",
    "foi pego(a) tentando banir a alegria da escola",
    "está procurando feitiços de purpurina nas roupas",
    "está tentando adivinhar quem vai aprontar hoje",
    "está reclamando que o chá não tem açúcar suficiente",
    "foi visto(a) fugindo de rojões dos irmãos Weasley",
    "está tentando proibir conversas no corredor",
    "está babando no meio de um sermão moralista",
    "está anotando nomes em seu caderninho cor-de-rosa"
]


locais_hogwarts = [

    "nas masmorras - Sala de Poções",
    "nas masmorras - Escritório de Poções",
    "nas masmorras - Salão Comunal da Sonserina",
    "no subsolo - Cozinhas de Hogwarts",
    "no subsolo - Salão Comunal da Lufa-Lufa",
    "nas profundezas do castelo - Câmara dos Segredos",


    "no térreo - Saguão de Entrada",
    "no térreo - Grande Salão",
    "no térreo - Sala dos Professores",
    "no térreo - Escritório de Filch",
    "no térreo - Sala de Aula 11",


    "no andar 1 - Sala de Aula de História da Magia",
    "no andar 1 - Ala Hospitalar",


    "no andar 2 - Banheiro da Murta Que Geme",
    "no andar 2 - Escritório de Defesa Contra as Artes das Trevas",


    "no andar 3 - Corredor Proibido",
    "no andar 3 - Sala de Troféus",
    "no andar 3 - Sala de Aula de Feitiços",
    "no andar 3 - Galeria de Armaduras",
    "no andar 3 - Estátua da Bruxa de Um Olho Só",


    "no andar 4 - Biblioteca de Hogwarts",
    "no andar 4 - Seção Restrita da Biblioteca",


    "no andar 5 - Banheiro dos Monitores",


    "no andar 6 - Banheiro Masculino",
    "no andar 6 - Corredor de Glanmore Peakes",


    "no andar 7 - Sala Precisa",
    "no andar 7 - Salão Comunal da Grifinória",
    "no andar 7 - Corredor da Mulher Gorda",
    "no andar 7 - Escritório de Flitwick",


    "na Torre da Corvinal - Salão Comunal da Corvinal",
    "na Torre Norte - Sala de Aula de Divinação",
    "na Torre Norte - Escritório de Divinação",
    "na Torre de Astronomia - Ponto Mais Alto do Castelo",
    "na Torre Oeste - Corujal",
    "na torre do diretor - Escritório do Diretor",


    "nos terrenos - Cabana do Hagrid",
    "nos terrenos - Horta de Abóboras",
    "nos terrenos - Estufas de Herbologia",
    "nos terrenos - Campo de Quadribol",
    "nos terrenos - Lago Negro",
    "nos terrenos - Salgueiro Lutador",
    "nos terrenos - Círculo de Pedras",
    "nos terrenos - Hangar das Barcas",
    "nos terrenos - Entrada da Floresta Proibida",
    "nos terrenos - Floresta Proibida",


    "na passagem secreta - Estátua da Bruxa de Um Olho Só para o Dedos de Mel",
    "na passagem secreta - Raízes do Salgueiro Lutador para a Casa dos Gritos",
    "na passagem secreta - Quadro de Ariana Dumbledore para o Cabeça de Javali",


    "em Hogwarts - Escritório do Diretor",
    "em Hogwarts - Sala de Estudos dos Trouxas",
    "em Hogwarts - Sala de Aula de Aritmancia",
    "em Hogwarts - Sala de Aula de Runas Antigas",
    "em Hogwarts - Corredores do Castelo",
    "em Hogwarts - Escadarias Móveis",
]


acoes = [
    "está atualmente",
    "foi visto(a) caminhando por",
    "foi avistado(a) de bobeira em",
    "encontra-se",
    "está rondando",
    "foi visto(a) rindo sozinho(a)",
    "está tramando algo suspeito",
    "sussurra feitiços misteriosos",
    "está escondido(a)",
    "apareceu de repente",
    "corre apressado(a) para",
    "está descansando",
    "está estudando furtivamente"
]

acoes_professores = [
    "está corrigindo uma pilha gigantesca de pergaminhos",
    "está preparando o material para a próxima aula",
    "está demonstrando um feitiço complexo",
    "está tirando dúvidas de um aluno dedicado",
    "está aplicando uma prova surpresa sem dó",
    "está patrulhando os corredores em busca de alunos fora da cama",
    "está tirando pontos de uma casa por má conduta",
    "está aplicando uma detenção bem merecida",
    "está confiscando um objeto contrabandearia da Zonko's",
    "está encarando com um olhar feio quem passa conversando",
    "está tomando um chá quente enquanto descança",
    "está procurando o diretor para um assunto urgente",
    "está murmurando reclamações sobre a conduta dos alunos",
    "está tentando manter a calma no meio do caos"
]

@commands.cooldown(3,10, commands.BucketType.user)
@bot.command()
async def alunos(ctx: commands.Context):
    local = random.choice(locais_hogwarts)
    acao = random.choice(acoes)
    aluno = random.choice(personages_alunos)

    await ctx.reply(f"{aluno} {acao} {local}")


@commands.cooldown(3,10, commands.BucketType.user)
@bot.command()
async def vacarosa(ctx: commands.Context):
    local = random.choice(locais_hogwarts)
    acao = random.choice(umbridge)

    await ctx.reply(f"Umbridge {acao} {local}")


@commands.cooldown(3,10, commands.BucketType.user)
@bot.command()
async def professores(ctx: commands.Context):
    local = random.choice(locais_hogwarts)
    acao = random.choice(acoes_professores)
    professor = random.choice(personages_professores)


    await ctx.reply(f"{professor} {acao} {local}")

@commands.cooldown(3,10, commands.BucketType.user)
@bot.command()
async def users(ctx: commands.context, mention_author: bool = True):
    membros = [m for m in ctx.guild.members if not m.bot]
    membro = random.choice(membros)
    await ctx.reply(f"{membro.mention} {random.choice(acoes)} {random.choice(locais_hogwarts)}")
    if not membros:
        await ctx.reply("Não encontrei membros disponíveis.")
        return


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.reply(f'Aguarde {error.retry_after:.1f} segundos antes de tentar novamente.')


load_dotenv()
api_key = os.getenv("DISCORD_TOKEN")
bot.run(api_key)
if not api_key:
    raise ValueError ("Token do discord não encontrado!")