import telebot
from telebot import types
from telebot.types import InputMediaPhoto

token='2130693492:AAFDmHms9z6s34KI0PrRamYniw5G8cBoFlQ'
bot = telebot.TeleBot(token)

#статическая клавиатура
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.row('Вернуться')
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.row('❄Двери с терморазрывом')
keyboard2.row('Трехконтурные Двери')
keyboard2.row('Двухконтурные Двери')
keyboard2.row('Технические Двери')
keyboard2.row('Вернуться к выбору дверей')

keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard3.row('🏠Входные двери')
keyboard3.row('✔Услуги')
keyboard3.row('📌Что нового?!')
keyboard3.row('ℹ️Контакты')


keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard4.row('✔Двери в наличии')
keyboard4.row('⌛Двери под заказ')
keyboard4.row('Возврат в Главное Меню')

#возврат к выбору заказ склад

keyboard5 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard5.row('Вернуться к выбору дверей')

#двери под заказ 1
key5 = types.InlineKeyboardMarkup(row_width=1)
but1a = types.InlineKeyboardButton(text="3 контура... Зеркало.. Shelter", callback_data="one")
but2a = types.InlineKeyboardButton(text="3 контура... Shelter", callback_data="two")
but3a = types.InlineKeyboardButton(text="Сенатор 3к...зеркало", callback_data="three")
but4a = types.InlineKeyboardButton(text="2х контура... Двери Регионов", callback_data="Fore")
but5a = types.InlineKeyboardButton(text="3 контура.Зеркало.Shelter", callback_data="five")
but6a = types.InlineKeyboardButton(text="Венеция", callback_data="sex")
but7a = types.InlineKeyboardButton(text="3 контура... Терморазрыв... Дверной Континент", callback_data="seven")
but8a = types.InlineKeyboardButton(text="Следующая страница", callback_data="nine")
key5.add(but1a,but2a,but3a,but4a,but5a,but6a,but7a,but8a)

#двери под заказ 2
key6 = types.InlineKeyboardMarkup(row_width=1)
but1b = types.InlineKeyboardButton(text="Дверь Вегас... Корабельная Фанера", callback_data="one_a")
but2b = types.InlineKeyboardButton(text="Дверь Токио... Фирма Shelter", callback_data="two_b")
but3b = types.InlineKeyboardButton(text="Дверь М-2 Ливерпуль 1...Shelter", callback_data="three_c")
but4b = types.InlineKeyboardButton(text="Дверь Титан.. Shelter", callback_data="Fore_d")
but5b = types.InlineKeyboardButton(text="Дверь Оникс... Shelter", callback_data="five_i")
but6b = types.InlineKeyboardButton(text="3 контура... Терморазрыв... ДК Ковка", callback_data="sex_f")
but7b = types.InlineKeyboardButton(text="Предыдущая страница", callback_data="seven_j")
but8b = types.InlineKeyboardButton(text="Следующая страница", callback_data="nine_h")
key6.add(but1b,but2b,but3b,but4b,but5b,but6b,but7b,but8b)


#двери под заказ страница 3

key7 = types.InlineKeyboardMarkup(row_width=1)
but1b1 = types.InlineKeyboardButton(text="3к... двери Регионов", callback_data="one_a1")
but2b1 = types.InlineKeyboardButton(text="3 контура... Двери Регионов", callback_data="two_b1")
but3b1 = types.InlineKeyboardButton(text="3 контура... Терморазрыв... Shelter", callback_data="three_c1")
but4b1 = types.InlineKeyboardButton(text="3 контура... Терморазрыв.. Эмаль... Shelter", callback_data="Fore_d1")
but5b1 = types.InlineKeyboardButton(text="3 контура... Биометрический замок... Двери Регионов", callback_data="five_i1")
but6b1 = types.InlineKeyboardButton(text="3 контура... Дверной Континент", callback_data="sex_f1")
but7b1 = types.InlineKeyboardButton(text="3к Терморазрыв... Дверной Континен", callback_data="seven_j1")
but8b1 = types.InlineKeyboardButton(text="3 контура... Зеркало... Дверной Континент", callback_data="nine_h1")
but9b1 = types.InlineKeyboardButton(text="Предыдущая страница", callback_data="ten_h1")
key7.add(but1b1,but2b1,but3b1,but4b1,but5b1,but6b1,but7b1,but8b1,but9b1)



# терморазрыв
key = types.InlineKeyboardMarkup(row_width=1)
but_3 = types.InlineKeyboardButton(text="Изотерма серебро, Листвинница Бежевая", callback_data="NumberThere")
but_1 = types.InlineKeyboardButton(text="ТермоМакс", callback_data="NumberOne")
but_2 = types.InlineKeyboardButton(text="Термаль Ультра Белёный дуб", callback_data="NumberTwo")
but_4 = types.InlineKeyboardButton(text="Термаль экстра Белая Сосна", callback_data="NumberFore")
key.add(but_3,but_2,but_1,but_4)
#возврат терморазрыв
key_back = types.InlineKeyboardMarkup(row_width=1)
but__1 = types.InlineKeyboardButton(text="Назад", callback_data='back')
key_back.add(but__1)
#возврат техконтурные
key_back3a = types.InlineKeyboardMarkup(row_width=1)
but__2 = types.InlineKeyboardButton(text="Назад", callback_data='back3')
key_back3a.add(but__2)

#возврат 2х контурные

