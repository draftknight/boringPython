
def collatz(number):
    try:
        numInt = int(number)
        if numInt % 2 == 0:
            gusu = numInt / 2
            print(int(gusu))
            collatz(gusu)
        elif numInt == 1:
            print(numInt)
        elif numInt % 2 == 1:
            kisu = 3 * numInt + 1
            print(int(kisu))
            collatz(kisu)
    except ValueError:
        print('数値を入力してください')

num = input()
collatz(num)