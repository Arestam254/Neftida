import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Главное меню
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("Хочу Расклад"), KeyboardButton("Хочу Обряд"))

# Меню раскладов
tarot_menu = ReplyKeyboardMarkup(resize_keyboard=True)
tarot_menu.add(
    "Расклад Я и Он", "Расклад Бывший",
    "Расклад Треугольник", "Расклад Измена",
    "Расклад Есть ли будущее у отношений", "Расклад Будущий Муж"
)
tarot_menu.add("🔙 Назад")

# Меню обрядов
ritual_menu = ReplyKeyboardMarkup(resize_keyboard=True)
ritual_menu.add(
    "Сексуальное влечение", "Руническая привязка",
    "Розжиг чувств", "Обряд рассорки",
    "Под венец", "Обряд на удачу",
    "Обряд чистка"
)
ritual_menu.add("🔙 Назад")

user_state = {}

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(
        """🌙 Здравствуйте, меня зовут Neftida, потомственная ведунья и гадалка
Вы не просто так зашли ко мне в гости, я знаю что вас беспокоит 👇

Нажмите /start и выберите, что вас интересует

❗ БЕСПЛАТНО НЕ РАБОТАЮ — магия требует энергообмена!
Написать мне — @neftida_taro
Канал — https://t.me/neftida_witch
Отзывы — https://t.me/otzivi_Neftida""",
        reply_markup=main_menu
    )

@dp.message_handler(lambda m: m.text == "Хочу Расклад")
async def choose_tarot(message: types.Message):
    await message.answer("Выберите интересующий вас расклад:", reply_markup=tarot_menu)

@dp.message_handler(lambda m: m.text == "Хочу Обряд")
async def choose_ritual(message: types.Message):
    await message.answer("Выберите нужный обряд:", reply_markup=ritual_menu)

@dp.message_handler(lambda m: m.text == "🔙 Назад")
async def back_to_main(message: types.Message):
    user_state.pop(message.from_user.id, None)
    await message.answer("Вы вернулись в главное меню.", reply_markup=main_menu)

async def handle_tarot_selection(message: types.Message, title: str, questions: list):
    user_state[message.from_user.id] = title
    await message.answer(
        "Привет! Я отвечу на вопросы:\n" + "\n".join(f"- {q}" for q in questions) +
        "\n\nПожалуйста, опиши ситуацию и укажи ваши имена и даты рождения."
    )

@dp.message_handler(lambda m: m.text == "Расклад Я и Он")
async def tarot_1(message: types.Message):
    questions = [
        "Какой он меня видит",
        "Его чувства ко мне",
        "Его мысли обо мне",
        "Перспектива отношений",
        "Совет от карт"
    ]
    await handle_tarot_selection(message, "Расклад Я и Он", questions)

@dp.message_handler(lambda m: m.text == "Расклад Бывший")
async def tarot_2(message: types.Message):
    questions = [
        "Какой он меня видит сейчас",
        "Какой он меня помнит в этих отношениях",
        "Его чувства ко мне",
        "Хочет ли восстановить отношения",
        "Стоит ли восстанавливать эти отношения"
    ]
    await handle_tarot_selection(message, "Расклад Бывший", questions)

@dp.message_handler(lambda m: m.text == "Расклад Треугольник")
async def tarot_3(message: types.Message):
    questions = [
        "Его отношение ко мне",
        "Его чувства ко мне",
        "Его отношение к ней",
        "Его чувства к ней",
        "Кого выберет"
    ]
    await handle_tarot_selection(message, "Расклад Треугольник", questions)

@dp.message_handler(lambda m: m.text == "Расклад Измена")
async def tarot_4(message: types.Message):
    questions = [
        "Его чувства ко мне",
        "Какой он меня воспринимает",
        "Что скрывает",
        "Способен ли на измену",
        "Была ли измена"
    ]
    await handle_tarot_selection(message, "Расклад Измена", questions)

@dp.message_handler(lambda m: m.text == "Расклад Есть ли будущее у отношений")
async def tarot_5(message: types.Message):
    questions = [
        "Какие есть проблемы",
        "Возможное развитие отношений",
        "Что будет дальше",
        "О чем думает партнёр",
        "Какие могут быть проблемы в отношениях",
        "Как вам себя вести"
    ]
    await handle_tarot_selection(message, "Расклад Будущее Отношений", questions)