key_back2 = types.InlineKeyboardMarkup(row_width=1)
but2a = types.InlineKeyboardButton(text="Назад", callback_data='back2')
key_back2.add(but2a)

#возврат в заказные

key_back3 = types.InlineKeyboardMarkup(row_width=1)
but2b = types.InlineKeyboardButton(text="Назад", callback_data='back3a')
key_back3.add(but2b)

#возврат  заказные 2 страница
key_back4 = types.InlineKeyboardMarkup(row_width=1)
but2b = types.InlineKeyboardButton(text="Назад", callback_data='back4b')
key_back4.add(but2b)

#возврат  заказные 3 страница
key_back5 = types.InlineKeyboardMarkup(row_width=1)
but2b1 = types.InlineKeyboardButton(text="Назад", callback_data='back5c')
key_back5.add(but2b1)



#3контурные
key1 = types.InlineKeyboardMarkup(row_width=1)
but3 = types.InlineKeyboardButton(text="Рубикон Капучино, Серебристый Антик", callback_data="NumberFive")
but1 = types.InlineKeyboardButton(text="Теплолюкс-Венге", callback_data="NumberSix")
but2 = types.InlineKeyboardButton(text="Византия", callback_data="NumberSeven")
but4 = types.InlineKeyboardButton(text="Гарда 7.5 серебро, Серая эмаль", callback_data="NumberTen")
but5 = types.InlineKeyboardButton(text="Сити-с... Лиственница серая", callback_data="NumberNine1")
but6 = types.InlineKeyboardButton(text="Филадельфия с Зеркалом", callback_data="NumberEight")
key1.add(but3,but2,but1,but4,but5,but6)

#2 контурные

key2 = types.InlineKeyboardMarkup(row_width=1)
but3 = types.InlineKeyboardButton(text="Гарда 7.5 Медный Антик", callback_data="NumberNine")
but1 = types.InlineKeyboardButton(text="Доминанта Медный Антик", callback_data="NumberElevan")
but2 = types.InlineKeyboardButton(text="Гарда 8мм.дуб рустикальный", callback_data="NumberTwelve")
but4 = types.InlineKeyboardButton(text="Ротердам", callback_data="NumberThirteen")
but5 = types.InlineKeyboardButton(text="Модель Форте-Беленый дуб", callback_data="NumberForeteen")
key2.add(but3,but2,but1,but4,but5)

#1 контур
key3 = types.InlineKeyboardMarkup(row_width=1)
but___1 = types.InlineKeyboardButton(text="Мастер ХдФ", callback_data="NumberSexteen")
key3.add(but___1)







@bot.message_handler(commands=['start'])




def start_message(message):
  bot.send_photo(message.chat.id, open('vizitka.jpg', 'rb'))
  bot.send_message(message.chat.id,'''🏠Добро пожаловать в главное меню 
Телеграм-Галереи "Лучшие двери России."

Выберите интересующий вас раздел наших товаров⤵️''',reply_markup=keyboard3)



#  bot.send_photo(message.chat.id, photo='https://content.foto.my.mail.ru/mail/nurd/11/h-18.jpg')
#  bot.send_photo(message.chat.id, open('d:/a13.jpg', 'rb')) из адреса
#  bot.send_photo(message.chat.id, open('a13.jpg', 'rb')) из корня




@bot.message_handler(content_types=['text'])
def send_text(message):     #блок кнопок дверей

    if message.text == '❄Двери с терморазрывом':
        bot.send_message(message.chat.id,'выбери дверь',reply_markup=key)
        bot.send_message(message.chat.id,'Двери с терморазрывом',reply_markup=keyboard1)

    elif message.text == '🏠Входные двери':
        bot.send_message(message.chat.id, 'Выбери раздел', reply_markup=keyboard4)

    elif message.text == '✔Двери в наличии':
        bot.send_message(message.chat.id, 'Выбери раздел', reply_markup=keyboard2)

    elif message.text == '⌛Двери под заказ':
        bot.send_message(message.chat.id, 'Выбери раздел', reply_markup=key5)
        bot.send_message(message.chat.id, 'Выбери дверь', reply_markup=keyboard5)




    elif message.text == 'Вернуться':
        bot.send_message(message.chat.id, 'Выбери раздел',reply_markup=keyboard2)

    elif message.text == 'Вернуться к выбору дверей':
        bot.send_message(message.chat.id, 'Выбери раздел',reply_markup=keyboard4)

    elif message.text == 'Трехконтурные Двери':
        bot.send_message(message.chat.id, 'выбери дверь', reply_markup=key1)
        bot.send_message(message.chat.id, 'Трехконтурные двери',reply_markup=keyboard1)

    elif message.text == 'Двухконтурные Двери':
        bot.send_message(message.chat.id, 'Двухконтурные двери', reply_markup=key2)
        bot.send_message(message.chat.id, 'Выбери дверь', reply_markup=keyboard1)

    elif message.text == 'Технические Двери':
        bot.send_message(message.chat.id, 'Технические двери', reply_markup=key3)
        bot.send_message(message.chat.id, 'Выбери раздел', reply_markup=keyboard1)

    elif message.text == '✔Услуги':

        bot.send_message(message.chat.id,'''Установка межкомнатных и входных дверей.
Быстро,качественно, надёжно, гарантия.Выезд на замер.''', reply_markup=keyboard3)

    elif message.text == 'ℹ️Контакты':
        bot.send_message(message.chat.id, '''г.Наро-Фоминск Т.К  
"Красная пресня",ТЦ-10, пав. Г-19
тел :Евгений 8(926)394-12-97
тел :Антон.    8(906)752-90-33''', reply_markup=keyboard3)

    elif message.text == 'Возврат в Главное Меню':
        bot.send_photo(message.chat.id, open('vizitka.jpg', 'rb'))
        bot.send_message(message.chat.id,'''🏠Добро пожаловать в главное меню 
Телеграм-Галереи "Лучшие двери России."

Выберите интересующий вас раздел наших товаров⤵️''', reply_markup=keyboard3)


