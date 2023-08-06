from fastapi import FastAPI
from yamldb import YamlDB
from cloudmesh.common.util import path_expand
import yamldb
from cloudmesh.common.util import path_expand
from pathlib import Path
from pprint import pprint

app = FastAPI()

filename = path_expand("~/.cloudmesh/catalog/data.yml")
print (filename)
print(yamldb.__version__)

db = yamldb.YamlDB(filename=filename)

#
# PATH NEEDS TO BE DONE DIFFERENTLY, probably as parameter to start.
# see also load command
source = path_expand("~/Desktop/cm/nist/catalog")

def _find_sources_from_dir(source=None):
    source = Path(source).resolve()
    result = Path(source).rglob('*.yaml')
    return result

files = _find_sources_from_dir(source=source)

for file in files:
    db.update(file)

@app.get("/")
def read_root():
    return {"Cloudmesh Catalog": "running"}

@app.get("/list")
def list_db():
    return db

@app.get("/load/{directory}")
def load(directory: str):
    return {"Cloudmesh Catalog": directory}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
