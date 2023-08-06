from dataclasses import dataclass, field

from fastapi import FastAPI

from cloudmesh.catalog.deprecated.pickleable_mixin import PickleableMixin

app = FastAPI()


@app.get("/cloudmesh/v1-0/registry/{name}")
async def get_name(name):
    registry = Registry()
    entry = registry.query({'name': name})
    return entry


class Registry(PickleableMixin):
    def __init__(self, directory):
        self.directory = directory  # string (i.e., 'data/')
        self.data = {}  # dictionary
        self.load(directory)  # loads self.data using yaml files in the given directory

    # takes a query in the form {'name': name}, i.e. {'name': 'Amazon Comprehend'}
    # search : dict
    def query(self, search):
        if 'name' in search.keys():
            for entry in self.data:
                if self.data[entry]['name'] == search['name']:
                    return self.data[entry]
        return None

    # adds a yaml file to this catalog's self.data 
    # file : string (i.e., 'data/amazon_comprehend.yaml')
    def add(self, file):
        with open(file, "r") as stream:
            try:
                parsed_yaml = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        self.data.update(parsed_yaml)  # update self.data with data from new file

    # loads self.data using yaml files in the given directory
    # directory : string (i.e., 'data/')
    def load(self, directory=None):
        if directory is None:
            directory = self.directory
        files = glob.glob(directory + '*.yaml')  # gets list of yaml files in given directory
        for file in files:
            self.add(file)


@dataclass
class RegistryEntry:
    # UUID, globally unique
    id: str
    # Name of the service
    name: str
    # Human readable title
    title: str
    # True if public (needs use case to delineate what pub private means)
    public: bool
    # Human readable short description of the service
    description: str
    # The endpoint of the service
    endpoint: str
    # A list of parameters to the service.
    # The parameters have each the form of name, function, type, value, access. 
    # - The type indicates the data type.
    # - The access indicates if the parameter is a data stream, database, single value/function, event. 
    # - The function responds to a different function in case multiple are provided by the service.
    input: list
    # List of responses cast by the service. 
    # The responses have the form of function, name, type, value, access, timestamp. 
    # - The type indicates the data type. 
    # - The access indicates if the parameter is a data stream, database, single value/function, event.
    # - The function responds to a different function in case multiple are provided by the service.
    output: list
    # The version number or tag of the service  
    version: str
    # The license description
    license: str
    # e.g., REST
    protocol: str
    # Modification timestamp
    modified: str
    # Name of the distributing entity, organization or individual. It could be a vendor.
    owner: str
    # contact details of the people or organization responsible for the service (freeform string)
    authors: str
    # Human readable common tags that are used to identify the service that are associated with the service
    tags: list = field(default_factory=list)
    # A category that this service belongs to (NLP, Finance, …)
    categories: list = field(default_factory=list)
    # Date and time on which the analytics service was instantiated or created
    created: str = 'unknown'
    # State and timestamp of the last check when the service was active
    heartbeat: str = 'unknown'
    # Link to documentation/detailed description of service
    documentation: str = 'unknown'
    # Link to source code if available
    source: str = 'unknown'
    # Pointer to where specification schema is located
    specification: str = 'unknown'
    # Additional metadata: Pointer to where additional is located including the one here
    additional_metadata: str = 'unknown'
    # SLA/Cost: service level agreement including cost
    sla: str = 'unknown'
    # Caching interval
    # If a service is accessed a lot, the caching interval can be used to put
    # a limitation on the Response with an LRU cache
    caching_interval: str = 'unknown'
    # Data integration
    # In case of big data the data cannot be provided as a parameter to the analysis function. 
    # Instead, we need to provide the data as endpoint. 
    # However, often data may need to be uploaded or can be downloaded. 
    # In this case this field provides the upload and download endpoints and the protocol to access the data
    data_integration: str = 'unknown'


# for testing
if __name__ == "__main__":
    pass
