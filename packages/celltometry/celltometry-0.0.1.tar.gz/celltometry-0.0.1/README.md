[![Latest PyPI version](https://img.shields.io/pypi/v/celltometry.svg)](https://pypi.org/project/celltometry/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation Status](https://readthedocs.org/projects/topometry/badge/?version=latest)](https://topometry.readthedocs.io/en/latest/?badge=latest)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/DaviSidarta.svg?style=social&label=Follow%20%40davisidarta)](https://twitter.com/davisidarta)

# CellTOMetry: single-Cell Topologically Optimized Geometry

CellTOMetry is a python library to
orchestrate topological single-cell data analysis. It is centered around 
[TopOMetry](https://github.com/davisidarta/topometry) and 
[scanpy](https://scanpy.readthedocs.io/en/stable/index.html).

## Installation and dependencies

CellTOMetry requires [scanpy](https://scanpy.readthedocs.io/en/stable/index.html) 
and [TopOMetry](https://github.com/davisidarta/topometry). After installing both,
install celltometry with:

```
pip3 install celltometry
```

## Using CellTOMetry with scanpy

This is a quick-start. For further instructions, check [TopOMetry documentation](https://topometry.readthedocs.io/en/latest/pbmc3k.html).

First, we load libraries and some data to work with:
```
import scanpy as sc
import topo as tp
import celltometry as ct

# Load the PBMC3k dataset
adata = sc.datasets.pbmc3k()
```

Next, we perform the default preprocessing workflow with scanpy: libraries are size-normalized,
log-transformed for variance stabilization, and subset to highly variable genes. 

```
# Normalize and find highly variable genes
adata = ct.preprocess(adata)
```

Then, we proceed to the default scanpy workflow. It corresponds to:
* Scaling data (optional, changes adata.X) - ``
* Performing PCA 
* Learning a neighborhood graph
* Learn an UMAP projection with this graph
* Cluster this graph with the Leiden community detection algorithm

Similar to preprocessing, we wrap it
with an one-liner:

```
adata = ct.default_workflow(adata, scale=True)
```

To run the topological workflow, create a [TopOGraph](https://topometry.readthedocs.io/en/latest/topograph.html#topograph) object `tg` and use it to learn and add information to `AnnData`:

```
adata = ct.topological_workflow(adata, tg)
```

For further instructions, please check [TopOMetry documentation](https://topometry.readthedocs.io/en/latest/index.html).

