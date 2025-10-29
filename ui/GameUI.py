import tkinter
from data.assets.fonts.banner.banner import banner
from game.command import Command
class GameUI:
    def __init__(self):
        # Fenêtre principale
        self.root = tkinter.Tk()
        self.root.title("Ephec Quest")
        self.root.configure(background="black")
        self.root.geometry("1280x720")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)


        # Titre ASCII
        self.title = tkinter.Label(
            self.root,
            text=banner.shw_banner(),
            font=("Courier", 8),
            bg="black",
            fg="white",
            justify="center",
        )
        self.title.grid(column=0, row=0, columnspan=2, sticky="nsew")

        # Cadre principal pour output + scrollbar
        frame = tkinter.Frame(self.root)
        frame.grid(column=0, row=1, columnspan=2, padx=10,sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=0)

        # Scrollbar
        scrollbar = tkinter.Scrollbar(frame)
        scrollbar.grid(column=1, row=0,sticky="ns" )

        # Zone d'affichage (output)
        self.output_zone = tkinter.Text(
            frame,
            height=20,
            width=80,
            bg="black",
            fg="white",
            font=("Courier", 12),
            yscrollcommand=scrollbar.set
        )
        self.output_zone.grid(column=0, row=0,columnspan=1,sticky='nsew')

        scrollbar.config(command=self.output_zone.yview)

        # Zone de saisie (input)
        self.input_zone = tkinter.Entry(
            self.root,
            width=80,
            font=("Courier", 12),
            bg="gray15",
            fg="white",
            insertbackground="white"  # curseur blanc
        )
        self.input_zone.grid(column=0, row=2, columnspan=2, pady=10,sticky="nsew")
        self.input_zone.bind("<Return>", self.process_command)

        self.command_handler = Command(self)  # donne la class Command

    #pour lancer la loop
    def run(self):
        self.root.mainloop()
    #pour pull la commande
    def process_command(self, event):
        command = self.input_zone.get()
        command = command.strip().lower()
        self.output_zone.insert(tkinter.END, f"> {command}\n")
        self.command_handler.execute(command)
        self.input_zone.delete(0, tkinter.END)
