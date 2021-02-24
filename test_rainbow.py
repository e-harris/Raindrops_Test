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

    # test to see if Plong returns it's correct value, "Plong" when provided with a number divisible by 7
    def test_plong(self):
        self.assertEqual(raindrop.raindrop(49), "Plong")
        self.assertEqual(raindrop.raindrop(-7), "Plong")

    # test to see if PlingPlang returns it's correct value, "PlingPlang" when provided with a number divisible by 3 and 5
    def test_plingplang(self):
        self.assertEqual(raindrop.raindrop(90), "PlingPlang")
        self.assertEqual(raindrop.raindrop(-15), "PlingPlang")

    # test to see if PlingPlong returns it's correct value, "PlingPlong" when provided with a number divisible by 3 and 7
    def test_plingplong(self):
        self.assertEqual(raindrop.raindrop(42), "PlingPlong")
        self.assertEqual(raindrop.raindrop(-21), "PlingPlong")

    # test to see if PlangPlong returns it's correct value, "PlangPlong" when provided with a number divisible by 5 and 7
    def test_plangplong(self):
        self.assertEqual(raindrop.raindrop(70), "PlangPlong")
        self.assertEqual(raindrop.raindrop(-35), "PlangPlong")

    # test to see if PlingPlangPlong returns it's correct value, "PlingPlangPlong" when provided with a number divisible by 3, 5 and 7
    def test_plingplangplong(self):
        self.assertEqual(raindrop.raindrop(210), "PlingPlangPlong")
        self.assertEqual(raindrop.raindrop(-105), "PlingPlangPlong")
        self.assertEqual(raindrop.raindrop(0), "PlingPlangPlong")

    # test to see if the number provided returns it's value to see if it's not divisible by 3, 5 and 7
    def test_notdivisible(self):
        self.assertEqual(raindrop.raindrop(424), 424)
        self.assertEqual(raindrop.raindrop(-11), -11)

# allows the tests to be run in terminal without having to call upon the unittest module
if __name__ == '__main__':
    unittest.main()