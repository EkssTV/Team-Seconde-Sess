from pathlib import Path
import json
from ..object.object_class import CreaObject
from ..object.object_scripting import load_csv_object

"""
===============================================
 EPHEC QUEST - player_class.py
-----------------------------------------------
 Description : création de la class player
 Auteur      : Matthieu
 Date        : 2025
===============================================
"""
class Player:
    """
    Represents a player in EPHEC QUEST.

    Attributes:
        inv (list): The player's inventory.
        __name (str): The player's private name.
        health (int): The player's current health points.
        current_area (str): The current area the player is in.
        current_script (str): The current script or scenario.
    """

    def __init__(self, name: str = 'student', inv: list = None, health: int = 5,
                 current_area: str = 'PLACEEPHEC', current_script: str = 'script_debut', save_path=None):
        """
        Initializes a new player with base attributes and creates a save file if it doesn't exist.

        Args:
            name (str): The player's name.
            inv (list): Optional starting inventory.
            health (int): Initial health points.
            current_area (str): Starting area.
            current_script (str): Initial script.
        """
        self.inv = inv if inv is not None else []
        self.__name = name
        self.health = health
        self.current_area = current_area
        self.current_script = current_script
        self.save_path = f'saves/{name}.json'

        Path('saves').mkdir(exist_ok=True)
    def add_inv(self, id_obj: str):
        """
        Adds an object to the player's inventory.

        Args:
            id_obj (str): The object ID to add.
        """
        self.inv.append(id_obj)

    def supp_inv(self, id_obj: str):
        """
        Removes an object from the player's inventory if it exists.

        Args:
            id_obj (str): The object ID to remove.
        """
        if id_obj in self.inv:
            self.inv.remove(id_obj)

    def add_health(self, much: int):
        """
        Increases the player's health.

        Args:
            much (int): Amount of health to add.
        """
        self.health += much

    def supp_health(self, much: int):
        """
        Decreases the player's health. Prints a message if the player dies.

        Args:
            much (int): Amount of health to remove.
        """
        self.health = max(0, self.health - much)
        if self.health == 0:
            print('player dead')

    def move_area(self, new_area: str):
        """
        Changes the player's current area.

        Args:
            new_area (str): The new area ID.
        """
        self.current_area = new_area

    def change_script(self, new_script: str):
        """
        Changes the current script.

        Args:
            new_script (str): The new script ID.
        """
        self.current_script = new_script

    @property
    def name(self):
        """
        Gets the player's name.

        Returns:
            str: The player's name.
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Sets the player's name with validation.

        Args:
            new_name (str): The new name.

        Raises:
            ValueError: If the name is empty or only whitespace.
        """
        if not new_name.strip():
            raise ValueError("Name cannot be empty.")
        self.__name = new_name

    def __str__(self):
        """
        Returns a readable summary of the player's state.

        Returns:
            str: A formatted string with player details.
        """
        return (
            f"👤 Player : {self.name}\n"
            f"❤️ Health : {self.health}\n"
            f"📦 Inventory : {', '.join(self.inv) if self.inv else 'Empty'}\n"
            f"📍 Current Area : {self.current_area}\n"
            f"🎬 Current Script : {self.current_script}"
        )
    def show_inv(self):
        bag=""
        if len(self.inv) == 0:
            bag = 'Rien ne se trouve dans ton sac'
        else :
            str_of_name_object = ""
            for i in self.inv:
                str_of_name_object+= f'{load_csv_object()[i].nom}[{i}] : {load_csv_object()[i].descri}\n{load_csv_object()[i].utilite}'
            bag = f'Dans ton sac il y a :\n{str_of_name_object}'
        return bag
    def save(self):
        """
        Saves the player's current state to a JSON file.
        """
        with open(self.save_path, 'w') as f:
            data = {
                "name": self.name,
                "health": self.health,
                "inv": self.inv,
                "current_area": self.current_area,
                "current_script": self.current_script,
                "save_path": self.save_path
            }
            json.dump(data, f, indent=4)
            z
    def load(self,path):
        """
        Loads the player's state from a JSON file, if it exists and is valid.
        """
        try:
            with open(path, 'r') as f:
                data = json.load(f)
            self.name = data["name"]
            self.health = data["health"]
            self.inv = data["inv"]
            self.current_area = data["current_area"]
            self.current_script = data["current_script"]
        except FileNotFoundError:
            print(f'Loading failed: file not found → {self.save_path}')
        except json.JSONDecodeError:
            print("Failed to read: invalid JSON format.")
        except IOError:
            print('I/O error occurred while loading.')

