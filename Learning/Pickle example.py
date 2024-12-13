import pickle

f = open('store.pckl', 'rb')
obj = pickle.load(f)
f.close()

f = open('store.pckl', 'wb')
pickle.dump(obj, f)
f.close()