from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Command

cb = CallbackData('buy', 'prod_id', 'price')
Ad = CallbackData('adres', 'ad_id')

#ГЛАВНОЕ МЕНЮ
Start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Профиль 👤', callback_data='Профиль'),
            InlineKeyboardButton(text='Меню 📄', callback_data='Меню')
        ],
        [
            InlineKeyboardButton(text='Корзина 🗑', callback_data='Корзина'),
            InlineKeyboardButton(text='Помощь 🛠', callback_data='Помощь')
        ],
        [
            InlineKeyboardButton(text='Рассказать анекдот 💭', callback_data='Рассказать анекдот')
        ]
    ]
)

Card = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Просмотреть Корзину 👀', callback_data='Просмотреть Корзину')
        ],
        [
            InlineKeyboardButton(text='Очистить Корзину ❌', callback_data='Очистить Корзину')
        ],
        [
            InlineKeyboardButton(text='Оформить заказ 💳', callback_data='Оформить заказ')
        ],
        [
            InlineKeyboardButton(text='◀ Вернуться на главную', callback_data='Вернуться на главную')
        ]
    ]
)

Menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Классический Кофе', callback_data='Классический Кофе')
        ],
        [
            InlineKeyboardButton('Авторский Раф', callback_data='Авторский Раф')
        ],
        [
            InlineKeyboardButton('Авторские Чаи', callback_data='Авторские Чаи')
        ],
        [
            InlineKeyboardButton('Прочие Напитки', callback_data='Прочие Напитки')
        ],
        [
            InlineKeyboardButton('Фреш', callback_data='Фреш')
        ],
        [
            InlineKeyboardButton('Выпечка', callback_data='Выпечка')
        ],
        [
            InlineKeyboardButton(text='◀ Вернуться на главную', callback_data='Вернуться на главную')
        ]
    ]
)

Info = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Адреса 📍', callback_data='Адреса')
        ],
        [
            InlineKeyboardButton(text='Контакты 📞', callback_data='Контакты')
        ],
        [
            InlineKeyboardButton(text='Наш сайт 💻', url='http://monolyte.tilda.ws/')
        ],
        [
            InlineKeyboardButton(text='Инструкция 📕', callback_data='Инструкция')
        ],
        [
            InlineKeyboardButton(text='◀ Вернуться на главную', callback_data='Вернуться на главную')
        ]
    ]
)

#РАЗДЕЛЫ НАПИТКОВ
Klas = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Флэт Уайт / 189р', callback_data='buy:Флэт Уайт:189'),
        ],
        [
            InlineKeyboardButton('Капучино / 149р', callback_data='buy:Капучино:149')
        ],
        [
            InlineKeyboardButton('Латте / 149р', callback_data='buy:Латте:149')
        ],
        [
            InlineKeyboardButton('Мокко / 179р', callback_data='buy:Мокко:179')
        ],
        [
            InlineKeyboardButton('Американо / 119р', callback_data='buy:Американо:119')
        ],
        [
            InlineKeyboardButton(text='◀ Назад', callback_data='Назад')
        ]
    ]
)

Raf = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Пряная Тыква / 149р', callback_data='buy:Раф Пряная Тыква:149')
        ],
        [
            InlineKeyboardButton('Сникерс / 149р', callback_data='buy:Раф Сникерс:149')
        ],
        [
            InlineKeyboardButton('Халва / 149р', callback_data='buy:Раф Халва:149')
        ],
        [
            InlineKeyboardButton('Орео / 149р', callback_data='buy:Раф Орео:149')
        ],
        [
            InlineKeyboardButton('Арахисовый / 149р', callback_data='buy:Раф Арахисовый:149')
        ],
        [
            InlineKeyboardButton('Цитрусовый / 149р', callback_data='buy:Раф Цитрусовый:149')
        ],
        [
            InlineKeyboardButton('Ванильный / 149р', callback_data='buy:Раф Ванильный:149')
        ],
        [
            InlineKeyboardButton(text='◀ Назад', callback_data='Назад')
        ]
    ]
)

Tea = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Брусничный Каркаде / 149р', callback_data='buy:Брусничный Каркаде:149')
        ],
        [
            InlineKeyboardButton('Фруктово-Ягодный Пунш / 149р', callback_data='buy:Фруктово-Ягодный Пунш:149')
        ],
        [
            InlineKeyboardButton('Имбирный Пуэр / 149р', callback_data='buy:Имбирный Пуэр:149')
        ],
        [
            InlineKeyboardButton('Матча / 249р', callback_data='buy:Матча:249')
        ],
        [
            InlineKeyboardButton('Глинтвейн / 189р', callback_data='buy:Глинтвейн:189')
        ],
        [
            InlineKeyboardButton('Облепиха-Маракуйя / 169р', callback_data='buy:Облепиха-Маракуйя:169')
        ],
        [
            InlineKeyboardButton('Листовой Чай / 109р', callback_data='buy:Листовой Чай:109')
        ],
        [
            InlineKeyboardButton(text='◀ Назад', callback_data='Назад')
        ]
    ]
)

