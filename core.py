"""Tools for displaying and downloading the data and metadata associated with
a Zenodo Record.

This module contains the following classes & functions:


"""

import reprlib
import requests
import wget

class Record:
    """ """

    # 1. I want this to be a dot access object that has all the important keys of
    # the json response, I need to determine what to keep
    # 2. I want this object to have a peek or show method to show me the
    #    datasets that I can download
    # 3. I want this object to nicely print itself
    # 4. I want this object to have a load method that can take the name of
    #    a dataset(s) or open a dialog with the available datasets that can be
    #    selected
    # 5. I want this object to display the sizes of the datasets in the record
    # 6. I want this object to gracefully raise errors
    # 7. I want this object to estimate the time to download or show a progress
    #    bar

    def __init__(self, record_id):
        """ """

        self._base_url = 'https://zenodo.org/api/records/'
        self._record = self._base_url + str(record_id)



if __name__ == '__main__':

    url = 'https://zenodo.org/api/records/6799475'
    response = requests.get(url)
    jstr = response.json()

    print(jstr.keys())
