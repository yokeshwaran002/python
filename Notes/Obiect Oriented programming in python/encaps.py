class InstagramPass:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  
    def get_password(self):
        return self.__password
    def set_password(self, new_password):
        self.__password = new_password
    def check_password(self, password_to_check):
        return self.__password == password_to_check
p = InstagramPass("user123", 1234567890)
print(p.get_password()) 

passward=int(input("Enter the password:"))
if p.check_password(passward):
    print("Password is correct")
else:
    print("Password is incorrect")


