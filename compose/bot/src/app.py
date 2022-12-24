import asyncio
from aiogram import Bot, Dispatcher, types
import config

bot = Bot(token=config.BOT_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    with open("images/arthas.jpg", 'rb') as photo:
        await bot.send_photo(message.chat.id, photo,
                             caption="Привет! Это я, твой единственный зритель. На протяжении многих лет я "
                                     "создавал иллюзию того, что тебя смотрят много людей. Но это был я. "
                                     "Сейчас напишу это сообщение со всех аккаунтов.")
    await message.reply("Отправь /help для просмотра доступных команд.")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я могу ответить на следующие команды: /joke1, /joke2, /joke3, /joke4")


@dp.message_handler(commands=["joke1"])
async def send_joke_1(message: types.Message):
    with open("images/joke1.png", 'rb') as photo:
        await bot.send_photo(message.chat.id, photo,
                             caption="У разных народов всегда были разные понятия о смерти. В древности, люди считали, "
                                     "что умирая, они попадают в такой же мир, при этом забирая с собой вещи из "
                                     "нашего. Позже, появились христиане, которые считают, что если ты живешь по "
                                     "Законам Божьим, то ты попадешь в рай, а иначе - а ад. Негры же, умирая, "
                                     "попадают в баскетбольное кольцо.")


@dp.message_handler(commands=["joke2"])
async def send_joke_2(message: types.Message):
    with open("images/joke2.jpg", 'rb') as photo:
        await bot.send_photo(message.chat.id, photo,
                             caption="Я не верю в эволюцию. Если бы это было правдой, "
                                     "то чёрные уже давно были бы пуленепробиваемыми.")


@dp.message_handler(commands=["joke3"])
async def send_joke_3(message: types.Message):
    with open("images/joke3.jpg", 'rb') as photo:
        await bot.send_photo(message.chat.id, photo,
                             caption="Шахматы придумал мудрец по имени Сисса, который показал своё изобретение "
                                     "правителю страны. Тому так понравилась игра, что он дал изобретателю право "
                                     "самому выбрать награду. Мудрец попросил у короля за первую клетку шахматной "
                                     "доски заплатить ему одно зерно пшеницы, за вторую — два, за третью — четыре "
                                     "и так далее, удваивая количество зёрен на каждой следующей клетке. Правитель "
                                     "ответил: \n— Да-а, что у тебя за имя такое дурацкое, Сисса?")


@dp.message_handler(commands=["joke4"])
async def send_joke_4(message: types.Message):
    with open("images/joke4.jpg", 'rb') as photo:
        await bot.send_photo(message.chat.id, photo,
                             caption="Колобка ведут на расстрел, он говорит: \n— Можно последнее желание? \n— Можно. "
                                     "\n— Не стреляйте в голову аххахаххахахах \nВ итоге колобка повесили")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
