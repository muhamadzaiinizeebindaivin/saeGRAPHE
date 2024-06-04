import json
import networkx as nx
import tkinter as tk
from tkinter import messagebox, simpledialog
import requetes 
#Pour l'applicaion graphique


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
        result = requetes.est_proche(G, u, v, k)  # Assuming G is defined somewhere
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

def main():
    global G
    requetes.txt_to_json('data_100.txt', 'data_100.json')
    G = requetes.json_vers_nx('data_100.json')
    root = tk.Tk()
    root.title("Application de Collaboration des Acteurs")

    btn_collaborateurs_communs = tk.Button(root, text="Trouver les collaborateurs communs", command=trouver_collaborateurs_communs)
    btn_collaborateurs_communs.pack(fill=tk.X)

    btn_collaborateurs_proches = tk.Button(root, text="Trouver les collaborateurs proches", command=trouver_collaborateurs_proches)
    btn_collaborateurs_proches.pack(fill=tk.X)

    btn_est_proche = tk.Button(root, text="Vérifier si deux acteurs sont proches", command=verifier_est_proche)
    btn_est_proche.pack(fill=tk.X)

    btn_distance = tk.Button(root, text="Trouver la distance entre deux acteurs", command=trouver_distance)
    btn_distance.pack(fill=tk.X)

    btn_centralite = tk.Button(root, text="Trouver la centralité d'un acteur", command=trouver_centralite)
    btn_centralite.pack(fill=tk.X)

    btn_centre_hollywood = tk.Button(root, text="Trouver le centre d'Hollywood", command=trouver_centre_hollywood)
    btn_centre_hollywood.pack(fill=tk.X)

    btn_eloignement_max = tk.Button(root, text="Trouver l'éloignement maximal", command=trouver_eloignement_max)
    btn_eloignement_max.pack(fill=tk.X)

    btn_quitter = tk.Button(root, text="Quitter", command=root.quit)
    btn_quitter.pack(fill=tk.X)

    root.mainloop()

if __name__ == "__main__":
    main()