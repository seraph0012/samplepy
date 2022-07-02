.. samplepy documentation master file, created by
   sphinx-quickstart on Thu Jun 30 22:53:45 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SamplePy: A Sample Python Project Documentation
===============================================

.. image:: https://img.shields.io/pypi/l/pypsa.svg
    :target: License

This is a sample documatation for a typical python project. The documentation page is generated using `readthedoc <https://readthedocs.org/>`_ and `sphinx <https://www.sphinx-doc.org/en/master/>`_.

The api references are automatically generated from python code using the `sphinx autodoc extension <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_. The python code documentation should follow the PEP8 conventions (`PEP 257 <https://peps.python.org/pep-0257/>`_ and `PEP 287 <https://peps.python.org/pep-0287/>`_). The `NumPy <https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard>`_ or `Google <https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings>`_ style docstrings are also supported.


Documentation
=============

**Getting Started**

* :doc:`introduction`
* :doc:`installation`
* :doc:`quick_start`

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Getting Started
   
   introduction
   installation
   quick_start
   
**Examples**

* :doc:`examples-basic`

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Examples
   
   examples-basic
   
**References**

* :doc:`api_reference`

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: References
   
   api_reference