'''
Uzdevumi

exercise_1 -> 1. Uzrakstīt funkciju Python valodā, kas kā parametrus saņem divas simbolu virknes, bet kā
rezultātu uz ekrāna izdod šo virkņu «pinumu», kur viens simbols ir no pirmās virknes, bet
otrais no otrās

exercise_2 -> 2. Uzrakstīt funkciju Python valodā, kas ģenerē funkcijas izsaucēja norādīta skaita nejaušus
skaitļus no 1 līdz 10 un saglabā tos List sarakstā (programmas sākumā lieto komandu import
random un pēc tam funkciju random.randint(1,10), kā arī uzrakstīt Python funkciju, kas
aprēķina List iekļauto skaitļu reizinājumu; abu funkciju rezultātu izvadīt uz ekrāna

exercise_3 -> 3. Uzrakstīt programmu Python valodā, kas List saglabā 10 nejaušus skaitļus (0-100) un pēc
tam sakārto šo List augošā secībā, izmantojot gan Bubble Sort algoritmu (piem.,
https://www.geeksforgeeks.org/bubble-sort/), kas realizēta kā atsevišķa Python funkcija,
gan izmantojot List iebūvētās iespējas; abus kārtošanu rezultātus izvada uz ekrāna.
'''

def exercise_1():
    def list_mixing(a, b):
        c = list()
        a_list = list(a)
        b_list = list(b)
        for i in range(len(a_list)):
            c.append(a_list[i])
            c.append(b_list[i])
        print(c)

    try:
        str_input_1 = input("Enter string: ")
        str_input_2 = input("Enter string (same length as previous): ")
        if len(str_input_1) == len(str_input_2):
            list_mixing(str_input_1,str_input_2)
        else:
            exit()
    except:
        print('Invalid input, try again')

def exercise_2():
    import random

    def generate_random_lst (input_number):
        c = list()
        for i in range(input_number):
            c.append(random.randint(1,10))
        print('Randomly generated list: ', c)
        return c

    def calculate_sum(lst):
        sum_lst = 1
        for i in lst:
            sum_lst = sum_lst * i
        print('Multiplied sum: ', sum_lst)
    #    return sum_lst

    input_number = input("Enter positive number: ")
    try:
        value = int(input_number)
        calculate_sum(generate_random_lst(value))
    except:
        print('Invalid input, try again')

def exercise_3():
    import random

    def bubbleSort(arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    #print('while sorting: ', arr)
        print('Sorted list (bubble sort): ', arr)


    lst = list()
    for i in range(10):
        lst.append(random.randint(0,100))
    print('Randomly generated list: ', lst)

    a = lst[:]
    a.sort()
    print('Sorted list (built-in function): ', a)
    bubbleSort(lst)

while True:
    print("Enter number of homework exercise (1-3): ")
    try:
        pick = int(input())
        if (pick < 1) or (pick > 3):
            print("Invalid number input")
        elif (pick == 1):
            exercise_1()
        elif (pick == 2):
            exercise_2()
        elif (pick == 3):
            exercise_3()
        print("Do you want to choose another homework exercise (Y/N)")
        answer = input()
        if answer == 'n' or answer == 'N':
            break
    except:
        print("Invalid input, try again")
        continue