from concurrent.futures import process
from html.parser import HTMLParser
import process_post_text

import unittest

from bs4 import BeautifulSoup
import spacy

class Test_ProcessPostText(unittest.TestCase):   

    """ Used to test the methods in the process_post_text file.	"""

    def test_read_word_list(self):
    
        """ Test the read_word_list method by checking if the specified files for this mehod exist.
        :raises: FIleNotFoundError
    
        :rtype:
        """    
        #Arrange
        try:
            POSITIVE_WORD_FILE = "../data/positive-words.txt"
            NEGATIVE_WORD_FILE = "../data/negative-words.txt"
    
        except FileNotFoundError:
            print('The file is not present.')

        #Act and Asert
        assert(process_post_text.read_word_list(POSITIVE_WORD_FILE, True))
        assert(process_post_text.read_word_list(NEGATIVE_WORD_FILE, True))

    def test_remove_code_snippet(self):
    
        """ Test remove_code_snipped method
        :raises:
    
        :rtype:
        """    
        #Arrange
        try:
            body = "Testing stirng Hello Wo rld"
            soup = BeautifulSoup(body, 'html.parser')

        except:
            print("No body was found.")

        #Act and Asert
        assert(process_post_text.remove_code_snippet(body.soup, True))

    def test_process_raw_text():
        #Arrange
        try:
            snippet = "asdf"

        except:
            print("Cannot find code snippet.")

        #Act and Asert
        assert(process_post_text.process_raw_text(snippet.decompose, True))

    def test_breakdown_sentences():
        #Arrange
        try:
            sentence = "This is a sentence."

        except:
            print("Cannot find code sentence.")

        #Act and Asert
        assert(process_post_text.breakdown_sentences(sentence.text.strip, True))

    def test_extract_sentence_with_keywords():
        #Arrange
        try:
            sentence = "This is a sentence."
            keyword = "Keyword."

        except:
            print("Cannot find code sentence or keyword.")

        #Act and Asert
        assert(process_post_text.sentence.append(keyword), True)

    def test_extract_sentence_with_adjectives():
        #Arrange
        try:
            sentence = "This is a sentence."
            adjective = "adjective"

        except:
            print("Cannot find code sentence or adjective.")

        #Act and Asert
        assert(process_post_text.breakdown_sentences(sentence.append(adjective), True))

    def test_passed():
        pass