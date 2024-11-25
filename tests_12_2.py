import unittest
import runner_2
from pprint import pprint

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner_2.Runner('Усейн', 10)
        self.runner2 = runner_2.Runner('Андрей', 9)
        self.runner3 = runner_2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    def test_turn1(self):
        self.tur_1 = runner_2.Tournament(90, self.runner1, self.runner3)
        self.all_results = self.tur_1.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    def test_turn2(self):
        self.tur_2 = runner_2.Tournament(90, self.runner2, self.runner3)
        self.all_results = self.tur_2.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    def test_turn3(self):
        self.tur_3 = runner_2.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = self.tur_3.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[3] = self.all_results



if __name__ == '__main__':
    unittest.main()

    def tearDownClass(cls):
        pprint(cls.all_results)