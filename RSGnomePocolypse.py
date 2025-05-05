import random
import time
numLives = 50
bezoHealth = 20
jfk_health = 20
church_gnome = 15
granny_health = 30
joe_health = 50
susan_health = 30
if numLives <= 0:
    print("You are out of lives!")
    game_over()
    
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    #print(style.YELLOW + "Hello, World!" + style.RESET)
    
def instruct():
    print(style.RED + "Welcome to Holiday Gnome-pocolipse" + style.RESET)
    time.sleep(1)
    print("Your mission is to survive the holidays by evading and")
    time.sleep(2)
    print("or taking down the infamous gnome army.")
    time.sleep(1)
    print("Gnome attacks increase during the holidays, mostly because")
    time.sleep(2)
    print("they are fed up with being called elfs. To choose your actions,")
    time.sleep(2)
    print("enter the number associated with the listed choices present.")
    time.sleep(2)
    print("You have 50hp")
    time.sleep(2)
    print("When you make a minor wrong choice, you lose health.")
    time.sleep(2)
    print("If you make a major wrong choice, you immediately die.")
    print("if you run out of lives, you die")
    time.sleep(2)
    print("Good luck soldier. You'll need it.")
    time.sleep(1)
    print("---------------------------------------------------------------")
    print("all is jolly and bright, you are finally on holiday break")
    time.sleep(2)
    print("and in the Christmas spirit")
    intro_xmas()
    
def intro_xmas():
    print("Which holiday activity do you want to do?")
    time.sleep(1)
    ans = input("Enter 1 to build a snowman, 2 to watch a movie, or 3 to drink eggnog: ")
    if ans == "1":
        snowman()
    elif ans == "2":
        movie()
    elif ans == "3":
        eggnog()
    else:
        print("Please enter a valid number")
        intro_xmas()
        
def snowman():
    print("--------------------------------------------------------------")
    print("After you finish building your snowman")
    time.sleep(1)
    print("you walk inside and grab a snack")
    time.sleep(1)
    print("After grabbing a couple cookies, you walk outside to admire your work")
    time.sleep(3)
    print("You notice your snowman's nose appears crooked so you move to fix it")
    time.sleep(3)
    print("Suddenly you feel a stab in your finger and realize it's the gnomes!")
    time.sleep(2)
    print("AHHHHHHH they used the snowman as a trojan horse!")
    time.sleep(1.5)
    print("They begin attacking you and you look for something to hit them with, what do you grab?")
    time.sleep(3)
    snowman_choice()
    
def snowman_choice():
    ans = input("Enter 1 to grab a flamthrower, enter 2 to throw a cookie, enter 3 to use a shovel: ")
    if ans == "1":
        flamethrow()
    elif ans == "2":
        cookie()
    elif ans == "3":
        shovel()
    else:
        print("please enter valid choice")
        snowman_choice()
    
def flamethrow():
    print(" you accidentally burn down your house and get hit by a flaming board and die")
    print("------------------------------------------------------------------")
    game_over()
    
def cookie():
    print("the gnomes are confused, you use this opportunity to run inside to safety")
    escape()

def shovel():
    global numLives
    print("you scoop the mass of gnomes and catapult them into the forest")
    time.sleep(1.5)
    print("You walk back into your home, injured but alive")
    time.sleep(1)
    numLives-=5
    print("Current health: ", numLives)
    escape()
    
def escape():
    print("------------------------------------------------------------------")
    print("you no longer feel safe and must leave the area quickly, where do you go?")
    ans = input("Enter 1 for graveyard, 2 for church, 3 for neighbors house: ")
    if ans == "1":
        graveyard()
    elif ans == "2":
        church()
    elif ans == "3":
        neighbors()
    else:
        print("Please enter valid choice")
        escape()
        
        
