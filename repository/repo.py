
def addUser(user):
    with open('UserList.csv', 'a', encoding="cp1251") as userList:
        userList.write(user.toString())

def viewAll():
    with open('UserList.csv', 'r', encoding="cp1251") as userList:
        print("All users: \n")
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
                 if id != int(delID):
                     users.append(line)

    open('UserList.csv', 'w').close()
    with open('UserList.csv', 'a') as userList:
        for line in users:
            userList.write(line)

def getCheck(getCheckID):
    with open('UserList.csv', 'r') as userList:
         for line in userList:
             if line != '':
                 id = int(line[line.find('ID=') + 3: line.find(', ')])
                 if id == int(getCheckID):
                     print(line[line.find('check=') + 6: line.find('}')])


def enrollment(id, summ):
    users = []
    with open('UserList.csv', 'r') as userList:
        for line in userList:
            if line != '':
                countID = int(line[line.find('ID=') + 3: line.find(', ')])
                if countID != int(id):
                    users.append(line)
                else:
                    newCheck = int(line[line.find('check=') + 6: line.find('}')]) + int(summ)
                    newLine = line[: line.find('check=') + 6] + str(newCheck) + '}'
                    users.append(newLine)



    open('UserList.csv', 'w').close()
    with open('UserList.csv', 'a') as userList:
        for line in users:
            userList.write(line)

