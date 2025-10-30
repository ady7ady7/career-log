#Tutaj akurat robię sobie zadania z kursu ML Mastery - ogólnie one są na Google Colab, ale...
#tutaj jest wygodniej i szybciej, bo Colab momentami zamula + wygodniej na drugim monitorze mieć zadanie

#Zadanie 1

# def show_numbers():
#   numbers = list(range(11))
#   numbers.append(11)
#   numbers.pop(-1)
#   print(numbers[::-1])

# show_numbers()

#Zadanie 2
# def check_colors():
#     colors = ["red", "green", "blue", "yellow"]
#     if "blue" in colors:
#         print(colors.index("blue"))

# check_colors()


#Zadanie 3

# def print_co_3_number():
#     numbers = list(range(21)) #ma być od 1 do 20
#     print(numbers) #żeby się upewnić
#     print(numbers[5:16]) #indeksy od 5 do 15 (włącznie)
#     print(numbers[::3])
    
# print_co_3_number()


#Zadanie 4

# def divide_into_odds_and_evens():
#     numbers = list(range(21))
#     odds = numbers[1::2]
#     print(f'The odds list is {odds}')
#     evens = numbers[2::2] #bez zera
#     print(f'The evens list is {evens}')
    
# divide_into_odds_and_evens()

#Zadanie 5

# def food_sorting():
#     fruits = ["apple", "banana", "cherry"]
#     vegetables = ["carrot", "broccoli", "spinach"]
    
#     food = fruits + vegetables
#     print(f'Food list before sorting: {food}')
#     sorted_food = list(sorted(food))
#     list(sorted(food))
#     print(f'Food list after sorting: {sorted_food}')
#     print(f'Food list after sorting: {food}') #czyli jednak trzeba dać jakiś nowy obiekt tutaj
    
# food_sorting()




#ĆWICZENIA NA SETACH (ZBIORACH)

#Zadanie 1
#chcemy uzyskać efekt symmetric difference - czyli wyjąć elementy, które unikalnie występują w obu zbiorach i nie powtarzają się
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# set1_uniques = set2 - set1
# set2_uniques = set1 - set2
# set5 = set1_uniques.union(set2_uniques)
# print(set5)


#Zadanie2
# def join_sets():
#     list_x = list(range(51))
#     filtered_list_x = [i for i in list_x if i % 3 == 0]
#     set_x = set(filtered_list_x)
#     #DZIAŁA, SUPER
    
#     #teraz powtarzamy procedurę, ale z modulo 4
#     list_y = list(range(51))
#     filtered_list_y = [i for i in list_y if i % 4 == 0]
#     set_y = set(filtered_list_y)
#     print(set_y)
    
#     common_set = set_x.intersection(set_y)
#     print(f'Common elements of the two sets are: {common_set}')
    
#     unionized_sets = set_x.union(set_y) #robimy tak, żeby nie było powtórek, bo chcemy sumę unikalnych
#     print(f'Unionized set elements: {unionized_sets}')
#     sum_of_sets = sum(unionized_sets)
#     print(f'The sum of all unique numbers from both sets is {sum_of_sets}')
    
#     list_for_division_check = list(unionized_sets)
#     final_list = [i for i in list_for_division_check if i % 3 == 0 and i % 4 == 0]
#     final_set = set(final_list)
#     print(f'The items that are divided by 3 and 4 is: {final_set}')
    
# join_sets()


#Zadanie3

# def check_sentences(sentence1, sentence2):
#     words1 = set(sentence1.split())
#     print(words1)
#     words2 = set(sentence2.split())
#     print(words2)
    
#     intersected_words = words1.intersection(words2)
#     print(f'Słowa, które występują w obu zdaniach: {intersected_words}')
    
#     first_set_only_words = words1 - words2
#     print(first_set_only_words)
#     second_set_only_words = words2 - words1
#     print(second_set_only_words)
    
    
# sentence1 = input(str('Wpisz dowolne zdanie: '))
# sentence2 = input(str('Wpisz drugie dowolne zdanie: '))
# check_sentences(sentence1, sentence2)
#ciekawe jest to, że jak mamy kropkę to ona się zalicza do danego słowa, ale działa wszystko


#29.10 
#ĆWICZENIA NA SŁOWNIKACH I KROTKACH - DICT/TUPLE

#Zadanie1 
# def create_dict(n):
#  keys = list((range(n+1)))
#  print(keys)
#  values = [i ** 2 for i in keys]
#  print(values)

#  my_dict = dict(zip(keys, values)) #TU MIAŁEM PROBLEM, BO PRÓBOWAŁEM NAJPIERW Z NAWIASAMI {} xd
#  print(my_dict.items())


# n = int(input('Please input an integer value: '))
# create_dict(n)



''' Zadania praktyczne
Zadanie 1
Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową, np.: 112 - > „jeden jeden dwa” 9973 -> „dziewięć dziewięć siedem trzy”
Podpowiedź: potrzebujesz funkcji input(), słownika oraz pętli.

Zadanie 2
Stwórz funkcję przyjmującą listę liczb całkowitych, a zwracającą informację, na której pozycji znajduje się najmniejsza liczba.
Nie korzystaj z wbudowanych funkcji.

np. dla listy [42, 13, 56, 7, 12, 3, 85] funkcja powinna zwrócić 5, ponieważ pod tym indeksem w tej liście znajduje się element najmniejszy.

Zadanie 3
Stwórz funkcję, która sprawdzi, czy liczba podana w argumencie jest pierwsza (tzn. dzieli się bez reszty tylko przez 1 i przez samą siebie). Funkcja powinna przyjmować wartość numeryczną, a zwracać powinna wartość logiczną True/False.
Dla 11 funkcja zwróci True, natomiast dla 12 -> False.'''


