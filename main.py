


# def greet(somthing):
#     print("Hello")
#     print("How do you do ?: ")
#     print("Isn't the weather nice ?:  ")
#
# greet()

def life_in_weeks(age) :
    age = int (age)
    years_left = 90 - age

    weeks_left = years_left * (12*4)

    print (f"You have {weeks_left} weeks left. ")

life_in_weeks(45)





# ---------------------------------------day 7 ---------------------------------------------
# import random
#
# secret_word_liste = ["halim","nassim","sami","salim","nada","wissam","hana"]
# secret_word_to_find = random.choice(secret_word_liste)
# print(secret_word_to_find)
#
# #initialise les blanc dans la liste
# nbr_de_blanc = len(secret_word_to_find)
# nbr_de_blanc_list = []
# for i in range(0,nbr_de_blanc):
#     nbr_de_blanc_list.append("-")
# print(nbr_de_blanc_list)
#
# #converti le mot en une liste
#
# secret_word_choosen = list(secret_word_to_find)
# # print(secret_word_choosen)
#
# nbr_life = 10
# jackpot = False
#
# while nbr_life > 0 and not jackpot:
#
#     print(f"Il vous rest {nbr_life} vie")
#     print(nbr_de_blanc_list)
#     character = input("Entree un character :").lower()
#
#     for i in range (0,nbr_de_blanc):
#         if character == secret_word_choosen [i]:
#             nbr_de_blanc_list[i] = character
#
#         if nbr_de_blanc_list == secret_word_choosen :
#             jackpot = True
#             print("Jackpot")
#
#     nbr_life -=1
#
#
# if not jackpot :
#     print ("Game Over")
#
# #print (nbr_de_blanc_list)
#
# ---------------------------------------day 5 ---------------------------------------------

# generature de mot de pass
# list_letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
#                "v", "w", "x", "y", "z",
#                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
#                "V", "W", "X", "Y", "Z"]
# list_nombres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
# list_symboles = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
#                  "{", "}", "[", "]", ":", ";", "'", "<", ">", ",", ".", "?", "/", "|", "~", "`"
#                  ]
#
# print("Password Generator")
# nbr_of_letter = int(input("How many letter do you nwant in your password :"))
# nbr_of_numbers = int(input("How many number do you want in your password "))
# nbr_of_symbol = int(input("How many symbol do you want in your password "))
#
# password_list = []
#
# for char in range(0, nbr_of_letter):
#     password_list.append(random.choice(list_letter))
#     print(password_list)
#
# for nombre in range(0, nbr_of_numbers):
#     password_list.append(random.choice(list_nombres))
#     print(password_list)
#
# for symb in range(0, nbr_of_symbol):
#     password_list.append(random.choice(list_symboles))
#     print(password_list)
#
# random.shuffle(password_list)
#
# final_password =""
# for char in password_list:
#     final_password+=char
#
# print(final_password)


#     final_password += password (pass_wrd_index)
# print (f"le mot de pass final et {final_password}")


# ---------------------------------Day 5---------------------------------------
# weight = 185
# height = 1.85
#
# bmi = weight / (height ** 2)
# print (round (bmi,2))
#
# if   bmi < 18.5 :
#     print ("Underweight")
#
# elif 18.5 <= bmi <= 24.9 :
#      print ("Normal weight")
#
# else :
#     print ("Overweight")
#
# number_to_chek = int(input ("What is the number you want to chek ?:"))
#
# if number_to_chek % 2 == 0:
#     print ("Even")
# else:
#     print ("0dd")
#
#
#
# print("Welcom to teh rollercoaster !")
# height = int (input("What is your height in cm ? "))
#
# if height >= 120 :
#     print ("you can ride the rollercoaster")
#     age = int(input("What is your age : ? "))
#     if age <=12:
#         bill = 5
#         print("Child tikets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tikets are $7.")
#     else:
#         bill = 12
#         print("Adult tikets are $12.")
#
#     wants_a_photo = input("Do you want a photo Y or N :")
#     if wants_a_photo.lower() == "y" :
#         bill +=3
#     print(f"Your final bill is {bill}")
#
# else:
#     print ("Sorry you have to grow taller before you can ride.")
#
#
#
#
#
# ---------------------------------Day 2---------------------------------------
#
# print ("Welcom to the tip calculator")
# bill = float(input ("What was the total bill :? "))
# tip = float(input("How much tip would you like to give ? 10 , 12 , or 15 ?: "))
# nbr_personne = int(input ("How many people to split th bill ? : "))
#
# bill_percent = bill * (tip / 100)
# total_bill = bill_percent + bill
# bill_per_personne = total_bill / nbr_personne
# final_amount = round(bill_per_personne,2)
# print(f"Each personne should pay : {final_amount}")
#
#
#
# bmi = 105/1.81*2
# print (bmi)
# print(int(bmi))
#
# print(round(bmi,3))
#
#
#
#
#
#
# print("Number of letters in your name :" + len(input("Enter your name")))
#
# name = input("Enter your name ?")
# name_len = len (name)
# print ("Number of letters in your name :" + str(name_len))
#
# print (type(123))
# print (type(123.25))
# print (type("hello"))
# print (type(True))
#
#
#
#
#
# ---------------------------------Day 1---------------------------------------
# print ("Welcom to the Band Name Generator. ")
# city = input ("What's the name of the city you grew up in ?\n")
# pets_name = input ("What's your pet's name ?\n")
# print ("Your band name could be "+city+" "+pets_name)
# # print ("hello " + input("What is your name ?")+ " !")
# # username = input ("What is your name : ?")
# # length = len(username)
# # print (length)
#
# # time_until_midnight = "5"
# # print ("There are " + time_until_midnight + " hours until midnight")
#
# # num_hours = "5"
# # print ("There are " + num_hours + " hours until midnight")
#
# time_until_midnight = "5"
# print ("There are "+time_until_midnight+" hours until midnight")
