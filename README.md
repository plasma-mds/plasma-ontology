# Plasma-Ontology

## Description

This is a repository for the plasma ontology development. Plasma Ontology (`plasma-ontology.ttl`), also called Plasma-O, is a domain-specific ontology for low-temperature plasma science and technology. It reuses several classes and properties from other ontologies such as [VIVO](https://github.com/vivo-ontologies/vivo-ontology), [BIBO](https://www.dublincore.org/specifications/bibo/bibo/), and [FOAF](http://xmlns.com/foaf/spec/). The repository also consists of an example knowledge graph, called Plasma Knowledge Graph (`data/plasma-knowledge-graph.rdf`) or Plasma-KG, which was built using Plasma-O (version 0.5.0) and the [VIVO software platform](https://vivoweb.org/) (version 1.13). From the provided knowledge graph, users can query various instance data using SPARQL (example python scripts with SPARQL queries are also provided in the repository under the `scripts` directory).

## Development

Using the [Protégé](https://protege.stanford.edu/) software is recommended to further develop the ontology.

## Getting started with the query scripts

Example queries can be run using the provided python scripts (under the `scripts` directory). To set up the python environment to run the scripts, do the following (on a Linux machine):

- `$ git clone https://github.com/plasma-mds/plasma-ontology.git`—clone the repository
- `$ cd plasma-ontology`—go to the project directory
- `plasma-ontology$ python -m venv venv`—create a python virtual environment (note that Python 3.8.7 was used as the time the scripts were prepared)
- `plasma-ontology$ source venv/bin/activate`—activate the virtual environment
- `plasma-ontology$ pip install -r scripts/requirements.txt`—install the dependencies needed to run the scripts
- `plasma-ontology$ python scripts/sparql_querry1.py`—run the script for the first SPARQL query example

## Support

Currently, this repository is maintained by the Research Data Management (RDM) group of the Leibniz Institute for Plasma Science and Technology. For support and inquiry, please send an e-mail to `ihda.chaeronysiffa@inp-greifswald`.


## Roadmap

Plasma-O and Plasma-KG will be developed further to accommodate various and new competency questions arising in the field of low-temperature plasma science and technology.

## Contributing

We are open to collaborations. Feed backs from low-temperature plasma scientists and researchers, as well as ontology experts are welcome, as we believe collaborative work is an important key to develop the ontology and knowledge graph further. 

## Acknowledgment

This work was partly funded by the Deutsche Forschungsgemeinschaft (DFG,German Research Foundation)—Project Number 496963457.

## License

Plasma-O and Plasma-KG are distributed under a [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).


