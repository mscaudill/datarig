"""Tools for displaying and downloading the data and metadata associated with
responses from websources utilizing a RESTful api. Currently this module
supports reading repository records from 

This module contains the following classes & functions:


"""

import abc
from collections import namedtuple
import copy
from pathlib import Path
import reprlib
import requests
from types import SimpleNamespace
from typing import ByteString, Dict, List, NamedTuple, Optional, Sequence, Union

from datarig.mixins import ViewInstance


class Record(abc.ABC, ViewInstance):
    """Abstract base class for reading records from a data repository with a 
    RESTful API.

    This ABC defines a protocol for reading data repositories from any websource
    utilizing a RESTful API. Inheritors are required to override the datasets
    and 'find' abstract methods in their concrete Record classes. 
    """

    def __init__(self, url: str,
                 params: Optional[Union[Dict, List, ByteString]] = None,
                 **kwargs,
    ) -> None:
        """Initialize this Record with a respository url where all datasets are
        housed & all additional parameters for a properly authorized GET
        request.

        Args:
            repo_url:
                A string url for a data repository.
            params:
                Additional information to include in the URL string with GETs
                request such as search terms that appear in the URL. For details
                see https://requests.readthedocs.io/en/latest/user/quickstart/
            kwargs:
                Any additional kwargs for requests GET method.
        """
        
        self.url = url
        self.response = requests.get(url, params, **kwargs)
        self._json = self.response.json()
        self.data = self.datasets() 

    @abc.abstractmethod
    def datasets(self) -> Sequence[NamedTuple]:
        """Returns namedtuples each representing a single data file."""

    @abc.abstractmethod
    def find(self, name:str) -> NamedTuple:
        """Returns a named dataset from all datasets in this Record."""

    def download(self, name: str , path: Optional[Path] = None, 
                 chunksize: Optional[int] = 2048,
    ) -> None:
        """Iteratively downloads a named dataset in this Record to path dir.

        Args:
            name:
                The name of the datum in this Record's datasets to download.
            path:
                A directory location where the named dataset will be saved to.
                If None, the current working directory will be used.
            chunksize:
                The number of bytes that should be read into memory at any time
                during the saving process. If None it will use whatever size
                chunks are recieved from the server.

        Returns: None

        Raises:
            A ValueError is raised if the named dataset does not exist in this
            Record.
        """

        dset = self.find(name)
        # use the name of the downloading file as the filename to save
        fname = Path(dset.links).name
        path = Path().cwd() if not path else Path(path)
        target = Path(path).joinpath(fname)

        # get the dataset url's response with streaming and write chunks
        r = requests.get(dset.links, stream=True)
        with open(target, 'wb') as outfile:
            for chunk in r.iter_content(chunk_size=chunksize):
                outfile.write(chunk)


class Zenodo(Record):
    """A Zenodo Repository Record for reading datasets stored on Zenodo.

    This Record type extends the base Record type to include additional
    properties pulled from the server's response.
    
    Attributes:
        doi:
            The string doi associated with this repository.
        date:
            The publication date of this repository.
        license:
            The license under which this data repository was published.
        creators:
            The authors of this repository and their respective affiliations.
        description:
            A string description of the contents of this repository.
        statistics;
            The usage statistics of this repository.
    """

    def datasets(self) -> Sequence[NamedTuple]:
        """Returns a sequence of namedtuples representing this Repositories
        datasets.

        Each named tuple datum will have the following accessible attributes.

        Attributes:
            bucket:
                The bucket url of this datum.
            checksum:
                A md5 checksum for security. No validation of these checksums
                occurs.
            key:
                The string name of this datum.
            links:
                The url link to this datum that will be used to download the
                data.
            size:
                The size of the file in bytes.
            type:
                The file extension of this datum.
        
        Returns:
            A list of namedtuples.
        """

        ls = copy.deepcopy(self._json['files'])
        for dic in ls: 
            # simplify the 'links' nested dict field of the response 
            dic['links'] = dic['links']['self']
        
        File = namedtuple('File', ls[0])
        return [File(**dic) for dic in ls]

    def find(self, name:str) -> NamedTuple:
        """Returns a named dataset from all datasets in this Zenodo Record."""

        names = [dset.key for dset in self.data]
        try:
            idx = names.index(name)
        except ValueError:
            msg = 'No dataset in this record is named {}.'
            raise ValueError(msg.format(name))

        return self.data[idx]

    @property
    def doi(self) -> str:
        """Returns the DOI of this Zenodo Record."""

        return self._json['doi']

    @property
    def date(self) -> str:
        """Returns the publication date of this Zenodo Record."""

        return self._json['metadata']['publication_date']

    @property
    def license(self) -> str:
        """Returns the license of this Zenodo Record."""

        return self._json['metadata']['license']['id']

    @property
    def creators(self) -> Sequence[NamedTuple]:
        """Returns a sequence of namedtuples representing repository authors."""

        ls = self._json['metadata']['creators']
        Creator = namedtuple('Creator', ls[0])
        return [Creator(**dic) for dic in ls]

    @property
    def description(self) -> str:
        """Returns a string description of this data Record."""

        return self._json['metadata']['description']

    @property
    def statistics(self) -> NamedTuple:
        """Returns a namedtuple containing the repositories statistics."""

        Stats = namedtuple('Statistics', self._json['stats'])
        return Stats(**self._json['stats'])

    
class Figshare(Record):
    """ """

    pass

if __name__ == '__main__':

    url = 'https://zenodo.org/api/records/6799475'
    
    """
    response = requests.get(url, stream=True)
    jstr = response.json()
    print(jstr.keys())
    """
    
    zen = Zenodo(url)
