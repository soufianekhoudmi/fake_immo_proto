import unittest
import pandas as pd

from src.etl.filters import filter_abnormale, filter_nature, filter_type

class TestFilterFunctions(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'nature_mutation': ['Vente', 'Vente', 'Donation'],
            'type_local': ['Appartement', 'Maison', 'Appartement'],
            'valeur_mc': [600, 800, 9000],
            'surface_reelle_bati': [20, 150, 10],
            'nombre_pieces_principales': [2, 5, 0],
            'id_mutation': ['1', '1', '2']
        })

    def test_filter_nature(self):
        
        computed = filter_nature(self.data)
        expected = pd.DataFrame({
            'nature_mutation': ['Vente', 'Vente'],
            'type_local': ['Appartement', 'Maison'],
            'valeur_mc': [600, 800],
            'surface_reelle_bati': [20, 150],
            'nombre_pieces_principales': [2, 5],
            'id_mutation': ['1', '1']
        })

        expected = expected.reset_index(drop=True)
        computed = computed.reset_index(drop=True)
        self.assertTrue(expected.equals(computed))

    def test_filter_type(self):
        computed = filter_type(self.data)

        expected = pd.DataFrame({
            'nature_mutation': ['Donation'],
            'type_local': ['Appartement'],
            'valeur_mc': [9000],
            'surface_reelle_bati': [10],
            'nombre_pieces_principales': [0],
            'id_mutation': ['2']
        })


        expected = expected.reset_index(drop=True)
        computed = computed.reset_index(drop=True)

        self.assertTrue(expected.equals(computed))


    def test_filter_abnormale(self):
        computed = filter_abnormale(self.data)

        expected = pd.DataFrame({
            'nature_mutation': ['Vente', 'Vente'],
            'type_local': ['Appartement', 'Maison'],
            'valeur_mc': [600, 800],
            'surface_reelle_bati': [20, 150],
            'nombre_pieces_principales': [2, 5],
            'id_mutation': ['1', '1']
        })
        
        
        expected = expected.reset_index(drop=True)
        computed = computed.reset_index(drop=True)

        self.assertTrue(expected.equals(computed))
