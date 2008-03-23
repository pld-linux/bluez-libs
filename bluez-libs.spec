Summary:	Bluetooth libraries
Summary(pl.UTF-8):	Biblioteki Bluetooth
Name:		bluez-libs
Version:	3.29
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: http://www.bluez.org/download.html
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	7aeb26abb96c1b8d362f49d7b69bf88c
URL:		http://www.bluez.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.2-9
Conflicts:	bluez-sdp
ExcludeArch:	s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries for use in Bluetooth applications.

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%description -l pl.UTF-8
Biblioteki do używania w aplikacjach Bluetooth.

Znaki towarowe BLUETOOTH są własnością Bluetooth SIG, Inc. z USA.

%package devel
Summary:	Header files for Bluetooth applications
Summary(pl.UTF-8):	Pliki nagłówkowe dla aplikacji Bluetooth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	bluez-sdp-devel

%description devel
bluez-libs-devel contains header files for use in Bluetooth
applications.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do używania w aplikacjach
Bluetooth.

%package static
Summary:	Static Bluetooth libraries
Summary(pl.UTF-8):	Biblioteki statyczne Bluetooth
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	bluez-sdp-static

%description static
bluez-libs-static contains development static libraries for use in
Bluetooth applications.

%description static -l pl.UTF-8
Ten pakiet zawiera biblioteki statyczne, których można używaź do
aplikacji Bluetooth.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libbluetooth.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbluetooth.so
%{_libdir}/libbluetooth.la
%{_includedir}/bluetooth
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/bluez.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libbluetooth.a
