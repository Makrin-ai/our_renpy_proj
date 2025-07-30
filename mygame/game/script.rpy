# Определение персонажей
define e = Character('Эйлин', color="#c8ffc8")
define m = Character('Мия', color="#ffc8c8")

# Начало игры
label start:

    scene bg room
    show eileen happy

    e "Привет! Добро пожаловать в нашу игру на Ren'Py."
    e "Хочешь узнать, что будет дальше?"

    menu:
        "Да, конечно!":
            jump good_path

        "Нет, я просто смотрю.":
            jump neutral_path

label good_path:

    scene bg park with fade
    show eileen happy

    e "Супер! Тогда вперёд в приключения!"
    m "Привет! Я Мия. Я тоже с вами!"

    return

label neutral_path:

    scene bg street with fade
    show eileen neutral

    e "Ну ладно. Просто посмотри, что мы тут делаем :)"
    e "Если передумаешь — возвращайся!"

    return
