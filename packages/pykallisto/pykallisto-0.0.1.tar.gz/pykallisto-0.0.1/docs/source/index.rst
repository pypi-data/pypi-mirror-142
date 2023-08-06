.. PyKallisto documentation master file, created by
   sphinx-quickstart on Tue Mar 15 19:56:13 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyKallisto: A Python API for RNA-seq analysis via Kallisto & Bustools
============================================================================

**PyKallisto** is a Python wrapper for the `Kallisto <https://pachterlab.github.io/kallisto/>`_ tools from the Patcher Lab, and serves as a tool to easily align, quantify and normalize RNA-seq data, as well as generating cell x expression matrices for single-cell RNA-seq data. Additionally, **PyKallisto** is meant to be easily implemented in a bioinformatics pipeline for easy use in downstream analysis.

Usage
========

Installation
______________

To use PyKallisto, install the latest version with pip via 
::
   $ pip install pykallisto 

.. autofunction:: pykallisto.index()
   
.. toctree::
   :maxdepth: 2

   usage 

