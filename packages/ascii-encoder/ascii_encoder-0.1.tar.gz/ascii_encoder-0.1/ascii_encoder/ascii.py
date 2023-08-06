class ascii:
    def __init__(self, letter):
        self.letter = letter

    def lenght(self):
        return int("255")

    def decode_ASCII(self):
        for i in range(255):
            if chr(i) == self.letter:
                return i
            else:
                pass

                
      