#обработчик хенлеров







@bot.callback_query_handler(func=lambda c:True) #функция инлайн(плавающие кнопки)

def inline(c):
    if c.data == 'NumberOne':

        pic1 = open("termomax1.jpg", "rb")

        pic2 = open("termomax2.jpg", "rb")

        pic3 = open('termomax3.jpg', 'rb')
        media = [InputMediaPhoto(pic1), InputMediaPhoto(pic2),InputMediaPhoto(pic3)]
        bot.send_media_group(c.message.chat.id, media)
        bot.send_message(c.message.chat.id,'''Модель:❄ Термомакс
🎨Внешняя отделка
➖полимерное атмосферостойкое покрытие цвет Мокко.
🔳Внутренняя отделка.
➖Фрезерованная МДФ-панель.
➖Размеры:880х2050,980х2050мм.
➖Толщина полотна:105мм.
➖Замки:сувальдные Guardian.
➖Количество петель:3.
➖Короб:Открытый. 
➖Уплотнитель:4 контура.
➖Утеплитель:комбинированный.
➖Ночная задвижка:ДА.
➖Терморазрыв рамы и полотна.''', reply_markup=key_back)

    elif c.data == 'NumberTwo':

        pic1 = open("termalultra1.jpg", "rb")

        pic2 = open("termalultra2.jpg", "rb")

        media1 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]

        bot.send_media_group(c.message.chat.id, media1)
        bot.send_message(c.message.chat.id,'''❄Модель:Термаль Ультра Беленый Дуб
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное Медный Антик.
🔳Внутренняя отделка.
➖Фрезерованная МДФ панель.
➖Размеры:860х2050,960х2050мм.
➖Толщина полотна:100мм.
➖Замки:сувальдные Бордер. 
➖Количество петель:3.
➖Короб:Закрытый утепленный.
➖Уплотнитель: 3 контура. 
➖Утеплитель:комбинированный.
➖Ночная задвижка: Да.
➖Терморазрыв рамы и полотна.''', reply_markup=key_back)


    elif c.data == 'back':
        bot.send_message(c.message.chat.id,'Выбери дверь',reply_markup=key)

    elif c.data == 'NumberThere':

        pic1 = open("izoterma1.jpg", "rb")

        pic2 = open("izoterma2.jpg", "rb")

        media3 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]

        bot.send_media_group(c.message.chat.id, media3)
        bot.send_message(c.message.chat.id,'''❄Изотерма Серебро Листвинница Беж Царга.
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное Cеребро Антик.
🔳Внутренняя отделка
➖царговая МДФ-панель 22 мм.
➖Размеры:860х2050,960х2050мм.
➖Толщина полотна:110мм.
➖Замки:сувальдные Kale.
➖Количество петель: 3
➖Короб: Открытый. 
➖Уплотнитель:3 контура. 
➖Утеплитель:ПИР плита.
➖Усиление замковой зоны:Да.
➖Ночная задвижка:Да.
➖Терморазрыв рамы и полотна.''', reply_markup=key_back)

    elif c.data == "NumberFore":

        pic1 = open("termalex1.jpg", "rb")

        pic2 = open("termalex2.jpg", "rb")

        media4 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]

        bot.send_media_group(c.message.chat.id, media4)
        bot.send_message(c.message.chat.id,"""❄Модель:ТЕРМАЛЬ ЭКСТРА Беленая Сосна
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное Медный Антик.
🔳Внутренняя отделка
➖Фрезированная МДФ панель.
➖Размеры:860х2050,960х2050мм.
➖Толщина полотна:100мм.
➖Утеплённая коробка:105мм.
➖Замки:сувальдные Бордер. 
➖Количество петель: 3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:комбинированный.
➖Усиление замковой зоны:Да.
➖Ночная задвижка:Да.
➖Терморазрыв рамы и полотна.""", reply_markup=key_back)
# модель хдф
    elif c.data == "NumberSexteen":

        pic1 = open("xdf1.jpg", "rb")

        pic2 = open("xdf2.jpg", "rb")

        media5 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]

        bot.send_media_group(c.message.chat.id, media5)
        bot.send_message(c.message.chat.id,'''Модель:Мастер ХДФ
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное Медный Антик.
🔳Внутренняя отделка
➖Панель ХДФ 5мм.
➖Размеры:850x2050,950x2050мм.
➖Толщина полотна:45 мм.
➖Замок:Просам цилиндрический.
➖Количество петель:2
➖Уплотнитель:1 контур.
➖Утеплитель:пенополистирол.
➖Усиление замковой зоны:НЕТ.
➖Ночная задвижка: НЕТ.


''')
#трехконтурны
    elif c.data == "back3":
        bot.send_message(c.message.chat.id, 'Возвращаемся к выбору', reply_markup=key1)

    elif c.data == "NumberEight":

        pic1 = open("filadelfia1.jpg", "rb")

        pic2 = open("filadelfia2.jpg", "rb")

        pic3 = open("filadelfia3.jpg", "rb")

        media4 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2),InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media4)
        bot.send_message(c.message.chat.id, '''▶Модель:SHELTER ФИЛАДЕЛЬФИЯ С ЗЕРКАЛОМ.
🎨Внешняя отделка
➖МДФ панель.
🔳Внутренняя отделка
➖Панель МДФ (зеркало).
➖Размеры:860х2050,960х2050мм.
➖Толщина полотна: 100 мм.
➖Замок:осн.КАЛЕ цилиндровый.
➖Замок:всп.БОРДЕР сувальдный. 
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:Мин плита.
➖Ночная задвижка: Да.
➖Глазок:Да.
''', reply_markup=key_back3a)
#готово до сюда
    elif c.data == "NumberNine1":
        pic1 = open("city1.jpg", "rb")

        pic2 = open("city2.jpg" , "rb")

        media4 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]

        bot.send_media_group(c.message.chat.id, media4)
        bot.send_message(c.message.chat.id,'''▶Модель:Сити-С3К.
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное Серебрянный Антик.
🔳Внутренняя отделка
➖Царговая панель.
➖Размеры:860х2050,960х2050мм.
➖Толщина полотна: 95 мм.
➖Замок:осн.Гардиан цилиндрич.
➖Замок:всп.Гардиан сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:базальтовая плита.
➖Ночная задвижка: Да.
➖Глазок:Да.''', reply_markup=key_back3a)

    elif c.data == "NumberTen":
        pic1 = open("garda71.jpg", "rb")

        pic2 = open("garda72.jpg" , "rb")

        pic3 = open("garda73.jpg", "rb")

        media5 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2) , InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media5)
        bot.send_message(c.message.chat.id,'''▶Модель:Гарда 7.5 Серебро Эмаль .
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное Серебрянный Антик.
🔳Внутренняя отделка
➖Фрезированная Панель МДФ.
➖Размеры:860х2050,960х2050мм.
➖Толщина полотна: 75 мм.
➖Замок:осн.Карат цилиндричес.
➖Замок:всп.Карат сувальдный. 
➖Количество петель:2.
➖Уплотнитель: 3 контура. 
➖Утеплитель:пенополистирол.
➖Ночная задвижка: Да.
➖Глазок:Да.''', reply_markup=key_back3a)

    elif c.data == "NumberSix":
        pic1 = open("teplovenge1.jpg", "rb")

        pic2 = open("teplovenge2.jpg" , "rb")

        media6 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]

        bot.send_media_group(c.message.chat.id, media6)
        bot.send_message(c.message.chat.id,'''▶Модель:ТЕПЛОЛЮКС (ВЕНГЕ).
🎨Внешняя отделка
➖Фрезированная Панель МДФ.
🔳Внутренняя отделка
➖Фрезированная Панель МДФ.
➖Размеры:860х2050,960х2050мм.
➖Толщина полотна: 102 мм.
➖Замок:осн.Гардиан цилиндрич.
➖Замок:всп.Гардиан сувальдный. 
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:базальтовая плита.
➖Ночная задвижка: Да
➖Глазок:Да
''', reply_markup=key_back3a)


    elif c.data == "NumberSeven":
        pic1 = open("vizantia1.jpg", "rb")

        pic2 = open("vizantia2.jpg", "rb")

        pic3 = open("vizantia3.jpg", "rb")

        media7 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media7)
        bot.send_message(c.message.chat.id,'''▶Модель:Shelter "ВИЗАНТИЯ".
🎨Внешняя отделка
➖Фрезированная Панель МДФ.
🔳Внутренняя отделка
➖Фрезированная Панель МДФ.
➖Размеры:860х2050,960х2050мм.
➖Толщина полотна: 105 мм.
➖Замок:осн.Гардиан цилиндрич.
➖Замок:всп.Гардиан сувальдный 
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:миниральная вата.
➖Ночная задвижка: Да.
➖Глазок:Да.''', reply_markup=key_back3a)

    elif c.data == "NumberFive":
        pic1 = open("rubic1.jpg", "rb")

        pic2 = open("rubic2.jpg", "rb")

        pic3 = open("rubic3.jpg", "rb")

        media7 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media7)
        bot.send_message(c.message.chat.id,'''▶Модель:Рубикон-1 Царга Капучино.
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное Серебрянный Антик.
🔳Внутренняя отделка
➖Царговая Панель.
➖Размеры:860х2050,960х2050мм. 
➖Толщина полотна: 96 мм.
➖Замок:осн.Галеон цилиндрич.
➖Замок:всп.Галеон сувальдный. 
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:пенополистерол.
➖Ночная задвижка:Да.
➖Глазок:Да.
''', reply_markup=key_back3a)
#двухконтурные
    elif c.data == "NumberNine":
        pic1 = open("gardaant1.jpg", "rb")

        pic2 = open("gardaant2.jpg", "rb")

        pic3 = open("gardaant3.jpg", "rb")

        media8 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media8)
        bot.send_message(c.message.chat.id, '''▶Модель:Гарда 7.5 Медный Антик.
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное Медный Антик.
🔳Внутренняя отделка
➖Фрезерованная панель МДФ.
➖Размеры:860х2050,960х2050мм. 
➖Толщина полотна: 75 мм.
➖Замок:осн.Карат цилиндричес.
➖Замок:всп.Карат сувальдный. 
➖Количество петель:2.
➖Уплотнитель: 2 контура. 
➖Утеплитель:пенополистерол.
➖Ночная задвижка: Да
➖Глазок:Да
''', reply_markup=key_back2)

    elif c.data == "NumberTwelve":
        pic1 = open("garda81.jpg", "rb")

        pic2 = open("garda82.jpg", "rb")

        media9 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]

        bot.send_media_group(c.message.chat.id, media9)
        bot.send_message(c.message.chat.id,'''▶Модель:Гарда 8мм дуб рустикальный.
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное Медный антик.
🔳Внутренняя отделка
➖Фрезерованная панель МДФ.
➖Размеры:860х2050,960х2050мм. 
➖Толщина полотна: 60 мм.
➖Замок:осн.Карат цилиндричес.
➖Замок:всп.Карат сувальдный. 
➖Количество петель:2.
➖Уплотнитель: 2 контура. 
➖Утеплитель:пенополистерол.
➖Ночная задвижка: Да
➖Глазок:Да
''', reply_markup=key_back2)

    elif c.data == "NumberElevan":
        pic1 = open("dom1.jpg", "rb")

        pic2 = open("dom2.jpg", "rb")

        media10 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]

        bot.send_media_group(c.message.chat.id, media10)
        bot.send_message(c.message.chat.id,'''▶Модель:Доминанта Медный Антик.
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное Медный Антик.
🔳Внутренняя отделка
➖Фрезерованная панель МДФ.
➖Размеры:860х2050,960х2050мм. 
➖Толщина полотна: 60 мм.
➖Замок:осн.Карат цилиндричес.
➖Замок:всп.Карат сувальдный. 
➖Количество петель:2.
➖Уплотнитель: 2 контура. 
➖Утеплитель:пенополистерол.
➖Ночная задвижка: НЕТ.
➖Глазок:Да
''', reply_markup=key_back2)

    elif c.data == "NumberThirteen":
        pic1 = open("rot1.jpg", "rb")

        pic2 = open("rot2.jpg", "rb")

        media11 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]

        bot.send_media_group(c.message.chat.id, media11)
        bot.send_message(c.message.chat.id,'''▶РОТЕРДАМ Листвинница Бежевая.
🎨Внешняя отделка
➖Фрезерованная панель МДФ.
🔳Внутренняя отделка
➖Царговая панель.
➖Размеры:860х2050,960х2050мм. 
➖Толщина полотна: 105 мм.
➖Замок:осн.Карат цилиндричес.
➖Замок:всп.Карат сувальдный. 
➖Количество петель:2.
➖Уплотнитель: 2 контура. 
➖Утеплитель:пенополистерол.
➖Ночная задвижка: Да
➖Глазок:Да''', reply_markup=key_back2)


    elif c.data == "NumberForeteen":
        pic1 = open("fort1.jpg", "rb")

        pic2 = open("fort2.jpg", "rb")

        media12 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]

        bot.send_media_group(c.message.chat.id, media12)
        bot.send_message(c.message.chat.id,'''▶Модель:Форт Беленый дуб.
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное Медный Антик.
🔳Внутренняя отделка
➖Панель ХДФ.
➖Размеры:860х2050,960х2050мм. 
➖Толщина полотна: 105 мм.
➖Замок:осн.Гардиан цилиндрич.
➖Замок:всп.Гардиан сувальдный 
➖Количество петель:2.
➖Уплотнитель: 2 контура. 
➖Утеплитель:миниральная вата.
➖Ночная задвижка: Да
➖Глазок:Да
''', reply_markup=key_back2)

    elif c.data == "back2":
        bot.send_message(c.message.chat.id, 'здесь будет описание', reply_markup=key2)

    elif c.data == "back3a":
        bot.send_message(c.message.chat.id, 'здесь будет описание', reply_markup=key5)
