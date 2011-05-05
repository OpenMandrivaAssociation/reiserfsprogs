Summary:	The utilities to create reiserfs volumes
Name:		reiserfsprogs
Version:	3.6.21
Epoch:		1
Release:	%manbo_mkrel 2
License:	GPLv2 with exceptions
Group:		System/Kernel and hardware
Url:		http://ftp.kernel.org/pub/linux/utils/fs/reiserfs/
Source0:	http://ftp.kernel.org/pub/linux/utils/fs/reiserfs/%{name}-%{version}.tar.bz2
Patch1:		reiserfsprogs-3.6.2-make-the-force-option-works-in-resize_reiserfs.patch
Patch3:		reiserfsprogs-3.6.21-uuid.patch
BuildRequires:	libblkid-devel
Obsoletes:	reiserfs-utils
Provides:	reiserfs-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package contains tools for reiserfs filesystems.
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms.

%prep
%setup -q
%patch1 -p0 -b .make-the-force-option-works-in-resize_reiserfs
%patch3 -p1 -b .uuid

%build
%configure2_5x

%make OPTFLAGS="%{optflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}%{_mandir}/man8

%makeinstall_std

mv %{buildroot}/{usr/,}sbin
ln -s mkreiserfs %{buildroot}/sbin/mkfs.reiserfs
ln -s reiserfsck %{buildroot}/sbin/fsck.reiserfs
ln -s mkreiserfs.8 %{buildroot}%{_mandir}/man8/mkfs.reiserfs.8
ln -s reiserfsck.8 %{buildroot}%{_mandir}/man8/fsck.reiserfs.8

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) /sbin/*
%{_mandir}/*/*
