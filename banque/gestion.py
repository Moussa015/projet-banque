import datetime

#classe Banque
class Banque:
    def __init__(self, name_bank):
        self.name_bank = name_bank
        self.siege = "Ouagadougou"
        self.type_account =["courant","epargne","bloque"]


#classe Client
class Client(Banque):
    def __init__(self, name_bank,name,firstname,phone,balance_init,type_account):
        super().__init__(name_bank)
        self.name = name
        self.firstname = firstname
        self.phone = phone
        self.balance = balance_init
        self.type_account = type_account
        self.category = self.define_category()

    #methode pour definir la categorie du client
    def define_category(self):
        if self.balance >= 100_000_000:
            return "VIP"
        elif self.balance >= 10_000_000:
            return "Classique"
        elif self.balance >= 100_000:
            return "Jeune/Etudiant"
        else:
            return "Non admissible"


    #methode pour faire un depot
    def deposit(self, amount):
        self.balance += amount
        self._register_transaction("Depot", amount)

    
    #methode pour faire un retrait
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self._register_transaction("Retrait", amount)
        else:
            print("Solde insuffisant")

    #methode pour afficher le solde
    def show_balance(self):
        print(f"Solde de {self.name} {self.firstname} : {self.balance} FCFA")


    #methode pour enregistrer les transactions sur le fichier rapport.txt
    def _register_transaction(self, type_transaction, amount):
        now= datetime.now()
        with open("rapport.txt", "a") as f:
            f.write(f"{self.name} {self.firstname} - {type_transaction} de {amount} FCFA le {now.strftime('%d-%m-%Y %H:%M:%S')}\n")