#ZADANIA Z PĘTLI

#Zadanie 1
# def convert_nums_to_literals(numbers):
#     numbers = list(numbers)
#     numbers_dict = {'1': 'jeden', '2': 'dwa', '3': 'trzy', '4': 'cztery', '5': 'pięć', '6': 'sześć', '7': 'siedem', '8': 'osiem', '9': 'dziewięć', '0': 'zero'}
#     converted_numbers = [numbers_dict[num] for num in numbers]
#     print(converted_numbers)


# numbers: str = str(input("Podaj dowolny ciąg liczb całkowitych np. 4205, 554: "))
# convert_nums_to_literals(numbers)


#Zadanie 2
# def find_the_lowest_number(numbers):
#     lowest = numbers[0]
#     for i in numbers:
#         if i < lowest:
#             lowest = i
#     print(f'The lowest number is {lowest}')    

# input = (input("Podaj dowolną listę liczb całkowitych np. 12, 530, 1, 7: "))
# numbers = [int(x.strip()) for x in input.split(',')]
# find_the_lowest_number(numbers)

#Zadanie3 
#Sprawdzamy, czy dana liczba jest liczbą pierwszą
# #Musiałem się wesprzeć tutaj Claude - bo moje rozwiązanie nie było poprawne matematycznie
#Liczby pierwsze dzielą się tylko przez 1 i samą siebie i są większe od 2.
#Najpierw bierzemy liczbę i sprawdzamy, czy jest mniejsza od 2 - na pewno nie jest pierwsza.
#Dalej bierzemy sobie pętlę for na zakresie od 2 do danej liczby - jeśli znajdziemy, że dzieli się przez jakąkolwiek z liczb w zakresie no to z automatu nie jest liczbą pierwszą.

#Nie jest to skomplikowane, ale wymaga znajomości podstaw matmy - u mnie ich aktualnie JESZCZE nie ma 

# def check_the_number(number):
#     if number < 2:
#         print(f'{number} nie jest liczbą pierwszą')
#         return False
    
#     for i in range(2, number):
#         if number % i == 0:
#             print(f'{number} nie jest liczbą pierwszą (dzieli się przez {i})')
#             return False
        
#     print(f'{number} to liczba pierwsza')
#     return True

# number = int(input('Podaj liczbę całkowitą (np. 5, 77, 120): '))
# check_the_number(number)


##Zadania ze stringami

#Zadanie 1 - szuakmy palindroma
# def check_palindroma(string):
#     string = string.lower() #Dodane po tym, jak Madam mi odrzuciło jako nie palindrom
#     pozycja = -1
#     for x in range(0, len(string)):
#         obecna_litera = string[x]
#         if obecna_litera == string[pozycja]:
#             pozycja-=1
#             continue
#         else:
#             print(f'Litera {obecna_litera} z pozycji {x} w słowie {string} nie jest równa literze {string[pozycja]}. Słowo nie jest palindromem')
#             return False

#     print(f'Słowo {string} jest palindromem')
#     return True
    

# string = str(input('Wpisz dowolne słowo: '))
# check_palindroma(string)

#Cieszę się, że to wykminiłem - niby nic super skomplikowaneog, ale jednak :))

#Zadanie2 - Liczenie wielkich i małych liter w ciągu
#W zasadzie bardzo proste zadanie, wystarczy znać metody isupper() i islower()

# def counting_letters(string):
#     lower_counter = 0
#     upper_counter = 0
    
#     string.replace(" ", "")
#     print(string)
#     for i in string:
#         if i.isupper():
#             upper_counter+=1
#         elif i.islower():
#             lower_counter+=1    
#     print(f"Zdanie {string} zawiera {lower_counter} małych i {upper_counter} wielkich liter.")

    
# string = str(input('Wpisz dowolne zdanie: '))
# counting_letters(string)
    
    
    
#Zadanie 3
#Szukamy anagramów - zdań, w których po przestawieniu liter otrzymamy drugie zdanie.

# def check_anagramy(string1, string2):
    
#     letters1 = [char for char in string1 if char.isalpha()] #wcześniejsza iteracja działała przy słowach i niektórych zdaniach, ale gubiła się przy znakach interpunkcyjnych i innej ilości spacji
#     letters2 = [char for char in string2 if char.isalpha()] #isalpha musiałem podejrzeć!
    
#     print(letters1, letters2)
    
#     if len(letters1) != len(letters2):
#         print('Zdania nie są anagramami')
#         return False
#     for i in letters1:
#         if i in letters2:
#             letters2.remove(i)
#         else:
#             print(f'Nie ma już litery {i} w {letters2}. Zdanie nie jest anagramem')
#             return False
#     print(f'Zdania {string1} i {string2} są anagramami')
        
# #O KURDE, DZIAŁA XD
# Działa, ale gubi się przy znakach interpunkcyjnych i innej ilości spacji
    

# string1 = str(input('Wpisz dowolne zdanie: ')).lower()
# string2 = str(input('Wpisz drugie zdanie: ')).lower()
# check_anagramy(string1, string2)
