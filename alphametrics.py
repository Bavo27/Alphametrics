from itertools import permutations

def alphametics():
    wordList = ["saturn", "uranus", "neptune", "pluto", "planets"]
    letterList = ["s", "p", "n", "u", "a", "t", "r", "e", "o", "l"]
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    allDigitsPermutations = permutations(digits)

    for i in allDigitsPermutations:
        currList = i
        if currList[0] == 0 or currList[1] == 0 or currList[2] == 0 or currList[3] == 0:
                continue
        setLetters = {}
        # setLetters = {letterList[k]: currList[k] for k in range(len(letterList))}
        numbers = []
        for j in range(len(currList)):
            setLetters.setdefault(letterList[j], currList[j])
        for w in wordList:
            if w == "planets":
                break
            multiplier = 0
            value = 0
            
            for y in range(len(w)-1, -1, -1):
                value = value + (setLetters[w[y]] * 10**multiplier)
                multiplier += 1
            numbers.append(value)
        
        total = sum(numbers[:-1])
        if total == numbers[len(numbers)-1]:
            return setLetters

print(alphametics())
