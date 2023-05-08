import service.UserService
import service.MoneyService


def viewAllUsers():
    service.UserService.viewAll()

def addUser():
    service.UserService.addUser()

def deleteUser():
    service.UserService.deleteUser()

def getCheck():
    service.MoneyService.getCheck()

def enrollment():
    service.MoneyService.enrollment()

def consumption():
    service.moneyService.consumption()
