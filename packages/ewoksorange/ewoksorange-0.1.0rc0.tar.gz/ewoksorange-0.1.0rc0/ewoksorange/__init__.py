from .bindings.owsignal_manager import patch_signal_manager

patch_signal_manager()

from .bindings import execute_graph  # noqa F401

__version__ = "0.1.0-rc"
