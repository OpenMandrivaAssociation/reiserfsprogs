%bcond_without	uclibc

Summary:	The utilities to create reiserfs volumes
Name:		reiserfsprogs
Epoch:		1
Version:	3.6.24
Release:	1
License:	GPLv2 with exceptions
Group:		System/Kernel and hardware
Url:		http://ftp.kernel.org/pub/linux/utils/fs/reiserfs/
Source0:	http://ftp.kernel.org/pub/linux/utils/fs/reiserfs/%{name}-%{version}.tar.xz
Patch1:		reiserfsprogs-3.6.2-make-the-force-option-works-in-resize_reiserfs.patch
BuildRequires:	pkgconfig(blkid)
%if %{with uclibc}
BuildRequires:	uClibc-devel >= 0.9.33.2-16
%endif
%rename		reiserfs-utils

%description
This package contains tools for reiserfs filesystems.
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms.

%package -n	uclibc-%{name}
Summary:	The utilities to create reiserfs volumes (uClibc build)
Group:		System/Kernel and hardware

%description -n	uclibc-%{name}
This package contains tools for reiserfs filesystems.
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms.

%prep
%setup -q
%patch1 -p0 -b .force~

%if %{with uclibc}
mkdir .uclibc
cp -a * .uclibc
%endif

%build
%if %{with uclibc}
pushd .uclibc
%uclibc_configure \
		--sbindir=%{uclibc_root}/sbin
%make
popd
%endif

%configure	--sbindir=/sbin
#clang compat
echo '#define inline' >> include/config.h
%make

%install
%if %{with uclibc}
%makeinstall_std -C .uclibc

%endif

rm -f %{buildroot}%{_mandir}/man8/*
%makeinstall_std

%files
%doc README ChangeLog
/sbin/*
%{_mandir}/*/*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}/sbin/*
%endif

