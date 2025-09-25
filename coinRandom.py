import random

number_of_streaks = 0
for experiment_number in range(10000):
    # 100個の表裏
    omouraList = []
    for i in range(100):
        omouraList.append(random.randint(0,1))

    for i in range(len(omouraList)):
        if i == len(omouraList) - 5:
            break
        if len(set(omouraList[i:i+5])) == 1:
            number_of_streaks += 0.01

print(f'同じ面が6連続出現する確率：{number_of_streaks / 100}%')
