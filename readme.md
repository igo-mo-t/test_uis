Тестовое задание

1. Запуск приложения

    - должен быть установлен Docker

    - пример установки Docker для Mac:
        https://www.cprime.com/resources/blog/docker-for-mac-with-homebrew-a-step-by-step-tutorial/

    - комманда для запуска приложения в терминале Mac:
        docker-compose up -d --build

    - запуск тестов через pytest в терминале из докера:
        python -m pytest -v    


2. Структура приложения

APP3/ - основная папка проекта
    
    APP3/project - папка проекта с основными файлами .py
        APP3/project/__init__.py  - файл инициализации пакета приложения с объектами приложения и БД   
        APP3/project/functions.py - файл с определяемыми функциями приложения
        APP3/project/models.py - модель данных
        APP3/project/views.py - функции-обработчики эндпоинтов
    
    APP3/tests - папка с тестами
        APP3/tests/__init__.py - файл инициализации пакета
        APP3/tests/test_functions.py - файл с тестами
    
    manage.py - настройка запуска приложения

    docker-entrypoint.sh - файл определяющий команды терминала для запуска приложения

    _.dev/yml/md/txt - прочие файлы(Докер,зависимости и т.д)


3. Реализация задания

    Решения оформлены в виде HTTP-запросов с методами GET. Входные данные передаются через аргументы запроса.

   
    - Задача 1.
    Даны две даты в виде строк формата YYYY-MM-DD. Посчитать количество дней между
    этими датами без использования библиотек.

    Пример решения:
        Запрос:
        http://127.0.0.1:5000/task_1?date1=2020-01-15&date2=2019-12-14
        
        Ответ:
        {"Number of days between dates":31}

    
    - Задача 2.
    Дано целое положительное число "num", представленное в виде строки, и целое
    число "k". Вернуть минимальное возможное число, полученное после удаления из
    строки k цифр.

    Пример решения:
        Запрос:
        http://127.0.0.1:5000/task_2?num=135353&k=2
        
        Ответ:
        {"The minimum number after removing 'k' digits from the string 'num'":"1333"}


    - Задача 3.
    Есть две коллекции (таблицы) данных: accrual (долги) и payment (платежи). Обе
    коллекции имеют поля:
    * id
    * date (дата)
    * month (месяц)
    Необходимо написать функцию, которая сделает запрос к платежам и найдёт для
    каждого платежа долг, который будет им оплачен. Платёж может оплатить только
    долг, имеющий более раннюю дату. Один платёж может оплатить только один долг, и
    каждый долг может быть оплачен только одним платежом. Платёж приоритетно должен
    выбрать долг с совпадающим месяцем (поле month). Если такого нет, то самый
    старый по дате (поле date) долг.
    Результатом должна быть таблица найденных соответствий, а также список платежей,
    которые не нашли себе долг.
    Запрос можно делать к любой базе данных (mongodb, postgresql или другие) любым
    способом

    Пример решения:
        Запрос:
        http://127.0.0.1:5000/task_3
        
        Ответ:

        {
    "Accrual, Payment": [
        [
            {
                "date": "2023-01-25",
                "id": 1,
                "month": 1
            },
            {
                "date": "2023-06-28",
                "id": 5,
                "month": 6
            }
        ],
        [
            {
                "date": "2023-02-25",
                "id": 2,
                "month": 2
            },
            {
                "date": "2023-06-29",
                "id": 6,
                "month": 6
            }
        ],
        [
            {
                "date": "2023-03-25",
                "id": 3,
                "month": 3
            },
            {
                "date": "2023-03-28",
                "id": 1,
                "month": 3
            }
        ],
        [
            {
                "date": "2023-04-25",
                "id": 4,
                "month": 4
            },
            {
                "date": "2023-04-28",
                "id": 2,
                "month": 4
            }
        ],
        [
            {
                "date": "2023-04-27",
                "id": 5,
                "month": 4
            },
            {
                "date": "2023-04-29",
                "id": 3,
                "month": 4
            }
        ],
        [
            {
                "date": "2023-05-25",
                "id": 6,
                "month": 5
            },
            {
                "date": "2023-05-27",
                "id": 4,
                "month": 5
            }
        ],
        [
            {
                "date": "2023-05-27",
                "id": 7,
                "month": 5
            },
            {
                "date": "2023-07-25",
                "id": 7,
                "month": 7
            }
        ]
    ],
    "List of not used payments": [
        {
            "date": "2023-07-28",
            "id": 8,
            "month": 7
        },
        {
            "date": "2023-08-25",
            "id": 9,
            "month": 8
        },
        {
            "date": "2023-09-25",
            "id": 10,
            "month": 9
        }
    ]
}
