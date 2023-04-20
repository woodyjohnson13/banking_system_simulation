
#Parent class
class User():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age 
        self.gender=gender
        
        
    def deatils(self):
        print("User Details")
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
        print(f'Gender:{self.gender}')
        
    