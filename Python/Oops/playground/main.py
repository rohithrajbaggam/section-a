
class Calculator:

    def sum(self, a, b):
        return a + b 

    def sub(self, a, b):
        return a - b 
    
    def mul(self, a, b):
        return a * b

    def mod(self, a, b):
        return a%b 


class Expression(Calculator):

    def lhs(self, a, b):
        return (self.mul( 
            self.sum(a, b),  self.sum(a, b) 
            ) )

    def rhs(self, a, b):
        exp1 = self.sum( 
            self.mul(a, a), self.mul(b, b)
              )
        exp2 = self.sum(
            self.mul(a, b), self.mul(a, b)
        )
        return self.sum(exp1, exp2)

obj = Expression()

# print(obj.lhs(2, 3))
# print(obj.rhs(2, 3))
if obj.lhs(2, 3) == obj.rhs(2, 3):
    print("Expression is valid") 
else:
    print("Expression is invalid")




# math = Calculator()

# print(math.sum(2, 3))
# print(math.sub(2, 3))


# class Example:
#     name = "name"
    
#     def __init__(self, name):
#         self.name = name 
        
#     def __str__(self):
#         return "This is a example class"
         

#     def hello(self):
#         print(f"Hello, {self.name}")


# obj1 = Example("Max")
# # obj2 = Example()
# print(obj1)

# obj1.hello()
# obj1.hello()
# obj1.hello()

# print(obj1.name)
# print(obj2.name)



