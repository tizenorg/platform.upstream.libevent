Name:           libevent
Version:        2.0.20
Release:        0
Summary:        Library Providing an Event Handling API
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://monkey.org/~provos/libevent/
Source0:        http://monkey.org/~provos/libevent-%{version}-stable.tar.gz
Source1:        baselibs.conf 
Source1001: 	libevent.manifest
BuildRequires:  pkgconfig

%description
The libevent library provides a mechanism to execute a function when a
specific event on a file descriptor occurs or after a given time has
passed.


%package devel
Summary:        Development files for libevent2
Group:          Development/Libraries/C and C++
Requires:       %name = %{version}
Requires:       glibc-devel
Provides:       %{name}:/usr/include/event.h

%description devel
The libevent library provides a mechanism to execute a function when a
specific event on a file descriptor occurs or after a given time has
passed.

This package holds the development files for libevent2.

%prep
%setup -q  -n %{name}-%{version}-stable
cp %{SOURCE1001} .

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%make_install

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/%{name}-2.0.so.5*
%{_libdir}/%{name}_core-2.0.so.5*
%{_libdir}/%{name}_extra-2.0.so.5*
%{_libdir}/%{name}_pthreads-2.0.so.5*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_bindir}/event_rpcgen.py
%{_includedir}/*.h
%{_includedir}/event2
%{_libdir}/%{name}.so
%{_libdir}/%{name}_core.so
%{_libdir}/%{name}_extra.so
%{_libdir}/%{name}_pthreads.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}_pthreads.pc

%changelog
