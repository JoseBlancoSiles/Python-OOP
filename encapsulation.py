# Encapsulation in OOP is used to hide attributes and methods to be only used internally

class DataEngineer:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.__salary = 5000
    self.__onboarded_datasets = 0
  
  # getter function
  def get_salary(self):
    return self.__salary
  
  # setter function
  def set_salary(self, value):
    self.__salary = value
    
  def onboard_dataset(self):
    self.__onboarded_datasets += 1
    
  def get_datasets(self):
    return self.__onboarded_datasets
    
# attributes starting with "__" are considered as private and can't be accessed from outisde
# the function. An error will be raised if you try the following code:

de = DataEngineer("Jose", 25)
# print(de.__salary)

# However, you can access and modify this private attributes using getter and setter functions

print(de.get_salary()) # --> 5000

for i in range(100):
  de.onboard_dataset()

print(de.get_datasets())