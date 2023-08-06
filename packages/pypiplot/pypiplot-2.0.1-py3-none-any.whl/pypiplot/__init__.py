from pypiplot.pypiplot import Pypiplot

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '2.0.1'

# module level doc-string
__doc__ = """
pypiplot
=====================================================================

Description
-----------
Python package to count and plot the number of downloads from Pypi.

Example
-------
>>> # import library
>>> from pypiplot import Pypiplot
>>>
>>> # initialize
>>> pp = Pypiplot(username='erdogant')
>>>
>>> # Gather all repos
>>> pp.update()
>>>
>>> # Compute statistics
>>> pp.stats()
>>>
>>> # Make plot per calender
>>> pp.plot_cal()
>>> pp.plot_year()
>>> pp.plot()
>>>

References
----------
* https://github.com/erdogant/pypiplot

"""
