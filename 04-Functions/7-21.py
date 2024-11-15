def f(name):
    return ''.join(word[0] for word in name.split())
if __name__ == "__main__":
    print(f("Internet of Things")) 
    