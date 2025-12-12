#on this we will run test
def weather(temp):
    if temp>20:
        return "hot"
    else:
        return "cold"
def divider(a,b):
    if b==0:
        raise ValueError("cannot divide by zero")
    else:
        return a/b
class UserManager:
    def __init__(self):
        self.users = {}
    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username]=email
        return True
    def get_user(self, username):
        return self.users.get(username) #dictionary method
def is_prime(n):
    if n<2:
        return False 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False 
    return True 
    