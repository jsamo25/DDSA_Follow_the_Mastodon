import networkx as nx
import pandas as pd
import simplejson as json

"""
The dataset is made up by five files: 
mastodon_first_snapshot_anonim.csv 
mastodon_growth_from_1_16_to_3_16_anonim.csv 
instances_position.json 
data_instances_over_time.json 
instances_topics.json

mastodon_first_snapshot_anonim.csv contains the first snapshot of the Mastodon network, 
i.e. the data collected by the first run of our crawler. 
The crawler terminated on January 16, 2018. 
The directed network is represented by an edge list, where each line has the format:

<source>,<destination> 

Source and destination are delimited by the character ',' and they follow the format:

username@instance 

where 'username' is the anonimyzed username (number) and instance is the server hosting the user. 
mastodon_growth_from_1_16_to_3_16_anonim.csv captures the growth of the Mastodon network from 16/01/2108 to 16/03/2018. 
Each line represents a new directed link and reports:

source destination crawling time of the new link. It follows the format 'YYYY-MM-DD HH:mm:ss.milliseconds'

"""

""" Load the Network """

mastodon_digraph = nx.read_edgelist("mastodon_first_snapshot_anonim.csv", create_using= nx.DiGraph(),delimiter=",")

#To load the temporal annotated links...
with open("mastodon_growth_from_1_16_to_3_16_anonim.csv","r") as f:
    for line in f:
        source, destination, date = line.strip().split(",")
        mastodon_digraph.add_edge(source,destination,timestamp=date)

""" Instance meta-data"""

"""
instances_position.json contains the location of the instances. 
From the JSON file we can create a Pandas DataFrame (table):
"""

instances_location = pd.read_json("instances_position.json")
print(instances_location.head())

"""
The index of the DataFrame is the name of the instance. 
The column 'CountryCode' indicates the ISO 3166-1 alpha-3 6 code of the country hosting the server, 
while the column 'Location' reports the information returned by the geo-lookup service 'freegeoip.net'
"""

instances_info = pd.read_json("data_instances_over_time.json")
print(instances_info)
"""
The index of the DataFrame is the day we collected data about the instances. 
Each instance corresponds to a column, and we add four columns:

#Instances: the number of running instances in a specific day 
#Links: the total number of connections between the instances 
#Statuses: the total number of posts published till a specific day 
#Users: the total number of users till a specific day Each instance 
in a specific day is characterized by a Python dictionary storing information about 
the number of users, connections to other instances and number of posts
"""