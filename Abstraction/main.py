#parent class
class Person(object):
    #init_ _ is known as a constructor
    def __init__(self, name, idnumber) :
        self.name= name
        self.idnumber= idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
#child class  
class Employee(Person):
   def __init__(self, name,idnumber,salary,post):
      self.salary= salary
      self.post= post
      #invoking the init of the parent class
      Person.__init__(self,name,idnumber)
#creation of an object variable or an instance 
a= Employee('Penguin',20212024,15000,"Intern")
#callinhg a function of a class person using its instance
a.display()     