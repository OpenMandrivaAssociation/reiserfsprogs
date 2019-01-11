Summary:	The utilities to create reiserfs volumes
Name:		reiserfsprogs
Epoch:		1
Version:	3.6.27
Release:	1
License:	GPLv2 with exceptions
Group:		System/Kernel and hardware
Url:		https://www.kernel.org/pub/linux/kernel/people/jeffm/reiserfsprogs/
Source0:	https://mirrors.edge.kernel.org/pub/linux/kernel/people/jeffm/reiserfsprogs/v3.6.27/%{name}-%{version}.tar.xz
Patch1:		reiserfsprogs-3.6.2-make-the-force-option-works-in-resize_reiserfs.patch
BuildRequires:	pkgconfig(blkid)
%rename		reiserfs-utils

%description
This package contains tools for reiserfs filesystems.
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms.

%prep
%setup -q
%patch1 -p0 -b .force~

%build
%configure --sbindir=/sbin

#clang compat
echo '#define inline' >> include/config.h
%make

%install
rm -f %{buildroot}%{_mandir}/man8/*
%makeinstall_std

%files
%doc README
/sbin/*
%{_mandir}/*/*
