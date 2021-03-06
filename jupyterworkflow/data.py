from urllib.request import urlretrieve
import pandas as pd
import os

FREMONT_URL = "https://data.seattle.gov/api/views/7mre-hcut/rows.csv?accessType=DOWNLOAD"
def get_freemont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """Download and cache the fremont data
    
    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        location to load the data
    force_download bool (optional)
        force the download of the data

    Returns
    -------
    data : pandas.DataFrame
        the fremont bridge cycle count
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(URL, 'Fremont.csv')
    data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data
