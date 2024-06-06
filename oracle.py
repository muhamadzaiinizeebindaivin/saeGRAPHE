import json
from tkinter import filedialog
import networkx as nx
import tkinter as tk
from tkinter import messagebox, simpledialog
import requetes 


def choisir_fichier():
    filepath = filedialog.askopenfilename(title="Choisir un fichier", filetypes=[("Fichiers texte", "*.txt"), ("Fichiers JSON", "*.json")])
    if filepath:
        try:
            if filepath.endswith('.txt'):
                requetes.txt_to_json(filepath, 'data_100.json')
                fichier = 'data_100.json'
            else:
                fichier = filepath
            global G
            G = requetes.json_vers_nx(fichier)
            afficher_application_principale()
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue lors du chargement du fichier : {e}")



def trouver_collaborateurs_communs():
    u = simpledialog.askstring("Acteur 1", "Entrez le nom du premier acteur:")
    v = simpledialog.askstring("Acteur 2", "Entrez le nom du deuxième acteur:")
    result = requetes.collaborateurs_communs(G, u, v)
    messagebox.showinfo("Collaborateurs communs", str(result))

def trouver_collaborateurs_proches():
    u = simpledialog.askstring("Acteur", "Entrez le nom de l'acteur:")
    k = simpledialog.askinteger("Distance", "Entrez la distance maximale:")
    result = requetes.collaborateurs_proches(G, u, k)
    messagebox.showinfo("Collaborateurs proches", str(result))

def verifier_est_proche():
    try:
        u = simpledialog.askstring("Acteur 1", "Entrez le nom du premier acteur:")
        v = simpledialog.askstring("Acteur 2", "Entrez le nom du deuxième acteur:")
        k = simpledialog.askinteger("Distance", "Entrez la distance maximale (par défaut 1):", initialvalue=1)
        result = requetes.est_proche(G, u, v, k)  
        messagebox.showinfo("Est proche", str(result))
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

def trouver_distance():
    acteur1 = simpledialog.askstring("Acteur 1", "Entrez le nom du premier acteur:")
    acteur2 = simpledialog.askstring("Acteur 2", "Entrez le nom du deuxième acteur:")
    result = requetes.distance(G, acteur1, acteur2)
    messagebox.showinfo("Distance", str(result))

def trouver_centralite():
    u = simpledialog.askstring("Acteur", "Entrez le nom de l'acteur:")
    result = requetes.centralite(G, u)
    messagebox.showinfo("Centralité", str(result))

def trouver_centre_hollywood():
    result = requetes.centre_hollywood(G)
    messagebox.showinfo("Centre d'Hollywood", str(result))

def trouver_eloignement_max():
    result = requetes.eloignement_max(G)
    messagebox.showinfo("Éloignement maximal", str(result))

def afficher_application_principale():
    root.withdraw()  # Cache la fenêtre actuelle

    app = tk.Toplevel()
    app.title("Application de Collaboration des Acteurs")

    btn_collaborateurs_communs = tk.Button(app, text="Trouver les collaborateurs communs", command=trouver_collaborateurs_communs)
    btn_collaborateurs_communs.pack(fill=tk.X, padx=10, pady=5)

    btn_collaborateurs_proches = tk.Button(app, text="Trouver les collaborateurs proches", command=trouver_collaborateurs_proches)
    btn_collaborateurs_proches.pack(fill=tk.X, padx=10, pady=5)

    btn_est_proche = tk.Button(app, text="Vérifier si deux acteurs sont proches", command=verifier_est_proche)
    btn_est_proche.pack(fill=tk.X, padx=10, pady=5)

    btn_distance = tk.Button(app, text="Trouver la distance entre deux acteurs", command=trouver_distance)
    btn_distance.pack(fill=tk.X, padx=10, pady=5)

    btn_centralite = tk.Button(app, text="Trouver la centralité d'un acteur", command=trouver_centralite)
    btn_centralite.pack(fill=tk.X, padx=10, pady=5)

    btn_centre_hollywood = tk.Button(app, text="Trouver le centre d'Hollywood", command=trouver_centre_hollywood)
    btn_centre_hollywood.pack(fill=tk.X, padx=10, pady=5)

    btn_eloignement_max = tk.Button(app, text="Trouver l'éloignement maximal", command=trouver_eloignement_max)
    btn_eloignement_max.pack(fill=tk.X, padx=10, pady=5)

    btn_quitter = tk.Button(app, text="Quitter", command=app.quit)
    btn_quitter.pack(fill=tk.X, padx=10, pady=5)


def main():
    global root
    root = tk.Tk()
    root.title("Page d'accueil")

    btn_choisir_fichier = tk.Button(root, text="Choisir un fichier", command=choisir_fichier)
    btn_choisir_fichier.pack(fill=tk.X, padx=50, pady=50)

    root.mainloop()


if __name__ == "__main__":
    main()