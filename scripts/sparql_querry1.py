"""
A SPARQL querry for competency question: 'Who is experienced in the plasma source "kINPen-sci" at the institute "INP Greifswald?"'
"""

import rdflib
from utils import *
from prettytable import PrettyTable 

# Define and load the graph
g = rdflib.Graph()
g.parse("data//plasma-knowledge-graph.rdf")

# Define the query
query = """
PREFIX rdfs:        <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf:         <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX plasma-o:    <http://plasma-mds.org/ontology/>
PREFIX foaf:        <http://xmlns.com/foaf/0.1/>

#
# Who is experienced in the plasma source "kINPen-sci"
# at the institute "INP Greifswald?"
#

SELECT  ?Person ?PersonLabel ?PlasmaSource ?Institute 

WHERE
{
  # Define the type (the class) of Person
  ?Person rdf:type foaf:Person .
  
  # Get the instance with label "INP Greifswald"
  ?Institute rdfs:label "INP Greifswald"@en-US .
  # Get the instance with label "kINPen-sci"
  ?PlasmaSource rdfs:label "kINPen-sci"@en-US .
  
  # Main query
  ?Person plasma-o:isAffiliatedWith ?Institute .
  ?Person plasma-o:isExperiencedInDevice ?PlasmaSource .
  
  # Showing the labels for Person
  ?Person rdfs:label ?PersonLabel .  									
}
# Returns maximum of 5 results
LIMIT 5
"""

# Define the column names for the result
table = PrettyTable(["Person", "PersonLabel", "PlasmaSource", "Institute"]) 

# Conduct the query
qres = g.query(query)

# Pre-process the result and insert it to the table
for row in qres:
    col1 = remove_vivo_default_url(row[0])
    col3 = remove_vivo_default_url(row[2])
    col4 = remove_vivo_default_url(row[3])
    table.add_row([col1, row[1], col3, col4])

# Print the pre-processed result
print(table)