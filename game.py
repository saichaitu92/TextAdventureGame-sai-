
import world
from player import Player

def level():
    x = int (input ('enter level of difficulty '
                    'level " 0 " Easy'
                    'level " 1 " Medium'
                    'level " 2 " Hard :  '))
    return x

def play():
 #   sounds.intro()

    print("\n"
          ""
          ""
          ""
          ""
          "\n                    ,     \    /      ,       "  
          "\n                   / \    )\__/(     / \      "    
          "\n                  /   \  (_\  /_)   /   \     " 
          "\n             ____/_____\__\@  @/___/_____\__  "
          "\n            |             |\../|            |"
          "\n            |              \VV/             |"
          "\n            |       TEXT ADVENTURE GAME     |"
          "\n            |_______________________________|"
          "\n            |    /\ /      \\       \ /\    |"
          "\n            |  /   V        ))       V   \  |"
          "\n            |/     '       //        '     \| "
          "\n           `'              V                ' "
          "\n"
          "\n"
          ""
          "Hello Gamer! Welcome to the Superficial world "
          "\n My name is Arthur! I will guide you with all the instructions for the game"
          "\n you need to specify what level of difficulty you would like to play "
          "\nEasy-- 0 "
          "\nMedium-- 1"
          "\nHard --- 2"
          "\n this is Text based game developed from wellknown series Game Of Thrones,and "
          "\n here we need to defeat the 7 kingdoms in order to become a King and achieve the throne for entire country"
          "")
    world.load_tiles(level())
    #world.load_tiles2()
    player = Player()
    #These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break



if __name__ == "__main__":
    play()