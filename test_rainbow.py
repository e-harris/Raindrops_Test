import unittest
import raindrop



class TestRainbow(unittest.TestCase):

    # test to see if 12 returns it's correct value, "Pling"
    def test_pling(self):
        self.assertEqual(raindrop.raindrop(12), "Pling")
        self.assertEqual(raindrop.raindrop(-3), "Pling")


# allows the tests to be run in terminal without having to call upon the unittest module
if __name__ == '__main__':
    unittest.main()