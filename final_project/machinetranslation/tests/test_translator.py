import unittest
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

sys.path.append(parent_dir)

from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
  def test1(self):
    self.assertEqual(english_to_french(), "")                    # test when no input given, the output is empty string.
    self.assertEqual(english_to_french("Hello"), "Bonjour")      # test when "Hello" is given as input, the output is "Bonjour".
    self.assertNotEqual(english_to_french("Hi"), "Bonjour")      # test when "Hello" is given as input, the output is not "Bonjour".


class TestFrenchToEnglish(unittest.TestCase):
  def test1(self):
    self.assertEqual(french_to_english(), "")                    # test when no input given, the output is empty string.
    self.assertEqual(french_to_english("Bonjour"), "Hello")      # test when "Bonjour" is given as input, the output is "Hello".
    self.assertNotEqual(french_to_english("Bonjour"), "Hi")      # test when "Bonjour" is given as input, the output is not "Hello".


unittest.main()

