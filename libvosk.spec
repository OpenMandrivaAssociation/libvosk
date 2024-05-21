%define major 0
%define libname %mklibname vosk
%define devname %mklibname vosk -d

Name: libvosk
Version: 0.3.50
Release: 1
Source0: https://github.com/alphacep/vosk-api/archive/refs/tags/v%{version}.tar.gz
Summary: Speech recognition library
URL: https://github.com/alphacep/vosk-api
License: GPL
Group: System/Libraries
BuildRequires: %{mklibname -d fst}
BuildRequires: pkgconfig(lapack)
BuildRequires: pkgconfig(openblas)
BuildRequires: cmake(kaldi)
BuildSystem: cmake

%patchlist
libvosk-0.3.50-compile.patch

%description
Speech recognition library

%package -n %{libname}
Summary: Speech recognition library
Group: System/Libraries

%description -n %{libname}
Speech recognition library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep -a
sed -i -e 's,@LIBDIR@,%{_libdir},g' CMakeLists.txt
echo 'set_target_properties(vosk PROPERTIES VERSION %{version} SOVERSION 0)' >>CMakeLists.txt

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
