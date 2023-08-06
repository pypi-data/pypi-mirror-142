"""Tools for ensuring that Julia registries and packages are installed correctly and that PyCall works"""

__version__ = '0.1.0'


from .basic import ensure_project_ready, ensure_project_ready_fix_pycall, test_pycall
