from yamldb import YamlDB


class DataBase(YamlDB):


    def __init__(self, name="~/.cloudmesh/catalog/data.yaml", kind=YamlDB):
        self.db = YamlDB(filename=name)
        #
        # TODO: create the database if it does not exists
        # check if yamldb already does this
        #

    def update(self, name):
        self.db.uppdate(name)