#заказные
    elif c.data == 'one':
        pic1 = open("sheltzer1.jpg", "rb")

        pic2 = open("sheltzer2.jpg", "rb")

        pic3 = open("sheltzer3.jpg", "rb")

        media13 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2),InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media13)
        bot.send_message(c.message.chat.id,'''Модель:"ПАЛЕРМО ЗЕРКАЛО"
🎨Внешняя отделка
➖Фрезированная МДФ панель.
🔳Внутренняя отделка
➖Фрезированная МДФ панель с зеркалом.
➖Размеры:860х2070,960х2070мм. 
➖Толщина полотна: 95 мм.
➖Замок:осн.Kale цилиндрич.
➖Замок:всп.Kale сувальдный 
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:миниральная плита.
➖Ночная задвижка: Да
➖Глазок:Да''', reply_markup=key_back3)

    elif c.data == 'two':
        pic1 = open("shelt1.jpg", "rb")

        pic2 = open("shel2.jpg", "rb")

        pic3 = open("shel3.jpg", "rb")

        pic4 = open('shel4.jpg', 'rb')

        media14 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2),InputMediaPhoto(pic3) , InputMediaPhoto(pic4)]

        bot.send_media_group(c.message.chat.id, media14)
        bot.send_message(c.message.chat.id,'''Модель:"Дрезден V-1"
🎨Внешняя отделка
➖Фрезированная МДФ панель.
🔳Внутренняя отделка
➖Фрезированная МДФ панель с зеркалом.
➖Размеры:860х2070,960х2070мм. 
➖Толщина полотна: 115 мм.
➖Замок:осн.Border цилиндрич.
➖Замок:всп.Border сувальдный 
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:миниральная плита.
➖Ночная задвижка: Да
➖Глазок:Да''', reply_markup=key_back3)

    elif c.data == 'three':
        pic1 = open("senat1.jpg", "rb")

        pic2 = open("senat2.jpg", "rb")

        pic3 = open("senat3.jpg", "rb")

        media15 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media15)
        bot.send_message(c.message.chat.id,'''Модель:"Сенатор Зеркало"
🎨Внешняя отделка
➖Фрезированная МДФ панель.
🔳Внутренняя отделка
➖Фрезированная МДФ панель с зеркалом.
➖Размеры:860х2050,960х2050мм. 
➖Толщина полотна: 120 мм.
➖Замок:осн.Kale цилиндрич.
➖Замок:всп.Kale сувальдный 
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:пенополистерол.
➖Ночная задвижка: Да
➖Глазок:Да''', reply_markup=key_back3)

    elif c.data == 'Fore':
        pic1 = open("region1.jpg", "rb")

        pic2 = open("region2.jpg", "rb")

        pic3 = open("region3.jpg", "rb")

        pic4 = open("region4.jpg", "rb")

        media16 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3), InputMediaPhoto(pic4)]

        bot.send_media_group(c.message.chat.id, media16)
        bot.send_message(c.message.chat.id,'''Модель:"Quadro"
🎨Внешняя отделка
➖Фрезированная МДФ панель.
🔳Внутренняя отделка
➖Фрезированная МДФ панель.
➖Размеры:880х2050,980х2050мм. 
➖Толщина полотна: 105 мм.
➖Замок:осн.ЗВ 816 цилиндрич.
➖Замок:всп.ЗВ 817 сувальдный 
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:базальтовая плита.
➖Ночная задвижка: Да
➖Глазок:Да''', reply_markup=key_back3)


    elif c.data == 'five':
        pic1 = open("shelz1.jpg", "rb")

        pic2 = open("shelz2.jpg", "rb")

        pic3 = open("shelz3.jpg", "rb")


        media17 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media17)
        bot.send_message(c.message.chat.id,'''Модель:"ПАНОРАМА ЗЕРКАЛО"
🎨Внешняя отделка
➖Фрезированная МДФ панель.
🔳Внутренняя отделка
➖МДФ панель с зеркалом.
➖Размеры:860х2070/960х2070мм. 
➖Толщина полотна: 100 мм.
➖Замок:осн.Гардиан цилиндрич.
➖Замок:всп.Гардиан сувальдный 
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:миниральная плита.
➖Ночная задвижка: Да
➖Глазок:Да''', reply_markup=key_back3)


    elif c.data == 'sex':
        pic1 = open("venech.jpg", "rb")

        pic2 = open("venech1.jpg", "rb")

        pic3 = open("venech2.jpg", "rb")

        pic4 = open("venesh3.jpg", "rb")


        media19 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3),InputMediaPhoto(pic4)]

        bot.send_media_group(c.message.chat.id, media19)
        bot.send_message(c.message.chat.id,'''Модель:"Венеция"
🎨Внешняя отделка
➖атмосферостойкое порошково-полимерное «Медный Антик»
➖Двухкамерный стеклопакет.
➖Ковка:покрытие «Чёрный муар»
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:860х2050/960х2050мм. 
➖Толщина полотна: 75 мм.
➖Замок:осн.Kale цилиндрич.
➖Замок:всп.Kale сувальдный 
➖Количество петель:2.
➖Уплотнитель: 2 контура. 
➖Утеплитель:миниральная плита.
➖Ночная задвижка: Да.
➖Глазок:НЕТ''', reply_markup=key_back3)

    elif c.data == 'seven':
        pic1 = open("termdver1.jpg", "rb")

        pic2 = open("termdver2.jpg", "rb")

        pic3 = open("termdver3.jpg", "rb")

        pic4 = open("termdver4.jpg", "rb")

        media20 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3),InputMediaPhoto(pic4)]

        bot.send_media_group(c.message.chat.id, media20)
        bot.send_message(c.message.chat.id,'''Модель:Термаль Премиум.
🎨Внешняя отделка
➖термопласт, 10 мм
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:860х2050/960х2050мм. 
➖Толщина полотна: 103 мм.
➖Замок:осн.Гардиан сувальдный.
➖Замок:всп.Гардиан сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:комбинированнный.
➖Ночная задвижка: Да
➖Терморазрыв рамы и полотна''', reply_markup=key_back3)

    elif c.data == 'nine':
        bot.send_message(c.message.chat.id, 'Переходим в следующий каталог', reply_markup=key6)

