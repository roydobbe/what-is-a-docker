import http.server
import socketserver
from os import path
import os


title = """            
                                                      |>>>
         *                                            |
                        *                             |
          ___  _         _  _                    |;|_|;|_|;|
           |  | | |   | |_ |_|            *      \ .    .  /
           |  |_| |_|_| |_ | \        *           \ :  .  /
    *              _   _                           ||:   |
                  | | |_      *                    ||:.  |
         *        |_| |                *           ||:  .|    \,/
    _  _      ___  _              _     ___        ||:   |
   |  | | |\|  |  |_| | |\| |\/| |_ |\|  |         ||: , |       /`\ 
   |_ |_| | |  |  | | | | | |  | |_ | |  |         ||:   |
                                                   ||: . |
              __             *              ___.   ||_   |
     ____--``    '--``__            __ ----`    ``---,___|_.           
-`--`                   `---__ ,--`'                        `_____-`'

"""

dragon = """ 
                     ,-,-      
                     / / |      
   ,-'             _/ / /       
  (-_          _,-' `Z_/        
   "#:      ,-'_,-.    \  _     
    #'    _(_-'_()\     \."|    
  ,--_,--'                 |    
 / ""                      L-'\ 
 \,--^---v--v-._        /   \ | 
   \_________________,-'      | 
                    \           
                     \          
                      \         
"""

demon = """          
          (                      )
          |\    _,--------._    / |
          | `.,'            `. /  |
          `  '              ,-'   '
           \/_         _   (     /
          (,-.`.    ,',-.`. `__,'
           |/#\ ),-','#\`= ,'.` |
           `._/)  -'.\_,'   ) ))|
           /  (_.)\     .   -'//
          (  /\____/\    ) )`'\.
           \ |V----V||  ' ,    \.
            |`- -- -'   ,'   \  \      _____
     ___    |         .'    \ \  `._,-'     `-
        `.__,`---^---'       \ ` -'
           -.______  \ . /  ______,-
                   `.     ,'        """

died = """
                          _ _          _ 
                         | (_)        | |
 _   _  ___  _   _     __| |_  ___  __| |
| | | |/ _ \| | | |   / _` | |/ _ \/ _` |
| |_| | (_) | |_| |  | (_| | |  __/ (_| |
 \__, |\___/ \__,_|   \__,_|_|\___|\__,_|
  __/ |                               
 |___/                   
 
 """

gate = """ 
         A                                                                                            A
        / \                                                                                          / \.
       _\_/_                                         /\  /\                                         _\_/_
      / _ __\                                 /\     \/  \/     /\                                 / _ __\.
      \_____/                                 \/    <``><''>    \/                                 \_____/
       |___|                           /\    <``>    TT  TT    <''>    /\                           |___|
      /     \                          \/     TT     ||  ||     TT     \/                          /     \.
     /       \                  /\    <``>    ||     ||  ||     ||    <''>    /\                  /       \.
  __/____ ____\__               \/     TT    <||>._.<||  ||>._.<||>    TT     \/               __/____ ____\__
 /_______________\       /\    <``>    ||>.=""||,.-. ||  || .-.,||""=.<||    <''>    /\       /_______________\.
 )_______________(       \/     TT    <||,.-.<||"   "||  ||"   "||>.-.,||>    TT     \/       )_______________(
  |_|___|___|___|       <``>    ||>.=""||"   "||     ||  ||     ||"   "||""=.<||    <''>       |_|___|___|___|
  |___|___|___|_| /\     TT    <||,.-.<||     ||"-_-"||  ||"-_-"||     ||>.-.,||>    TT     /\ |___|___|___|_|
  |_|___|___|___| \/     ||>.=""||"   "||"-_-"||> .=<||  ||>=. <||"-_-"||"   "||""=.<||     \/ |_|___|___|___|
  |___|___|___|_|<``>    ||,.-.<||     ||> .=<||>"   ||__||   "<||>=. <||     ||>.-.,||    <''>|___|___|___|_|
  |_|___|___|___| TT    <||"   "||"-_-"||."   ||     ||/\||     ||   ".||"-_-"||"   "||>    TT |_|___|___|___|
  |___|___|___|_| ||  ,* ||     ||> .=<||>    ||     ||()||     ||    <||>=. <||     || *,  || |___|___|___|_|
  |_|___|___|___|_||>*  ,||"-_-"||."   ||     ||     ||\/||     ||     ||   ".||"-_-"||,  *<||_|_|___|___|___|
  |___|___|___|_|__|,.-.<||> .=<||>    | .d8888b.   .d8888b.   .d8888b. |    <||>=. <||>.-.,|__|___|___|___|_|
  |_|___|___|___| ||`   "||."   ||     |d88P  Y88b d88P  Y88b d88P  Y88b|     ||   ".||"   '|| |_|___|___|___|
  |___|___|___|_| ||"    ||>    ||     |888        888        888       |     ||    <||    "|| |___|___|___|_|
  |_|___|___|___| ||"-_-"||     ||     |888d888b.  888d888b.  888d888b. |     ||     ||"-_-"|| |_|___|___|___|
  |___|___|___|_| ||> .=<||     ||     |888P "Y88b 888P "Y88b 888P "Y88b|     ||     ||>=. <|| |___|___|___|_|
  |_|___|___|___|_||>"   ||     ||>,_,<|888    888 888    888 888    888|     ||     ||   "<||_|_|___|___|___|
  |___|___|___|_|__|     ||>,_,<|| .-. |Y88b  d88P Y88b  d88P Y88b  d88P|     ||>,_,<||     |__|___|___|___|_|
  |_|___|___|___| ||>,_,<|| .-. ||"   "| "Y8888P"   "Y8888P"   "Y8888P" |    <||>=. <||>.-.,|| |_|___|___|___|
  |___|___|___|_| || .-. ||"   "||     ||"-_-"||>"   ||  ||   "<||"-_-"||     ||"   "|| .-. || |___|___|___|_|
  |_|___|___|___| ||"   "||     ||"-_-"||  .=<||     ||  ||     ||>=.  ||"-_-"||     ||"   "|| |_|___|___|___|
  |___|___|___|_| ||     ||"-_-"||  .=<||>"   ||     ||  ||     ||   "<||>=.  ||"-_-"||     || |___|___|___|_|
  |_|___|___|___|_||"-_-"||  .=<||>"   ||     ||     ||  ||     ||     ||   "<||>=.  ||"-_-"||_|_|___|___|___|
  |___|___|___|_|__|  .=<||>"   ||     ||     ||     ||  ||     ||     ||     ||   "<||>=.  |__|___|___|___|_|
  |_|___|___|___| ||>"   ||     ||     ||     ||     ||  ||     ||     ||     ||     ||   "<|| |_|___|___|___|
  |___|___|___|_| ||     ||     ||     ||     ||     ||  ||     ||     ||     ||     ||     || |___|___|___|_|
  |_|___|___|___| ||>___<||>___<||>___<||>___<||>___<||  ||>___<||>___<||>___<||>___<||>___<|| |_|___|___|___|
  |___|___|___|_| "-----------------------------------"  "-----------------------------------" |___|___|___|_|
"""

