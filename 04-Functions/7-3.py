def f(sentence):
    return sum(1 for char in sentence if char in 'e')
if __name__ == "__main__":
    sentence = "You never get a second chance to make a first impression"
    print(f(sentence))