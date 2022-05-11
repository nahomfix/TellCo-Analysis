import unittest

import pandas as pd


class TestDataframe(unittest.TestCase):    
    def setUp(self) -> pd.DataFrame:
        try:
            data = pd.read_csv('../data/clean_data.csv', parse_dates=["Start", "End"])
            self.dataframe = data
        except IOError:
            print('could not open csv file')
        

    def test_dataframe_shape(self):
        self.assertEqual(self.dataframe.shape, (148506, 55))





if __name__ == '__main__':
	unittest.main()
