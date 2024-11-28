import tkinter as tk
from tkinter import messagebox

def ajouter_tache():
    """Ajoute une tâche à la liste."""
    tache = entry_tache.get()
    if tache.strip():  # Vérifie que la tâche n'est pas vide
        listbox_taches.insert(tk.END, tache)
        entry_tache.delete(0, tk.END)  # Efface le champ d'entrée
    else:
        messagebox.showwarning("Erreur", "Veuillez entrer une tâche valide.")

def supprimer_tache():
    """Supprime la tâche sélectionnée."""
    try:
        selection = listbox_taches.curselection()
        if selection:
            listbox_taches.delete(selection)
        else:
            messagebox.showinfo("Info", "Veuillez sélectionner une tâche à supprimer.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

def marquer_complete():
    """Marque une tâche comme complète."""
    try:
        selection = listbox_taches.curselection()
        if selection:
            index = selection[0]
            tache = listbox_taches.get(index)
            listbox_taches.delete(index)
            listbox_taches.insert(index, f"{tache} ✅")
        else:
            messagebox.showinfo("Info", "Veuillez sélectionner une tâche à marquer comme complète.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

# Configuration de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Application ToDoList")
fenetre.geometry("400x400")

# Champ d'entrée

frame_haut = tk.Frame(fenetre)
frame_haut.pack(pady=10)

entry_tache = tk.Entry(frame_haut, width=30)
entry_tache.pack(side=tk.LEFT, padx=5)

bouton_ajouter = tk.Button(frame_haut, text="Ajouter",bg="green", command=ajouter_tache)
bouton_ajouter.pack(side=tk.LEFT)

# Liste des tâches
listbox_taches = tk.Listbox(fenetre, width=50, height=15)
listbox_taches.pack(pady=10)

# Boutons pour supprimer et marquer comme complet
frame_bas = tk.Frame(fenetre)
frame_bas.pack(pady=10)

bouton_supprimer = tk.Button(frame_bas, text="Supprimer",bg="red", command=supprimer_tache)
bouton_supprimer.pack(side=tk.LEFT, padx=10)

bouton_marquer = tk.Button(frame_bas, text="Marquer comme complet",bg="blue", command=marquer_complete)
bouton_marquer.pack(side=tk.LEFT, padx=10)

# Lancer l'application
fenetre.mainloop()
