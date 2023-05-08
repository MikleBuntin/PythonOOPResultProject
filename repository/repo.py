
def addUser(user):
    with open('UserList.csv', 'a', encoding="cp1251") as userList:
        userList.write(user.toString())

def viewAll():
    with open('UserList.csv', 'r', encoding="cp1251") as userList:
        for line in userList:
            print(line)

def getNewID():
    with open('UserList.csv', 'r') as userList:
        max_id = 0
        for line in userList:
            if line != '':
                id = int(line[line.find('ID=') + 3: line.find(', ')])
                if id > max_id:
                    max_id = id
    return max_id + 1

def deleteUser(delID):
    users = []
    with open('UserList.csv', 'r') as userList:
         for line in userList:
             if line != '':
                 id = int(line[line.find('ID=') + 3: line.find(', ')])
                 if id != delID:
                     users.append(line)

    open('UserList.csv', 'w').close()
    with open('UserList.csv', 'a') as userList:
        for line in users:
            userList.write(line)
