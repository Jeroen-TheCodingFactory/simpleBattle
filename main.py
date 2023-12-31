from random import randint

monsterAlive = True
playerAlive = True
ranAway = False
playerHP = 50
monsterHP = 50
playerMP = 20
monsterNames = [
    "BUMBLEBLAZE", "GIGGLEFROST", "WHISKERWHIRL", "SNUGGLEFLAME", "GLOOMSPARK",
    "RAINBOWWHISPER", "FUZZYGLOOM", "SPARKLEPAW", "TOOTHYSWIRL", "FLUFFERNOVA",
    "CHUCKLEFANG", "SUNNYWHISK", "WIGGLESNOOT", "SNICKERCLAW", "JELLYGAZE",
    "TWINKLEBOUNCE", "BREEZYWHISPER", "MARSHMALLOWCLAW", "WOBBLEFLAME", "SILLYWING",
    "DAZZLEWHISK", "BOUNCYSNICKER", "GIGGLEBEAM", "PICKLEWHISPER", "SUNNYTALON",
    "FUZZYSPRINKLE", "CUDDLEFLARE", "BREEZYGONIMMER", "PUMPKINSWIRL", "SNOOZYGLOW",
    "JELLYBLAZE", "TWINKLEWHIRL", "WHISKERSPARK", "GIGGLEFLAME", "BOUNCEYWOBBLE",
    "FROSTYWINK", "TOOTHYGAZE", "RAINBOWCLAW", "SUNNYWHISPER", "BREEZYFIZZLE",
    "SNUGGLEBOUNCE", "GIGGLEGLEAM", "DAZZLEWHISPER", "FLUFFERNIBBLE", "PICKLEBLAZE",
    "CHUCKLEFROST", "SNOOZYTWINKLE", "JELLYWHISK", "BOUNCYSPARK", "SILLYTALON",
    "WOBBLEBEAM", "FUZZYFLAME", "CUDDLEGAZE", "PUMPKINWHISPER", "TWINKLESNICKER",
    "BREEZYFLOW", "MARSHMALLOWWHIRL", "WHISKERWHISPER", "GIGGLEBLAZE", "SNUGGLEFROST",
    "BUMBLEWIGGLE", "SUNNYBOUNCE", "FLUFFYTWINKLE", "TOOTHYWHISPER", "RAINBOWFLAME",
    "SILLYCLAW", "GLOOMGAZE", "DAZZLEBREEZE", "CUDDLEWHISK", "PICKLEBOUNCE",
    "SNOOZYWHIRL", "JELLYSPARK", "BOUNCYNIBBLE", "SILLYWHISPER", "BREEZYGLIMMER",
    "WOBBLEFLAME", "GIGGLEWHIRL", "FLUFFYPAW", "CHUCKLEBEAM", "SNUGGLEFIZZLE",
    "RAINBOWGAZE", "TWINKLENIBBLE", "BUMBLEWHISK", "SUNNYCLAW", "DAZZLEWOBBLE",
    "TOOTHYTWINKLE", "FUZZYBLAZE", "PUMPKINSNICKER", "SILLYBOUNCE", "CUDDLEFLAME",
    "JELLYWHISPER", "BREEZYGLOW", "WOBBLETALON", "GIGGLEBEAM", "FLUFFYWHIRL",
    "MARSHMALLOWGAZE", "SNUGGLEFLAME", "CHUCKLEWHISPER", "SNOOZYGLOW", "BOUNCYCLAW"
]

monsterName = monsterNames[randint(0,99)]

# Start of game
name = input("Hi Player! What is your name?\n")
print("Hi", name, ", everything seems quiet and relaxed until .....")
print("A HORRIBLE MONSTER NAMED", monsterName, "APPEARS!")

while(playerAlive == True and monsterAlive == True and ranAway == False):
    print("----------------------------------------------------------")
    print(name + ":", playerHP, "HP", playerMP,"MP")
    print(monsterName, ":", monsterHP, "HP")
    print("----------------------------------------------------------")
    move = input("[A]ttack, [R]un or [M]agic?")
    if(move == "A" or move == "a"):
        print("You attack!")
        random = randint(1,6)
        monsterHP -= random
        print(name,"did", random, "damage!")
        random = randint(1,10)
        playerHP -= random
        print(monsterName,"did", random, "damage!")
        if(monsterHP <= 0):
            print("You defeated", monsterName, "!")
            monsterAlive = False
        elif(playerHP <= 0 ):
            print("You are defeated :( ")
            playerAlive = False
    elif(move == "R" or move == "r"):
        random = randint(1,6)
        if(random % 2 == 0):
            ranAway = True
            print(name, "ran away!")
        else:
            print(monsterName, "blocks you!")
    elif(move == "M" or move == "m"):
        if(playerMP > 0):
            random = randint(10, 15)
            playerMP -= randint(4, 10)
            print(name, "used fire magic and did", random, "damage!")
            monsterHP -= random
            random = randint(1, 10)
            playerHP -= random
            print(monsterName, "did", random, "damage!")
            if (monsterHP <= 0):
                print("You defeated", monsterName, "!")
                monsterAlive = False
            if(playerHP <= 0):
                print("You are defeated :( ")
                playerAlive = False
            if(playerMP < 0):
                playerMP = 0;
    else:
        print(name,"did nothing")


