Summary:	Bluetooth libraries
Name:		bluez-libs
Version:	2.3
Release:	3
License:	GPL v2
Group:		Libraries
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-CFLAGS.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://bluez.sourceforge.net/
BuildRequires:	glib-devel >= 1.2
ExcludeArch:	s390 s390x

%description
Libraries for use in Bluetooth applications.

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%package devel
Summary:	Development libraries for Bluetooth applications
Group:		Development/Libraries
Requires:	bluez-libs = %{version}

%description devel
bluez-libs-devel contains development libraries and headers for use in
Bluetooth applications.

%package static
Summary:	Development libraries for Bluetooth applications - static version
Group:		Development/Libraries
Requires:	bluez-libs-devel = %{version}

%description static
bluez-libs-static contains development static libraries for use in
Bluetooth applications.

%prep
%setup  -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_libdir}/libbluetooth.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/bluetooth/*
%{_libdir}/libbluetooth.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libbluetooth.a