door = """
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
"""

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'tower_of_containment/first_gate/second_gate/portal.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyHttpRequestHandler

PORT = 666
my_server = socketserver.TCPServer(("", PORT), handler_object)

print(title)
print("")
print("You are a hero, looking to save the princess from the Tower of Containment. After days of walking you finally reach the tower. You step inside...")
print("")
try:
    input("You suddenly freeze. If only there was a way to interact with this Tower of Containment...")
except:
    print("")
    print("")
    print("Frozen as a statue, you spend the rest of your live rotting away...")
    print(died)
    exit()
print("")
print("Succes! You break free and walk further in to the tower.")
print("")
print("When you enter, you're confronted with a large firespitting dragon.")
print("")
print(dragon)
print("")
print("You try to reach for your inventory and:")
print("")
input("Press Enter to continue...")
print("")
if (path.exists("./inventory")):
    print("You see three items:")
    print("1. Bow")
    print("2. A large trout")
    print("3. A token of Friendship")
    print("")
    txt = input("Select an item [1-3]: ")
    print("")
    if txt == "1":
        print("You fire off an arrow to the dragon. That seems to just annoy him.'Hey, that's animal cruelty man'. He crushes you between his rock hard abs.")
        print(died)
    elif txt == "2":
        print("You slap the dragon around a bit with a large trout. 'Hey man, that's uncalled for.' He takes the trout from you slaps you around a bit as well.")
        print(died)
    elif txt == "3":
        print("You present the dragon with the gift of Friendship, the entire collection of Friends, including never seen before footage. He seems content. 'Thanks man! It get's so boring in here. Let's watch some of these together.'")
        print("")
        input("Press Enter to continue...")
        print("")
        print("You and the dragon start watching some classic Friends episodes. The dragon seems really into it. You take your chance")
        print("and slowly slide behind him. You give him the ol' Tombstone Piledriver and crush him on the cold hard floor. A bit")
        print("out of proportion. He would have probably let you pass by now... Oh well, what ever gets you off man.")
        print("")
        input("Press Enter to continue...")
        print("")
        print("You go the the next chamber. In front of you, you see a door. There's a note beside it.")
        print("")
        print(door)
        print("")
        print("'Note to self, before running in to the Tower of Containment, don't forget to pass a variable with the password.")
        print("The code is 'Are you not contained?' and the variable name is PASSWORD'")
        print("")
        input("Press Enter to continue...")
        print("")
        try:
            PASSWORD = os.environ.get('PASSWORD')
        except:
            print("'A varia-what-now? What's that?' You look at the cryptic message as the previous door locks behind you. You die a slow and boring death.")
            print(died)
            exit()
        if PASSWORD != "Are you not contained?":
                print("'A varia-what-now? What's that?' You look at the cryptic message as the previous door locks behind you. You die a slow and boring death.")
                print(died)
                exit()
        else:
            print("As you read the cryptic message the door slides open. You don't know what you did, but it worked. Good for you.")
            print("")
            input("Press Enter to continue...")
            print("")
            print("You walk through the door and see a princess and a evil looking demon devil guy right beside her.")
            print("")
            print(demon) 
            input("Press Enter to continue...")
            print("")
            print("When he spots you, he quickly opens a PORTal to hell and pushes the princess through")
            print("")
            print("'You'll never find her now!' As he laughs manically! 'I have to go now as well, I'm HOSTing a party in my LOCAL pub. Cheers'")
            print("")
            print("You're left behind as the portal closes behind the demon.")
            print("")
            print(gate)
            print("")
            print("GAME OVER? You can look for the princess or press CTRL-C to exit.")
            try:
                my_server.serve_forever()
            except KeyboardInterrupt:
                pass
            my_server.server_close()     
    else:
        print("You certainly don't have that with you. The dragon stares at you whiles getting impatient. A quick fireball kills you instantly.")
        print(died)
else:
    print("You fool! You left your inventory outside of the Tower of Containment. The dragon kills you instantly. Luckily life inside containers get reset when destroyed...")
    print(died)



