import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk



def valider():
    prenom = prenom_entry.get()
    nom = nom_entry.get()
    ville = ville_entry.get()

    if prenom and nom and ville:
        resultat = f"{prenom} // {nom} // {ville}"
        messagebox.showinfo("Résultat", resultat)
    else:
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")

def reinitialiser():
    prenom_entry.delete(0, tk.END)
    nom_entry.delete(0, tk.END)
    ville_entry.delete(0, tk.END)

fenetre = tk.Tk()
fenetre.title("Tk Formulaire")

# Labels et entrées
prenom_label = tk.Label(fenetre, text="Votre prénom :")
prenom_label.grid(row=0, column=0, sticky="w")
prenom_entry = tk.Entry(fenetre)
prenom_entry.grid(row=0, column=1)

nom_label = tk.Label(fenetre, text="Votre nom :")
nom_label.grid(row=1, column=0, sticky="w")
nom_entry = tk.Entry(fenetre)
nom_entry.grid(row=1, column=1)

ville_label = tk.Label(fenetre, text="Votre ville :")
ville_label.grid(row=2, column=0, sticky="w")
ville_entry = tk.Entry(fenetre)
ville_entry.grid(row=2, column=1)

# Boutons
valider_button = tk.Button(fenetre, text="Valider",bg = "green", command=valider)
valider_button.grid(row=3, column=0)

reinitialiser_button = tk.Button(fenetre, text="Réinitialiser",bg="blue", command=reinitialiser)
reinitialiser_button.grid(row=3, column=1)

quitter_button = tk.Button(fenetre, text="Quitter",bg="red", command= fenetre.quit)
quitter_button.grid(row=4, columnspan=2)

#chargement de l'image
image_path="D:/inshot/62003.jpg"
image=Image.open(image_path)
photo=ImageTk.PhotoImage(image)

#redimensionner l'image
"""image=image.resize((150, 100))"""

image_resized=image.resize((150, 150))
photo=ImageTk.PhotoImage(image_resized)

image_tk=ImageTk.PhotoImage(image)

#label pour afficher l'image a droite
image_label=tk.Label(fenetre, image=photo)
image_label.grid(row=0, column=2, rowspan=5)

fenetre.mainloop()