def graveyard():
    print("------------------------------------------------------------------------")
    print("you walk into the spooky graveyard feeling like you are being watched")
    time.sleep(2)
    print("Suddenly, you hear a growling voice,")
    time.sleep(1)
    print("ask not what your country can do for you, ask may I eat your brains AGHHHHH!!!")
    time.sleep(3)
    print("zombified JFK lunges at you")
    time.sleep(1)
    print("\n")
    print("--PLAYER ATTACKS--")
    print("----------------------------")
    print("Attack 1: summon grassy noel")
    print(" Damage = 15")
    print(" Accuracy = 50")
    print("description: You summon the ghost of Grassy Noel Atkenson to damage the former president")
    print("----------------------------")
    print("Attack 2: pig throw")
    print(" Damage = 7")
    print(" Accuracy = 75")
    print("description: You start chucking pigs at JFK which reminds him of the Bay of Pigs invasion, sending him into a spiral")
    print("-----------------------------")
    print(style.RED)
    print("JFK current health: ", jfk_health)
    print(style.RESET)
    print("|\/\/\/\/|")
    print("|~~~~~~~~|")
    print("| @\  /@ |")
    print("{  /vvv\ }  ~BRAINSSSS*")
    print("   \^^^/")
    graveyard_turns()

def graveyard_turns():
    num = random.randint(1,2) 
    while jfk_health > 0 and numLives > 0:
        if num == 1:
            jfk_fight()
        elif num == 2:
            jfk_attack()
def jfk_fight():
    print("\n")
    ans = input("What do you do? Enter 1 for summon Grassy Noel or 2 for pig throw: ")
    if ans == "1":
        summon()
    elif ans == "2":
        pig()
    else:
        print("invalid answer")
        jfk_fight()
    
            
def summon():
    global jfk_health
    num = random.randint(1,2)
    if num == 1:
        print(style.RED + "That hits!" + style.RESET)
        jfk_health-=15
        display_jfk_health()
    if num == 2:
        print(style.RED + "You miss!" + style.RESET)
        display_jfk_health()
        
def display_jfk_health():
    global jfk_health
    if jfk_health > 0:
        print(style.RED)
        print("JFK current health: ", jfk_health)
        print(style.RESET)
        print("|\/\/\/\/|")
        print("|~~~~~~~~|")
        print("| @\  /@ |")
        print("{  /vvv\ }  ~BRAINSSSS*")
        print("   \^^^/")
        graveyard_turns()
    elif jfk_health <= 0:
        print(style.RED)
        print("JFK dies! A second time?...")
        print(style.RESET)
        print("|\/\/\/\/|")
        print("|~~~~~~~~|")
        print("| x\  /x |")
        print("{  /vvv\ }  ~BLURGHHH*")
        print("   \^^^/")
        neighbors()
def jfk_health_player():
    global numLives
    if numLives > 0:
        print(style.RED)
        print("Player current health: ", numLives)
        print(style.RESET)
        graveyard_turns()
    elif numLives <= 0:
        game_over()
        
def pig():
    global jfk_health
    num = random.randint(1,4)
    if num == 1:
        print("That hits!")
        jfk_health-=7
        display_jfk_health()
    elif num == 3:
        print("That hits!")
        jfk_health-=7
        display_jfk_health()
    if num == 2:
        print("That hits!")
        jfk_health-=7
        display_jfk_health()
    elif num == 4:
        print("You miss!")
        display_jfk_health()

def jfk_attack():
    global numLives
    num = random.randint(1,4)
    print("\n")
    print("JFK LUNGES AT YOU!")
    if num == 1:
        time.sleep(1)
        print("JFK's attack hits!")
        numLives-=3
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        graveyard_turns()
    elif num == 3:
        time.sleep(1)
        print("JFK's attack hits!")
        numLives-=3
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        graveyard_turns()
    if num == 2:
        time.sleep(1)
        print("JFK's attack hits!")
        numLives-=3
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        graveyard_turns()
    elif num == 4:
        time.sleep(1)
        print("JFK's attack misses!")
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        graveyard_turns()
    
def church():
    print("-----------------------------------------------------------------")
    print("you enter the church feeling a gnawing sensation on your neck")
    time.sleep(2)
    print("At first you think it's just catholic guilt")
    time.sleep(1)
    print("but soon realize it is a gnome slowly munching on your neck")
    time.sleep(1.5)
    print("you shake the church gnome off and prepare for battle")
    time.sleep(1)
    print("--PLAYER ATTACKS--")
    print("----------------------------")
    print("Attack 1: women's ankle")
    print(" Damage = 12")
    print(" Accuracy = 50")
    print("description: You show the church gnome a picture of a women's ankle you keep in your back pocket just in case you have to fight a church gnome. This angers the church gnome and he takes 12 physic damage")
    print("----------------------------")
    print("Attack 2: facebook delete")
    print(" Damage = 15")
    print(" Accuracy = 25")
    print("description: You steal the church gnome's phone and delete facebook, destroying the source of their power")
    print("-----------------------------")
    print(style.RED)
    print("Church gnome current health: ", church_gnome)
    print(style.RESET)
    print("   /\ ")
    print("  /  \ ")
    print(" /____\  ")
    print("(|0\/0|)")
    print(" |-C--|")
    print(" \___/ ")
    church_turns()

