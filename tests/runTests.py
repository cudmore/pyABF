"""
This file is a temporary stand-in for a more rigorous test suite.
When run, it re-genereates the index pages (readme.md) and graphs for
the data folder and the getting started guide.

If a code change does not effect the output at all, no changes will be
recognized in the output content (text or graphics).
"""

import os
import sys
PATH_HERE = os.path.abspath(os.path.dirname(__file__))
PATH_PROJECT = os.path.abspath(PATH_HERE+"/../")
PATH_DATA = os.path.abspath(PATH_PROJECT+"/data/abfs/")
import importlib.util
import warnings
import glob

def runFunctionInFile(filename, functionName="go"):
    """
    If a specific python file contains a "go()" function, load that file
    as a python module and call the go() function.
    """
    assert os.path.exists(filename)
    spec = importlib.util.spec_from_file_location("tempModule", filename)
    theModule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(theModule)
    if not functionName in dir(theModule):
        print("ERROR: %s has no %s() function" %
              (os.path.basename(filename), functionName))
    else:
        getattr(theModule, functionName)()

def clearOldFiles():
    for fname in glob.glob(PATH_DATA.replace("abfs", "headers")+'/*.*'):
        os.remove(fname)


if __name__ == "__main__":

    # clear everything that used to be in the headers folder
    #clearOldFiles()
    
    # test header parsing and value reading
    runFunctionInFile(PATH_PROJECT+"/tests/valueChecks.py")
    runFunctionInFile(PATH_PROJECT+"/data/generate-header-pages.py")

    # tests involving plotting of signal data
    runFunctionInFile(PATH_PROJECT+"/data/generate-data-index.py")
    #runFunctionInFile(PATH_PROJECT+"/docs/getting-started/generate-docs.py")

    print("\n\n### TESTS COMPLETED SUCCESSFULLY###\n")
