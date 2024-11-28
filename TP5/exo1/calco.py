import tkinter as tk

class Calculatrice:
    def __init__(self, master):
        self.master = master
        master.title("Calculatrice")

        self.resultat = tk.Entry(master, width=20, font=('Arial', 16), borderwidth=5)
        self.resultat.grid(row=0, column=0, columnspan=4)

        # Créer les boutons
        self.creer_boutons()

    def creer_boutons(self):
        boutons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for bouton in boutons:
            tk.Button(self.master, text=bouton, width=5, height=2, command=lambda b=bouton: self.appuyer(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def appuyer(self, bouton):
        if bouton == '=':
            try:
                expression = self.resultat.get()
                resultat = eval(expression)
                self.resultat.delete(0, tk.END)
                self.resultat.insert(0, resultat)
            except Exception as e:
                self.resultat.delete(0, tk.END)
                self.resultat.insert(0, "Erreur")
        else:
            self.resultat.insert(tk.END, bouton)

if __name__ == "__main__":
    root = tk.Tk()
    calculatrice = Calculatrice(root)
    root.mainloop()