def church_turns():
    num = random.randint(1,2) 
    while church_gnome > 0 and numLives > 0:
        if num == 1:
            church_fight()
        elif num == 2:
            church_attack()
def church_fight():
    print("\n")
    ans = input("What do you do? Enter 1 for women ankle 1 or 2 for facebook delete: ")
    if ans == "1":
        ankle()
    elif ans == "2":
        facebook()
    else:
        print("invalid answer")
        church_fight()
    
            
def ankle():
    global church_gnome
    num = random.randint(1,2)
    if num == 1:
        print("That hits!")
        church_gnome-=15
        display_church_health()
    if num == 2:
        print("You miss!")
        display_church_health()
        
def display_church_health():
    global church_gnome
    if church_gnome > 0:
        print(style.RED)
        print("Church gnome current health: ", church_gnome)
        print(style.RESET)
        print("   /\ ")
        print("  /  \ ")
        print(" /____\  ")
        print("(|0\/0|)")
        print(" |-C--|")
        print(" \___/ ")
        church_turns()
    elif church_gnome <= 0:
        print(style.RED)
        print("Church gnome dies! Hopefully his soul goes up...")
        print(style.RESET)
        print("   /\ ")
        print("  /  \ ")
        print(" /____\  ")
        print("(|X\/X|)")
        print(" |-C--|")
        print(" \___/ ")
        print("after a tough battle you decide to run to your neighbors house")
        neighbors()

def church_health_player():
    global numLives
    if numLives > 0:
        print(style.RED)
        print("Player current health: ", numLives)
        print(style.RESET)
        church_turns()
    elif numLives <= 0:
        game_over()
        
def facebook():
    global church_gnome
    num = random.randint(1,4)
    if num == 1:
        print("That hits!")
        church_gnome-=15
        display_church_health()
    elif num == 3:
        print("You miss!")
        display_church_health()
    if num == 2:
        print("You miss!")
        display_church_health()
    elif num == 4:
        print("You miss!")
        display_church_health()

def church_attack():
    global numLives
    num = random.randint(1,4)
    print("\n")
    print("CHURCH GNOME LUNGES AT YOU!")
    if num == 1:
        time.sleep(.5)
        print("Church gnome's attack hits!")
        print("OPPONENT USES WHITE-WASH WHIP!")
        numLives-=3
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        church_turns()
    elif num == 3:
        time.sleep(.5)
        print("Church gnome's attack hits!")
        print("OPPONENT USES FEAR MONGER!")
        numLives-=3
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        church_turns()
    if num == 2:
        time.sleep(.5)
        print("Church gnome's attack hits!")
        print("OPPONENT USES CATHOLIC GUILT!")
        numLives-=3
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        church_turns()
    elif num == 4:
        print("Church gnome's attack misses!")
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        church_turns()
        
def neighbors():
    print("-------------------------------------------------------------")
    time.sleep(.5)
    print("\a")
    time.sleep(.5)
    print("\a")
    time.sleep(.5)
    print("\a")
    time.sleep(.5)
    print("you knock on your neighbor's door and hear things clanging")
    time.sleep(1)
    print("The door swings open and you see your neighbor, Susan as pale as a ghost")
    time.sleep(2.5)
    print("You look behind her and see your arch nemesis, Joe")
    time.sleep(1)
    print("In a high pitched voice he goes into a passionate villain monologue. What do you do?")
    time.sleep(3)
    neighbor_choice()   
def neighbor_choice():
    ans = input("Enter 1 to fight, 2 for call Joe a cute little guy, 3 for challenge him to rock paper scissors: ")
    if ans == "1":
        boss_attacks()
    elif ans == "2":
        cutie()
    elif ans == "3":
        RPSgame()
    else:
        print("please enter valid number")
        neighbor_choice()

