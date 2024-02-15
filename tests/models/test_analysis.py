import unittest

import pandas as pd

from src.models.analysis import compute_absolute_error

class TestComputeAbsoluteError(unittest.TestCase):

    def test_compute_absolute_error(self):
        data = pd.DataFrame({
            'valeur_mc': [100, 150, 200],
            'predicted': [110, 140, 210]
        })
        predicted_column = 'predicted'

        expected_data = pd.DataFrame({
            'valeur_mc': [100, 150, 200],
            'predicted': [110, 140, 210],
            'predicted_error': [0.1, 0.066666667, 0.05]
        })

        result_data = compute_absolute_error(data, predicted_column)

        self.assertTrue(result_data.round(3).equals(expected_data.round(3)))
