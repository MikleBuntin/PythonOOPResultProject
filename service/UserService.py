import repository.repo
from model.User import User


def viewAll():
    repository.repo.viewAll();

def addUser():
    id = repository.repo.getNewID();
    name = input("Введите имя")
    check = input("Введите баланс")
    user = User(id, name, check)
    repository.repo.addUser(user)

def deleteUser():
    id = input("Введите ID")
    repository.repo.deleteUser(id)