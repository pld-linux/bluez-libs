Summary:	Bluetooth libraries
Summary(pl):	Biblioteki Bluetooth
Name:		bluez-libs
Version:	2.3
Release:	3
License:	GPL v2
Group:		Libraries
Source0:	http://bluez.sourceforge.net/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-CFLAGS.patch
URL:		http://bluez.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2
BuildRequires:	libtool
ExcludeArch:	s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries for use in Bluetooth applications.

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%description -l pl
Biblioteki do u¿ywania w aplikacjach Bluetooth.

Znaki towarowe BLUETOOTH s± w³asno¶ci± Bluetooth SIG, Inc. z USA.

%package devel
Summary:	Header files for Bluetooth applications
Summary(pl):	Pliki nag³ówkowe dla aplikacji Bluetooth
Group:		Development/Libraries
Requires:	bluez-libs = %{version}

%description devel
bluez-libs-devel contains header files for use in Bluetooth
applications.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe do u¿ywania w aplikacjach
Bluetooth.

%package static
Summary:	Static Bluetooth libraries
Summary(pl):	Biblioteki statyczne Bluetooth
Group:		Development/Libraries
Requires:	bluez-libs-devel = %{version}

%description static
bluez-libs-static contains development static libraries for use in
Bluetooth applications.

%description static -l pl
Ten pakiet zawiera biblioteki statyczne, których mo¿na u¿ywa¼ do
aplikacji Bluetooth.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libbluetooth.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbluetooth.so
%{_libdir}/libbluetooth.la
%{_includedir}/bluetooth

%files static
%defattr(644,root,root,755)
%{_libdir}/libbluetooth.a
