import axelrod as axl

from match import play_different_stategies, play_with_human
from typing import Iterable


def test_input(value, correct_values: Iterable) -> bool:
    if value in correct_values:
        return True
    return False


def get_correct_option(correct_values: Iterable) -> str:
    option = input("Выберите вариант: ")
    while not test_input(option, correct_values):
        input("Выбран неверный вариант, повторите: ")
    return option


def ask_strategy():
    correct_values = ["1", "2", "3", "4", "5"]
    menu = """
    1. Кооператор
    2. Предатель
    3. Око за око
    4. Завистливая
    5. Выйти
    """

    print(menu)
    option = get_correct_option(correct_values)

    if option == "1":
        return axl.Cooperator()
    elif option == "2":
        return axl.Defector()
    elif option == "3":
        return axl.TitForTat()
    elif option == "4":
        return axl.Grudger()
    elif option == "5":
        exit()


def main_menu():
    correct_values = ("1", "2", "3")
    menu = """
    1. Сыграть ряд матчей
    2. Сыграть самому
    3. Выйти
    """

    print(menu)
    option = get_correct_option(correct_values)

    if option == "1":
        players = [
            axl.Cooperator(),
            axl.Defector(),
            axl.TitForTat(),
            axl.Grudger(),
        ]
        play_different_stategies(players)
    elif option == "2":
        player = ask_strategy()
        play_with_human(player)
    elif option == "3":
        exit()
