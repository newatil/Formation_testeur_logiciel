
def code_caesar(msg, nbr, sens):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    
    # Normaliser nb pour qu'il soit dans la plage 0-25
    nbr = nbr % 26
    
    # Inverser le nb si sens est 'inverse'
    if sens == 'inverse':
        nbr = -nbr
    
    # Traiter chaque caractère dans msg
    for char in msg.upper():
        if char in alphabet:
            original_index = alphabet.index(char)
            new_index = (original_index + nbr) % 26
            result += alphabet[new_index]
        else:
            result += char
    
    return result

# Début du programme principal
if __name__ == "__main__":
    # Lire le message à chiffrer saisi par l'utilisateur
    msg = input("Enter the message to encrypt: ")
    
    # Lire la valeur du décalage (nb) depuis l'utilisateur et la convertir en entier
    nb = int(input("Enter the shift value (nb): "))
    
    # Lire la direction du décalage (sens) depuis l'utilisateur et la convertir en minuscule
    sens = input("Enter the direction of shift ('order' or 'inverse'): ").lower()
    
    # Tant que direction n'est pas 'order' ou 'inverse'
    while sens not in ['order', 'inverse']:
        sens = input("Invalid input. Please enter 'order' or 'inverse': ").lower()
    
    # Appeler la fonction code_caesar avec msg, nb et sens et stocker le résultat dans encrypted_msg
    encrypted_msg = code_caesar(msg, nb, sens)
    
    # Afficher "Encrypted msg: " suivi de encrypted_msg
    print("Encrypted msg: ", encrypted_msg)

