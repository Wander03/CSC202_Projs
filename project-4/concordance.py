from typing import Any, List, Optional
from hash_quad import *
import string

class Concordance:

    def __init__(self) -> None:
        """ Starting size of hash table should be 191: self.concordance_table = HashTable(191) """
        self.stop_table: Optional[HashTable] = None          # hash table for stop words
        self.concordance_table: HashTable = HashTable(191)              # hash table for concordance

    def load_stop_table(self, filename: str) -> None:
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            with open(filename, 'r') as f:
                self.stop_table = HashTable(191)
                lines = f.read().splitlines()
                for word in lines:
                    self.stop_table.insert(word, None)
        except:
            raise FileNotFoundError

    def load_concordance_table(self, filename: str) -> None:
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)

        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError """
        try:
            with open(filename, 'r') as f:
                all_lines = f.read().splitlines()                                   # List of strings, where each string is a line
                self.process_words(all_lines)
                for i in range(len(all_lines)):                                     # Each line in file
                    for word in all_lines[i]:                                       # Each word in line
                        if word in self.concordance_table:                          # If word has appeared before
                            cur_vals = self.concordance_table[word]  
                            cur_vals.append(i + 1)        
                            self.concordance_table[word] = cur_vals
                        else:                                                       # If word is NEW
                            self.concordance_table[word] = [i + 1]
        except:
            raise FileNotFoundError

    def process_words(self, lines: List) -> None:
        """  Removes punctuation, numbers and filters out words that are in the stop words hash table. """
        final = ""                                                   
        for i in range(len(lines)):                                     # Each line in file
                                                    
            for char in lines[i]:                                       # Each character in word
                        
                if char not in string.punctuation and char.isalpha():   # Remove punctuation
                    final += char 
                elif char != "'":
                    final += " "

            lines[i] = final.lower()                                    # Make lowercase
            lines[i] = lines[i].split()                                 # Make the line a list of words

            j = 0
            while j != len(lines[i]):                                   # Each word in line
                if self.stop_table is not None:
                    if lines[i][j] in self.stop_table:                  # Remove word if in stop table
                        lines[i].pop(j)
                        j -= 1
                    j += 1

            if lines[i] != []:
                lines[i] = set(lines[i])                                # Turn list of words into a set to remove duplicates
            final = ""

    def write_concordance(self, filename: str) -> None:
        """ Write the concordance entries to the output file(filename)
        See sample output files for format. """
        all_words = self.concordance_table.get_all_keys()
        all_words.sort()
        result = ""
        for word in all_words:
            result += word + ":"
            for i in range(len(self.concordance_table[word])):
                result += " %d" % (self.concordance_table[word][i])
            result += "\n"

        with open(filename, 'w') as f:
            f.write(result.strip())