def boss_attacks():
    print("----------------------------")
    print("Attack 1: drone strike")
    print(" Damage = 20")
    print(" Accuracy = 50")
    print("description: You call in a favor and call in a drone strike to explode joe")
    print("----------------------------")
    print("Attack 2: jump kick")
    print(" Damage = 15")
    print(" Accuracy = 75")
    print("description: jump kick joe and send him across the room")
    bossB_turns()

def bossB_turns():
    num = random.randint(1,5) 
    while joe_health > 0 and numLives > 0:
        if num == 1:
            time.sleep(1)
            playJ_attack()
        elif num == 2:
            time.sleep(1)
            boss_attack()
        elif num == 3 and susan_health > 0:
            time.sleep(1)
            susan_attack()
        elif num == 4:
            time.sleep(1)
            boss_attack()
        elif num == 5:
            time.sleep(1)
            playJ_attack()

def playJ_attack():
    print("\n")
    ans = input("What do you do? Enter 1 for attack 1 or 2 for attack 2")
    if ans == "1":
        drone()
    elif ans == "2":
        kick()
    else:
        print("invalid answer")
        playJ_attack()
        
def susan_attack():
    global susan_health
    global numLives
    num = random.randint(1,4)
    if num == 1:
        print("\n")
        print("Susan heals herself, 5 hp regained")
        susan_health += 5
        susan_Bhealth()
    elif num == 2:
        print("\n")
        print("Susan heals you, 5 hp regained")
        numLives += 5
        health_Bplayer()
    elif num == 3:
        print("\n")
        print("susan tries to heal you but fails")
        health_Bplayer()
    elif num == 4:
        print("\n")
        print("susan tries to heal herself but fails!")
        susan_Bhealth()
        
def susan_Bhealth():
    if susan_health > 0:
        print("Susan current health: ")
        bossB_turns()
    elif susan_health <= 0:
        susan_death()
    
            
def drone():
    global joe_health
    num = random.randint(1,2)
    if num == 1:
        print("That hits!")
        joe_health-=20
        display_joe_health()
    if num == 2:
        print("You miss!")
        display_joe_health()
        
def display_joe_health():
    global joe_health
    if joe_health > 0:
        print("Joe current health: ", joe_health)
        bossB_turns()
    elif joe_health <= 0 and susan_health <= 0:
        print("Joe dies!")
        susan_ending()
    elif joe_health <= 0:
        hap_susan()

def health_Bplayer():
    global numLives
    if numLives > 0:
        print("Player current health: ", numLives)
        bossB_turns()
    elif numLives <= 0:
        game_over()
        
def susan_Bhealth():
    if susan_health > 0:
        print("Susan current health: ", susan_health)
        bossB_turns()
    elif susan_health <= 0:
        susan_death()
        
def kick():
    global joe_health
    num = random.randint(1,4)
    if num == 1:
        time.sleep(1)
        print("That hits!")
        joe_health-=15
        display_joe_health()
    elif num == 3:
        time.sleep(1)
        print("That hits!")
        joe_health-=15
        display_joe_health()
    if num == 2:
        time.sleep(1)
        print("That hits!")
        joe_health-=15
        display_joe_health()
    elif num == 4:
        time.sleep(1)
        print("You miss!")
        display_joe_health()
        
def boss_attack():
    global numLives
    global susan_health
    num = random.randint(1,4)
    print("\n")
    if num == 1:
        print("Joe's attack hits susan!")
        susan_health-=13
        susan_Bhealth()
    elif num == 3:
        print("Joe's attack hits you!")
        numLives-=13
        health_Bplayer()
    if num == 2:
        print("Joe's attack misses!")
        print("current player health:", numLives)
        bossB_turns()
    elif num == 4:
        print("Joe's attack misses!")
        print("current player health:", numLives)
        bossB_turns()
        
def susan_death():
    print("You hear a scream and quickly turn around")
    print("You see Susan on the brink of death and cradle her in your arms")
    print("She looks at you lovingly and whispers I have always loved you")
    print("Crying and enraged you look at Joe and prepare to fight")
    print("----------------------------")
    print("NEW BUFF GAINED")
    print("increased speed: you are now more likely to attack Joe first")
    print("----------------------------")
    bossB_turns()
