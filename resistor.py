import unittest


def encode_resistor_colors(ohms_string):
    result = ""
    codes = {0: "black", 1: "brown", 2: "red", 3: "orange", 4: "yellow", 5: "green", 6: "blue", 7: "violet", 8: "gray",
             9: "white"}
    without_ohms = ohms_string.replace(" ohms", "")
    x = 0
    if without_ohms.endswith('k'):
        x = without_ohms.replace('k', '')
        if len(x) == 1:
            result += codes[int(x[0])] + " black"  " red"
        elif len(x) == 2:
            result += codes[int(x[0])] + " " + codes[int(x[1])] + " orange"
        else:
            if x[1] == '.':
                result += codes[int(x[0])] + " " + codes[int(x[2])] + " red"
            else:
                result += codes[int(x[0])] + " " + codes[int(x[1])] + " yellow"
    elif without_ohms.endswith('M'):
        x = without_ohms.replace('M', '')
        if len(x) == 1:
            result += codes[int(x[0])] + " black"  " green"
        elif len(x) == 2:
            result += codes[int(x[0])] + " " + codes[int(x[1])] + " blue"
        else:
            if x[1] == '.':
                result += codes[int(x[0])] + " " + codes[int(x[2])] + " green"
            else:
                result += codes[int(x[0])] + " " + codes[int(x[1])] + " violet"
    else:
        x = without_ohms
        result += codes[int(x[0])] + " " + codes[int(x[1])]
        if len(x) == 3:
            result += " brown"
        else:
            result += " black"

    result += " gold"
    return result
    # 0: black, 1: brown, 2: red, 3: orange, 4: yellow, 5: green, 6: blue, 7: violet, 8: gray, 9: white


class Tests(unittest.TestCase):
    def test_resistors_test(self):
        self.assertEqual(encode_resistor_colors("10 ohms"), "brown black black gold")

    def test_resistors_test1(self):
        self.assertEqual(encode_resistor_colors("47 ohms"), "yellow violet black gold")

    def test_resistors_test2(self):
        self.assertEqual(encode_resistor_colors("100 ohms"), "brown black brown gold")

    def test_resistors_test3(self):
        self.assertEqual(encode_resistor_colors("220 ohms"), "red red brown gold")

    def test_resistors_test4(self):
        self.assertEqual(encode_resistor_colors("330 ohms"), "orange orange brown gold")

    def test_resistors_test5(self):
        self.assertEqual(encode_resistor_colors("470 ohms"), "yellow violet brown gold")

    def test_resistors_test6(self):
        self.assertEqual(encode_resistor_colors("680 ohms"), "blue gray brown gold")

    def test_resistors_test7(self):
        self.assertEqual(encode_resistor_colors("1k ohms"), "brown black red gold")

    def test_resistors_test8(self):
        self.assertEqual(encode_resistor_colors("4.7k ohms"), "yellow violet red gold")

    def test_resistors_test9(self):
        self.assertEqual(encode_resistor_colors("10k ohms"), "brown black orange gold")

    def test_resistors_test10(self):
        self.assertEqual(encode_resistor_colors("22k ohms"), "red red orange gold")

    def test_resistors_test11(self):
        self.assertEqual(encode_resistor_colors("47k ohms"), "yellow violet orange gold")

    def test_resistors_test12(self):
        self.assertEqual(encode_resistor_colors("100k ohms"), "brown black yellow gold")

    def test_resistors_test13(self):
        self.assertEqual(encode_resistor_colors("330k ohms"), "orange orange yellow gold")

    def test_resistors_test14(self):
        self.assertEqual(encode_resistor_colors("1M ohms"), "brown black green gold")

    def test_resistors_test15(self):
        self.assertEqual(encode_resistor_colors("2M ohms"), "red black green gold")

    def test_resistors_test16(self):
        self.assertEqual(encode_resistor_colors("470M ohms"), "yellow violet violet gold")


if __name__ == '__main__':
    unittest.assertEqual(encode_resistor_colors("10 ohms"), "brown black black gold")
    # encode_resistor_colors("10 ohms")
