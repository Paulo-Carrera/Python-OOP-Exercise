import random
class WordFinder:
    """
    Takes a given path and reads from a file line by line (single word lines)
    """
    def __init__(self , path):
        self.path = path
        self.words = self.read_words()
        print(f"{len(self.words)} words read.")

    def read_words(self):
        """
        Reads from a list of words that are gathered from the given file . 
        """
        words = []
        try:
            with open(self.path, 'r') as file:
                for line in file:
                    words.append(line.strip())
        
        except FileNotFoundError:
            print(f"The file at {self.path} was not found.")
        except IOError:
            print(f"An error occured while reading the file at {self.path}.")
        return words
    
    def random(self):
        """
        Returns one random word from the file .
        """
        return random.choice(self.words)
    






class SpecialWordFinder(WordFinder):
    """
    Takes a given path and reads from a file line by line (single word lines)
    """
    def read_words(self):
        """
        Returns the list of words, excluding empty lines and lines that being with # .
        """
        with open(self.path, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.strip().startswith('#')]
                         
