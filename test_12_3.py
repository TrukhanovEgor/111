import unittest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе пропушены')
    def test_walk(self):
        n1 = runner.Runner('Mike')
        for i in range(10):
            n1.walk()
        self.assertEqual(n1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе пропушены')
    def test_run(self):
        n1 = runner.Runner('Mike')
        for i in range(10):
            n1.run()
        self.assertEqual(n1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе пропушены')
    def test_challenge(self):
        n1 = runner.Runner('Mike')
        n2 = runner.Runner('Den')
        for i in range(10):
            n1.walk()
            n2.run()
        self.assertNotEqual(n1.distance, n2.distance)


# Module_12_2 Upgrade
class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе пропушены')
    def test_turn1(self):
        self.tur_1 = runner_2.Tournament(90, self.runner1, self.runner3)
        self.all_results = self.tur_1.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе пропушены')
    def test_turn2(self):
        self.tur_2 = runner_2.Tournament(90, self.runner2, self.runner3)
        self.all_results = self.tur_2.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе пропушены')
    def test_turn3(self):
        self.tur_3 = runner_2.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = self.tur_3.start()
        self.assertTrue(self.all_results[list(self.all_results.keys())[-1]] == 'Ник')
        TournamentTest.all_results[3] = self.all_results