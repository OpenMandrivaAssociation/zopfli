%define major 1
%define libname %mklibname zopfli
%define pnglibname %mklibname zopflipng
%define devname %mklibname zopfli -d

%global optflags %{optflags} -O3

Name: zopfli
Version: 1.0.3
Release: 3
Source0: https://github.com/google/zopfli/archive/refs/tags/zopfli-%{version}.tar.gz
Summary: Library to perform very good but slow deflate (zlib) compression
URL: https://github.com/google/zopfli
License: Apache-2.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(zlib)

%description
Library to perform very good but slow deflate (zlib) compression.

%package -n %{libname}
Summary: Library to perform very good but slow deflate (zlib) compression
Group: System/Libraries

%description -n %{libname}
Library to perform very good but slow deflate (zlib) compression

%package -n %{pnglibname}
Summary: Library to perform very good but slow deflate (zlib) compression in PNGs
Group: System/Libraries

%description -n %{pnglibname}
Library to perform very good but slow deflate (zlib) compression in PNGs

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{pnglibname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Library to perform very good but slow deflate (zlib) compression.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libzopfli.so.%{major}*

%files -n %{pnglibname}
%{_libdir}/libzopflipng.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/Zopfli
