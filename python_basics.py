'''
Uzdevumi

exercise_1 -> 2.1. Uzrakstīt programmu Python valodā, kas prasa lietotājam ievadīt veselu
nenegatīvu skaitli, un pēc tam izdrukā šo skaitli kvadrātā. Piemēram, lietotājs
ievada skaitli 5, programma izvada rezultātu 25.

exercise_2 -> 2.2. Uzrakstīt programmu Python valodā, kas prasa lietotājam ievadīt atlikušo
degvielas daudzumu auto bākā. Ja atlikušais daudzums ir virs 10 litriem, tad
programma izdrukā vārdu «daudz»; ja daudzums ir <=10, bet lielāks par 0, tad
programma izdrukā «maz»; ja daudzums ir 0, tad izdrukā «nav degvielas».

exercise_3 -> 2.3. Python valodā uzrakstīt programmu, kas darbojas kā vienkāršs kalkulators.
Lietotājs var ievadīt 2 veselus skaitļus un izvēlēties aritmētisko darbību.
Programma uz ekrāna izdrukā rezultātu, un pēc tam piedāvā vai nu rēķināt no
jauna, vai beigt darbu.

exercise_4 -> 2.4. Python valodā uzrakstīt programmu, kas prasa ievadīt skaitli n robežās 1-
1000 un pēc tam izdrukā skaitļu virkni 1 2 3 4 5 ..... n. Piemēram, ja ievada n=3,
tad izdrukā 1 2 3.

exercise_5 -> 2.5. Python valodā uzrakstīt programmu, kas prasa ievadīt skaitli n robežās 1-
1000 un pēc tam izdrukā nepāra skaitļu virkni 1 3 5 7..... n. Piemēram, ja ievada
n=11, tad izdrukā 1 3 5 7 9 11.

exercise_6 -> 2.6. Python valodā uzrakstīt programmu, kas ļauj 2 lietotājiem spēlēt spēli
«akmens šķēres papīrītis». Lietotāji izdara gājienus, ievadot skaitļus (1-akmens,
2-šķēres, 3-papīrs), un programma nosaka rezultātu. Pēc spēles beigām
programma piedāvā spēlēt vēlreiz vai arī iziet no spēles.
'''


def exercise_1():
    while True:
        try:
            number = float(input('Enter positive number: '))
            if (float(number) <= 0) :
                print('Invalid input, try again')
                continue
            value = float(number)
            value_squared = value*value
            print('Your input value squared is: ',value_squared)
            break
        except:
            print('Invalid input, try again')
            continue

def exercise_2():
    while True:
        try:
            number = float(input('Enter amount of remaining fuel (l): '))
            if (float(number) < 0):
                print('Invalid input, try again')
                continue
            elif (float(number) == 0):
                print('nav degvielas')
                break
            elif(float(number) <= 10) and (float(number) > 0):
                print('maz')
                break
            elif(float(number) > 10):
                print('daudz')
                break
        except:
            print('Invalid input, try again')
            continue

def exercise_3():
    while True:
        print("calculator")
        print("----------")
        number1 = input("Enter first number: ")
        operation = input ('Enter operation (+, -, *, /): ')
        number2 = input('Enter second number: ')
        try:
            value1 = float(number1)
            value2 = float(number2)
            if operation == "+":
                print('Result: ', value1 + value2)
            elif operation == "-":
                print('Result: ', value1 - value2)
            elif operation == "*":
                print('Result: ', value1  * value2)
            elif operation == "/":
                print('Result: ', value1 / value2)
            else:
                print("invalid operator, try again")
                continue
            print("Do you want to calculate again? (Y/N)")
            answer = input()
            if answer == 'n' or answer == 'N':
                break
        except:
            print('Invalid number input, try again')
            continue

def exercise_4():
    while True:
        try:
            number = int(input('Enter number 1-1000: '))
            if (int(number) <= 0) or (int(number) > 1000):
                print('Invalid input, try again')
                continue
            else:
                for single_number in range(number):
                    print(single_number + 1)
                break
        except:
            print('Invalid input, try again')
            continue

def exercise_5():
    while True:
        try:
            number = int(input('Enter number 1-1000: '))
            if (int(number) <= 0) or (int(number) > 1000):
                print('Invalid input, try again')
                continue
            else:
                for single_number in range(number + 1):
                    if single_number % 2 != 0:
                        print(single_number)
                break
        except:
            print('Invalid input, try again')
            continue

def exercise_6():
    while True:
        print("Game - Rock, Papper, Scissors.")
        print("------------------------------")
        try:
            user1_input = int(input('User 1, Enter number(1 - rock; 2 - paper; 3 - scissors): '))
            if (int(user1_input) < 1) or (int(user1_input) > 3):
                print('Invalid input, try again')
                continue
            else:
                user2_input = int(input('User 2, Enter number(1 - rock; 2 - paper; 3 - scissors): '))
                if (int(user2_input) < 1) or (int(user2_input) > 3):
                    print('Invalid input, try again')
                    continue
                else:
                    if (user1_input == user2_input):
                        print('it a tie')
                    elif (user1_input == 1) and (user2_input == 2):
                        print('User 2 wins')
                    elif (user1_input == 2) and (user2_input == 1):
                        print('User 1 wins')
                    elif (user1_input == 3) and (user2_input == 1):
                        print('User 2 wins')
                    elif (user1_input == 1) and (user2_input == 3):
                        print('User 1 wins')
                    elif (user1_input == 2) and (user2_input == 3):
                        print('User 2 wins')
                    elif (user1_input == 3) and (user2_input == 2):
                        print('User 1 wins')
            print("Do you want to play again? (Y/N)")
            answer = input()
            if answer == 'n' or answer == 'N':
                break
        except:
            print('Invalid input, try again')
            continue



while True:
    print("Enter number of homework exercise (1-6): ")
    try:
        pick = int(input())
        if (pick < 1) or (pick > 6):
            print("Invalid number input")
        elif (pick == 1):
            exercise_1()
        elif (pick == 2):
            exercise_2()
        elif (pick == 3):
            exercise_3()
        elif (pick == 4):
            exercise_4()
        elif (pick == 5):
            exercise_5()
        elif (pick == 6):
            exercise_6()
        print("Do you want to choose another homework exercise (Y/N)")
        answer = input()
        if answer == 'n' or answer == 'N':
            break
    except:
        print("Invalid input, try again")
        continue