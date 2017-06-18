#Packages

import pandas as pd
import urllib2
import simplejson as json
from collections import defaultdict
import subprocess
from datetime import datetime


#Point to the data
url = 'https://gbfs.citibikenyc.com/gbfs/en/station_status.json'
page = urllib2.urlopen(url)
content = page.read()
result = json.loads(content)


#Create a DataFrame
stations_df = pd.DataFrame(result['data']['stations'], columns=['eightd_has_available_keys','is_installed','is_renting','is_returning','last_reported','num_bikes_available','num_bikes_disabled','num_docks_available','num_docs_disabled','station_id'])
stations_df['last_reported'] = pd.to_datetime(stations_df['last_reported'], unit = 's')

#Calculate the number of available bikes

total_avail = stations_df['num_bikes_available'].sum()
print total_avail