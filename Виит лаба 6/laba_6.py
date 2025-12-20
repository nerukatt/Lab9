class UserAccount:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.__password = password
    
    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль успешно изменен!")

    def check_password(self,password):
        return password==self.__password

user1=UserAccount('userr','mail@mail.com','parolyaka')
password2 = input("Введите новый пароль: ")
user1.set_password(password2)

u_pass = input("Введите пароль для проверки: ")
print(user1.check_password(u_pass))