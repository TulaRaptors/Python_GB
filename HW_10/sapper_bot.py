import asyncio, logging, uuid
from random import randrange
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.WARNING)

bot = Bot("5984285484:AAHfYQUG3Ff2kBlNKqiQmK9jYNvPeD6ysOQ")
dp = Dispatcher(bot=bot)

games = {}

size_field = 4
mines_count = 2

unknown_no_miness = 0
unknown_miness = -1
known_no_mines = 1
known_mines = -2

ICONS = {
    unknown_no_miness: '?',
    unknown_miness: '?',
    known_no_mines: ' ',
    known_mines: '💥'}


def hasUnknownEmptyFields(minefield):
    for item in minefield:
        if item == unknown_no_miness:
            return True
    return False


def expose(minefield):
    for i in range(len(minefield)):
        if minefield[i] == unknown_no_miness:
            minefield[i] = known_no_mines
        elif minefield[i] == unknown_miness:
            minefield[i] = known_mines
    return minefield


async def render(chat_id, original_message=None):
    markup = types.InlineKeyboardMarkup()
    pos = 0

    for i in range(size_field):
        row = []
        for j in range(size_field):
            icon = ICONS[games[chat_id]['minefield'][pos]]
            row.append(types.InlineKeyboardButton(icon, callback_data=f'{pos}|{games[chat_id]["uuid"]}'))
            pos += 1
        markup.row(*row)

    if original_message:
        await original_message.edit_reply_markup(markup)
    else:
        await bot.send_message(chat_id, "Минное поле:", reply_markup=markup)


@dp.message_handler(commands=['start'])
async def handler(message: types.Message):
    user_name = message.from_user.first_name
    await message.reply(f"Привет, {user_name}!")
    await message.reply(f"Сапёр ошибается дважды!\n"
                        f"Одну ошибку ты уже совершил...")

    minefield = [unknown_no_miness] * (size_field ** 2)
    mines_count_left = mines_count

    assert mines_count_left <= size_field ** 2

    while mines_count_left > 0:
        r = randrange(size_field ** 2)
        if minefield[r] == 0:
            minefield[r] = unknown_miness
            mines_count_left -= 1

    chat_id = message.chat.id
    games[chat_id] = {
        'is_over': False,
        'uuid': str(uuid.uuid4()),
        'minefield': minefield
    }

    await render(chat_id, original_message=None)


@dp.callback_query_handler()
async def callback(query: types.CallbackQuery):
    args = query.data.split('|')

    pos = int(args[0])
    game_uuid = args[1]

    chat_id = query.message.chat.id

    if not chat_id in games or \
            games[chat_id]['uuid'] != game_uuid:
        return await query.answer("Ошибка: эта игра недействительна, попробуйте начать новую при помощи /start.")

    if games[chat_id]['is_over']:
        return await query.answer("Игра окончена, попробуйте начать новую при помощи /start.")

    if games[chat_id]['minefield'][pos] == known_no_mines:
        return await query.answer()
    elif games[chat_id]['minefield'][pos] == known_mines:
        return await query.answer()

    elif games[chat_id]['minefield'][pos] == unknown_miness:
        games[chat_id]['minefield'][pos] = known_mines
        games[chat_id]['is_over'] = True
        msg = "Вы проиграли! Используйте /start, чтобы начать новую игру."
        await query.answer(msg)
        await bot.send_animation(chat_id, open('files/fail.gif', 'rb'), caption=msg)
        games[chat_id]['minefield'] = expose(games[chat_id]['minefield'])
        await render(chat_id, original_message=query.message)

    elif games[chat_id]['minefield'][pos] == unknown_no_miness:
        games[chat_id]['minefield'][pos] = known_no_mines
        if not hasUnknownEmptyFields(games[chat_id]['minefield']):
            games[chat_id]['is_over'] = True
            games[chat_id]['minefield'] = expose(games[chat_id]['minefield'])
            msg = "Вы победили! Используйте /start, чтобы начать новую игру."
            await query.answer(msg)
            await bot.send_animation(chat_id, open('files/won.mp4', 'rb'), caption=msg)

        await render(chat_id, original_message=query.message)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop, skip_updates=True)