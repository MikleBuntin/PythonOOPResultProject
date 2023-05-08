import controller.Controller



print("Добрый день!")
command = 0

while command != "Q":
    print("Доступные операции:\n"
        "1 - Просмотреть всех пользователей; \n" +
        "2 - Добавить пользователя \n" +
        "3 - Удалить пользователя \n" +
        "4 - Узнать баланс \n" +
        "5 - Зачислить средства \n" +
        "6 - Снять средства \n" +
        "Q - выйти")

    if command == "1":
        controller.Controller.viewAllUsers()
    elif command == "2":
        controller.Controller.addUser()
    elif command == "3":
        controller.Controller.deleteUser();
    elif command == "4":
        controller.Controller.getCheck();
    elif command == "5":
        controller.Controller.enrollment();
    elif command == "3":
        controller.Controller.consumption();

    command = input("Введите команду")
