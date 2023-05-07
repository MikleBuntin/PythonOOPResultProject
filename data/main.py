# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# package org.example.data;
#
# import org.example.controller.Controller;
#
# import java.io.IOException;
# import java.util.Scanner;


print("Добрый день!")
command = 0

while command != "Q":
    print("Доступные операции:"
        "1 - Просмотреть всех пользователей; \n" +
        "2 - Добавить пользователя \n" +
        "3 - Удалить пользователя \n" +
        "4 - Узнать баланс \n" +
        "5 - Зачислить средства \n" +
        "6 - Снять средства \n" +
        "Q - выйти")

    if command == "1":
        userController.viewAllUsers()
    elif command == "2":
        userController.addUser()
    elif command == "3":
        Controller.deleteUser();
    elif command == "4":
        Controller.getCheck();
    elif command == "5":
        Controller.enrollment();
    elif command == "3":
        Controller.consumption();

    command = input("Введите команду")
