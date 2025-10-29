

                    """Création de classe player"""
class Player():
                    """param vie + nom (protégé)"""
    def __init__(self, health: int = 100, name: str ):
        self.__name = name
        self.health = health
                    """soigner le joueur"""
    def heal(self,amount:int):
        self.health += amount
                """" fct str pour impression""""
    def __str__(self):
        return f'blabbla'