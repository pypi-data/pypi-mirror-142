from setuptools import setup, Extension, find_packages


from distutils.command.build_ext import build_ext as build_ext_orig
class CTypesExtension(Extension): pass
class build_ext(build_ext_orig):
    def build_extension(self, ext):
        self._ctypes = isinstance(ext, CTypesExtension)
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)

    def get_ext_filename(self, ext_name):
        if self._ctypes:
            return ext_name + '.so'
        return super().get_ext_filename(ext_name)

module = CTypesExtension(
    'libpyeigenisolve',
    ['pyeigenisolve.cpp'],
    include_dirs=['eigen-3.4.0'],
    extra_compile_args=[
        '-fPIC', '-O3', '-shared', '-fopenmp'
    ],
    libraries=["gomp"],
    language="c++"
)


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyeigenisolve",
    version="1.0.0",
    author="dror",
    author_email="dror.mastershin@gmail.com",
    description="Sparse matrix iterative solvers with Eigen",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drorspei/pyeigenisolve",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    #cmdclass={'install': CustomInstall},
    py_modules=["pyeigenisolve"],
    cmdclass={'build_ext': build_ext},
    ext_modules=[module],
)
