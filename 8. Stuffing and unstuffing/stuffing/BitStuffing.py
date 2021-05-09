from typing import Sequence
from colorama import Fore
from .cls import cls

class BitStuffing(object):
    def __init__(self, sequence:list=None):
        if sequence == None:
            sequence = input("Enter the sequence (No Spaces): ")
            sequence = list(map(int, list(sequence)))
        self.sequence = sequence
        self.bitFlag = "{}0, 1, 1, 1, 1, 1, 1, 0{}".format(Fore.LIGHTRED_EX, Fore.RESET)
        self.count = 0
        self.stuffed = []
        self.stuffedColored = ""
    
    def stuff(self):
        for bit in self.sequence:
            if self.count == 5:
                self.stuffed.append(0)
                self.addColoredBit(0,True)
                self.count = 0

            self.stuffed.append(bit)
            self.addColoredBit(bit)

            if bit == 1:
                self.count += 1
            else:
                self.count = 0

    def addColoredBit(self,bit:int, added:bool=False):
        if len(self.stuffedColored) == 0:
            self.stuffedColored = "["
        else:
            self.stuffedColored =  self.stuffedColored.replace("]",",")
        if added:
            self.stuffedColored += "{}{}{} ]".format(Fore.LIGHTGREEN_EX, bit, Fore.RESET)
        else:
            self.stuffedColored += "{} ]".format(bit)
    
    def getStuffedColored(self) -> str:
        return "[{}, {}, {}]".format(self.bitFlag, self.stuffedColored[1:-1], self.bitFlag)
        


if __name__ == "__main__":
    stuff = BitStuffing([0,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0])
    stuff.stuff()
    cls()
    print("Main Sequence:    {}".format(stuff.sequence))
    print("Stuffed Sequence: {}".format(stuff.getStuffedColored()))