import telepot
minha_chave = "6281805284:AAH67xKOcyYk07VdNV-BapvT1aO68I09k3o"
bot = telepot.Bot(minha_chave)
print(bot.getUpdates())
print(bot.sendMessage(6013892149, 'olá'))
print(bot.getUpdates())

