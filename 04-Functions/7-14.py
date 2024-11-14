def  f(detector):
    count = 0  
    for event in detector:
        if event == "+":
            count += 1  
        elif event == "-":
            count -= 1  
        if count >= 3:
            return True
    return False
if __name__ == "__main__":
    print(f('+-+++-+---')) #True
    print(f('+-++-+--')) #False