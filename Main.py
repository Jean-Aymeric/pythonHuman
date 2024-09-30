from Boxer import Boxer
from Human import Human
from Shirt import Shirt

paul = Human()
gabriel = Human()

gabriel.wear(Boxer())
gabriel.wear(Shirt())

paul.wear(Boxer())
paul.wear(Shirt())

brain = paul.harvest("Cerveau")
gabriel.harvest("Cerveau")
gabriel.transplant(brain)

print(paul)
print(gabriel)