#блок заказ 2 страница
#кнопки управления назад вперед
    elif c.data == 'seven_j':
        bot.send_message(c.message.chat.id, 'Переходим на первую страницу', reply_markup=key5)

    elif c.data == 'nine_h':
        bot.send_message(c.message.chat.id, 'Переходим на первую страницу', reply_markup=key7)

    elif c.data == 'back4b':
        bot.send_message(c.message.chat.id, 'Переходим в следующий каталог', reply_markup=key6)

    elif c.data == 'one_a':
        pic1 = open("korab1.jpg", "rb")

        pic2 = open("korab2.jpg.", "rb")

        pic3 = open("korab3.jpg", "rb")

        media21 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media21)
        bot.send_message(c.message.chat.id,'''Модель:входная уличная дверь Вегас
🎨Внешняя отделка
➖Влагостойкий щит Waterproof veneer
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:900х2045/980х2045мм. 
➖Толщина полотна: 105 мм.
➖Замок:осн.Kale цилиндрич.
➖Замок:всп.Меттэм сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:Базальтовая плита.
➖Ночная задвижка: Да.
➖Глазок:Нет.
➖Возможна установка на улицу.''', reply_markup=key_back4)

    elif c.data == 'two_b':
        pic1 = open("tokio1.jpg", "rb")

        pic2 = open("tokio2.jpg.", "rb")

        pic3 = open("tokio3.jpg", "rb")

        media22 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media22)
        bot.send_message(c.message.chat.id,'''Модель:Дверь стальная ТОКИО
🎨Внешняя отделка
➖Антик темное серебро
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:860х2070 / 960х2070мм. 
➖Толщина полотна: 110 мм.
➖Замок:осн.Гардиан цилиндрич.
➖Замок:всп.Гардиан сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:Миниральная плита.
➖Ночная задвижка: Да.
➖Глазок:ДА.''', reply_markup=key_back4)

    elif c.data == 'three_c':
        pic1 = open("liver1.jpg", "rb")

        pic2 = open("liver2.jpg.", "rb")

        pic3 = open("liver3.jpg", "rb")

        media23 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media23)
        bot.send_message(c.message.chat.id,'''Модель:Дверь стальная ТОКИО
🎨Внешняя отделка
➖Фрезированная МДФ панель.
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:2070х860 /2070х960мм. 
➖Толщина полотна: 115 мм.
➖Замок:осн.BORDER  цилиндрич.
➖Замок:всп.BORDER  сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:Миниральная плита.
➖Ночная задвижка: Да.
➖Глазок:ДА.''', reply_markup=key_back4)

    elif c.data == 'Fore_d':
        pic1 = open("titan1.jpg", "rb")

        pic2 = open("titan2.jpg.", "rb")

        pic3 = open("titan3.jpg", "rb")

        pic4 = open("titan4.jpg", "rb")

        media24 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3), InputMediaPhoto(pic4)]

        bot.send_media_group(c.message.chat.id, media24)
        bot.send_message(c.message.chat.id,'''Модель:Дверь стальная Титан
🎨Внешняя отделка
➖Фрезированная МДФ панель.
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:2070х860 /2070х960мм. 
➖Толщина полотна: 110 мм.
➖Замок:осн.Гардиан  цилиндрич.
➖Замок:всп.Гардиан  сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:Миниральная плита.
➖Ночная задвижка: Да.
➖Глазок:ДА.''', reply_markup=key_back4)

    elif c.data == 'five_i':
        pic1 = open("oniks1.jpg", "rb")

        pic2 = open("oniks2.jpg.", "rb")

        pic3 = open("oniks3.jpg", "rb")

        pic4 = open("oniks4.jpg", "rb")

        media25 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3), InputMediaPhoto(pic4)]

        bot.send_media_group(c.message.chat.id, media25)
        bot.send_message(c.message.chat.id,'''Модель:Дверь стальная Оникс
🎨Внешняя отделка
➖Фрезированная МДФ панель.
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:2070х860 /2070х960мм. 
➖Толщина полотна: 100 мм.
➖Замок:осн.Гардиан  цилиндрич.
➖Замок:всп.Гардиан  сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:Миниральная плита.
➖Ночная задвижка: Да.
➖Глазок:ДА.''', reply_markup=key_back4)

    elif c.data == 'sex_f':
        pic1 = open("kovka1.jpg", "rb")

        pic2 = open("kovka2.jpg.", "rb")

        pic3 = open("kovka3.jpg", "rb")

        media26 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media26)
        bot.send_message(c.message.chat.id,'''Модель:Дверь стальная Лион.
🎨Внешняя отделка
➖Фрезированная МДФ панель.
➖3-хкамерный стеклопакет
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:2050х860 /2050х960мм. 
➖Толщина полотна: 115 мм.
➖Замок:осн.Гардиан  цилиндрич.
➖Замок:всп.Гардиан  сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:Базательтовая плита.
➖Ночная задвижка: Да.
➖Глазок:НЕТ.
➖Возможна установка на улицу.''', reply_markup=key_back4)

