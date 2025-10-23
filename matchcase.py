print('''
      1: Begin Game
      2: High Scores
      3: Settings
      4: Leave
      ''')

menu = int(input("Enter the number: "))

def mainMenu():
    match menu:
        case 1:
            print("Game started")
        case 2:
            print("High scores list")
        case 3:
            print("Settings screen")
        case 4:
            print("ARE YOU SURE YOU WANT TO LEAVE?!?!?!?")
            if 4 == ("Yes"):
              print("OK")
            else:
                print("GAME LEFT")
  