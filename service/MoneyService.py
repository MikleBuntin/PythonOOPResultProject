import repository.repo
def getCheck():
    id = input("Введите ID")
    repository.repo.getCheck(id)

def enrollment():
    id = input("Введите ID")
    summ = input("Введите сумму")
    repository.repo.enrollment(id, summ)

def consumption():
    id = input("Введите ID")
    summ = input("Введите сумму")
    repository.repo.enrollment(id, int(summ)*-1)