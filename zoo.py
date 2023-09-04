# Creating a Zoo simulation using classes and implementing various features within this simulation.

# Define the base class Animal
class Animal:
  def __init__(self, name, species, sound):
    ''' Every animal is defined by a name, specie and sound'''
    self.name = name
    self.species = species
    self.sound = sound
  
  def make_sound(self):
    print("The animal", self.name, "has the sound:", self.sound)
    
# Define the Zoo class --> composed of a list of animals
class Zoo:
  def __init__(self):
    self.animals = []
    
  def add_animal(self, animal):
    self.animals.append(animal)
  
  def make_sounds(self):
    '''Polymorphism --> using a method from the Animal class in the Zoo class'''
    for animal in self.animals:
      print(animal.make_sound())
      
class Lion(Animal):
  '''Inheritance --> Inherit the class parent Animal. Initialize sound with a characteristic sound for lions'''
  def __init__(self, name, species, sound="roar"):
    super().__init__(name, species, sound)
    
# Create instances of animals
dog = Animal("dog", "mammal", "woof")
cat = Animal("cat", "mammal", "miau")
frog = Animal("frog", "amphibian", "croack")
lion = Lion("lion", "mammal")

# Creat an instance of a Zoo
zoo = Zoo()

# Add animal instances to the zoo
zoo.add_animal(dog)
zoo.add_animal(cat)
zoo.add_animal(frog)
zoo.add_animal(lion)

# Make all animals in the zoo make their sounds
zoo.make_sounds()