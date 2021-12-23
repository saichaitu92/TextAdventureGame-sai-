import random
from ctypes import util
import items, world
import sounds


class Player():
    def __init__(self):
        self.inventory = [items.Gold(150),items.BabyDragon(),items.PetTiger(),items.Wolfpack(),
                          items.PrivateArmy(),items.smallpotion1(),items.smallpotion2()]  # Inventory on startup
        self.hp = 1300  # Health Points
        self.maxhp = 1300
        self.location_x, self.location_y = world.starting_position  # (0, 0)
        self.victory = False # no victory on start up
        self.money = 50
        self.experience =0
        self.level=1
        self.attackpower=1000
        self.nextlevelup=10
        self.chosenFightingAnimal =None
        self.currentFightingAnimal=self.inventory[1]

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    def Escape(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
    def Surrender(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.FightingAnimals):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_FightingAnimals = i

        print("You use {} against {}!".format(best_FightingAnimals.name, enemy.name))
        enemy.hp -= best_FightingAnimals.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def Withdraw(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.FightingAnimals):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_FightingAnimals = i

        print("You use {} against {}!".format(best_FightingAnimals.name, enemy.name)) # changed best wepon to best fighting animals
        enemy.hp -= best_FightingAnimals.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def Heal(self):
        print("\n These are the potions ")
        potion_list = []
        for Potions in self.inventory:
            if isinstance(Potions, items.Potions):
                if Potions.amt <= 0:
                    self.inventory.remove(Potions)
                    continue
                else:
                     potion_list.append(Potions)
        i = 1
        for Potions in potion_list:
            print(i, " . ", Potions.name, sep='')
            i += 1
        while True:
              if len(potion_list) == 0:
                  print("you have no potion")
                  return None
              itemchoice = int(input("\nselect potion")) - 1
              if itemchoice not in range(0, len(potion_list)):
                   print("invalid choice")
                   continue
              break
        self.healtoplayer(itemchoice, potion_list)
       # sounds.drink()

    def healtoplayer(self, itemchoice, potionlist):
        chosenpotion = potionlist[itemchoice]
        print("\n you were healed for {} ", format(chosenpotion.health))
        print('hp. \n')
        self.hp = self.hp + chosenpotion.health
        chosenpotion.amt = chosenpotion.amt = 1
        if chosenpotion.amt == 0:
           self.inventory.remove(chosenpotion)
        if self.maxhp < self.hp:
           self.hp = self.maxhp
        sounds.drink()

    # is_alive method
    def is_alive(self):
        return self.hp > 0  # Greater than zero value then you are still alive

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def Assign(self):
        print("\n Available weapons: ")
        FightingAnimals_list =[]
        for item in self.inventory:
             if isinstance(item,items.FightingAnimals):
                 FightingAnimals_list.append(item)
        i =1
        for FightingAnimals in FightingAnimals_list:
            print(i, ".",FightingAnimals.name, sep='')
            i+=1

        while True:
            itemChoice = int(input(""" \n select the Fighting Animal and Assign: """))
            if itemChoice not in range(0,len(FightingAnimals_list)):
                print("\n Invalid choice")
       #         sounds.no()
                continue
            break
        print('\n')
        print(FightingAnimals_list[itemChoice].name, "Assigned.\n")
        self.currentFightingAnimal = FightingAnimals_list[itemChoice]


    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_FightingAnimals = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.FightingAnimals):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_FightingAnimals = i

        print("You use {} against {}!".format(best_FightingAnimals.name, enemy.name))
        enemy.hp -= best_FightingAnimals.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("You were killed! \n  {} HP is {}.".format(enemy.name, enemy.hp))


    def Status(self):
        print("\n you are level {} \n".format(self.level))
        print("***Current Hp*** {}/".format(self.hp), "{}\n",format(self.maxhp))
        print("***Attack power *** {}\n".format(self.attackpower))
        print("***Total XP *** {}\n".format(self.experience))
        print("*** XP until next level up : *** {}\n".format(self.nextlevelup - self.experience))


    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)