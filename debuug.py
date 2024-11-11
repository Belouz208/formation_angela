import random

# Choisir un mot aléatoire dans la liste
secret_word_list = ["halim", "nassim", "sami", "salim", "nada", "wissam", "hana"]
secret_word_to_find = random.choice(secret_word_list)
print(secret_word_to_find)

# Initialiser les blancs dans la liste
nbr_de_blanc_list = ["-"] * len(secret_word_to_find)
secret_word_choosen = list(secret_word_to_find)

nbr_life = 10
jackpot = False

while nbr_life > 0 and not jackpot:
    print(f"Il vous reste {nbr_life} vies")
    print(" ".join(nbr_de_blanc_list))
    character = input("Entrez un caractère : ").lower()

    # Mettre à jour les blancs si le caractère est trouvé
    if character in secret_word_choosen:
        for i, letter in enumerate(secret_word_choosen):
            if letter == character:
                nbr_de_blanc_list[i] = character

    # Vérifier si le mot a été deviné
    if nbr_de_blanc_list == secret_word_choosen:
        jackpot = True
        print("Jackpot! Vous avez trouvé le mot:", secret_word_to_find)
    else:
        nbr_life -= 1

if not jackpot:
    print("Game Over. Le mot était :", secret_word_to_find)







