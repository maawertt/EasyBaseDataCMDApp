import os
import csv
from typing import List
from Menu import *

def deco_write_person(func: Callable[[str, str], None]) -> Callable:
    def wrapper(self, *args, **kwargs):
        name_user: str = input('Введите имя пользователя: ')
        name_group: str = input('Введите имя группы: ')
        func(self, name_user, name_group)
        input('Нажмите любую кнопку чтобы продолжить чтобы продолжить: ')
        Menu.clear_console()
    return wrapper

def deco_write(func: Callable[None]) -> Callable:
    def wrapper(self):
        func(self)
        input('Нажмите любую кнопку чтобы продолжить чтобы продолжить: ')
        Menu.clear_console()
    return wrapper

def func_reader(name_file: str) -> List[List[str]]:
    with open(name_file, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        rows = [row for row in reader]
    return rows

class Handler:

    def __init__(self):
        pass

    @deco_write_person
    def append_user(self, name_user: str, name_group: str, name_file: str = 'DataList.csv') -> None:
        file_exists = os.path.isfile(name_file)

        rows: List[List[str]] = func_reader(name_file)

        if not([name_user, name_group] in rows):
            with open(name_file, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=';')
                if not file_exists:
                    writer.writerow(['nameUser', 'groupName'])
                writer.writerow([name_user, name_group])
                print(f"\nПользователь '{name_user}' добавлен!")
        else: print(f"\nПользователь '{name_user}' уже есть в базе!")

    @deco_write_person
    def del_user(self, name_user: str, name_group: str, name_file: str = 'DataList.csv') -> None:
        file_exists = os.path.isfile(name_file)
        if not file_exists:
            print(f"\nФайл '{name_file}' Пустой."); return

        rows: List[List[str]] = func_reader(name_file)
        new_rows = [row for row in rows if row != [name_user, name_group]]

        if len(new_rows) != len(rows):
            with open(name_file, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=';')
                for row in rows:
                    writer.writerow(row)
            print(f"\nПользователь '{name_user}' удалён!.")
        else: print(f"\nПользователь '{name_user}' не найден")

    @deco_write
    def print_users_list(self, name_file: str = 'DataList.csv', **kwargs) -> None:
        rows: List[List[str]] = func_reader(name_file)
        if not kwargs:
            for row in rows:
                print(*row)
            return



