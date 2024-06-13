#Version pour le terminal


import json
import networkx as nx
import requetes
import os

# Fonction pour choisir un fichier à partir du système de fichiers
def choisir_fichier():
    filepath = input("Entrez le chemin du fichier (format .txt ou .json) : ")
    if os.path.isfile(filepath):
        try:
            # Conversion du fichier texte en JSON si nécessaire
            if filepath.endswith('.txt'):
                requetes.txt_to_json(filepath, 'data_100.json')
                fichier = 'data_100.json'
            else:
                fichier = filepath
            global G
            # Conversion du fichier JSON en graphe NetworkX
            G = requetes.json_vers_nx(fichier)
            afficher_application_principale()  # Afficher l'application principale
        except Exception as e:
            print(f"Une erreur est survenue lors du chargement du fichier : {e}")
    else:
        print("Fichier introuvable. Veuillez réessayer.")

# Fonction pour trouver les collaborateurs communs entre deux acteurs
def trouver_collaborateurs_communs():
    u = input("Entrez le nom du premier acteur: ")
    v = input("Entrez le nom du deuxième acteur: ")
    result = requetes.collaborateurs_communs(G, u, v)
    print("Collaborateurs communs:", result)

# Fonction pour trouver les collaborateurs proches d'un acteur dans une certaine distance
def trouver_collaborateurs_proches():
    u = input("Entrez le nom de l'acteur: ")
    k = int(input("Entrez la distance maximale: "))
    result = requetes.collaborateurs_proches(G, u, k)
    print("Collaborateurs proches:", result)

# Fonction pour vérifier si deux acteurs sont proches dans une certaine distance
def verifier_est_proche():
    try:
        u = input("Entrez le nom du premier acteur: ")
        v = input("Entrez le nom du deuxième acteur: ")
        k = int(input("Entrez la distance maximale (par défaut 1): ") or 1)
        result = requetes.est_proche(G, u, v, k)
        print("Est proche:", result)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Fonction pour trouver la distance entre deux acteurs
def trouver_distance():
    acteur1 = input("Entrez le nom du premier acteur: ")
    acteur2 = input("Entrez le nom du deuxième acteur: ")
    result = requetes.distance(G, acteur1, acteur2)
    print("Distance:", result)

# Fonction pour trouver la centralité d'un acteur
def trouver_centralite():
    u = input("Entrez le nom de l'acteur: ")
    result = requetes.centralite(G, u)
    print("Centralité:", result)

# Fonction pour trouver le centre d'Hollywood
def trouver_centre_hollywood():
    result = requetes.centre_hollywood(G)
    print("Centre d'Hollywood:", result)

# Fonction pour trouver l'éloignement maximal
def trouver_eloignement_max():
    result = requetes.eloignement_max(G)
    print("Éloignement maximal:", result)

# Fonction pour afficher l'application principale après avoir choisi le fichier
def afficher_application_principale():
    print("\nApplication de Collaboration des Acteurs")
    print("1. Trouver les collaborateurs communs")
    print("2. Trouver les collaborateurs proches")
    print("3. Vérifier si deux acteurs sont proches")
    print("4. Trouver la distance entre deux acteurs")
    print("5. Trouver la centralité d'un acteur")
    print("6. Trouver le centre d'Hollywood")
    print("7. Trouver l'éloignement maximal")
    print("8. Quitter")

    while True:
        choix = input("\nChoisissez une option (1-8) : ")
        if choix == "1":
            trouver_collaborateurs_communs()
        elif choix == "2":
            trouver_collaborateurs_proches()
        elif choix == "3":
            verifier_est_proche()
        elif choix == "4":
            trouver_distance()
        elif choix == "5":
            trouver_centralite()
        elif choix == "6":
            trouver_centre_hollywood()
        elif choix == "7":
            trouver_eloignement_max()
        elif choix == "8":
            print("Quitter l'application.")
            break
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 8.")

# Fonction principale pour afficher la page d'accueil
def main():
    print("Page d'accueil")
    choisir_fichier()

if __name__ == "__main__":
    main()