@dp.message_handler(lambda m: m.text == "Расклад Будущий Муж")
async def tarot_6(message: types.Message):
    questions = [
        "Его характер",
        "При каких обстоятельствах состоится встреча",
        "На что обратить внимание в отношениях",
        "Ваша характеристика",
        "Совет от карт"
    ]
    await handle_tarot_selection(message, "Расклад Будущий Муж", questions)

@dp.message_handler(lambda m: m.text in [
    "Сексуальное влечение", "Руническая привязка", "Розжиг чувств",
    "Обряд рассорки", "Под венец", "Обряд на удачу", "Обряд чистка"
])
async def ritual_response(message: types.Message):
    texts = {
        "Сексуальное влечение": "Обряд \"Сексуальное влечение\" помогает усилить именно влечение мужчины к вам. Работа проводится по 2 чакре и абсолютно безопасна. После проведения мужчину станет всё чаще тянуть к вам в сексуальном плане, ваша интимная жизнь заиграет новыми красками.\nДля проведения обряда расскажите подробнее о вашей ситуации, а также нужны ваше Имя и дата рождения!",

        "Руническая привязка": "Руническая привязка — это мощный способ создать глубокую эмоциональную связь с человеком. Мы используем древние руны для мягкого воздействия на его энергетику. Работа через 2 и 4 чакры помогает укрепить эмоциональную близость, а активация 5 чакры побуждает его быстрее выразить чувства.\nДля проведения обряда расскажите подробнее о вашей ситуации, а также нужны ваше Имя и дата рождения!",

        "Розжиг чувств": "Розжиг чувств — это обряд на пробуждение и усиление ярких любовных и искренних чувств. Очень хорошо помогает наладить отношения, вернуть страсть. Обряд безопасный, идёт работа с чакрами.\nДля проведения обряда расскажите подробнее о вашей ситуации, а также нужны ваше Имя и дата рождения!",

        "Обряд рассорки": "Обряд рассорки — это способ разделить людей, чтобы они перестали общаться. Работа проводится по чакрам, абсолютно безопасен и не имеет откатов.\nДля проведения обряда расскажите подробнее о вашей ситуации, а также нужны ваше Имя и дата рождения!",

        "Под венец": "Этот обряд поможет выйти замуж, укрепить связь или вывести отношения на новый уровень. Используются руны и работа с несколькими чакрами, особенно с 4 чакрой.\nДля проведения обряда расскажите подробнее о вашей ситуации, а также нужны ваше Имя и дата рождения!",

        "Обряд на удачу": "Если у вас \"чёрная полоса\", этот обряд поможет сменить её на \"белую\". Удача начнёт приходить во всех сферах жизни.\nДля проведения обряда расскажите подробнее о вашей ситуации, а также нужны ваше Имя и дата рождения!",

        "Обряд чистка": "Обряд убирает поверхностный негатив, выравнивает и очищает чакры. Особенно эффективен при сглазе, зависти и негативе.\nДля проведения обряда расскажите подробнее о вашей ситуации, а также нужны ваше Имя и дата рождения!"
    }
    user_state[message.from_user.id] = message.text
    await message.answer(texts[message.text])

@dp.message_handler()
async def forward_data(message: types.Message):
    state = user_state.get(message.from_user.id)
    if not state:
        await message.answer("Пожалуйста, выберите сначала расклад или обряд.")
        return

    text = (
        f"📥 Новая заявка от @{message.from_user.username or 'Без ника'}\n\n"
        f"📌 Выбрано: {state}\n"
        f"📩 Сообщение:\n{message.text}"
    )

    try:
        await bot.send_message(chat_id=ADMIN_CHAT_ID, text=text)
        await message.answer("Спасибо! Сообщение отправлено. Я свяжусь с вами в ближайшее время 🙏")
        user_state.pop(message.from_user.id, None)
    except Exception as e:
        await message.answer("Ошибка отправки сообщения. Пожалуйста, напишите напрямую — @neftida_taro")
        logging.error(f"Ошибка при отправке админу: {e}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
