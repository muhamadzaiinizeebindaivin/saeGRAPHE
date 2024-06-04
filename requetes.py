import json
import networkx as nx
import matplotlib.pyplot as plt


def txt_to_json(input_file, output_file):
    """
    Lit un fichier texte contenant des objets JSON sur chaque ligne et les écrit dans un nouveau fichier JSON.
    
    Args:
        input_file (str): Nom du fichier texte d'entrée contenant les chaînes JSON.
        output_file (str): Nom du fichier de sortie pour écrire le tableau JSON.
    """
    try:
        # Initialiser une liste pour stocker les objets JSON
        json_list = []
        
        # Ouvrir le fichier texte en mode lecture
        with open(input_file, 'r') as file:
            for line in file:
                # Convertir la chaîne JSON en un dictionnaire Python et l'ajouter à la liste
                json_obj = json.loads(line)
                json_list.append(json_obj)
        
        # Écrire la liste des objets JSON dans le fichier de sortie avec une indentation pour la lisibilité
        with open(output_file, 'w') as file1:
            json.dump(json_list, file1, indent=4)
        
        # Afficher un message de succès
        print("Les données ont été écrites avec succès dans " + output_file)
    
    except Exception as e:
        # Afficher un message d'erreur en cas d'exception
        print("Il y a une erreur !", str(e))



def json_vers_nx(chemin):
    """
    Convertit un fichier JSON contenant des informations de distribution de films en un graphe NetworkX.
    
    Chaque acteur est représenté comme un nœud, et une arête est ajoutée entre deux acteurs 
    s'ils ont joué dans le même film.
    
    Args:
    chemin (str): Le chemin du fichier JSON à lire.
    
    Returns:
    networkx.Graph: Un graphe où les nœuds représentent des acteurs et les arêtes représentent
                    des collaborations dans des films.
    """
    # Ouvrir le fichier JSON en mode lecture
    with open(chemin, 'r') as f:
        # Charger le contenu du fichier JSON dans une variable 'donnees'
        donnees = json.load(f)
    
    # Initialiser un graphe non orienté avec le nom G
    G = nx.Graph()

    # Pour chaque film dans les données JSON
    for film in donnees:
        # Pour chaque acteur dans la distribution du film
        for actor in film['cast']:
            # Extraire le nom de l'acteur en supprimant les délimiteurs [[ et ]] et en prenant la partie après le dernier '|'
            actor_name = actor.replace('[[', '').replace(']]', '').split('|')[-1]
            # Ajouter l'acteur comme un nœud dans le graphe
            G.add_node(actor_name)
            # Ajouter des arêtes entre cet acteur et tous les autres acteurs du film
            for actor2 in film['cast']:
                # Extraire le nom du deuxième acteur de la même manière
                actor_name2 = actor2.replace('[[', '').replace(']]', '').split('|')[-1]
                # Ajouter le deuxième acteur comme un nœud dans le graphe (si pas déjà présent)
                G.add_node(actor_name2)
                # Si les deux acteurs ne sont pas le même, ajouter une arête entre eux
                if actor_name != actor_name2:
                    G.add_edge(actor_name, actor_name2)
    # Retourner le graphe construit
    return G


def collaborateurs_communs(G, u, v):
    """
    Trouve les collaborateurs communs entre deux acteurs/actrices dans un graphe.
    
    Args:
    G (networkx.Graph): Le graphe représentant les collaborations entre acteurs.
    u (str): Le nom du premier acteur/actrice.
    v (str): Le nom du deuxième acteur/actrice.
    
    Returns:
    set: Un ensemble de collaborateurs communs.
    """
    # Vérifier si les acteurs sont dans le graphe
    if u not in G:
        print("Le nœud " + u + " n'est pas présent dans le graphe.")
        return None
        
    if v not in G:
        print("Le nœud " + v + " n'est pas présent dans le graphe.")
        return None
    
    # Obtenir les voisins de u et v
    voisins_u = set(G.neighbors(u))
    voisins_v = set(G.neighbors(v))
    
    # Trouver les collaborateurs communs
    collaborateurs_communs = voisins_u.intersection(voisins_v)
    
    return collaborateurs_communs


 
def collaborateurs_proches(G, u, k):
    """
    Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G.
    La fonction renvoie None si u est absent du graphe.
    
    Paramètres:
        G: le graphe (représenté sous forme de graphe NetworkX)
        u: le sommet de départ (l'acteur de départ)
        k: la distance maximale depuis u (le nombre de niveaux de séparation)
    """
    
    # Vérifie si l'acteur u est présent dans le graphe
    if u not in G.nodes:
        print(u, "est un illustre inconnu")
        return None
    
    # Ensemble des collaborateurs, initialement avec l'acteur de départ u
    collaborateurs = set()
    collaborateurs.add(u)
    
    # Boucle pour chaque niveau de distance jusqu'à k
    for i in range(k):
        collaborateurs_directs = set()
        
        # Parcourt tous les collaborateurs trouvés jusqu'à présent
        for c in collaborateurs:
            
            # Parcourt tous les voisins de chaque collaborateur
            for voisin in G.adj[c]:
                
                # Ajoute le voisin s'il n'est pas déjà dans l'ensemble des collaborateurs
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        
        # Met à jour l'ensemble des collaborateurs avec les nouveaux collaborateurs directs trouvés
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    
    return collaborateurs


