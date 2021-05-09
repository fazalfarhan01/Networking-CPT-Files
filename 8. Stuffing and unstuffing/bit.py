from stuffing.BitStuffing import BitStuffing
from stuffing.cls import cls

if __name__ == "__main__":
    stuff = BitStuffing([0,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0])
    stuff.stuff() # START STUFFING
    cls() # CLEAR SCREEN

    # PRINT SEQUENCES TO SCREEN
    print("Main Sequence:    {}".format(stuff.sequence))
    print("Stuffed Sequence: {}\n\n".format(stuff.getStuffedColored()))