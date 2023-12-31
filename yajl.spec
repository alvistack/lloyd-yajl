# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

Name: yajl
Epoch: 100
Version: 2.1.0
Release: 1%{?dist}
Summary: Yet Another JSON Library
License: ISC
URL: https://github.com/pybind/pybind11/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: make
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150000
Requires: libyajl2 = %{epoch}:%{version}-%{release}
%endif

%description
A small, fast library for parsing JavaScript Object Notation (JSON). It
supports incremental parsing from a stream and leaves data
representation to higher level code.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%cmake
%cmake_build

%install
%cmake_install

%check

%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150000
%package -n libyajl2
Summary: Yet Another JSON Library
Group: System/Libraries

%description -n libyajl2
YAJL is a small event-driven (SAX-style) JSON parser written in ANSI C, and a
small validating JSON generator.

%package -n libyajl-devel
Summary: Yet Another JSON Library (Development Environment)
Group: Development/Libraries/C and C++
Requires: libyajl2 = %{epoch}:%{version}-%{release}

%description -n libyajl-devel
This package provides the necessary environment for compiling and linking
against yajl.

%package -n libyajl-devel-static
Summary: Yet Another JSON Library (Static Library)
Group: Development/Libraries/C and C++
Requires: libyajl-devel = %{epoch}:%{version}-%{release}

%description -n libyajl-devel-static
This package provides the necessary environment for linking statically
against yajl.

%post -n libyajl2 -p /sbin/ldconfig
%postun -n libyajl2 -p /sbin/ldconfig

%files -n libyajl2
%license COPYING
%{_libdir}/*.so.*

%files -n libyajl-devel
%{_includedir}/yajl
%{_libdir}/*.so
%{_libdir}/pkgconfig/yajl.pc

%files -n libyajl-devel-static
%{_libdir}/*.a

%files
%{_bindir}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package devel
Summary: Libraries, includes, etc to develop with YAJL
Requires: yajl = %{epoch}:%{version}-%{release}

%description devel
This package contains the header files and static libraries needed for
compiling software that uses the yajl library.

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%dir %{_includedir}/yajl
%{_includedir}/yajl/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/yajl.pc
%endif

%changelog
