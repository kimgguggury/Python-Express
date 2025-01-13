import pickle

file = open("text_file/save.p", "rb")
obj = pickle.load( file )
print(obj)