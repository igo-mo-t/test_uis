from project import app
from project.functions import *



@app.route('/task_1')
def task_1() -> dict[str, int]:
    """
    Получает аргументы запроса (даты) и возвращает с ними вызов функции,
    получающей количество дней между этими датами.
    При неверно введенных аргументах запроса вернет сообщение.
    """
    request_args = get_request_args_for_task_1()
    
    try:
        return days_between_dates(request_args['date1'], request_args['date2'])
    except Exception:
        return 'Request arguments must be in the format: \'date1=YYYY-MM-DD&date2=YYYY-MM-DD\''



@app.route('/task_2')
def task_2() -> str:
    """
    Получает аргументы запроса (целое положительное число в виде строки и целое число k) 
    и возвращает с ними вызов функции, получающей минимальное возможное число, 
    полученное после удаления из строки k цифр.
    """
    try:
        request_args = get_request_args_for_task_2()

        return remove_k_digits(request_args['num'], request_args['k'])
    
    except IndexError:
        return '\'k\' must be less than the number of digits in \'num\''
    except Exception: 
        return 'Request arguments must be in the format: \'num=12345&k=3\'. \'k\' and \'num\' must be positive. '
    
   



@app.route('/task_3')
def task_3()  -> dict[str, Any]:
    """
    Возвращает вызов функции, получающей список соответствий "долг-платёж", 
    а также список платежей, которые не нашли себе долг.
    """
    
    return get_list_of_not_used_payments_and_payment_table()        