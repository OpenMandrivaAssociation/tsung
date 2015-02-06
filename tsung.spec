Summary:	A distributed multi-protocol load testing tool
Name:		tsung
Version:	1.4.2
Release:	2
License:	GPLv2
Group:		Development/Other
Url:		http://tsung.erlang-projects.org/
Source0:	http://tsung.erlang-projects.org/dist/%{name}-%{version}.tar.gz
Patch0:		tsung-1.3.1-destdir.patch
BuildRequires:	erlang-devel
BuildRequires:	erlang-xmerl
BuildRequires:	erlang-ssl
BuildRequires:	erlang-crypto
BuildRequires:	erlang-compiler
BuildRequires:	erlang-snmp
BuildRequires:	erlang-eunit
Requires:	erlang-xmerl
Requires:	erlang-ssl
Requires:	erlang-crypto
Requires:	erlang-snmp

%description
It is protocol-independent and can currently be used to stress and
benchmark HTTP, Jabber/XMPP, PostgreSQL, MySQL and LDAP servers.
It simulates user behaviour using an XML description file, reports
many measurements in real time (statistics can be customized with
transactions, and graphics generated using gnuplot).
For HTTP, it supports 1.0 and 1.1, has a proxy mode to record
sessions, supports GET and POST methods, Cookies, and Basic
WWW-authentication. It also has support for SSL.

%prep
%setup -q %{name}-%{version}
#%patch0 -p1

%build
# (tpg) needed by patch0
autoreconf -fiv
%configure2_5x

%make

%install
%makeinstall_std

rm -rf %{buildroot}%{_docdir}/%{name}

%files
%doc examples/* doc/*
%doc CHANGES CONTRIBUTORS README TODO
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/erlang/lib/%{name}*
%{_datadir}/%{name}
%{_mandir}/man1/t*


%changelog
* Tue Mar 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4.2-1
+ Revision: 782463
- version update 1.4.2

* Sun Aug 22 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.3-1mdv2011.0
+ Revision: 571977
- update to new version 1.3.3

* Mon Aug 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.2-1mdv2011.0
+ Revision: 570612
- add buildrequires on erlang-eunit
- update to new version 1.3.2

* Tue Feb 23 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.1-1mdv2010.1
+ Revision: 510316
- restrict to max two jobs
- import tsung