def est_proche(G, u, v, k=1):
    """
    Fonction vérifiant si deux acteurs, u et v, sont à distance au plus k dans le graphe G.
    
    Paramètres:
        G: le graphe (représenté sous forme de graphe NetworkX)
        u: le premier acteur
        v: le second acteur
        k: la distance maximale (par défaut, 1)
        
    Retourne:
        True si v est à distance au plus k de u, False sinon.
    """
    
    # Obtenir les collaborateurs de u à distance 1
    collaborateur = collaborateurs_proches(G, u, 1)
    
    # Vérifier si v est un noeud du graphe et s'il est dans les collaborateurs de u
    if v in G.nodes() and v in collaborateur:
        return True
    else:
        return False


def distance_naive(G, u, v):
    """
    Fonction calculant la distance la plus courte entre deux acteurs u et v dans le graphe G.
    La fonction renvoie None si l'un des acteurs n'est pas dans le graphe ou s'il n'y a pas de chemin entre eux.
    
    Paramètres:
        G: le graphe (représenté sous forme de graphe NetworkX)
        u: le premier acteur
        v: le second acteur
        
    Retourne:
        La distance la plus courte entre u et v, ou None s'il n'y a pas de chemin ou si l'un des acteurs est absent.
    """
    
    # Vérifier si l'un des nœuds n'est pas dans le graphe
    if u not in G.nodes() or v not in G.nodes():
        return None

    # Vérifier s'il n'y a pas de chemin entre u et v
    if not nx.has_path(G, u, v):
        print("Il n'y a pas de chemin entre " + u + " et " + v)
        return "hi"
    
    res = 0
    # Obtenir l'ensemble des voisins de u à distance res (initialement 0)
    ensemble_voisin_u = collaborateurs_proches(G, u, res)
    
    # Continuer à chercher jusqu'à ce que v soit trouvé dans les voisins de u
    while v not in ensemble_voisin_u:
        res += 1
        # Obtenir les voisins de u à la nouvelle distance res
        ensemble_voisin_u = collaborateurs_proches(G, u, res)

    return res


def distance(G, u, v):
    """
    Fonction calculant la distance la plus courte entre deux acteurs u et v dans le graphe G.
    La fonction renvoie None si l'un des acteurs n'est pas dans le graphe ou s'il n'y a pas de chemin entre eux.
    
    Paramètres:
        G: le graphe (représenté sous forme de graphe NetworkX)
        u: le premier acteur
        v: le second acteur
        
    Retourne:
        La distance la plus courte entre u et v, ou None s'il n'y a pas de chemin ou si l'un des acteurs est absent.
    """
    
    # Vérifier si l'un des nœuds n'est pas dans le graphe
    if u not in G.nodes or v not in G.nodes:
        print("L'acteur n'est pas trouvé")
        return None
    
    # Vérifier s'il n'y a pas de chemin entre u et v
    if not nx.has_path(G, u, v):
        print("Il n'y a pas de chemin entre " + u + " et " + v)
        return None
    
    distance = 0
    # Ensemble des acteurs trouvés, initialement avec l'acteur de départ u
    acteurs_trouves = {u}
    
    # Boucle jusqu'à ce que v soit trouvé parmi les acteurs
    while v not in acteurs_trouves:
        distance += 1
        nouveaux_acteurs = set()
        
        # Parcourt tous les acteurs trouvés jusqu'à présent
        for acteur in acteurs_trouves:
            voisins = G.adj[acteur]  # Obtenir les voisins de chaque acteur
            nouveaux_acteurs.update(voisins)  # Ajouter les voisins à l'ensemble des nouveaux acteurs
        
        # Met à jour l'ensemble des acteurs trouvés avec les nouveaux acteurs
        acteurs_trouves.update(nouveaux_acteurs)
    
    return distance


def centralite(G, u):
    try:
        if u not in G.nodes():
            raise ValueError(f"Le nœud {u} n'existe pas dans le graphe.")

        centralite_max = 0  # Initialiser la centralité maximale à 0

        for acteur in G.nodes():
            if u != acteur:
                try:
                    distance = nx.shortest_path_length(G, acteur, u)
                    if distance > centralite_max:
                        centralite_max = distance
                except nx.NetworkXNoPath:
                    print(f"Pas de chemin entre {acteur} et {u}.")
                except Exception as e:
                    print(f"Erreur lors du calcul de la distance entre {acteur} et {u} : {e}")

        return centralite_max

    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")
        return None


# Fonction pour trouver le nœud le plus central dans le graphe G
def centre_hollywood(G):

    centralite_min = None  # Initialiser la centralité minimale à None
    acteur_central = None  # Initialiser l'acteur central à None

    for acteur in G.nodes():  # Parcourir tous les nœuds du graphe

        centre = centralite(G, acteur)  # Calculer la centralité de l'acteur

        if centralite_min is None or centre > centralite_min:  # Mettre à jour la centralité minimale et l'acteur central
            centralite_min = centre
            acteur_central = acteur

    return acteur_central  # Retourner l'acteur le plus central


# Fonction pour trouver la distance maximale entre deux nœuds dans le graphe G
def eloignement_max(G):
    try:
        if len(G) == 0:
            raise ValueError("Le graphe est vide.")

        # Calculer toutes les distances les plus courtes entre les nœuds
        all_distances = dict(nx.all_pairs_shortest_path_length(G))

        # Initialiser la distance maximale à 0
        distance_max = 0

        # Parcourir toutes les distances calculées
        for distances in all_distances.values():
            max_distance_for_node = max(distances.values())
            if max_distance_for_node > distance_max:
                distance_max = max_distance_for_node

        return distance_max  # Retourner la distance maximale trouvée
    
    except ValueError as ve:
        print(f"Erreur de valeur : {ve}")
        return None
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")
        return None