def hap_susan():
    print("Joe dies! You win! Susan and you live happily ever after")
    winner()
def susan_ending():
    print("you won the war but at what cost")
    winner()
def game_over():
    print("game over")
    
def cutie():
    num = random.randint(1,2)
    if num == 1:
        print("------------------------------------------------------------")
        print("he blushes, nobody has ever complimented him in that way.")
        time.sleep(1)
        print("He thinks back to the time when his betrothed tragically passed away in a skydiving accident.")
        time.sleep(2)
        print("He's nervous to trust others, I mean, he's been out of the game so long.")
        time.sleep(2.5)
        print("He tearfully decides to trust you and the two of you live happily ever after")
        time.sleep(2)
        print("   /\ ")
        print("  /  \ ")
        print(" /____\  ")
        print("(|/0 0\|)")
        print(" |  3 |    <3")
        print("  \__/ ")
        winner()
    else:
        print("Joe says he's taken and not falling for your tricks!")
        boss_attacks()
    
def RPSgame():
    compHand = randomCompChoice()
    userHand = getUserChoice()
    print("Joe chose:",compHand)
    if compHand == "rock":
        print("    _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___)")
    elif compHand == "paper":
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("          _______)")
        print("         _______)")
        print("---.__________)")
    elif compHand == "scissors":
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")
    compareChoices(compHand, userHand)
def randomCompChoice():
    num = random.randint(1,3)
    if num ==1:
        return "rock"
    elif num ==2:
        return "paper"
    else:
        return "scissors"
def getUserChoice():
    user = input("Enter rock, paper or scissors: ")
    user = user.lower()
    while user != "rock" and user != "scissors" and user != "paper":
        user = input('Try again. Enter rock, paper or scissors: ')
        user = user.lower()
    return user
def compareChoices(compChoice, userChoice):
    if compChoice == userChoice:
        print("You tie, try again")
        RPSgame()
    elif compChoice == "rock" and userChoice == 'scissors':
        print("Joe wins! He lunges at you and kills you!")
        game_over()
    elif compChoice == "rock" and userChoice == "paper":
        print("You win! The gnomes explode and you emerge victorious!")
        winner()
    elif compChoice == "scissors" and userChoice == "rock":
        print("You win! The gnomes explode and you emerge victorious!")
        winner()
    elif compChoice == "scissors" and userChoice == "paper":
        print("Joe wins He lunges at you and kills you!")
        game_over()
    elif compChoice == "paper" and userChoice == "rock":
        print("Joe wins! He lunges at you and kills you")
        game_over()
    elif compChoice == "paper" and userChoice == "scissors":
        print("You win! The gnomes explode and you emerge victorious!")
        winner()


def movie():
    print("-----------------------------------------------------")
    print("you begin to watch your favorite Christmas movie.")
    time.sleep(1)
    print("Suddenly, an emergency broadcast appears on the TV")
    time.sleep(1)
    print("and warns you about the impending gnome-pocolipse.")
    time.sleep(1)
    print("You are fearful, what do you do to prepare?")
    time.sleep(1)
    movie_choice()
def movie_choice():
    ans = input("enter 1 to use poison eggnog as bait, 2 to take down dangerous decorations, 3 to flee to Florida: ")
    if ans == "1":
        poison()
    elif ans == "2":
        decor()
    elif ans == "3":
        florida()
    else:
        print("please enter valid number")
        movie_choice()
      
def poison():
    global numLives
    print("----------------------------------------------------------")
    print("you poison the eggnog and leave it out as bait. you end up")
    time.sleep(1)
    print("taking out a good chunk of the gnome army.")
    time.sleep(1)
    print("one night they ambush you! You make it out of the house, hurt but safe")
    time.sleep(2.5)
    numLives-=5
    print("Current health", numLives)
    escape()
    
def decor():
    print("------------------------------------------------------------")
    print("after taking down the decorations you feel prepared and relieved.")
    time.sleep(2)
    print("Suddenly, the army of gnomes attacks")
    time.sleep(1)
    print("and strangles you with the Christmas lights you forgot to take down.")
    time.sleep(2.5)
    print("You die.")
    game_over()
    
