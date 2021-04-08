#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmwaw
Version  : 0.3.18
Release  : 6
URL      : https://dev-www.libreoffice.org/src/libmwaw-0.3.18.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libmwaw-0.3.18.tar.xz
Summary  : Library for reading and converting ClarisWorks, MacWrite, WriteNow word processor documents
Group    : Development/Tools
License  : LGPL-2.1 MPL-2.0-no-copyleft-exception
Requires: libmwaw-bin = %{version}-%{release}
Requires: libmwaw-lib = %{version}-%{release}
Requires: libmwaw-license = %{version}-%{release}
BuildRequires : doxygen
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-generators-0.0)
BuildRequires : pkgconfig(zlib)

%description
Library that handles ClarisWorks, MacWrite, WriteNow documents.

%package bin
Summary: bin components for the libmwaw package.
Group: Binaries
Requires: libmwaw-license = %{version}-%{release}

%description bin
bin components for the libmwaw package.


%package dev
Summary: dev components for the libmwaw package.
Group: Development
Requires: libmwaw-lib = %{version}-%{release}
Requires: libmwaw-bin = %{version}-%{release}
Provides: libmwaw-devel = %{version}-%{release}
Requires: libmwaw = %{version}-%{release}

%description dev
dev components for the libmwaw package.


%package doc
Summary: doc components for the libmwaw package.
Group: Documentation

%description doc
doc components for the libmwaw package.


%package lib
Summary: lib components for the libmwaw package.
Group: Libraries
Requires: libmwaw-license = %{version}-%{release}

%description lib
lib components for the libmwaw package.


%package license
Summary: license components for the libmwaw package.
Group: Default

%description license
license components for the libmwaw package.


%prep
%setup -q -n libmwaw-0.3.18
cd %{_builddir}/libmwaw-0.3.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617894375
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1617894375
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmwaw
cp %{_builddir}/libmwaw-0.3.18/COPYING.LGPL %{buildroot}/usr/share/package-licenses/libmwaw/6ec1f37ffe429f1cd0585eb50658a1877da1658b
cp %{_builddir}/libmwaw-0.3.18/COPYING.MPL %{buildroot}/usr/share/package-licenses/libmwaw/98fc4d9117e318bd75af8a544c8a0238c3334186
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mwaw2csv
/usr/bin/mwaw2html
/usr/bin/mwaw2raw
/usr/bin/mwaw2svg
/usr/bin/mwaw2text
/usr/bin/mwawFile
/usr/bin/mwawZip

%files dev
%defattr(-,root,root,-)
/usr/include/libmwaw-0.3/libmwaw/MWAWDocument.hxx
/usr/include/libmwaw-0.3/libmwaw/libmwaw.hxx
/usr/lib64/libmwaw-0.3.so
/usr/lib64/pkgconfig/libmwaw-0.3.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libmwaw/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmwaw-0.3.so.3
/usr/lib64/libmwaw-0.3.so.3.0.18

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmwaw/6ec1f37ffe429f1cd0585eb50658a1877da1658b
/usr/share/package-licenses/libmwaw/98fc4d9117e318bd75af8a544c8a0238c3334186
