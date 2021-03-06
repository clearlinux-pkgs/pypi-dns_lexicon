#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-dns_lexicon
Version  : 3.11.3
Release  : 73
URL      : https://files.pythonhosted.org/packages/2f/c7/66b8657c03846353d6d46910329a853308810ea602914ebd254ddf7c2cb8/dns-lexicon-3.11.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/2f/c7/66b8657c03846353d6d46910329a853308810ea602914ebd254ddf7c2cb8/dns-lexicon-3.11.3.tar.gz
Summary  : Manipulate DNS records on various DNS providers in a standardized/agnostic way
Group    : Development/Tools
License  : MIT
Requires: pypi-dns_lexicon-bin = %{version}-%{release}
Requires: pypi-dns_lexicon-license = %{version}-%{release}
Requires: pypi-dns_lexicon-python = %{version}-%{release}
Requires: pypi-dns_lexicon-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

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
Requires: pypi(importlib_metadata)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(tldextract)

%description python3
python3 components for the pypi-dns_lexicon package.


%prep
%setup -q -n dns-lexicon-3.11.3
cd %{_builddir}/dns-lexicon-3.11.3
pushd ..
cp -a dns-lexicon-3.11.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655822024
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-dns_lexicon
cp %{_builddir}/dns-lexicon-3.11.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-dns_lexicon/d7389b6482179505c25d9b209b006826fcb6b85c
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
