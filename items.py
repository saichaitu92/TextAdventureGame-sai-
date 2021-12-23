# Base class for all items
import sounds


class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name  # attribute of the Item class and any subclasses
        self.description = description  # attribute of the Item class and any subclasses
        self.value = value  # attribute of the Item class and any subclasses

    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


# Extend the Items class
# Gold class will be a child or subclass of the superclass Item
class Gold(Item):
    # __init__ is the contructor method
    def __init__(self, amt):
        self.amt = amt  # attribute of the Gold class
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class FightingAnimals(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class BabyDragon(FightingAnimals):
    def __init__(self):
        super().__init__(name="BabyDragon",
                         description=" BabyDragon throws the fire ",
                         value=800,
                         damage=500)
      #  sounds.babydragon()
class Dragon(FightingAnimals):
    def __init__(self):
        super().__init__(name="Dragon",
                         description=" Dragon throws the fire ",
                         value=1000,
                         damage=800)
       # sounds.Dragon()
class Wolfpack(FightingAnimals):
    def __init__(self):
        super().__init__(name="Wolfpack",
                         description=" A pack of wolfs kills the enemys ",
                         value=200,
                         damage=100)
      #  sounds.wolfpack()
class PetTiger(FightingAnimals):
    def __init__(self):
        super().__init__(name ="petTiger",
                         description=" tiger helps in war to kill enemys ",
                         value=500,
                         damage=300)
      #  sounds.petTiger()

class Army(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


# Extend the Items class
# Gold class will be a child or subclass of the superclass Item
class Gold(Item):
    # __init__ is the contructor method
    def __init__(self, amt):
        self.amt = amt  # attribute of the Gold class
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)


class PrivateArmy(Army):
    def __init__(self):
        super().__init__(name="Private Army",
                         description="A private army for backup supports",
                         value=500,
                         damage=700)
       # sounds.Privatearmy()

class Gaints(Army):
    def __init__(self):
        super().__init__(name="Gaints Army",
                         description="Gaints for support in war",
                         value=400,
                         damage=500)
        #sounds.Gaints()
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)
        #sounds.dragger()


class Loot(Item):
        def __init__(self, name, description,value, amt):
            self.amt = amt
            super().__init__(name, description, value,amt)

        def __str__(self):
            return "{}\n=====\n{}\nValue: {}\n Gold: {}".format(self.name, self.description, self.value, self.amt)


class Money(Loot):
    def __init__(self):
        super().__init__(name="Gold coins",description=" A bag of gold coins",value= 70,
                         amt=100)

class Silver(Loot):
    def __init__(self):
        super().__init__(name="silver coins",description=" A bag of silver coins",value=60,
                         amt=100)


class Pistol(Weapon):
    def __init__(self):
        super().__init__(name="Pistol",
                         description="pistol with bullets good to use for Dangerous and good animals",
                         value=40,
                         damage=40)
        #sounds.pistol()
class Potions(Item):
    def __init__(self, name, description, value, amt, health):
        self.amt = amt
        self.health = health
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHealth: {}".format(self.name, self.description, self.value,self.amt, self.health)


class smallpotion1(Potions):
    def __init__(self):
        super().__init__(name="potion",
                         description="potion which helps increase hp ",
                         value=50,
                         amt=1,
                         health=200)
        #sounds.drink()
class smallpotion2(Potions):
    def __init__(self):
        super().__init__(name="potion",
                         description="potion which helps increase hp ",
                         value=50,
                         amt=2,
                         health=150)
        #sounds.drink()