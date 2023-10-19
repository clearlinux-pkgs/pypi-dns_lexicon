#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v2
# autospec commit: f032afc
#
Name     : pypi-dns_lexicon
Version  : 3.16.1
Release  : 91
URL      : https://files.pythonhosted.org/packages/2a/43/3b0eff450444321c10469e6108e9f319094a48c44386b4437bb62e71d43d/dns_lexicon-3.16.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2a/43/3b0eff450444321c10469e6108e9f319094a48c44386b4437bb62e71d43d/dns_lexicon-3.16.1.tar.gz
Summary  : Manipulate DNS records on various DNS providers in a standardized/agnostic way
Group    : Development/Tools
License  : MIT
Requires: pypi-dns_lexicon-bin = %{version}-%{release}
Requires: pypi-dns_lexicon-license = %{version}-%{release}
Requires: pypi-dns_lexicon-python = %{version}-%{release}
Requires: pypi-dns_lexicon-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
============
|logo_named|
============
Manipulate DNS records on various DNS providers in a standardized/agnostic way.

%package bin
Summary: bin components for the pypi-dns_lexicon package.
Group: Binaries
Requires: pypi-dns_lexicon-license = %{version}-%{release}

%description bin
bin components for the pypi-dns_lexicon package.


%package license
Summary: license components for the pypi-dns_lexicon package.
Group: Default

%description license
license components for the pypi-dns_lexicon package.


%package python
Summary: python components for the pypi-dns_lexicon package.
Group: Default
Requires: pypi-dns_lexicon-python3 = %{version}-%{release}

%description python
python components for the pypi-dns_lexicon package.


%package python3
Summary: python3 components for the pypi-dns_lexicon package.
Group: Default
Requires: python3-core
Provides: pypi(dns_lexicon)
Requires: pypi(beautifulsoup4)
Requires: pypi(cryptography)
Requires: pypi(pyotp)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(tldextract)

%description python3
python3 components for the pypi-dns_lexicon package.


%prep
%setup -q -n dns_lexicon-3.16.1
cd %{_builddir}/dns_lexicon-3.16.1
pushd ..
cp -a dns_lexicon-3.16.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697727691
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
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-dns_lexicon
cp %{_builddir}/dns_lexicon-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-dns_lexicon/d7389b6482179505c25d9b209b006826fcb6b85c || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lexicon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-dns_lexicon/d7389b6482179505c25d9b209b006826fcb6b85c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
