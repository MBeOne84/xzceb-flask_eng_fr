import unittest
import translator

from translator import english_to_french, french_to_english

class Test1(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('0'), '0') 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class Test2(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('0'), '0') 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 

unittest.main()
