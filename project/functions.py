from . import db
from project.models import Accrual, Payment



def days_between_dates(date1, date2):
    year1, month1, day1 = map(int, date1.split('-'))
    year2, month2, day2 = map(int, date2.split('-'))
    
    # количество дней в каждой из дат, начиная с 1 января года 0
    days1 = day1 + 365 * year1 + (year1 // 4) - (year1 // 100) + (year1 // 400) + ((month1 * 306 + 5) // 10) - 307
    days2 = day2 + 365 * year2 + (year2 // 4) - (year2 // 100) + (year2 // 400) + ((month2 * 306 + 5) // 10) - 307
    
    # разница между количеством дней в двух датах
    return abs(days2 - days1)

def remove_k_digits(num: str, k: int) -> str:
    stack = []
    for digit in num:
        while stack and k and digit < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0:
        stack.pop()
        k -= 1
    return ''.join(stack).lstrip('0') or '0'


def get_accrual_list():
    accrual_list = db.session.query(Accrual.id, Accrual.date, Accrual.month).order_by(Accrual.month).all()
    return accrual_list


def get_payment_list():
    payment_list = db.session.query(Payment.id, Payment.date, Payment.month).order_by(Payment.month).all()
    return payment_list

def get_payment_table_and_remaining_payment_list():
    """
    функция приводит в соответствие долги и платежи, принимает курсор БД sqlite3
    обращается к таблицам платежей и долгов и приводит их в соответствие в 2 этапа:
    сперва в соответствие долгам приводятся платежи совпадающие с ними по месяцу, и имеющие более позднюю дату
    затем остальные, имеющие более позднюю дату в порядке от самых старых долгов
    :param cursor:
    :return: таблица распределенных платежей в виде списка, а также список не нашедших соответствия платежей
    """

    # при выборке из БД упорядочиваем по возрастанию даты платежей и долгов
    # sql = "SELECT * FROM accrual ORDER BY month, date"
    # cursor.execute(sql)
    accrual_list = get_accrual_list()

    # sql = "SELECT * FROM payment ORDER BY month, date"
    # cursor.execute(sql)
    payment_list = get_payment_list()

    # создаем словарь с ключами в виде долгов, которым в соответствие будем приводить id платежей.
    payment_table = {accrual: None for accrual in accrual_list}

    # проверка и присваивание первого этапа, более приоритетная
    for accrual in payment_table:
        if not payment_table[accrual]:
            for payment in payment_list:
                if accrual[2] == payment[2] and accrual[1] < payment[1]:
                    payment_table[accrual] = payment
                    payment_list.remove(payment)
    
    return payment_table, payment_list                


def get_list_of_not_used_payments_and_payment_table():
    payment_table_and_remaining_payment_list = get_payment_table_and_remaining_payment_list()
    payment_table = payment_table_and_remaining_payment_list[0]
    payment_list = payment_table_and_remaining_payment_list[1]
    # здесь будут храниться платежи, которые не нашли себе долга
    list_of_not_used_payments = []

    # проверка и присваивание второго этапа, оставшиеся платежи
    searching = True
    while searching:
        if payment_list:
            for accrual in payment_table:
                if not payment_table[accrual]:
                    for payment in payment_list:
                        if payment[2] < accrual[2] or payment[2] == accrual[2] and payment[1] < accrual[1]:
                            list_of_not_used_payments.append(payment)
                            payment_list.remove(payment)
                        else:
                            payment_table[accrual] = payment
                            payment_list.remove(payment)
                        break
                    break
        else:
            searching = False
        if all(payment_table.values()):
            # Добавляем в список оставшиеся платежи
            list_of_not_used_payments.extend(payment_list)
            searching = False
            
    return list_of_not_used_payments, payment_table    

    # Создадим список с кортежами из долгов и платежей.
def get_list():
    list_of_not_used_payments_and_payment_table = get_list_of_not_used_payments_and_payment_table()
    payment_table = [(accrual, payment) for accrual, payment in list_of_not_used_payments_and_payment_table[1].items()]
    return payment_table
    # return payment_table, list_of_not_used_payments

