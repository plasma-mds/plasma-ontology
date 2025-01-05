"""
A SPARQL querry for competency question: 'Who is experienced in the plasma source "kINPen-sci" at the institute "INP Greifswald?"'
"""

import rdflib
from utils import *
from prettytable import PrettyTable 

# Define and load the graph
g = rdflib.Graph()
g.parse("data//plasma-knowledge-graph-instances-only.rdf")

# Define the query
query = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX plsmo: <https://plasma-mds.org/ontology/plasma-o/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX vivo: <http://vivoweb.org/ontology/core#>
#
# Who is experienced in the plasma source "kINPen-sci"
# at the institute "INP Greifswald?"
#

SELECT DISTINCT ?Person ?PersonLabel ?PlasmaSource ?Institute 

WHERE
{
  # Define the types of the involved entities
  ?Person rdf:type foaf:Person .
  ?Institute rdf:type vivo:Institute .
  ?PlasmaSource rdf:type plsmo:PLSMO_C0005 .
  
  # Get the instance with label "INP Greifswald"
  ?Institute rdfs:label "INP Greifswald"@en-US .
  # Get the instance with label "kINPen-sci"
  ?PlasmaSource rdfs:label "kINPen-sci"@en-US .
  
  # Main query
  
  # Get Person and Institute instances that are connected with
  # a predicate "affiliatedWith" which has IRI plsmo:PLSMO_R0003
  ?Person plsmo:PLSMO_R0003 ?Institute .
  
  # Get Person and PlasmaSource instances that are connected with
  # a predicate "experiencedIn" which has IRI plsmo:PLSMO_R0032
  ?Person plsmo:PLSMO_R0032 ?PlasmaSource .
  
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