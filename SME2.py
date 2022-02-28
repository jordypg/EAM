#SME
#By Jordy Perry-Greene
#Based off of Tom Kerrigan's SME

kValue = 32
def predictor(eloA, eloB):
    delta = eloB - eloA
    power = delta / 400
    denominator = 1 + 10**power
    return 1 / denominator

def changeInRating(eloPlayer, eloOpponent, didWin):
    prediction = predictor(eloPlayer, eloOpponent)
    #print("initial rating is " + str(eloPlayer) + ", predictor is " + str(prediction))
    if didWin:
        change = kValue * (1 - prediction)
    else:
        change = kValue * (0 - prediction)
    return change

#eloa = input("enter elo a: ")
#elob = input("enter elo B: ")
#print(str(predictor(int(eloa), int(elob))))
#print(str(changeInRating(int(eloa), int(elob), True)))

info = []
currentPlayer = 1

while True:
    name = input('Enter name for player ' + str(currentPlayer) + ', or type "next" to continue: ')
    if(name == "next"):
        break
    elo = float(input("Enter elo for " + name + ": "))
    info.append([name, elo])
    currentPlayer+=1

#print(info)

orderedInfo = []
for i in range(len(info)):
    orderedInfo.append(1)

#print(orderedInfo)

for information in info:
    placement = input("Enter placement for " + str(information[0]) + ": ")
    #print("setting index " + str(int(placement) - 1) + " to " + str(information))
    orderedInfo[(int(placement) - 1)] = information

#print(orderedInfo)

winners = []
losers = orderedInfo.copy()

finalElos = []

sizeAdjustment = 1 / (len(orderedInfo) - 1)

for player in orderedInfo:
    print("player is " + str(player[0]))
    originalElo = player[1]
    finalElo = originalElo
    #remove first element of losers
    losers = losers[1:]
    for winner in winners:
        delta = changeInRating(originalElo, winner[1], False)
        finalElo += sizeAdjustment * delta
        print("a winner is " + str(winner[0]) + " with delta " + str(delta))
    print("winners is " + str(winners))
    for loser in losers:
        delta = changeInRating(originalElo, loser[1], True)
        finalElo += sizeAdjustment * delta
        print("a loser is " + str(loser[0]) + " with delta " + str(delta))
    print("losers is " + str(losers))
    finalElos.append([player[0], round(finalElo, 1)])
    winners.append(player)

for player in finalElos:
    print("Final elo for " + str(player[0]) + " is " + str(player[1]))        