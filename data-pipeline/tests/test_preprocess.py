import unittest
import pandas as pd
from src.preprocess import load_and_clean_data

class TestPreprocess(unittest.TestCase):

    def setUp(self):
        self.test_data = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Alice', None, 'Charlie', 'Bob'],
            'Age': [25, 30, 25, None, 35, 30]
        })
        self.test_data.to_csv('data/raw/customers-1000.csv', index=False)

    def test_load_and_clean_data(self):
        cleaned_data = load_and_clean_data('data/raw/customers-1000.csv')
        
        # Check for duplicates
        self.assertEqual(cleaned_data['target'].nunique(), 3)
        
        # Check for NaN values
        self.assertFalse(cleaned_data.isnull().values.any())
        
        # Check if the first column is renamed to 'target'
        self.assertIn('target', cleaned_data.columns)

    def tearDown(self):
        import os
        os.remove('data/raw/customers-1000.csv')

if __name__ == '__main__':
    unittest.main()
