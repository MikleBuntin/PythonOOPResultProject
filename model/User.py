class User:
    def __new__(cls, id, name, check):
        return super().__new__(cls)

    def __init__(self, id, name, check):
        self.id = id
        self.name = name
        self.check = check

    def toString(self):
        return "User{" + "ID=" + str(self.id) + ", name=" + self.name + ", check=" + self.check + '}' + "\n"
