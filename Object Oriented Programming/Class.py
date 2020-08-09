class person:
   def __init__(self,personName,height,age):
       self.name=personName
       self.height=height
       self.age=age
   def fix(self,newName):
       self.name=newName
   def getSummary(self):
       return f"Name: {self.name} Height: {self.height} Age: {self.age}"


b_person=person("JACK", "5.6", "22" )



print(b_person.getSummary())
b_person.fix("Jack Pritom Soren")
print(b_person.getSummary())


