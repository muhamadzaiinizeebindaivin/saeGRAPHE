# test_graph_utils.py

import unittest
import networkx as nx
from requetes import (
    collaborateurs_communs, collaborateurs_proches, est_proche,
    distance_naive, distance, centralite, centre_hollywood, eloignement_max
)

class TestGraphUtils(unittest.TestCase):
    
    # Initialisation du graphe pour nos tests
    def setUp(self):
        # Création d'un nouveau graphe 
        self.G = nx.Graph()
        # Ajoute des arêtes au graphe, représentant des collaborations entre acteurs
        self.G.add_edges_from([
            ("Acteur A", "Acteur B"),
            ("Acteur A", "Acteur C"),
            ("Acteur B", "Acteur C"),
            ("Acteur C", "Acteur D"),
            ("Acteur D", "Acteur E")
        ])

    # Test pour la fonction collaborateurs_communs
    def test_collaborateurs_communs(self):
        result = collaborateurs_communs(self.G, "Acteur A", "Acteur B")
        self.assertEqual(result, {"Acteur C"})

    # Test pour la fonction collaborateurs_proches
    def test_collaborateurs_proches(self):
        result = collaborateurs_proches(self.G, "Acteur A", 1)
        self.assertEqual(result, {"Acteur A", "Acteur B", "Acteur C"})

    # Test pour la fonction est_proche
    def test_est_proche(self):
        result = est_proche(self.G, "Acteur A", "Acteur D", k=2)
        self.assertTrue(result)

    # Test pour la fonction distance_naive
    def test_distance_naive(self):
        result = distance_naive(self.G, "Acteur A", "Acteur E")
        self.assertEqual(result, 3)

    # Test pour la fonction distance
    def test_distance(self):
        result = distance(self.G, "Acteur A", "Acteur E")
        self.assertEqual(result, 3)

    # Test pour la fonction centralite
    def test_centralite(self):
        result = centralite(self.G, "Acteur A")
        self.assertEqual(result, 3)

    # Test pour la fonction centre_hollywood
    def test_centre_hollywood(self):
        result = centre_hollywood(self.G)
        self.assertEqual(result, "Acteur C")

    # Test pour la fonction eloignement_max
    def test_eloignement_max(self):
        result = eloignement_max(self.G)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
