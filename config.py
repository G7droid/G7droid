# Token do seu bot
BOT_TOKEN = "6333722224:AAE7Yx5C8T1LR25afFG3uAuFi7-acuEvGYM"

# ID e Hash da API do Telegram. Este NÃO é o token do seu bot e não deve ser alterado.
API_ID = 28665962
API_HASH = "d4808928e6432422874dc99b2c89da0d"

# Bate-papo usado para registrar erros.
LOG_CHAT = -1001820588722

# Bate-papo usado para registrar ações do usuário (como comprar, presentear, etc).
ADMIN_CHAT = -1001820588722

#Quantas atualizações podem ser tratadas em paralelo.
#Não ouse valores altos para servidores de baixo custo.
WORKERS = 20

# Os administradores podem acessar o painel e adicionar novos materiais ao bot.
ADMINS = [5703174005]

# Os sudoers têm acesso total ao servidor e podem executar comandos.
SUDOERS = [5703174005]


# Todos os sudoers devem ser administradores também
ADMINS.extend(SUDOERS)

GIFTERS = []

