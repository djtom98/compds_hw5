import unittest
import pytest
from pandas.testing import assert_frame_equal
#%%
from hw5.hw5 import car_at_light,safe_subtract,retrieve_age_eafp,retrieve_age_lbyl,read_data,count_simba,compute_distance,get_day_month_year,sum_general_int_list
#%%
import pandas as pd
from datetime import datetime
class tests(unittest.TestCase):

    # Q1 
    def test_car_at_light_red(self):
        assert car_at_light("red") == "stop"

    def test_car_at_light_green(self):
        assert car_at_light("green") == "go"

    def test_car_at_light_yellow(self):
        assert car_at_light("yellow") == "wait"

    def test_car_at_light_other(self):
        light = "purple"
        with pytest.raises(Exception, match = "Undefined instruction for color: " + str(light)):
            car_at_light(light)

    # Q2 
    def test_safe_subtract_valid(self):
        assert safe_subtract(6, 4) == 2

    def test_safe_subtract_invalid(self):
        with pytest.raises(TypeError):
            raise Exception('Invalid operation.')

    # Q3 
    def test_retrieve_age_eafp(self):
        res = retrieve_age_eafp({'name': 'John', 'last_name': 'Doe', 'birth': 1987})
        self.assertEqual(res, 35)
        with self.assertRaises(KeyError):
            retrieve_age_eafp({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})

    def test_retrieve_age_lbyl(self):
        res = retrieve_age_lbyl({'name': 'John', 'last_name': 'Doe', 'birth': 1987})
        self.assertEqual(res, 35)
        with self.assertRaises(KeyError):
            retrieve_age_lbyl({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})

    # Q4 
    def test_read_data(self):
        ans = pd.read_csv("sample_diabetes_mellitus_data.csv")
        res = read_data("sample_diabetes_mellitus_data.csv")
        assert_frame_equal(res, ans)
        with self.assertRaises(FileNotFoundError):
            raise Exception('File not found.')

    # Q6
    def test_count_simba(self):
        paragraph = ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
        assert count_simba(paragraph) == 3

    # Q7 
    def test_get_day_month_year(self):
        dates = ['12-10-1990', '30-11-2022', '15-12-1902']
        dates = [datetime.strptime(date, '%d-%m-%Y') for date in dates]
        date_list = [[12,10,1990], [30,11,2022], [15,12,1902]]
        ans = pd.DataFrame(date_list, columns = ['day', 'month', 'year'])
        res = get_day_month_year(dates)
        assert_frame_equal(res, ans)

    # Q8
    def test_compute_distance(self):
        coords1 = ((41.23, 23.5), (41.5, 23.4))
        coords2 = ((52.38, 20.1), (52.3, 17.8))
        dist = [31.13186522205169, 157.00582786889402]
        assert compute_distance([coords1, coords2]) == dist

    # Q9 
    def test_sum_general_int_list(self):
        assert sum_general_int_list([[2], 3, [[1,2],5]]) == 13


