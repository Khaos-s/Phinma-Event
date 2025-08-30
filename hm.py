class Personas:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"My name is {self.name} and My age is {self.age}")
        
    def saludar(self):
        self.info()
        
            
            
    

mypersonals = Personas("Negga", "Black")
mypersonals.saludar()
            
            
