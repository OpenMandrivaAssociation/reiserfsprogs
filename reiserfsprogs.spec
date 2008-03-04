Summary:	The utilities to create reiserfs volumes
Name:		reiserfsprogs
Version:	3.6.19
Epoch:		1
Release:	%manbo_mkrel 4
License:	GPLv2-like
Group:		System/Kernel and hardware
Url:		http://www.namesys.com/
Source0:	ftp://ftp.namesys.com/pub/reiserfsprogs/%{name}-%{version}.tar.bz2
Patch1:		reiserfsprogs-3.6.2-make-the-force-option-works-in-resize_reiserfs.patch
# From Ubuntu: avoid use of unaligned.h, which does not exist any more
Patch2:		reiserfsprogs-3.6.19-unaligned.patch
Patch3:		reiserfsprogs-3.6.19-uuid.patch
BuildRequires:	libext2fs-devel
Obsoletes:	reiserfs-utils
Provides:	reiserfs-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms. The results when
compared to the ext2fs conventional block allocation based file system
running under the same operating system and employing the same
buffering code suggest that these algorithms are overall more
efficient, and are becoming more so every passing month.

%prep
%setup -q
%patch1 -p1
%patch2 -p1 -b .unaligned
%patch3 -p1

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