Proch = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Аффогато / 179р', callback_data='buy:Аффогато:179')
        ],
        [
            InlineKeyboardButton(text='Молочный Коктейль / 179р', callback_data='buy:Молочный Коктейль:179')
        ],
        [
            InlineKeyboardButton(text='Бамбл Кофе / 219р', callback_data='buy:Бамбл Кофе:219')
        ],
        [
            InlineKeyboardButton(text='Сливочный Щербет / 249р', callback_data='buy:Сливочный Щербет:249')
        ],
        [
            InlineKeyboardButton(text='◀ Назад', callback_data='Назад')
        ]
    ]
)

Fresh = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Апельсиновый / 199р', callback_data='buy:Апельсиновый:199')  
        ],
        [
            InlineKeyboardButton(text='Яблочный / 199р', callback_data='buy:Яблочный:199')
        ],
        [
            InlineKeyboardButton(text='◀ Назад', callback_data='Назад')
        ]
    ]
)

Bread = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Вафельная Трубочка', callback_data='buy:Вафельная Трубочка')
        ],
        [
            InlineKeyboardButton(text='Наполеон', callback_data='buy:Наполеон')
        ],
        [
            InlineKeyboardButton(text='Медовик', callback_data='buy:Медовик')
        ],
        [
            InlineKeyboardButton(text='Прага', callback_data='buy:Прага')
        ],
        [
            InlineKeyboardButton(text='Ягодный Флан', callback_data='buy:Ягодный Флан')
        ],
        [
            InlineKeyboardButton(text='Твороженное Кольцо', callback_data='buy:Твороженное Кольцо')
        ],
        [
            InlineKeyboardButton(text='◀ Назад', callback_data='Назад')
        ]
    ]
)

#FSM_DELIV
adres = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Мельникайте 106', callback_data='Мельникайте 106')
        ],
        [
            InlineKeyboardButton(text='ТРЦ "Сити Молл"', callback_data='ТРЦ "Сити Молл"')
        ],
        [
            InlineKeyboardButton(text='ТРЦ "Матрешка"', callback_data='ТРЦ "Матрешка"')
        ],
        [
            InlineKeyboardButton(text='ЖК "Айвазовский"', callback_data='ЖК "Айвазовский"')
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='Отмена')
        ]
    ]
)

deliv = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Заберу Сам', callback_data='Заберу Сам')
        ],
        [
            InlineKeyboardButton(text='Доставка', callback_data='Доставка')
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='Отмена')
        ]
    ]
)

hourse = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='08', callback_data='08'),
            InlineKeyboardButton(text='09', callback_data='09'),
            InlineKeyboardButton(text='10', callback_data='10'),
            InlineKeyboardButton(text='11', callback_data='11'),
            InlineKeyboardButton(text='12', callback_data='12'),
            InlineKeyboardButton(text='13', callback_data='13')
        ],
        [
            InlineKeyboardButton(text='14', callback_data='14'),
            InlineKeyboardButton(text='15', callback_data='15'),
            InlineKeyboardButton(text='16', callback_data='16'),
            InlineKeyboardButton(text='17', callback_data='17'),
            InlineKeyboardButton(text='18', callback_data='18'),
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='Отмена')
        ]
    ]
)

min = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='00', callback_data='00'),
            InlineKeyboardButton(text='05', callback_data='05'),
            InlineKeyboardButton(text='10', callback_data='10'),
            InlineKeyboardButton(text='15', callback_data='15'),
            InlineKeyboardButton(text='20', callback_data='20'),
            InlineKeyboardButton(text='25', callback_data='25')
        ],
        [
            InlineKeyboardButton(text='30', callback_data='30'),
            InlineKeyboardButton(text='35', callback_data='35'),
            InlineKeyboardButton(text='40', callback_data='40'),
            InlineKeyboardButton(text='45', callback_data='45'),
            InlineKeyboardButton(text='50', callback_data='50'),
            InlineKeyboardButton(text='55', callback_data='55'),
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='Отмена')
        ]
    ]
)

time = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Как можно скорее', callback_data='Как можно скорее')
        ],
        [
            InlineKeyboardButton(text='Указать время', callback_data='Указать время')
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='Отмена')
        ]
    ]
)

pay = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Оплатить', callback_data='Оплатить')
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='Отмена')
        ]
    ]
)


Zakaz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Оформить заказ 💳', callback_data='Оформить заказ')
        ],
        [
            InlineKeyboardButton(text='◀ Вернуться на главную', callback_data='Вернуться на главную')
        ]
    ]
)

History = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Просмотр', callback_data='Просмотр')
        ],
        [
            InlineKeyboardButton(text='◀ Вернуться на главную', callback_data='Вернуться на главную')
        ]
    ]
)

Bonus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Списать', callback_data='Списать'),
            InlineKeyboardButton(text='Начислить', callback_data='Начислить')
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='Отмена')
        ]
    ]
)
