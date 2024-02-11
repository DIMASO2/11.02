import pickle

big_object = {
    "items": ["1", (2, 3), ["some", "else"], {"op": "ap"}]
}

result = pickle.dumps(big_object)

print(result)