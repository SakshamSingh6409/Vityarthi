# Compatibility shim for legacy imports.
# Prefer using bookmgr.config for any new code.
from config import *  
# noqa: F401,F403
# The above line imports all variables from config.py to maintain compatibility with legacy code that imports from variables.py.
# flake8: noqa
# pylint: disable=unused-wildcard-import
# type: ignore
# The above comments disable linting and type checking warnings for this compatibility shim.
# This file is kept to ensure that existing codebases that import from bookmgr.variables continue to function correctly.
# However, new code should import directly from bookmgr.config to avoid confusion and improve maintainability.
# End of compatibility shim.
