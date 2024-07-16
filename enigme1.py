
def decode_phone_numbers(numbers):
    # Dictionnaire de correspondance chiffre -> lettre
    phone_map = {
        '2': 'ABC', '3': 'DEF', '4': 'GHI',
        '5': 'JKL', '6': 'MNO', '7': 'PQRS',
        '8': 'TUV', '9': 'WXYZ', '0': ' '
    }

    # Initialisation des variables de travail
    decoded_message = ""
    current_char = None
    count = 0

    for number in numbers:
        if number == '-':
            # Traitement de la fin d'une séquence de chiffres
            if current_char is not None:
                decoded_message += current_char
                current_char = None
                count = 0
        else:
            # Conversion du chiffre en lettre selon le dictionnaire
            letters = phone_map[number]
            current_char = letters[count % len(letters)]
            count += 1

    # Ajouter le dernier caractère si nécessaire
    if current_char is not None:
        decoded_message += current_char

    return decoded_message

# Exemples à décoder
numbers1 = "4-33-66-444-666-88-7777"
numbers2 = "999-666-88-0-9-444-66"
numbers3 = "555-33-0-3-33-333-444"
numbers4 = "33-7777-8-0-4-2-4-66-33"

# Affichage des résultats
print("Message 1:", decode_phone_numbers(numbers1))
print("Message 2:", decode_phone_numbers(numbers2))
print("Message 3:", decode_phone_numbers(numbers3))
print("Message 4:", decode_phone_numbers(numbers4))

