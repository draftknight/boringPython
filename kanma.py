def canmaAnd(spamList):
    spamStr = ''
    for i in range(len(spamList)):
        if i == len(spamList) -2:
            spamStr = spamStr + spamList[i] + ' and '
        elif i == len(spamList) -1:
            spamStr = spamStr + spamList[i]
        else:
            spamStr = spamStr + spamList[i] + ', '

    print(spamStr)


spam = ['apples', 'bananas', 'tofu', 'cats']
canmaAnd(spam)