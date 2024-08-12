"""
A SPARQL querry for competency question: 'Which datasets are obtained with the diagnostic method "Cavity Ring-Down Spectroscopy applied (CRDS)" to diagnose the plasma source "kINPen-sci?"'
"""

import rdflib
from utils import *
from prettytable import PrettyTable 

# Define and load the graph
g = rdflib.Graph()
g.parse("data//plasma-knowledge-graph.rdf")

# Define the query
query = """
PREFIX rdfs:      <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf:       <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX plasma-o:  <http://plasma-mds.org/ontology/>
PREFIX vivo:      <http://vivoweb.org/ontology/core#>

#
# Which datasets are obtained with the diagnostic 
# method "Cavity Ring-Down Spectroscopy applied (CRDS)" 
# to diagnose the plasma source "kINPen-sci?"
#

SELECT  ?Dataset ?DatasetLabel ?PlasmaStudy ?DiagnosticMethod ?PlasmaSource

WHERE
{
  # Define Dataset and PlasmaStudy
  ?Dataset rdf:type vivo:Dataset .
  ?PlasmaStudy rdf:type plasma-o:PlasmaStudy .

  # Get the instance with label "Cavity Ring-Down Spectroscopy (CRDS)"
  ?DiagnosticMethod rdfs:label "Cavity Ring-Down Spectroscopy (CRDS)"@en-US .
  # Get the instance with label "kINPen-sci"
  ?PlasmaSource rdfs:label "kINPen-sci"@en-US .
  
  # Main query
  ?PlasmaStudy plasma-o:experimentUsesMethod ?DiagnosticMethod .
  ?PlasmaStudy plasma-o:hasPlasmaSource ?PlasmaSource .
  ?Dataset plasma-o:isOutputOf ?PlasmaStudy .
  # Note: Dataset is connected to PlasmaStudy by the isOutputOf property,
  # which is the inverse of the hasOutput property
  
  # Showing the labels for Dataset
  ?Dataset rdfs:label ?DatasetLabel .  				
}
# Returns maximum of 5 results
LIMIT 5
"""

# Define the column names for the result
table = PrettyTable(["Dataset", "DatasetLabel", "PlasmaStudy", "DiagnosticMethod", "PlasmaSource"]) 

# Conduct the query
qres = g.query(query)

# Pre-process the result and insert it to the table
for row in qres:
    col1 = remove_vivo_default_url(row[0])
    col3 = remove_vivo_default_url(row[2])
    col4 = remove_vivo_default_url(row[3])
    col5 = remove_vivo_default_url(row[4])
    table.add_row([col1, row[1], col3, col4, col5])

# Print the pre-processed result
print(table)