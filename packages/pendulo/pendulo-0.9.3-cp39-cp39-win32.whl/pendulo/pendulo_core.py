# -*- coding: utf-8 -*-
'''package interface for Pendulo Penwin32.dll API '''
import re
from typing import List, Tuple, Callable

from pendulo._getdll import _getdllinfo

VectF = List[float]

# lookup for a matching folder, dll and import it
_dll_dir, _dll_name, _dll_api, _dll_context, _dll_from_embed = _getdllinfo()

if not _dll_api:
    raise ImportError(f'DLL {_dll_name}: not found or too old.\n')

# get the lang and the protection mode from the folder name
_m = re.search(r'(?:pendulo)_?(fr|fra|eng|esp|sp|uk|us)_?(ck)?\Z',
               _dll_dir, re.IGNORECASE)
_lang, _protmode = _m.group(1, 2) if _m else (None, None)
if not _lang:
    _lang = 'FR'
if not _protmode:
    _protmode = 'Flex?'
# print('Lang is:', _lang, ' * prot is:', _protmode)

close : Callable[[None], None] = _dll_api.quit
loadmodel : Callable[[str], None] = _dll_api.loadmodel
size_TS : Callable[[str, str, str], int] = _dll_api.size_ts
result_TS : Callable[[int], Tuple[VectF, VectF]] = _dll_api.result_ts

def init(debug : int = 0) -> bool:
    '''kernel initialisation - debug=0 for silent use, 1 or 2 for verbose'''
    return _dll_api.init(debug)

def ts(id_elem : str, typelt : str = 'NODE', attr : str = 'CH') -> Tuple[VectF, VectF]:
    '''Gets result TS from element id_elem - default CH (head) from NODE'''
    # Map UK attr to French
    attr = dict(HH='CH').get(attr, attr)
    # Build internal lookup info and return arrays lenght for caller
    nbval = size_TS(typelt, id_elem, attr)
    # retrieve time and value arrays from last element and attr called
    if nbval:
        return result_TS(nbval)
    return [], []
