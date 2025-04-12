from banque.gestion import Client 


client_list = []

print("Bienvenue à la Banque X !")

for i in range(5):
    print(f"\n--- Enregistrement du Client {i+1} ---")

    name = input("Nom : ")
    firstname = input("Prenom : ")

    while True:
        phone = input("numero de telephone :")
        if phone.isdigit():
            phone= int(phone)
            break

        else :
            print("le numero ne doit comporter que des chiffres.")
        

    while True:
        try:
            balance = float(input("Solde initial en FCFA : "))
            break
        except ValueError:
            print("Veuiller entrer un montant valide.")
    
    type_account = ""
    while type_account not in ["courant","epargne","bloque"]:
        type_account = input("Type de compte(courant/epargne/bloque)")

    client = Client("Banque X", name, firstname, phone, balance,type_account)
    client_list.append(client)

    print(f"Client {client.name} {client.firstname} ajoute a la categorie : {client.category}")

print("\n=== Resume des clients enregistres ===")

for client in client_list:
    client.show_balance()
    client._register_transaction("Ouverture de compte", client.balance)
    print(f"Type de compte : {client.type_account}")