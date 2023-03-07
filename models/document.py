from collections import Counter

class Document:
    def __init__(self, value: str, lower: bool = False):
        self.value = value if not lower else value.lower()
        self.counter = None
    
    def _build_string(self, characters: Counter) -> (str, Counter):
        _value = ""
        subtracted = Counter(characters.items())
        for ch in self.value:
            ch_avaiable = characters.get(ch, 0)
            if ch_avaiable > 0:
                characters.subtract(ch)
            else:
                _value += ch
        return _value, subtracted

    def is_writable(self, document: 'Document'):
        counter = self.get_counter()
        doc_counter = document.get_counter()
        for ch, freq in counter.items():
            freq_art = doc_counter.get(ch, 0)
            if (not freq_art or freq > freq_art) and ch != " ":
                return False
        return True

    def get_counter(self):
        if not self.counter:
            self.counter = Counter(self.value)
        return self.counter
    
    def remove_characters(self, characters: Counter, update_value: bool = False) -> (str, Counter):
        new_value, subtracted = self._build_string(characters)

        if update_value:
            self.value = new_value
        
        return new_value, subtracted


    def rewrite_with_characters(self, characters: Counter) -> str:
        rewrited, _ = self._build_string(characters)
        return rewrited