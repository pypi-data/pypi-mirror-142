class calculator:
    def __init__(self):
        print('''                           Utsav's Basic Calculator
              
              Guide : 1) To Add two number use code [o.sum(a,b)](o is the object of the class you created) --> returns a + b
                      2) To Subtract two number use code [o.sub(a,b)] --> returns a - b
                      3) To Multiply two number use code [o.mul(a,b)] --> returns a * b
                      4) To Divide two numbers use code [o.div(a,b)] --> returns a/b ''')
              
              
        
    def sum(self,num1,num2):
        return num1 + num2

    def sub(self,num1,num2):
        return num1 - num2

    def mul(self,num1,num2):
        return num1 * num2
    
    def div(self,num1,num2):
        return num1 / num2
