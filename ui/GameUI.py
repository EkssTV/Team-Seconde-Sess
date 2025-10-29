import tkinter

class GameUI:
    def __init__(self):
        # Fenêtre principale
        self.root = tkinter.Tk()
        self.root.title("Ephec Quest")

        # Zone d'affichage (output)
        self.output_zone = tkinter.Text(self.root, height=20, width=80, bg="black", fg="white", font=("Times new Roman", 12))
        self.output_zone.pack()

        # Scrollbar
        scrollbar = tkinter.Scrollbar(self.root)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Zone de texte avec scroll
        self.output_zone = tkinter.Text(self.root, height=20, width=80, yscrollcommand=scrollbar.set)
        self.output_zone.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

        # Lien entre scrollbar et zone de texte
        scrollbar.config(command=self.output_zone.yview)

        # Zone de saisie (input)
        self.input_zone = tkinter.Entry(self.root, width=80)
        self.input_zone.pack()
        self.input_zone.bind("<Return>", self.process_command)

    def run(self):
        self.root.mainloop()

    def process_command(self, event):
        # Récupère le texte tapé
        command = self.input_zone.get()

        # Affiche la commande dans la zone d'output
        self.output_zone.insert(tkinter.END, f"{command}\n")
        self.input_zone.delete(0, tkinter.END)
