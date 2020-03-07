class Player(object):

    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []

    def __str__(self):
        result = ""
        for (v1, v2) in self.rolls:
            result = result + str((v1, v2)) + " " +\
                     str(v1 + v2) + "\n"
        return result

    def getNumberOfRolls(self):
        return len(self.rolls)

    def getRollsCount(self):
        return str(self.count + 1)

    def isLoser(self):
        print("You are a loser :(")

    def isWinner(self):
        print("Edi ikaw na magaling")

    def play(self):
        self.rolls = []
        firstInput = input("Roll first dice, type run: ")
        if firstInput == "k":
            self.die1.roll()
        secondInput = input("Roll second dice, type run: ")
        if secondInput == "run":
            self.die2.roll()
        (v1, v2) = (self.die1.getValue(),
                    self.die2.getValue())
        print ("Dice 1: ", str(self.die1.getValue()), " | Dice 2: ", str(self.die2.getValue()))
        self.rolls.append((v1, v2))
        initialSum = v1 + v2
        if initialSum in (2, 3, 12):
            return False
        elif initialSum in (7, 11):
            return True
        while (True):
            self.die1.roll()
            self.die2.roll()
            (v1, v2) = (self.die1.getValue(),
                        self.die2.getValue())
            self.rolls.append((v1, v2))
            laterSum = v1 + v2
            if laterSum == 7:
                return False
            elif laterSum == initialSum:
                return True

def playOneGame():
    player = Player()
    youWin = player.play()
    print(player)
    if youWin:
        player.isWinner()
    else:
        player.isLoser()

def playManyGames(number):
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        print("Roll ", str(player.getNumberOfRolls() + 1))
        hasWon = player.play()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    if wins > losses:
        player.isWinner()
    elif wins < losses:
        player.isLoser()
    else:
        print("Tie.")

from random import randint

class Die:

    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = randint(1, 6)

    def getValue(self):
        return self.value

    def __str__(self):
        return str(self.getValue())

def main():
    number = int(input("Enter the number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()