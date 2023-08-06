__author__ = 'IncognitoCoding'
__copyright__ = 'Copyright 2022, fchecker'
__credits__ = ['IncognitoCoding']
__license__ = 'GPL'
__version__ = '0.6'
__maintainer__ = 'IncognitoCoding'
__status__ = 'Beta'

from .dict_checks import KeyCheck
from .type_checks import type_check
from .file_checks import file_check
from .common import InputFailure, InvalidKeyError

__all__ = [
    'KeyCheck',
    'type_check',
    'file_check',
    'InputFailure',
    'InvalidKeyError'
]
