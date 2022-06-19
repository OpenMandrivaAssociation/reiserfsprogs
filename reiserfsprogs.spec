%global optflags %{optflags} -D_GNU_SOURCE

%define major 0
%define libname %mklibname %{name} %{major}
%define devel %mklibname %{name} -d

Summary:	The utilities to create reiserfs volumes
Name:		reiserfsprogs
Epoch:		1
Version:	3.6.27
Release:	2
License:	GPLv2 with exceptions
Group:		System/Kernel and hardware
Url:		https://www.kernel.org/pub/linux/kernel/people/jeffm/reiserfsprogs/
Source0:	https://www.kernel.org/pub/linux/kernel/people/jeffm/reiserfsprogs/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(com_err)
BuildRequires:	acl-devel
%rename		reiserfs-utils

%description
This package contains tools for reiserfs filesystems.
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms.

%package -n %{libname}
Summary:	The utilities to create reiserfs volumes
Group:		System/Kernel and hardware

%description -n %{libname}
This package contains tools for reiserfs filesystems.
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms.

%package -n %{devel}
Summary:	Development files for reiserfs
Group:		Development/C

%description -n %{devel}
This package contains tools for reiserfs filesystems.
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms.

%prep
%autosetup -p1

%build
%configure

#clang compat
echo '#define inline' >> include/config.h
%make_build

%install
rm -f %{buildroot}%{_mandir}/man8/*
%make_install

%files
%doc README
%{_sbindir}/*
%{_mandir}/*/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devel}
%{_includedir}/reiserfs/
%{_libdir}/*.so
%{_libdir}/pkgconfig/reiserfscore.pc
