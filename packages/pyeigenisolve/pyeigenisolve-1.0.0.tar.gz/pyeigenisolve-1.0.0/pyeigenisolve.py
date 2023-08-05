import ctypes
import os
from functools import wraps
import numpy as np

_libname = "libpyeigenisolve.so"
_libpaths = [
    _libname,
    "./" + _libname,
    os.path.join(os.path.dirname(__file__), _libname)
]
for _path in _libpaths:
    try:
        _lib = ctypes.CDLL(_path)
    except OSError:
        pass
    else:
        break
else:
    raise OSError("couldn't find libpyeigenisolve.so")


def _get_ptr_array(x):
    return x.__array_interface__['data'][0]


def _prepare(i, j, entries, y, x0):
    i = np.asarray(i)
    assert i.ndim == 1
    assert i.dtype == 'i4'
    assert np.all(i >= 0)

    j = np.asarray(j)
    assert j.ndim == 1
    assert j.dtype == 'i4'
    assert np.all(j >= 0)

    entries = np.asarray(entries, dtype=np.float64)
    assert entries.ndim == 1
    assert len(i) == len(j) == len(entries)

    y = np.asarray(y, dtype=np.float64)
    assert y.ndim == 1

    rows = len(y)
    assert rows >= np.max(i)
    cols = np.max(j) + 1

    if x0 is None:
        x0 = np.zeros(cols)
    else:
        x0 = np.asarray(x0)
        assert x0.ndim == 1
        assert len(x0) == cols

    return i, j, entries, y, rows, cols, x0

def _wrapeigen(func):
    @wraps(func)
    def inner(A, y, x0=None, tol=1e-5, maxiters=1000):
        i, j, entries = A.row, A.col, A.data
        i, j, entries, y, rows, cols, x0 = _prepare(
            i, j, entries, y, x0
        )
        
        x = np.empty(cols, dtype=np.float64)
        istop = (ctypes.c_int64 * 1)()
        niters = (ctypes.c_int64 * 1)()

        func(
            rows,
            cols,
            len(i),
            _get_ptr_array(i),
            _get_ptr_array(j),
            _get_ptr_array(entries),
            _get_ptr_array(y),
            _get_ptr_array(x0),
            _get_ptr_array(x),
            tol,
            maxiters,
            ctypes.cast(istop, ctypes.POINTER(ctypes.c_int64)),
            ctypes.cast(niters, ctypes.POINTER(ctypes.c_int64)),
        )

        return x, int(istop[0]), int(niters[0])
    return inner


argtypes = [
    ctypes.c_int64,
    ctypes.c_int64,
    ctypes.c_int64,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_int64
]

_lib.lscg.argtypes = argtypes
_lib.lscg.restype = None
eigenlscg = _wrapeigen(_lib.lscg)

_lib.lsqr.argtypes = argtypes
_lib.lsqr.restype = None
eigenlsqr = _wrapeigen(_lib.lsqr)

_lib.lsmr.argtypes = [
    ctypes.c_int64,
    ctypes.c_int64,
    ctypes.c_int64,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_int64
]
_lib.lsmr.restype = None

def eigenlsmr(
    A,
    y,
    x0=None,
    a_tol=1e-5,
    b_tol=1e-5,
    conlim=1e8,
    lambda_=0,
    maxiters=1000
):
    i, j, entries = A.row, A.col, A.data
    i, j, entries, y, rows, cols, x0 = _prepare(
        i, j, entries, y, x0
    )
    
    x = np.empty(cols, dtype=np.float64)
    istop = (ctypes.c_int64 * 1)()
    niters = (ctypes.c_int64 * 1)()

    _lib.lsmr(
        rows,
        cols,
        len(i),
        _get_ptr_array(i),
        _get_ptr_array(j),
        _get_ptr_array(entries),
        _get_ptr_array(y),
        _get_ptr_array(x0),
        _get_ptr_array(x),
        a_tol,
        b_tol,
        conlim,
        lambda_,
        maxiters,
        ctypes.cast(istop, ctypes.POINTER(ctypes.c_int64)),
        ctypes.cast(niters, ctypes.POINTER(ctypes.c_int64)),
    )

    return x, int(istop[0]), int(niters[0])


def _test():
    class sparse:
        row = np.array([0, 1, 2, 2], np.int32)
        col = np.array([0, 1, 0, 1], np.int32)
        data = np.r_[1., 1., 1., 1.]
    A = sparse()


    y = np.r_[2., 3., 5.]

    solvers = [
        eigenlscg, eigenlsmr, eigenlsqr
    ]

    for solver in solvers:
        x, istop, niters = solver(A, y, maxiters=1000)
        print(istop, niters)
        assert np.allclose(x, [2., 3.]), solver


if __name__ == "__main__":
    _test()
