from typing import final

print ("Welcom to the tip calculator")
bill = float(input ("What was the total bill :? "))
tip = float(input("How much tip would you like to give ? 10 , 12 , or 15 ?: "))
nbr_personne = int(input ("How many people to split th bill ? : "))

bill_percent = bill * (tip / 100)
total_bill = bill_percent + bill
bill_per_personne = total_bill / nbr_personne
final_amount = round(bill_per_personne,2)
print(f"Each personne should pay : {final_amount}")

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Belouz208/formation_angela.git
git push -u origin main


# bmi = 105/1.81*2
# print (bmi)
# print(int(bmi))
#
# print(round(bmi,3))
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