#блок дверей на заказ 3 страница

    elif c.data == 'ten_h1':
        bot.send_message(c.message.chat.id, 'Переходим на первую страницу', reply_markup=key6)

    elif c.data == 'back5c':
        bot.send_message(c.message.chat.id, 'Переходим в следующий каталог', reply_markup=key7)



    elif c.data == 'one_a1':
        pic1 = open("xz1.jpg", "rb")

        pic2 = open("xz2.jpg", "rb")

        pic3 = open("xz3.jpg", "rb")

        pic4 = open("xz4.jpg", "rb")

        media27 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3), InputMediaPhoto(pic4)]

        bot.send_media_group(c.message.chat.id, media27)
        bot.send_message(c.message.chat.id,'''Модель:Дверь стальная Прогресс
🎨Внешняя отделка
➖Фрезированная МДФ панель.
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:2050х880 /2050х980мм. 
➖Толщина полотна: 100 мм.
➖Замок:осн.Гардиан  цилиндрич.
➖Замок:всп.Гардиан  сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:Базательтовая плита.
➖Ночная задвижка: Да.
➖Глазок:ДА.
''', reply_markup=key_back5)

    elif c.data == 'two_b1':
        pic1 = open("2foto1.jpg", "rb")

        pic2 = open("2foto2.jpg", "rb")

        pic3 = open("2foto3.jpg", "rb")


        media28 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media28)
        bot.send_message(c.message.chat.id,'''Модель:Дверь стальная Министр
🎨Внешняя отделка
➖Фрезированная МДФ панель.
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:2050х880 /2050х980мм. 
➖Толщина полотна: 105 мм.
➖Замок:осн.Гардиан  цилиндрич.
➖Замок:всп.Гардиан  сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:Миниральная плита.
➖Ночная задвижка: Да.
➖Глазок:ДА.
''', reply_markup=key_back5)

    elif c.data == 'three_c1':
        pic1 = open("termoshel1.jpg", "rb")

        pic2 = open("termoshel2.jpg", "rb")

        pic3 = open("termoshel3.jpg", "rb")


        media28a = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media28a)
        bot.send_message(c.message.chat.id,'''Модель:Дверь стальная ТЕРМО-3 
🎨Внешняя отделка
➖Антик темное серебро.
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:2070х860 /2070х960мм. 
➖Толщина полотна: 115 мм.
➖Замок:осн.Гардиан  сувальдный.
➖Замок:всп.Гардиан  сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:комбинированный.
➖Ночная задвижка: Да.
➖Глазок:НЕТ.
➖Терморазрыв по раме и полотну.''', reply_markup=key_back5)

    elif c.data == 'Fore_d1':
        pic1 = open("emshelt1.jpg", "rb")

        pic2 = open("emshelt2.jpg", "rb")

        pic3 = open("emshelt3.jpg", "rb")


        media29 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media29)
        bot.send_message(c.message.chat.id,'''Модель:Терморазрыв Шелтер
🎨Внешняя отделка
➖Фрезированная МДФ панель.
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:2070х860 /2070х960мм. 
➖Толщина полотна: 115 мм.
➖Замок:осн.Kale  сувальдный.
➖Замок:всп.Kale  сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:комбинированный.
➖Ночная задвижка: Да.
➖Глазок:НЕТ.
➖Терморазрыв по раме и полотну.''', reply_markup=key_back5)

    elif c.data == 'five_i1':

        pic1 = open("bio1.jpg", "rb")

        pic2 = open("bio2.jpg", "rb")

        pic3 = open("bio3.jpg", "rb")

        pic4 = open("bio4.jpg", "rb")

        media30 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3),InputMediaPhoto(pic4)]

        bot.send_media_group(c.message.chat.id, media30)
        bot.send_message(c.message.chat.id,'''Модель:Дверь электронная взломостойкая Новатор
🎨Внешняя отделка
➖Щит Waterproof veneer .
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:2045х883 /2045х963мм. 
➖Толщина полотна: 120 мм.
➖Замок:Galion биометрический.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:комбинированный.
➖Ночная задвижка: Да.
➖Глазок:Да.''', reply_markup=key_back5)

 

    elif c.data == 'sex_f1':

        pic1 = open("new1.jpg", "rb")

        pic2 = open("new2.jpg", "rb")

        pic3 = open("new3.jpg", "rb")


        media32 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media32)
        bot.send_message(c.message.chat.id,'''Модель:Рубикон-1 Сандал белый
🎨Внешняя отделка
➖Медный Антик .
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:2050х860 /2050х960мм. 
➖Толщина полотна: 960 мм.
➖Замок:осн.Галион цилиндричес.
➖Замок:доп.Галион сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:комбинированный.
➖Ночная задвижка: Да.
➖Глазок:Да.''', reply_markup=key_back5)

    elif c.data == 'seven_j1':

        pic1 = open("new4.jpg", "rb")

        pic2 = open("new5.jpg", "rb")

        pic3 = open("new6.jpg", "rb")


        media33 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3)]

        bot.send_media_group(c.message.chat.id, media33)
        bot.send_message(c.message.chat.id,'''Модель:Термаль Экстра Лиственница бежевая
🎨Внешняя отделка
➖Медный Антик .
🔳Внутренняя отделка
➖Фрезированная МДФ панель .
➖Размеры:2050х860 /2050х960мм. 
➖Толщина полотна: 960 мм.
➖Замок:осн.Бордер сувальдный.
➖Замок:доп.Бордер сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:комбинированный.
➖Ночная задвижка: Да.
➖Глазок:НЕТ.
➖Терморазрыв рамы и полотна.''', reply_markup=key_back5)

    elif c.data == 'nine_h1':

        pic1 = open("a1.jpg", "rb")

        pic2 = open("a2.jpg", "rb")

        pic3 = open("a3.jpg", "rb")

        pic4 = open("a4.jpg", "rb")

        media34 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3),InputMediaPhoto(pic4)]

        bot.send_media_group(c.message.chat.id, media34)
        bot.send_message(c.message.chat.id,'''Модель:Рубикон-1 Зеркало Сандал белый
🎨Внешняя отделка
➖Медный Антик .
🔳Внутренняя отделка
➖МДФ панель с зеркалом .
➖Размеры:2050х860 /2050х960мм. 
➖Толщина полотна: 960 мм.
➖Замок:осн.Галион цилиндричес.
➖Замок:доп.Галион сувальдный.
➖Количество петель:3.
➖Уплотнитель: 3 контура. 
➖Утеплитель:комбинированный.
➖Ночная задвижка: Да.
➖Глазок:Да.''', reply_markup=key_back5)


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        logger.error(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)