#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: 5424026
#
Name     : pypi-jupyterlite_pyodide_kernel
Version  : 0.4.5
Release  : 6
URL      : https://files.pythonhosted.org/packages/49/f6/91fed30169dbef3470c65465ffc938e9181d4f8b13254b9b773e9aee48c4/jupyterlite_pyodide_kernel-0.4.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/49/f6/91fed30169dbef3470c65465ffc938e9181d4f8b13254b9b773e9aee48c4/jupyterlite_pyodide_kernel-0.4.5.tar.gz
Summary  : Python kernel for JupyterLite powered by Pyodide
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyterlite_pyodide_kernel-bin = %{version}-%{release}
Requires: pypi-jupyterlite_pyodide_kernel-data = %{version}-%{release}
Requires: pypi-jupyterlite_pyodide_kernel-license = %{version}-%{release}
Requires: pypi-jupyterlite_pyodide_kernel-python = %{version}-%{release}
Requires: pypi-jupyterlite_pyodide_kernel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
BuildRequires : pypi(jupyterlab)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# jupyterlite-pyodide-kernel
> A Python kernel for [JupyterLite](https://jupyterlite.rtfd.io) powered by
> [Pyodide](https://pyodide.org),

%package bin
Summary: bin components for the pypi-jupyterlite_pyodide_kernel package.
Group: Binaries
Requires: pypi-jupyterlite_pyodide_kernel-data = %{version}-%{release}
Requires: pypi-jupyterlite_pyodide_kernel-license = %{version}-%{release}

%description bin
bin components for the pypi-jupyterlite_pyodide_kernel package.


%package data
Summary: data components for the pypi-jupyterlite_pyodide_kernel package.
Group: Data

%description data
data components for the pypi-jupyterlite_pyodide_kernel package.


%package license
Summary: license components for the pypi-jupyterlite_pyodide_kernel package.
Group: Default

%description license
license components for the pypi-jupyterlite_pyodide_kernel package.


%package python
Summary: python components for the pypi-jupyterlite_pyodide_kernel package.
Group: Default
Requires: pypi-jupyterlite_pyodide_kernel-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyterlite_pyodide_kernel package.


%package python3
Summary: python3 components for the pypi-jupyterlite_pyodide_kernel package.
Group: Default
Requires: python3-core
Provides: pypi(jupyterlite_pyodide_kernel)
Requires: pypi(jupyterlite_core)
Requires: pypi(pkginfo)

%description python3
python3 components for the pypi-jupyterlite_pyodide_kernel package.


%prep
%setup -q -n jupyterlite_pyodide_kernel-0.4.5
cd %{_builddir}/jupyterlite_pyodide_kernel-0.4.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1733819485
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyterlite_pyodide_kernel
cp %{_builddir}/jupyterlite_pyodide_kernel-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyterlite_pyodide_kernel/489433bbf55cd22907d9a248dc6225e426144563 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-piplite

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/install.json
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/package.json
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/154.9feeb76655c460bb662b.js
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/154.9feeb76655c460bb662b.js.map
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/304.0bb9abc93cc92244ff25.js
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/304.0bb9abc93cc92244ff25.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/304.0bb9abc93cc92244ff25.js.map
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/352.199d03f2b99f4594a889.js
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/352.199d03f2b99f4594a889.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/352.199d03f2b99f4594a889.js.map
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/378.d1d840acae39794fdecd.js
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/378.d1d840acae39794fdecd.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/378.d1d840acae39794fdecd.js.map
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/620.52308b6425da4e3d805d.js
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/620.52308b6425da4e3d805d.js.LICENSE.txt
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/620.52308b6425da4e3d805d.js.map
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/pypi/all.json
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/pypi/ipykernel-6.9.2-py3-none-any.whl
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/pypi/piplite-0.4.5-py3-none-any.whl
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/pypi/pyodide_kernel-0.4.5-py3-none-any.whl
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/pypi/widgetsnbextension-3.6.999-py3-none-any.whl
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/pypi/widgetsnbextension-4.0.999-py3-none-any.whl
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/remoteEntry.d6704cdc807d45819742.js
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/remoteEntry.d6704cdc807d45819742.js.map
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/schema/kernel.v0.schema.json
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/schema/piplite.v0.schema.json
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/style.js
/usr/share/jupyter/labextensions/@jupyterlite/pyodide-kernel-extension/static/third-party-licenses.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyterlite_pyodide_kernel/489433bbf55cd22907d9a248dc6225e426144563

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
