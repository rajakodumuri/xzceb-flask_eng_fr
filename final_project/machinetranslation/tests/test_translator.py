"""
This module will:
    - Test english_to_french for null, and some inputs
    - Test french_to_english for null, and some inputs
"""

import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """
    Here lie tests for translator
    """
    def test_english_to_french(self):
        """
        Test english_to_french for null, and some inputs
        """
        # Testing for `null` input.
        self.assertIsNotNone(english_to_french('None'))
        # Testing translation does return translated words.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Testing translation does not return the same word.
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        # Testing translation does not return numbers.
        self.assertNotEqual(english_to_french(0), 0)

    def test_french_to_english(self):
        """
        Test french_to_english for null, and some inputs
        """
        # Testing for `null` input.
        self.assertIsNotNone(french_to_english('None'))
        # Testing translation does return translated words.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # Testing translation does not return the same word.
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        # Testing translation does not return numbers.
        self.assertNotEqual(french_to_english(0), 0)

if __name__ == '__main__':
    unittest.main()
