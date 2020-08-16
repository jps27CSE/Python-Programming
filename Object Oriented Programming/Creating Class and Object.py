class Person:

    name= 'Jack'

    def __init__(self,name,age):

        self.name=name
        self.age=age


input1=Person("jack",22)

input2=Person("pritom",20)

print("{}".format(input1.__class__.name))

print("My name is {} and i am {} years old".format(input1.name,input1.age))