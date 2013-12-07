%bcond_without	uclibc

Summary:	The utilities to create reiserfs volumes
Name:		reiserfsprogs
Version:	3.6.21
Epoch:		1
Release:	9
License:	GPLv2 with exceptions
Group:		System/Kernel and hardware
Url:		http://ftp.kernel.org/pub/linux/utils/fs/reiserfs/
Source0:	http://ftp.kernel.org/pub/linux/utils/fs/reiserfs/%{name}-%{version}.tar.bz2
Patch1:		reiserfsprogs-3.6.2-make-the-force-option-works-in-resize_reiserfs.patch
Patch3:		reiserfsprogs-3.6.21-uuid.patch
%rename		reiserfs-utils
BuildRequires:	pkgconfig(blkid)
%if %{with uclibc}
BuildRequires:	uClibc-devel >= 0.9.33.2-16
%endif

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
%patch3 -p1 -b .uuid~

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

%configure2_5x	--sbindir=/sbin
%make

%install
%if %{with uclibc}
%makeinstall_std -C .uclibc

ln -s mkreiserfs %{buildroot}%{uclibc_root}/sbin/mkfs.reiserfs
ln -s reiserfsck %{buildroot}%{uclibc_root}/sbin/fsck.reiserfs
%endif

%makeinstall_std

ln -s mkreiserfs %{buildroot}/sbin/mkfs.reiserfs
ln -s reiserfsck %{buildroot}/sbin/fsck.reiserfs
ln -s mkreiserfs.8 %{buildroot}%{_mandir}/man8/mkfs.reiserfs.8
ln -s reiserfsck.8 %{buildroot}%{_mandir}/man8/fsck.reiserfs.8

%files
%doc README ChangeLog
/sbin/*
%{_mandir}/*/*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}/sbin/*
%endif
