class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=15, damage=20)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)




class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf", hp=25, damage=15)


class Tiger(Enemy):
    def __init__(self):
        super().__init__(name="Tiger", hp=50, damage=30)


class Bear(Enemy):
    def __init__(self):
        super().__init__(name='Bear', hp=60, damage=40)



class TheNorth(Enemy):
    def  __init__(self):
        super().__init__(name="House of Stark", hp = 150 ,damage= 100)
class TheVale(Enemy):
    def  __init__(self):
        super().__init__(name="House of arryans", hp = 130 ,damage= 70)
class TheIronIlands(Enemy):
    def  __init__(self):
        super().__init__(name="House of Greyjoy", hp = 120 ,damage= 60)
class TheRiverland(Enemy):
    def  __init__(self):
        super().__init__(name="House of Tully", hp = 125 ,damage= 70)
class TheWesterLands(Enemy):
    def  __init__(self):
        super().__init__(name="House of Lannister", hp = 180 ,damage= 150)
class TheStromlands(Enemy):
    def  __init__(self):
        super().__init__(name="House of baratheon", hp = 120 ,damage= 60)
class TheReach(Enemy):
    def  __init__(self):
        super().__init__(name="House of tyrell", hp = 100 ,damage= 50)
class TheCrownlands(Enemy):
    def  __init__(self):
        super().__init__(name="House of targaryen", hp = 110 ,damage= 70)

class Whitewalkers(Enemy):
    def  __init__(self):
        super().__init__(name="Whitewalkers", hp = 800 ,damage= 300)

class Snowwalkers(Enemy):
    def  __init__(self):
        super().__init__(name="Snowwalkers", hp = 400 ,damage= 200)
class Ghosts(Enemy):
    def __init__(self):
        super().__init__(name="Ghosts", hp = 250 ,damage= 180)
class Zombies(Enemy):
    def __init__(self):
        super().__init__(name="Zombies", hp = 200 ,damage= 150)