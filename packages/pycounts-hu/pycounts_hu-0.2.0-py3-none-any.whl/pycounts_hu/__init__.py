# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_hu")

# populate package namespace
from pycounts_hu.pycounts import count_words
from pycounts_hu.plotting import plot_words