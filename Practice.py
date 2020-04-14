class Person:
    def __init__(self):
        self.name = None
        self.surname = None
        self.last_name = None
        self.age = None

    def user_input(self):
        self.name = input("Введите имя: ")
        self.surname = input("Введите фамилию :")
        self.last_name = input("Введите отчество:")
        self.age = int(input("Введите возраст: "))
        # people = {'first_name': name, 'surname': surname, 'last_name': last_name, 'age': age}

    def output(self):
        return "First name : {}\n" \
               "age        : {}\n" \
               "surname    : {}\n" \
               "last_name  : {}".format(self.name,
                                        self.surname,
                                        self.last_name,
                                        self.age)


ppp = Person()
ppp.user_input()
print(ppp.output())
