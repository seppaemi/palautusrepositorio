from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml = tomli.loads(content)
        #print(toml)

        dep = toml["tool"]["poetry"]["dependencies"]

        dev_dep = toml["tool"]["poetry"]["dev-dependencies"]

        #print(dev_dep)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project("Test name", "Test description", dep, dev_dep)
