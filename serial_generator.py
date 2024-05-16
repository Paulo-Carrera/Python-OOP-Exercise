import itertools

class SerialGenerator:
    def __init__(self, start):
        self.start = start
        self._counter = itertools.count(start)
        self._current = start - 1

    def generate(self): 
        self._current = next(self._counter)
        return self._current
        
    def reset(self):
        self._counter = itertools.count(self.start)
        self._current = self.start - 1 

    def __str__(self):
        return f"Current number: {self._current}"
        
