import pickle

def names():
    name = input("Как зовут? ")
    print("Привет", name)

thee = pickle.dumps(names)
print(thee)

end = pickle.loads(thee)
print(end)