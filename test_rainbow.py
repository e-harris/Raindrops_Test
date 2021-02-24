import unittest
import raindrop



class TestRainbow(unittest.TestCase):

    # test to see if Pling returns it's correct value, "Pling" when provided with a number divisible by 3
    def test_pling(self):
        self.assertEqual(raindrop.raindrop(12), "Pling")
        self.assertEqual(raindrop.raindrop(-3), "Pling")

    # test to see if Plang returns it's correct value, "Plang" when provided with a number divisible by 5
    def test_plang(self):
        self.assertEqual(raindrop.raindrop(25), "Plang")
        self.assertEqual(raindrop.raindrop(-50), "Plang")

# allows the tests to be run in terminal without having to call upon the unittest module
if __name__ == '__main__':
    unittest.main()