import os
import subprocess as s

# 1) BOXMOX is installed and working
if 'KPP_HOME' in os.environ.keys():
    try:
        res = s.check_call("validate_BOXMOX_installation")
    except:
        raise OSError("Cannot validate BOXMOX installation using validate_BOXMOX_installation!")
else:
    raise OSError('$KPP_HOME not found in environment - is BOXMOX installed?')

# 2) an work directory has been defined and is useable
work_path = "/does/not/exist"
if 'BOXMOX_WORK_PATH' in os.environ.keys():
    work_path = os.environ['BOXMOX_WORK_PATH']
    try:
        if not os.path.isdir(work_path):
            os.makedirs(work_path)
    except:
        raise OSError("Could not create work directory " + work_path)
else:
    raise OSError('$BOXMOX_WORK_PATH not found in environment - set it to a path were BOXMOX can write stuff to.')

if not os.path.isdir(work_path):
    import warnings
    warnings.warn("BOXMOX model unusable - experiment execution disabled.")
else:
    from .experiment import Experiment, ExperimentFromExample, ExperimentFromExistingRun, Namelist, examples, compiledMechs

from .data import InputFile, Output, ConcentrationOutput, RatesOutput, AdjointOutput, JacobianOutput, HessianOutput
from .fluxes import FluxParser

try:
    import matplotlib
    from .plotter import ExperimentPlotter
except:
    import warnings
    warnings.warn('matplotlib not found - plotting disabled.')
