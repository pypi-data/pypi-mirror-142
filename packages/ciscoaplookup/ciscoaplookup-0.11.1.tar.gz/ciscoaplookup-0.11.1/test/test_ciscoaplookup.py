from unittest import TestCase, main
from ciscoaplookup import *


class TestCiscoAPLookup(TestCase):
    def test_positive_models(self):
        cases = [
            ('AIR-CAP1532I', 'Belgium', '-E-K9'),
            ('AIR-AP1562I', 'Gibraltar', '-E-K9'),
            ('AIR-CAP1532I', 'Japan', '-Q-K9'),
            ('AIR-AP1572IC', 'Mexico', '-A-K9'),
            ('AIR-AP1572IC', 'New Zealand', '-Z-K9'),
            ('AIR-CAP1532I', 'Taiwan', '-T-K9'),
            ('AIR-AP2802I', 'Denmark', '-E-K9'),
            ('AIR-AP2802I', 'Nicaragua', '-W-K9'),  # used when no matches are made.
            ('C9136I', 'Denmark', '-E'),
            ('C9120AXI', 'Denmark', '-E')
        ]
        for c in cases:
            res = get_models_for(c[0], c[1])
            exp = [c[0]+c[2]]
            self.assertEqual(exp, res, '{} doesn\'t match {} for {} / {}'.format(res, exp, c[0], c[1]))

    def test_fail_models(self):
        self.assertRaises(ValueError, get_models_for, 'gnyf', 'Denmark')  # invalid model
        self.assertRaises(ValueError, get_models_for, 'AIR-CAP1532I', 'Neverland')  # invalid country
        self.assertRaises(ValueError, get_models_for, 'AIR-CAP1552H', 'Vietnam')  # not possible

    def test_hest(self):
        self.assertTrue(len(get_models()) > 20)

    def test_countries(self):
        import pycountry
        lawless_countries = []

        for c in pycountry.countries:
            try:
                klaf = get_models_for('AIR-AP2802I', c.name)
            except ValueError as ve:
                print(ve)


if __name__ == '__main__':
    main()
