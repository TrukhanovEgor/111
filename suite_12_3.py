import unittest
import test_12_3

BigTest = unittest.TestSuite()
BigTest.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
BigTest.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

runner= unittest.TextTestRunner(verbosity=2)
runner.run(BigTest)