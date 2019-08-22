birth = input('birth: ')
if int(birth) < 2000:
    print('00前')
else:
    print('00后')

height = 1.75
weight = 80.5
bmi = weight / height**2
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif bmi >= 25 and bmi < 28:
    print("过重")
elif bmi >= 28 and bmi < 32:
    print("肥胖")
elif bmi >= 32:
    print("严重肥胖")