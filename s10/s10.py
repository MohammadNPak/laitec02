

# class Student:
#     hands: int = 2
#     eyes: int = 2

#     def __init__(self, name: str) -> None:
#         self.name = name
#         print(f"hello from init {self}")


# s1 = Student("mohammad")
# s2 = Student("ali")
# print(type(s1))
# print(s1.name)
# print(s2.name)
# print(s2.eyes)
# print(s1.eyes)


# def a(a,c, b=None ):
#     pass

# a(0,0,1)




class Car:
  door=4

  def __init__(self,id,model=None) -> None:
    self.id=id
    self.model=model
    self.color=None
    
  def set_color(self,color):
    self.color = color


a=Car(123)
a.set_color("red")

print(a.color)