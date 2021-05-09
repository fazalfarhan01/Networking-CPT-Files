from stuffing.ByteStuffing import ByteStuffing


if __name__ == "__main__":
    # stuff = ByteStuffing(list("abcdefghijklmnopqrstuvwxyz".upper()))
    stuff = ByteStuffing()

    stuff.startStuffing()
    print(stuff.stuffed)
    
    stuff.startUnStuffing()
    print(stuff.unstuffed)