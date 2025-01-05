"""
A SPARQL querry for competency question: 'Which datasets are obtained with the diagnostic method "Cavity Ring-Down Spectroscopy applied (CRDS)" to diagnose the plasma source "kINPen-sci?"'
"""

import rdflib
from utils import *
from prettytable import PrettyTable 

# Define and load the graph
g = rdflib.Graph()
g.parse("data//plasma-knowledge-graph-instances-only.rdf")

# Define the query
query = """
PREFIX rdfs:        <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX plsmo:  <https://plasma-mds.org/ontology/plasma-o/>
PREFIX vivo: <http://vivoweb.org/ontology/core#>

#
# Which datasets are obtained with the diagnostic 
# method "Cavity Ring-Down Spectroscopy applied (CRDS)" 
# to diagnose the plasma source "kINPen-sci?"
#

SELECT DISTINCT ?Dataset ?DatasetLabel ?PlasmaStudy ?Method ?PlasmaSource

WHERE
{
  # Define the types of the involved entities
  ?Dataset rdf:type vivo:Dataset .
  ?PlasmaStudy rdf:type plsmo:PLSMO_C0024 .
  ?Method rdf:type plsmo:PLSMO_C0012 .
  ?PlasmaSource rdf:type plsmo:PLSMO_C0005 .

  # Get the instance with label "Cavity Ring-Down Spectroscopy (CRDS)"
  ?Method rdfs:label "Cavity Ring-Down Spectroscopy (CRDS)"@en-US .
  # Get the instance with label "kINPen-sci"
  ?PlasmaSource rdfs:label "kINPen-sci"@en-US .
  
  # Main query
  
  # Get instances of PlasmaStudy and Method connected
  # via a predicate "usesMethod" which has IRI plsmo:PLSMO_R0105
  ?PlasmaStudy plsmo:PLSMO_R0105 ?Method .
  
  # Get instances of PlasmaStudy and PlasmaSource connected
  # via a predicate "hasPlasmaSource" which has IRI plsmo:PLSMO_R0039
  ?PlasmaStudy plsmo:PLSMO_R0039 ?PlasmaSource .
  
  # Finally, get instances of Dataset and PlasmaStudy connected
  # via a predicate "outputOf" which has IRI plsmo:PLSMO_R0062
  ?Dataset plsmo:PLSMO_R0062 ?PlasmaStudy .
  
  # Note: Dataset is connected to PlasmaStudy by the outputOf property,
  # which is the inverse of the hasOutput property
  
  # Showing the labels for Dataset
  ?Dataset rdfs:label ?DatasetLabel .  				
}
# Returns maximum of 5 results
LIMIT 5
"""

# Define the column names for the result
table = PrettyTable(["Dataset", "DatasetLabel", "PlasmaStudy", "DiagnosticMethod", "PlasmaSource"]) 

print("DONE")

# Conduct the query
qres = g.query(query)

print("DONE")

print(len(qres))

# Pre-process the result and insert it to the table
for row in qres:
    print(row)
    col1 = remove_vivo_default_url(row[0])
    col3 = remove_vivo_default_url(row[2])
    col4 = remove_vivo_default_url(row[3])
    col5 = remove_vivo_default_url(row[4])
    table.add_row([col1, row[1], col3, col4, col5])

# Print the pre-processed result
print(table)