def florida():
    print("-----------------------------------------------------------------")
    print("after a long journey, you finally make it to Florida, what do you do?")
    ans = input("enter 1 to volunteer at an old folks home, enter 2 to try to make friends, enter 3 to tell the floridians about the gnomes")
    if ans == "1":
        retire()
    elif ans == "2":
        friends()
    elif ans == "3":
        hillbilly_army()
    else:
        print("please enter valid choice")
        florida()
    
def retire():
    print("\n")
    print("everything is fine until one day when you forget")
    time.sleep(2)
    print("it's your turn to run bingo night.")
    print("The enraged elderly begin to brutally tear you apart")
    print("--PLAYER ATTACKS--")
    print("----------------------------")
    print("Attack 1: punch")
    print(" Damage = 12")
    print(" Accuracy = 50")
    print("description: just punch granny in the face")
    print("----------------------------")
    print("Attack 2: early bird special")
    print(" Damage = 7")
    print(" Accuracy = 75")
    print("description: You karate kick granny and send her flying")
    print("-----------------------------")
    print(style.RED)
    print("Granny current health: ", granny_health)
    print("    /\/\/\/\ ")
    print("   (      # )")
    print("  (__________)")
    print(" (||_@\\\ //@_||)  BINGOOOOOOO RAGHHHHH!!!")
    print("   \ /vvvvv\ /   ")
    print("     \^^^^^/")
    print(style.RESET)
    granny_turns()

def granny_turns():
    num = random.randint(1,2) 
    while granny_health > 0 and numLives > 0:
        if num == 1:
            granny_fight()
        elif num == 2:
            granny_attack()
def granny_fight():
    print("\n")
    ans = input("What do you do? Enter 1 for punch or 2 for early bird special: ")
    if ans == "1":
        punch()
    elif ans == "2":
        early()
    else:
        print("invalid answer")
        granny_fight()
    
            
def punch():
    global granny_health
    num = random.randint(1,2)
    if num == 1:
        print("That hits!")
        granny_health-=15
        display_granny_health()
    if num == 2:
        print("You miss!")
        display_granny_health()
        
def display_granny_health():
    global granny_health
    if granny_health > 0:
        print(style.RED)
        print("Granny current health: ", granny_health)
        print("    /\/\/\/\ ")
        print("   (      # )")
        print("  (__________)")
        print(" (||_@\\\ //@_||)  BINGOOOOOOO RAGHHHHH!!!")
        print("   \ /vvvvv\ /   ")
        print("     \^^^^^/")
        print(style.RESET)
        granny_turns()
    elif granny_health <= 0:
        print("Granny dies!")
        print(style.RED)
        print("    /\/\/\/\ ")
        print("   (      # )")
        print("  (__________)")
        print(" (||_X\\\ //X_||)  BLURGHHH")
        print("   \ /vvvvv\ /   ")
        print("     \^^^^^/")
        print(style.RESET)
        print("After a tough battle, you escape the retirement home and decide to tell the hillbillies about the gnome invasion")
        hillbilly_army()
def granny_health_player():
    global numLives
    if numLives > 0:
        print(style.RED)
        print("Player current health: ", numLives)
        print(style.RESET)
        granny_turns()
    elif numLives <= 0:
        game_over()
        
def early():
    global granny_health
    num = random.randint(1,4)
    if num == 1:
        print("That hits!")
        granny_health-=7
        display_granny_health()
    elif num == 3:
        print("That hits!")
        granny_health-=7
        display_granny_health()
    if num == 2:
        print("That hits!")
        granny_health-=7
        display_granny_health()
    elif num == 4:
        print("You miss!")
        display_granny_health()

def granny_attack():
    global numLives
    num = random.randint(1,4)
    print("\n")
    print("GRANNY LUNGES AT YOU!")
    time.sleep(.5)
    if num == 1:
        print("Granny's attack hits!")
        print("Granny uses BACK IN MY DAY RAY")
        numLives-=4
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        granny_turns()
    elif num == 3:
        print("Granny's attack hits!")
        print("Granny uses DENTURE CHOMP")
        numLives-=5
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        granny_turns()
    if num == 2:
        print("Granny's attack hits!")
        print("Granny uses KNEE CAP CRUSH")
        numLives-=3
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        granny_turns()
    elif num == 4:
        print("Granny's attack misses!")
        print(style.RED)
        print("current player health:", numLives)
        print(style.RESET)
        granny_turns()
    
