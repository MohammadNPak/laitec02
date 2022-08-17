database_address = 'db.txt'


def register(username, password):
    with open(database_address, 'a+', encoding='utf8') as f:
        f.seek(0)
        for line in f.readlines():
            # data = line.split(',')
            # u = data[0]
            # p = data[1]
            u, p = line.split(',')
            if u == username:
                return False
        f.write(f"\n{username},{password}")
        return True


def login(username, password):
    with open(database_address, 'r', encoding='utf8') as f:
        for line in f.readlines():
            u, p = line.split(',')
            if u == username and p[:-1] == password:
                return True
        return False


print(login("mohammad", "123"))
# print(register("mohammad1", "345"))
# print(register("ahmad1", "345"))
