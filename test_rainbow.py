import unittest
import raindrop



class TestRainbow(unittest.TestCase):

    # test to see if 12 returns it's correct value, "Pling"
    def test_pling(self):
        result = raindrop.raindrop(12)
        self.assertEqual(result, "Pling")


# allows the tests to be run in terminal without having to call upon the unittest module
if __name__ == '__main__':
    unittest.main()