def friends():
    print("--------------------------------------------------------------------")
    print("the Floridians are offended by your political alignment")
    time.sleep(1)
    print("and start throwing alligators at you. Sadly you are out numbered You die.")
    time.sleep(1)
    print(style.GREEN)
    print("           _/\__/\_")
    print("   __     / (0)(0)")
    print("  /..\___/")
    print(" [vvv                RAWRR..I guess")
    print("  \____________(__")
    print(style.RESET)
    game_over()
    
def hillbilly_army():
    print("-------------------------------------------------------")
    print("they take you seriously, this isn't their first rodeo.")
    time.sleep(1)
    print("You are then surprised by the massive amount of weapons they have.")
    time.sleep(2)
    print("You and the Floridians set up a go fund me for a load of dynamite")
    time.sleep(2)
    print("and achieve the target amount.")
    time.sleep(1)
    print("The Floridian army defeats the gnomes by using the dynamite")
    time.sleep(2)
    print("to blow the gnomes straight to the bowels of hell.")
    time.sleep(1)
    print(style.RED)
    print(" _____________     . , ; .")
    print("(_____________|~~~~~X.;' .  KABOOMMM")
    print("                   ' ` `")
    print(style.RESET)
    winner()
    
def eggnog():
    global numLives
    print("-----------------------------------------------------------")
    print("you sit by the fire and watch as it dies down.")
    time.sleep(1)
    print("You then put your glass down for a second to go put another log on the fire")
    time.sleep(2.5)
    print("Big mistake. In your moment of weakness, a special squad team of gnomes run to your cup of eggnog.")
    time.sleep(2.5)
    print("They each carry three items: small bottles, rags, and lighters. OH NO!!!!!!!!!!!!!")
    time.sleep(2)
    print("They fill up the bottles with eggnog and create molotov cocktails")
    time.sleep(2)
    print("The gnomes proceed to chuck the bottles everywhere,")
    time.sleep(1)
    print("setting fire to your house and yourself. What do you do?")
    time.sleep(1)
    eggnog_choice()
        
def eggnog_choice():
    ans = input("Enter 1 to plead, 2 to accept death, 3 to jump out the window: ")
    if ans == "1":
        plead()
    elif ans == "2":
        acceptance()
    elif ans == "3":
        window()
    else:
        print("Please enter valid choice")
        eggnog_choice()
        
def plead():
    print("you plead for your life but they don't care, you die.")
    game_over()
    
def acceptance():
    print("The gnomes are offended by your lack of determination and kill you")
    game_over()
    
def window():
    print(" you successfully make it out alive but you are injured. what do you do?")
    ans = input("Enter 1 to go to your neighbors house, enter 2 to call the police: ")
    if ans == "1":
        neighbors()
    elif ans == "2":
        police()
    else:
        print("please enter valid choice")
        window()
        
def police():
    print("--------------------------------------------------------------------")
    print("you sit in the cold, watching as your house slowly burns down.")
    time.sleep(2)
    print("Soon you hear sirens and breathe a sigh of relief.")
    time.sleep(2)
    print("The ambulance driver steps out of his car and tells you that it will cost $7000 to ride in the ambulance.")
    time.sleep(3)
    print("You tell him that is an insane price and refuse.")
    time.sleep(1)
    print("Suddenly, the ambulance driver's large trenchcoat falls and you are face to face with a stack of gnomes.")
    time.sleep(3)
    print("You gasp in horror, realizing these aren't just regular gnomes,")
    time.sleep(1.5)
    print("but capitalist gnomes!")
    print("They tell you to give them all your possessions or they will lower your credit score")
    time.sleep(3)
    print("and report you for insurance fraud. You give them all you have")
    time.sleep(2)
    print("and think the situation can't get any worse.")
    time.sleep(1.5)
    print("You say, ~well at least I still have my dignity~ . The gnomes hear this and say they require your dignity as well. ")
    time.sleep(3)
    print("You give the gnomes your clothes and they wander away,")
    time.sleep(2)
    print("thinking of jolly thoughts like their love of tax evasion")
    time.sleep(1.5)
    print("Suddenly, in the distance you see man walking towards you")
    time.sleep(1.5)
    print("as he comes closer you gasp in horror!")
    time.sleep(1)
    print("before you stands Jeffrey Bezos, he looks at you and prepares for a fight")
    time.sleep(2)
    print("\n")
    print("--PLAYER ATTACKS--")
    print("----------------------------")
    print("Attack 1: mega death punch")
    print(" Damage = 15")
    print(" Accuracy = 50")
    print("description: You hurl a massive punch")
    print("----------------------------")
    print("Attack 2: increased tax liability")
    print(" Damage = 7")
    print(" Accuracy = 75")
    print("description: You hold Bezo accountable for his actions and send him into a mental panic")
    print("-----------------------------")
    bezo_turns()

