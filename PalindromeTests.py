import unittest
from Palindrome import palindrome

class Tests(unittest.TestCase):
    def test_word_is_palindrome(self):
        self.assertEqual(palindrome("madam"), True, "The word 'madam' is a palindrome")
        self.assertTrue(palindrome("madam"), "The word 'madam' is a palindrome")

    def test_word_is_not_palindrome(self):
        self.assertEqual(palindrome("tomato"), False, "The word 'tomato' is not a palindrome")

    def test_phrase_is_palindrome(self):
        self.assertEqual(palindrome("nurses run"), True, "The phrase 'nurses run' is a palindrome")

    def test_capital_word(self):
        self.assertEqual(palindrome("Madam"), True, "The word 'Madam' is a palindrome")
        self.assertEqual(palindrome("TOMATO"), False, "The word 'TOMATO' is not a palindrome")
        self.assertEqual(palindrome("Nurses Run"), True, "The phrase 'Nurses Run' is a palindrome")
    
    def test_punctuation_marks(self):
        self.assertEqual(palindrome("nurses run."), True, "The phrase 'nurses run.' is a palindrome")
        self.assertEqual(palindrome("Madam#"), True, "The word 'Madam' is a palindrome")
        self.assertEqual(palindrome("T_O_M_A_T_O"), False, "The word 'TOMATO' is not a palindrome")
        self.assertEqual(palindrome("nurses!@#$:;>/,'run."), True, "The phrase is a palindrome disregarding non-alphanumeric characters")
    
    def test_input_is_number(self):
        self.assertEqual(palindrome("101"), True, "The number '101' is a palindrome")
        self.assertEqual(palindrome("1_0_1"), True, "The number '101' is a palindrome disregarding the non-number characters")
        self.assertEqual(palindrome("10"), False, "The number '10' is not a palindrome")

    def test_input_is_alphanumeric(self):
        self.assertEqual(palindrome("Madam101"), False, "The string 'Madam101' is not a palindrome")
        self.assertEqual(palindrome("101Madam101"), True, "The string '101Madam101' is a palindrome")

    def test_input_is_characters(self):
        self.assertEqual(palindrome("###"), "Please enter a word or phrase")
        
if __name__=="__main__":
    unittest.main()