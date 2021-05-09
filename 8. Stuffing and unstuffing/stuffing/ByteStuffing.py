# from .cls import cls

def _breakAtEscape(sequence):
    try:
        indexOfEscape = sequence.index("E")
        return sequence[:indexOfEscape] + [sequence[indexOfEscape+1]] + _breakAtEscape(sequence[indexOfEscape+2:])
    except:
        return sequence

class ByteStuffing(object):
    def __init__(self, sequence:list = None) -> None:
        if sequence == None:
            sequence = list(input("Enter the sequence (No Spaces): ").upper())
        self.sequence = self.cleanSequence(sequence)
        self.escape = "E"
        self.flag = "F"
        self.stuffed = []
        self.unstuffed = []
    
    def startStuffing(self):
        for character in self.sequence:
            if self.flag in character or self.escape in character:
                self.stuffed.append(self.escape)
            self.stuffed.append(character)

    def cleanSequence(self, sequence):
        while True:
            try:
                del sequence[sequence.index(" ")]
            except:
                return sequence

    def startUnStuffing(self):
        self.unstuffed = _breakAtEscape(self.stuffed)





if __name__ == "__main__":
    stuff = ByteStuffing(list("abcdefghijklmnopqrstuvwxyz".upper()))
    stuff.startStuffing()
    print(stuff.stuffed)
    stuff.startUnStuffing()
    print(stuff.unstuffed)