import sys
from .celltometry import TopOGraph, preprocess, default_workflow, default_integration_workflow, \
    topological_workflow, topological_harmony_integration, topological_scanorama_integration,\
    topological_bbknn_integration
from ._utils import annotate_doc_types
from .version import __version__

sys.modules.update({f'{__name__}.{m}': globals()[m] for m in ['TopOGraph', 'preprocess', 'default_workflow',
                                                              'default_integration_workflow',
                                                              'topological_workflow',
                                                              'topological_harmony_integration',
                                                              'topological_scanorama_integration',
                                                              'topological_bbknn_integration']})

annotate_doc_types(sys.modules[__name__], 'celltometry')