def bezo_turns():
    turn_bzo = 0
    num = random.randint(1,2) 
    while bezoHealth > 0 and numLives > 0:
        if num == 1:
            bezo_fight()
        elif num == 2:
            bezo_attack()
    if numLives <= 0:
        game_over()
def bezo_fight():
    print("\n")
    ans = input("What do you do? Enter 1 for mega death punch or 2 for increased tax liability: ")
    if ans == "1":
        megaDeath()
    elif ans == "2":
        tax_li()
    else:
        print("invalid answer")
        bezo_fight()
    
            
def megaDeath():
    global bezoHealth
    num = random.randint(1,2)
    if num == 1:
        print("That hits!")
        bezoHealth-=15
        display_bezoHealth()
    if num == 2:
        print("You miss!")
        display_bezoHealth()
        
def display_bezoHealth():
    global bezoHealth
    if bezoHealth > 0:
        print(style.RED)
        print("Bezo current health: ", bezoHealth)
        print(style.RESET)
        print("   /\ ")
        print("  /  \ ")
        print(" /____\  ")
        print("(| $ $ |) ~TAX EVASION <33")
        print(" [ -C--]")
        print("  \___/ ")
        bezo_turns()
    elif bezoHealth <= 0:
        print("Bezos dies!!")
        print("   /\ ")
        print("  /  \ ")
        print(" /____\  ")
        print("(| X X |) ~NOOOOO")
        print(" [ -C--]")
        print("  \___/ ")
        neighbors()
        
def health_player():
    global numLives
    if numLives > 0:
        print(style.RED)
        print("Player current health: ", numLives)
        print(style.RESET)
        bezo_turns()
    elif numLives <= 0:
        game_over()
        
def tax_li():
    global bezoHealth
    num = random.randint(1,4)
    if num == 1:
        print("That hits!")
        bezoHealth-=7
        display_bezoHealth()
    elif num == 3:
        print("That hits!")
        bezoHealth-=7
        display_bezoHealth()
    if num == 2:
        print("That hits!")
        bezoHealth-=7
        display_bezoHealth()
    elif num == 4:
        print("You miss!")
        display_bezoHealth()

def bezo_attack():
    global numLives
    num = random.randint(1,4)
    print("\n")
    time.sleep(.5)
    print("BEZO LUNGES AT YOU!")
    if num == 1:
        print("Bezo's attack hits!")
        print("SAME DAY DESTRUCTION! - an amazon box falls on your head, crushing you and destroying the environment")
        numLives-=3
        print("current player health:", numLives)
        bezo_turns()
    elif num == 3:
        print("Bezo's attack hits!")
        print("SAME DAY DESTRUCTION! - an amazon box falls on your head, crushing you and destroying the environment")
        numLives-=3
        print("current player health:", numLives)
        bezo_turns()
    if num == 2:
        print("Bezos attack hits!")
        print("SAME DAY DESTRUCTION! - an amazon box falls on your head, crushing you and destroying the environment")
        numLives-=3
        print("current player health:", numLives)
        bezo_turns()
    elif num == 4:
        print("Bezo's attack misses!")
        print("current player health:", numLives)
        bezo_turns()

def game_over():
    print(style.RED)
    print(" _     _")
    print("/ \   / \ ")
    print("\  \ /  /")
    print(" \  \  / ")
    print("  \ / /")
    print("   \|/")
    print("GAME OVER")
    print(style.RESET)
def winner():
    print(style.GREEN)
    print("      CONGRATULATIONS!")
    print("      /| ________________")
    print("O|===|* >________________>")
    print("      \|") 
    print("       YOU SURVIVED!")

instruct()