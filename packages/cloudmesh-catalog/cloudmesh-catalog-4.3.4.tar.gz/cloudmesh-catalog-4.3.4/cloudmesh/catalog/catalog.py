import glob
from dataclasses import dataclass, field

import yaml
from fastapi import FastAPI

from cloudmesh.common.util import path_expand

# TODO: this is not a stand alone prg
# TODO: needs to use yamldb instead of pickle
# TODO: needs to read form defined relative directory for data
#    find data from source deployment while looking for cloudmesh/catalog/data
# TODO: the data directory is in home dire and therefore could be overwritten,
#   we need to moe likely elsewhere
# TODO: the version is hardcoded
# TODO: the initializer of where the data dire is is incorrect, it requires
#   this to be
#      started from dir in which data dir is
# TODO: if yamldb can be used its much more comfortable
# Option:       alternatively we could use containers and Mongo db or something
#               like that
# TODO: if name must be removed

catalog_api_version = "1.0"
catalog_api_base = f"/cloudmesh/{catalog_api_version}/catalog/"


# TODO: is there a way to just set the base url and than all following urls are
#       specified without the baseURL

#
# TODO: why is his not in the class?
#
@app.get("/cloudmesh/v1-0/catalog/{name}")
async def get_name(name):
    catalog = Catalog('data/')
    entry = catalog.query({'name': name})
    return entry


class Catalog:

    def __init__(self, directory):
        server()
        raise NotImplementedError

        # TODO: WE SHOUlD JUST USE dATAbASE AND MAKE SURE WE FIX THAT CLASS

        # self.directory = directory  # string (i.e., 'data/')
        # self.data = {}  # dictionary
        # self.load(directory)  # loads self.data using yaml files in the given directory

    def server(self):
        self.app = FastAPI()

    # takes a query in the form {'name': name}, i.e. {'name': 'Amazon Comprehend'}
    # search : dict
    def query(self, search):
        """
        Conducts a query using jmsepath

        :param search:
        :type search:
        :return:
        :rtype:
        """
        raise NotImplementedError
        return None

    def add(self, file):
        """
        # adds a yaml file to this catalog's self.data

        :param file: The filename.  EXAMPLE '~/data/amazon_comprehend.yaml'
        :type file: str
        :return: returns true if the upload was successful
        :rtype: bool
        """
        file = path_expand(file)
        with open(file, "r") as stream:
            try:
                parsed_yaml = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        self.data.update(parsed_yaml)  # update self.data with data from new file
        raise NotImplementedError

    # loads self.data using yaml files in the given directory
    # directory : string (i.e., 'data/')
    def load(self, directory=None):
        if directory is None:
            directory = self.directory
        files = glob.glob(directory + '*.yaml')  # gets list of yaml files in given directory
        for file in files:
            self.add(file)


@dataclass
class CatalogEntry:
    # UUID, globally unique
    id: str
    # Name of the service
    name: str
    # Author of the service
    author: str
    # slugline of the service (i.e., amazon-comprehend)
    slug: str
    # Human readable title
    title: str
    # True if public (needs use case to delineate what pub private means)
    public: bool
    # Human readable short description of the service
    description: str
    # The version number or tag of the service
    version: str
    # The license description
    license: str
    # yes/no/mixed
    microservice: str
    # e.g., REST
    protocol: str
    # Name of the distributing entity, organization or individual. It could be a vendor.
    owner: str
    # Modification timestamp (when unmodified, same as created)
    modified: str
    # Date on which the entry was first created
    created: str
    # Link to documentation/detailed description of service
    documentation: str = 'unknown'
    # Link to the source code if available
    source: str = 'unknown'
    # Human readable common tags that are used to identify the service that are associated with the service
    tags: list = field(default_factory=list)
    # A category that this service belongs to (NLP, Finance, …)
    categories: list = field(default_factory=list)
    # specification/schema: pointer to where schema is located
    specification: str = 'unknown'
    # Additional metadata: Pointer to where additional is located including the one here
    additional_metadata: str = 'unknown'
    # The endpoint of the service
    endpoint: str = 'unknown'
    # SLA/Cost: service level agreement including cost
    sla: str = 'unknown'
    # contact details of the people or organization responsible for the service (freeform string)
    authors: str = 'unknown'
    # description on how data is managed
    data: str = 'unknown'

# FOR TESTING
# if __name__ == "__main__":
#    catalog = Catalog('data/catalog/')
#    # print(cat.data)
#
#    query_result = catalog.query({'name': 'Amazon Comprehend'})
#    print(query_result)
