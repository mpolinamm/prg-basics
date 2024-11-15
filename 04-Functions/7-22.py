def f(password):
    if len(password) >= 6 and len(set(password)) == len(password):
        #Converting password to a set removes duplicates.
        return True
    return False
if __name__ == "__main__":
    print(f("ax15")) 
    print(f("A2water3")) 