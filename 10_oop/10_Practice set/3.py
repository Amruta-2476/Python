# create a class with class attribute a, create an object from it and set 'a' directly using object.a = 0. Does this change the class attribut ?
class Test:
    a = "john"

object = Test()
object.a = "Vicky"
# this won't change the original class attribute, it will only affect object.a
print(object.a)  #Vicky
print(Test.a)  #john