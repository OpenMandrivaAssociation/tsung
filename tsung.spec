Summary:	A distributed multi-protocol load testing tool
Name:		tsung
Version:	1.3.1
Release:	%mkrel 1
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
Requires:	erlang-xmerl
Requires:	erlang-ssl
Requires:	erlang-crypto
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%patch0 -p1

%build
# (tpg) needed by patch0
autoreconf -fiv
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc examples/* doc/*
%doc CHANGES CONTRIBUTORS README TODO
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/erlang/lib/%{name}*
%{_datadir}/%{name}
%{_mandir}/man1/t*
