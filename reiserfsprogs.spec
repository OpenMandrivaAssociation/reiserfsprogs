Summary:	The utilities to create Reiserfs volume
Name:		reiserfsprogs
Version:	3.6.19
Epoch:		1
Release:	%mkrel 2
License:	GPL
Group:		System/Kernel and hardware
Url:		http://www.namesys.com/
Source0:	ftp://ftp.namesys.com/pub/reiserfsprogs/%{name}-%{version}.tar.bz2
Patch1:		%{name}-3.6.2-make-the-force-option-works-in-resize_reiserfs.patch
Obsoletes:	reiserfs-utils
Provides:	reiserfs-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Reiserfs is a file system using a plug-in based object oriented
variant on classical balanced tree algorithms. The results when
compared to the ext2fs conventional block allocation based file system
running under the same operating system and employing the same
buffering code suggest that these algorithms are overall more
efficient, and are becoming more so every passing month.  Loosely
speaking, every month we find another performance cranny that needs
work, and we fix it, and every month we find some way of improving our
overall general usage performance. The improvement in small file space
and time performance suggests that we may now revisit a common OS
design assumption that one should aggregate small objects using layers
above the file system layer. Being more effective at small files DOES
NOT make us less effective for other files, this is a general purpose
FS, and our overall traditional FS usage performance is high enough to
establish that. Reiserfs has a commitment to opening up the FS design
to contributions, and we are now now adding plug-ins so that you can
create your own types of directories and files.

%prep
%setup -q
%patch1 -p1

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
%doc README ChangeLog COPYING
%attr(755,root,root) /sbin/*
%{_mandir}/*/*


