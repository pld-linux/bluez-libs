Summary: Bluetooth libraries
Name: bluez-libs
Version: 2.3
Release: 3
Copyright: GPL
Group: System Environment/Libraries
Source: http://bluez.sourceforge.net/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://bluez.sourceforge.net/
BuildRequires: glib-devel >= 1.2
ExcludeArch: s390 s390x

%description
Libraries for use in Bluetooth applications.

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%package devel
Summary: Development libraries for Bluetooth applications
Group: Development/Libraries
Requires: bluez-libs = %{version}

%description devel
bluez-libs-devel contains development libraries and headers for
use in Bluetooth applications.

%prep

%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README
%{_libdir}/libbluetooth.so.*

%files devel
%defattr(-,root,root)
/usr/include/bluetooth/*
%{_libdir}/libbluetooth.a
%{_libdir}/libbluetooth.so

%changelog
* Tue Feb 04 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add symlinks to shared libs

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan 16 2003 Bill Nottingham <notting@redhat.com> 2.3-1
- initial build
