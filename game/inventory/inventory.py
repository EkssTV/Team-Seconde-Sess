

#Création class Inventory

class Inventory:
    #initier l'inventaire (liste)
    def __init__(self):
        self.items = []
    #rajouter un item dans la liste items(l'inventaire)
    def add_item(self, item):
        self.items.append(item)
    #supprimer un item dans la liste items(l'inventaire)
    def rm_item(self, item):
        self.items.remove(item)
    #afficher l'inventaire
    def show_inventory(self):
        return self.items