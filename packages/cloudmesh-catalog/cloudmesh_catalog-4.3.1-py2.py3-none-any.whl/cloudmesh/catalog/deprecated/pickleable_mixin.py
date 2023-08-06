# replace with https://github.com/cloudmesh/yamldb

import pickle


# mixin to make a class pickleable
class PickleableMixin:
    # saves instance of this class as a pickle file with specified filename in the current working directory    
    def to_pickle(self, filename: str):
        file = open(filename, 'wb')
        pickle.dump(self, file)
        file.close()

    # returns data from a given pickle filename in the current working directory   
    def from_pickle(self, filename: str):
        file = open(filename, 'rb')
        retrieved = pickle.load(file)
        file.close()
        return retrieved
