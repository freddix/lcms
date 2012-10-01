Summary:	Open source color management engine
Name:		lcms
Version:	1.19
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://heanet.dl.sourceforge.net/lcms/%{name}-%{version}.tar.gz
# Source0-md5:	8af94611baf20d9646c7c2c285859818
URL:		http://www.littlecms.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Little CMS intends to be a small-footprint color management engine,
with special focus on accuracy and performance. It uses the
International Color Consortium standard (ICC), which is the modern
standard when regarding to color management. The ICC specification is
widely used and is referred to in many International and other
de-facto standards. It was approved as an International Standard, ISO
15076-1, in 2005.

%package devel
Summary:	Little CMS - header files and developer's documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files needed to compile programs with liblcms and some
documentation useful for programmers.

%package progs
Summary:	Example and demonstration programs for Little CMS
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
Example and demonstration programs for Little CMS.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--without-python
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install samples/{icctrans,wtpt} tifficc/tifficc $RPM_BUILD_ROOT%{_bindir}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.1ST
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*

