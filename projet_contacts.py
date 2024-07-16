
#########################################################################
"""
print("appli contacts")

def ajouter_contact():
    nom = input("Entrez le nom: ")
    prenom = input("Entrez le prénom: ")
    email = input("Entrez l'adresse email: ")
    with open("contacts.txt", "w") as file:
        file.write(f"{nom}, {prenom}, {email}\n")
    print("Contact ajouté avec succès.")
    
ajouter_contact()
 
#################################################################

def lire_contacts():
    try:
        with open("contacts.txt", "r") as f1:
            contacts = f1.readlines()
            for x in contacts:     # pour chaque ligne parmis toutes les lignes fait moi ca:
                nom, prenom, email = x.strip().split(", ")
                print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")
    except FileNotFoundError:
        print("Le fichier 'contacts.txt' n'existe pas encore.")
        
lire_contacts()     
"""   
#######################################################################

def trier_contacts():
    try:
        with open("contacts.txt", "r") as f2:
            contacts = f2.readlines()
        contacts.sort()
        with open("contacts.txt", "w") as f3:
            for cont in contacts:
                f3.write(cont)
        print("Les contacts ont été triés par ordre alphabétique.")
    except FileNotFoundError:
        print("Le fichier 'contacts.txt' n'existe pas encore.")
    lire_contacts()
    
    
#########################################################################
"""
def compter_contacts():
    try:
        with open("contacts.txt", "r") as f4:
            contacts = f4.readlines()
        nombre_contacts = len(contacts)
        print(f"Il y a {nombre_contacts} contact(s) dans le fichier.")
    except FileNotFoundError:
        print("Le fichier 'contacts.txt' n'existe pas encore.")
        
        
#########################################################################

def rechercher_contact():
    nom_recherche = input("Entrez le nom du contact à rechercher: ")
    try:
        with open("contacts.txt", "r") as f5:
            contacts = f5.readlines()
        for contact in contacts:
            nom, prenom, email = contact.strip().split(", ")
            if nom.lower() == nom_recherche:
                print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")
                return
        print("Aucun contact trouvé avec ce nom.")
    except FileNotFoundError:
        print("Le fichier 'contacts.txt' n'existe pas encore.")
        
        
#########################################################################

def modifier_contact():
    nom_recherche = input("Entrez le nom du contact à modifier: ")
    try:
        with open("contacts.txt", "r") as f6:
            contacts = fichier.readlines()
        contacts_modifies = []
        contact_trouve = False
        for contact in contacts:
            nom, prenom, email = contact.strip().split(", ")
            if nom == nom_recherche:
                contact_trouve = True
                nouveau_prenom = input(f"Entrez le nouveau prénom pour {nom} : ")
                nouveau_email = input(f"Entrez le nouvel email pour {nom} : ")
                contacts_modifies.append(f"{nom}, {nouveau_prenom}, {nouveau_email}\n")
            else:
                contacts_modifies.append(contact)
        if contact_trouve:
            with open("contacts.txt", "w") as f:
                f.writelines(contacts_modifies)
            print("Contact modifié avec succès.")
        else:
            print("Aucun contact trouvé avec ce nom.")
    except FileNotFoundError:
        print("Le fichier 'contacts.txt' n'existe pas encore.")
        


#########################################################################

def supprimer_contact():
    nom_recherche = input("Entrez le nom du contact à supprimer: ")
    try:
        with open("contacts.txt", "r") as f:
            contacts = f.readlines()
        contacts_restants = []
        contact_trouve = False
        for contact in contacts:
            nom, prenom, email = contact.strip().split(", ")
            if nom == nom_recherche:
                contact_trouve = True
            else:
                contacts_restants.append(contact)
        if contact_trouve:
            with open("contacts.txt", "w") as f:
                f.writelines(contacts_restants)
            print("Contact supprimé avec succès.")
        else:
            print("Aucun contact trouvé avec ce nom.")
    except FileNotFoundError:
        print("Le fichier 'contacts.txt' n'existe pas encore.")
        
        
#########################################################################

def afficher_menu():
    print("\nMenu de gestion des contacts:")
    print("1. Ajouter un contact")
    print("2. Lire les contacts")
    print("3. Trier les contacts")
    print("4. Compter les contacts")
    print("5. Rechercher un contact")
    print("6. Modifier un contact")
    print("7. Supprimer un contact")
    print("8. Quitter")
    
    
    
#########################################################################

def main():
    while True:
        afficher_menu()
        choix = input("Entrez votre choix (1-8): ")
        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            lire_contacts()
        elif choix == "3":
            trier_contacts()
        elif choix == "4":
            compter_contacts()
        elif choix == "5":
            rechercher_contact()
        elif choix == "6":
            modifier_contact()
        elif choix == "7":
            supprimer_contact()
        elif choix == "8":
            print("Merci pour votre visite!")
            break
        else:
            print("Choix non valide, veuillez réessayer.")

if __name__ == "__main__":
    main()
    
"""

