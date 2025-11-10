from game.area.area_class import CreaArea
from game.area.area_scripting import load_csv_area
list_command = ['look','caca']
dico_area = load_csv_area()
class Debut_script():
    def __init__(self):
        pass
    def run(self):
        area = 'PLA01'
        print('Bienvenue a lEphec')
        command = input('<')
        while command != 'look' :
            command = input('<')
        print('un homme sapproche de vous \n - Comment vous appeler vous ?')
        name = input('Entrer votre nom : ')
        print(f'Bonjour {name}, cest le Delvigne.')
        command = input('> ')
        while command not in list_command :
            command = input('<')
        if command == 'look' :
            print(dico_area[area].long_desc)
        elif command == 'caca' :
            print('caca partout partout')
        return name

debut = Debut_script()
print(debut.run())