"""
ARGUS background pdf.

See Also
--------
https://root.cern.ch/doc/master/classRooArgusBG.html
"""
import numpy as np
from ._util import _jit, _generate_wrappers, _prange

_doc_par = """
x : ArrayLike
    Random variate.
m0 : Sets the end-point (maximum) of the function.
p : Strength of the power-law term (often fixed to 0.5).
c : Strength of the exponential term.
"""


@_jit(1)
def _trans_x(x, m0):
    t = x / m0
    return 1 - np.power(t, 2)

@_jit(3)
def _pdf(x, m0, p, c):
    z = _trans_x(x, m0)
    out = np.empty_like(z)
    for i in _prange(len(z)):
        z_i = z[i]
        if z_i < 0.0:
            out[i] = 0.0
        else:
            out[i] = x[i] * np.power(z_i, p) * np.exp(c * z_i)

    return out

_generate_wrappers(globals())