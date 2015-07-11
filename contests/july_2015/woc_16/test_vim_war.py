import unittest
from vim_war import *

class RegexTest(unittest.TestCase):
    def setUp(self):
        self.num_soldiers = 4
        self.num_possible_skills = 2
        self.soldiers_array = [[0,0], [1, 0], [0, 1], [1, 1]]
        self.skillset_requirement = [1, 1]

    def test_is_valid_skillset(self):
        total_skillset = [1, 1]
        is_valid = is_valid_skillset(self.skillset_requirement, total_skillset, self.num_possible_skills)
        self.assertEqual(is_valid, True)

    def test_is_valid_army(self):
        army = set([3])
        is_valid = is_valid_army(army, self.soldiers_array, self.skillset_requirement, self.num_possible_skills)
        self.assertEqual(is_valid, True)

if __name__ == "__main__":
    unittest.main()
