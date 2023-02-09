NAME_MEINER_VENV = "masm"
PYTHON_VERSION = "python3.7"
MINICONDA_ROOT = "/miniconda3"

import sys, os
# INTERP = os.environ["HOME"]+MINICONDA_ROOT+"/envs/"+NAME_MEINER_VENV+"/bin/"+PYTHON_VERSION
INTERP = os.environ["HOME"]+"/miniconda3/envs/masm/bin/python3.7"


# INTERP is present twice so that the new Python interpreter knows the 
if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
from MartialArtSchoolManagementSystem.wsgi import application
