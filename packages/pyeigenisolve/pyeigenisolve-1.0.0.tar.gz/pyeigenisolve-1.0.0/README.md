# pyeigenisolve

A few iterative sparse matrix solvers written with Eigen, and python bindings.

In order to install you need a modern C++ compiler and openmp.

# License stuff

Eigen-3.4.0 is MPL-2.0 licensed. The original source code, available at https://eigen.tuxfamily.org/index.php?title=Main_Page was modified in the following ways:
1. Files and directories not necessary for this program were removed.

The LSQR implementation is Apache-2.0 licensed. The original source code, available at https://github.com/harusametime/LSQRwithEigen/tree/1921c44c65b5e26f3a6958c8277704cc33ffd101 was modified in the following ways:
1. Only the code from LSQR.cpp was copy pasted, and changed to work with sparse matrices instead of dense matrices.

These two together mean that this repo is kind of Apache-2.0 licensed. I think.
