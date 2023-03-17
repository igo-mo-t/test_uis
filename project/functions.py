from . import db
from flask import request
from project.models import Accrual, Payment
from typing import Any


def get_request_args_for_task_1() -> dict[str, Any]:
    """
    Определяет аргументы запроса и возвращает их в словаре.
    """
    date1 = request.args.get("date1")
    date2 = request.args.get("date2")

    return {"date1": date1, "date2": date2}


def get_request_args_for_task_2() -> dict[str, Any]:
    """
    Определяет аргументы запроса и возвращает их в словаре.
    """
    num = request.args.get("num")
    k = request.args.get("k")

    if k[0] == "-" or num[0] == "-":
        raise Exception("'k' must be accepted")

    return {"num": num, "k": int(k)}


def days_between_dates(date1: str, date2: str) -> dict[str, int]:
    """
    Определяет количество дней в каждой из 2-х дат аргументов, начиная с 1 января года 0
    и возвращает словарь с разницей между количеством дней в датах.
    """
    year1, month1, day1 = map(int, date1.split("-"))
    year2, month2, day2 = map(int, date2.split("-"))

    days1 = (
        day1
        + 365 * year1
        + (year1 // 4)
        - (year1 // 100)
        + (year1 // 400)
        + ((month1 * 306 + 5) // 10)
        - 307
    )
    days2 = (
        day2
        + 365 * year2
        + (year2 // 4)
        - (year2 // 100)
        + (year2 // 400)
        + ((month2 * 306 + 5) // 10)
        - 307
    )

    return {"Number of days between dates": abs(days2 - days1)}


def remove_k_digits(num: str, k: int) -> str:
    """
    Принимает целое положительное число в виде строки и целое число k
    и возвращает словарь с минимальным возможным числом строкой,
    полученным после удаления из строки k цифр.
    """
    stack = []
    for digit in num:
        while stack and k and digit < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0:
        stack.pop()
        k -= 1

    return {
        "The minimum number after removing 'k' digits from the string 'num'": "".join(
            stack
        ).lstrip("0")
        or "0"
    }


def get_accrual_list() -> list[tuple]:
    """
    Получает из БД и возвращает список кортежей долгов.
    """
    accrual_list = (
        db.session.query(Accrual.id, Accrual.date, Accrual.month)
        .order_by(Accrual.month)
        .all()
    )

    return accrual_list


def get_payment_list() -> list[tuple]:
    """
    Получает из БД и возвращает список кортежей платежей.
    """
    payment_list = (
        db.session.query(Payment.id, Payment.date, Payment.month)
        .order_by(Payment.month)
        .all()
    )

    return payment_list


def get_payment_table_and_remaining_payment_list() -> (
    tuple[dict[tuple, tuple], list[tuple]]
):
    """
    Функция приводит в соответствие долги и платежи, совпадающие по месяцу.
    Возвращает кортеж со словарем соответствий и списком с кортежами оставшихся платежей.
    """
    accrual_list = get_accrual_list()
    payment_list = get_payment_list()
    payment_table = {accrual: None for accrual in accrual_list}

    for accrual in payment_table:
        if not payment_table[accrual]:
            for payment in payment_list:
                if accrual[2] == payment[2] and accrual[1] < payment[1]:
                    payment_table[accrual] = payment
                    payment_list.remove(payment)

    return payment_table, payment_list


def get_list_of_not_used_payments_and_payment_table() -> dict[str, Any]:
    """
    Функция приводит в соответствие долги и платежи, несовпадающие по месяцу,
    и создает отдельный список неиспользованных платежей.
    Возвращает словарь со списком словарей "долг-платёж" и списком платежей, которые не нашли себе долг.
    """
    payment_table_and_remaining_payment_list = (
        get_payment_table_and_remaining_payment_list()
    )
    payment_table = payment_table_and_remaining_payment_list[0]
    payment_list = payment_table_and_remaining_payment_list[1]
    list_of_not_used_payments = []

    searching = True
    while searching:
        if payment_list:
            for accrual in payment_table:
                if not payment_table[accrual]:
                    for payment in payment_list:
                        if (
                            payment[2] < accrual[2]
                            or payment[2] == accrual[2]
                            and payment[1] < accrual[1]
                        ):
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
            list_of_not_used_payments.extend(payment_list)
            searching = False

    return {
        "Accrual, Payment": [
            [
                {"id": accrual[0], "date": str(accrual[1]), "month": accrual[2]},
                {"id": payment[0], "date": str(payment[1]), "month": payment[2]},
            ]
            for accrual, payment in list(payment_table.items())
        ],
        "List of not used payments": [
            {"id": id, "date": str(date), "month": month}
            for id, date, month in list_of_not_used_payments
        ],
    }
