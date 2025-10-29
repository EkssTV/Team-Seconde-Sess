

#Création de classe player
class Player:
#Définition des caractéristiques du player
    def __init__(self, health: int = 5, name: str ='Student', start_area: str = "place_de_l_ephec"):
        self.__name = name
        self.health = health
        self.current_area = start_area
    #Savoir si le personnage est vivant ou non
        self.alive = True
    #Sauvegarde du personnage
        self.save_slot = "save_1"


#Fonctions du player
    #Ajouter de la vie au player
    def add_health(self,amount:int):
        self.health += amount
    #Retirer de la vie au player
    def rmv_health(self,amount:int):
        self.health -= amount
    #Mort du personnage
    def death(self):
        self.alive = False
    @property
    def get_name(self):
        return self.__name
    @get_name.setter
    def get_name(self,new_name):
        self.__name = new_name
    #fct str pour impression
    def __str__(self):
        return f'le jouer est {self.get_name}'