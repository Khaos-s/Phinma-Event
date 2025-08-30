class calculatoris():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
    def  calculator_info(self):
        print(f"Calculator info: Brand: {self.brand}, Color: {self.color}")

    def add(self, num1, num2):
        result = num1 + num2
        self.calculator_info()
        print(f"The Addition of {num1} and {num2}  is: {result}")
        return result

        
    def subtract(self, num1, num2):
        result = num1 - num2
        self.calculator_info()
        print(f"The Subtraction of {num1} and {num2}  is: {result}")
        return result
        
    def multiply(self, num1, num2):
        result = num1 * num2 
        self.calculator_info()
        print(f"The multiplication of {num1} and {num2}  is: {result}")
        return result
        


        
    def divide(self, num1, num2):
        result = num1 / num2
        self.calculator_info()
        if num2 == 0:
            print("Error:  Division by zero is not allowed")
        else:
            print(f"The Division of {num1} and {num2}  is: {result}")
            return result
        
        
my_calculi = calculatoris("Casio", "Black")

my_calculi.add(10,10)

my_calculi.subtract(10,5)

my_calculi.multiply(5,5)

my_calculi.divide(15,3)