import items, eneimes, actions, world
from game import play


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []

        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
#        moves.append(actions.equip())
        return moves




class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyKingdom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Attack(enemy=self.enemy),
                    actions.Escape(tile=self),actions.Assign(tile=self), actions.Heal(tile=self),
                    actions.Status(tile=self)]
        else:
            return self.adjacent_moves()



class StartRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
        you were in initial room  of game play 
        prepare yourself to fight and find items in the rooms.....
        """

    def modify_player(self, player):
        # Room has no action on player
        pass





class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass



class TheNorth(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.TheNorth())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The  stark soldiers are ready to fight!
            """
        else:
            return """
            The kingdom defeated and you are their king!....
            """

class TheVale(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.TheVale())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The house of arryans soldiers are ready to fight!
            """
        else:
            return """
            The kingdom defeated and you are their king!....
            """
class TheIronIlands(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.TheIronIlands())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The TheIronIlands soldiers are ready to fight!
            """
        else:
            return """
            The kingdom defeated and you are their king!....
            """
class TheRiverland(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.TheRiverland())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The TheRiverland soldiers are ready to fight!
            """
        else:
            return """
            The kingdom defeated and you are their king!....
            """

class TheWesterLands(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.TheWesterLands())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The TheWesterLands soldiers are ready to fight!
            """
        else:
            return """
            The kingdom defeated and you are their king!....
            """

class TheStromlands(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.TheStromlands())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The TheStromlands soldiers are ready to fight!
            """
        else:
            return """
            The kingdom defeated and you are their king!....
            """
class TheReach(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.TheReach())

    def intro_text(self):
        #sounds.no()
        if self.enemy.is_alive():
            return """
            The TheReach soldiers are ready to fight!
            """
        else:
            return """
            The kingdom defeated and you are their king!....
            """


class TheCrownlands(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.TheCrownlands())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The TheCrownlands soldiers are ready to fight!
            """
        else:
            return """
            The kingdom defeated and you are their king!....
            """

class Snowwalkers(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.Snowwalkers())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The Snowwalkers soldiers are ready to fight!
            """
        else:
            return """
            you defeated snowwalkers and saved your kingdom!....
            """
class Ghosts(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.Ghosts())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The Ghosts soldiers are ready to fight!
            """
        else:
            return """
            you defeated Ghosts and saved your kingdom!....
            """

class Zombies(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.Zombies())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The Zombies soldiers are ready to fight!
            """
        else:
            return """
            you defeated Zombies and saved your kingdom!....
            """


class Whitewalkers(EnemyKingdom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.Whitewalkers())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The Whitewalkers soldiers are ready to fight!
            """
        else:
            return """
            you defeated Whitewalkers and saved your kingdom!....
            """

class SevenKingdoms(MapTile):
    def intro_text(self):
        return """ 
        you killed the seven kings  .....
        ... now you are the king of seven kingdoms!

        Hail the new king!
        """

    def modify_player(self, player):
        player.victory = True
   #     yes_no =["yes", "no"]

        if player.victory is True:

            #         print("\nDo you want to proceed to next level? (y or n)")
            #          while response not in yes_no:
            response = input("Would you like to step into the forest?\ny/n\n")
            if response == "y":

               # print("You head into the forest. You hear crows cawwing in the distance.\n")
               play()

            elif response == "n":
                print("You are not ready for this quest. Goodbye, .")
                quit()
            else:
                print("I didn't understand that.\n")

        else:
            exit()


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """

class LootRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Money())

    def intro_text(self):
        return """
        Something  is shiny in the corner.
        It's a bag of gold! You pick it up.
        """


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Attack(enemy=self.enemy), actions.Escape(tile=self),actions.Assign(tile=self), actions.Heal(tile=self),
                    actions.Status(tile=self)]
        else:
            return self.adjacent_moves()

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class TigerRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.Tiger())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A tiger jumps in front of you!
            """
        else:
            return """
            The corpse of a dead tiger on the ground.
            """


class BearRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.Bear())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant bear jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead bear on the ground.
            """


class WolfRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.Wolf())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             A wolf jumps down in front of you!
             """
        else:
            return """
             The corpse of a dead wolf is on the ground.
             """


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, eneimes.Wolf())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             An angry Ogre runs down in front of you!
             """
        else:
            return """
             The corpse of a dead Ogre is on the ground.
             """

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True
        if player.victory is True:

            #         print("\nDo you want to proceed to next level? (y or n)")
            #          while response not in yes_no:
            response = input("Would you like to step into the forest?\ny/n\n")
            if response == "y":

               # print("You head into the forest. You hear crows cawwing in the distance.\n")
               play()

            elif response == "n":
                print("You are not ready for this quest. Goodbye, .")
                quit()
            else:
                print("I didn't understand that.\n")

        else:
            exit()

