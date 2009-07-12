#
# Conditional build:
%bcond_without	doc             # without documentation which needed TeX
%bcond_without	tcl		# build without tcl (tcl is needed for tests)
%bcond_without	openldap	# don't build openldap plugin
%bcond_with	selinux		# build with selinux support
%bcond_without	tests		# don't perform make check
#
Summary:	Kerberos V5 System
Summary(pl.UTF-8):	System Kerberos V5
Name:		krb5
Version:	1.7
Release:	4
License:	MIT
Group:		Networking
Source0:	http://web.mit.edu/kerberos/dist/krb5/1.7/%{name}-%{version}-signed.tar
# Source0-md5:	9f7b3402b4731a7fa543db193bf1b564
Source2:	%{name}kdc.init
Source4:	kadm5.acl
Source5:	kerberos.logrotate
Source6:	%{name}.conf
Source7:	kdc.conf
Source8:	kerberos.sysconfig
Source9:	kerberos.sh
Source10:	kerberos.csh
Source11:	klogind.inetd
Source12:	kftpd.inetd
Source13:	ktelnetd.inetd
Source14:	kshell.inetd
Source15:	propagation
Source16:	kpropd.init
Source17:	kadmind.init
Source18:	kpropd.acl
Source19:	kftpd.pamd
Source20:	klogin.pamd
Source21:	kshell.pamd
Patch0:		%{name}-manpages.patch
Patch1:		%{name}-netkit-rsh.patch
Patch2:		%{name}-rlogind-environ.patch
Patch3:		%{name}-ksu-access.patch
Patch4:		%{name}-ksu-path.patch
Patch5:		%{name}-passive.patch
# http://lite.mit.edu/
Patch6:		%{name}-ktany.patch
Patch7:		%{name}-size.patch
Patch8:		%{name}-ftp-glob.patch
Patch9:		%{name}-paths.patch
Patch10:	%{name}-autoconf.patch
Patch11:	%{name}-brokenrev.patch
Patch12:	%{name}-dns.patch
Patch13:	%{name}-enospc.patch
Patch14:	%{name}-io.patch
Patch15:	%{name}-kprop-mktemp.patch
Patch16:	%{name}-login-lpass.patch
Patch17:	%{name}-rcp-markus.patch
Patch18:	%{name}-rcp-sendlarge.patch
Patch19:	%{name}-send-pr-tempfile.patch
Patch20:	%{name}-telnet-environ.patch
Patch21:	%{name}-as-needed.patch
Patch22:	%{name}-doc.patch
Patch23:	%{name}-tests.patch
Patch24:	%{name}-config.patch
Patch25:	%{name}-ftp_fdleak.patch
Patch26:	%{name}-ftp_glob_runique.patch
Patch27:	%{name}-key_exp.patch
Patch28:	%{name}-pam.patch
Patch29:	%{name}-selinux-label.patch
Patch200:	%{name}-trunk-doublelog.patch
Patch201:	%{name}-trunk-ftp_mget_case.patch
Patch202:	%{name}-trunk-kpasswd_tcp.patch
URL:		http://web.mit.edu/kerberos/www/
BuildRequires:	/bin/csh
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
# for bindir/mk_cmds
BuildRequires:	e2fsprogs
BuildRequires:	e2fsprogs-devel >= 1.35
BuildRequires:	flex
BuildRequires:	ghostscript
BuildRequires:	keyutils-devel
BuildRequires:	ncurses-devel
%{?with_openldap:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	pam-devel
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	rpmbuild(macros) >= 1.268
%{?with_tcl:BuildRequires:	tcl-devel}
%if %{with doc}
BuildRequires:	texinfo
%if "%{pld_release}" == "ti"
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-latex
BuildRequires:	tetex-makeindex
%else
BuildRequires:	texlive-latex
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-makeindex
BuildRequires:	texlive-xetex
%endif
%endif
BuildRequires:	words
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib/kerberos
# doesn't handle %{__cc} with spaces properly
%undefine	with_ccache
# mungles cflags
%undefine	configure_cache

%define		schemadir	/usr/share/openldap/schema

%description
Kerberos V5 is based on the Kerberos authentication system developed
at MIT. Under Kerberos, a client (generally either a user or a
service) sends a request for a ticket to the Key Distribution Center
(KDC). The KDC creates a "ticket-granting ticket" (TGT) for the
client, encrypts it using the client's password as the key, and sends
the encrypted TGT back to the client. The client then attempts to
decrypt the TGT, using its password. If the client successfully
decrypts the TGT (i.e., if the client gave the correct password), it
keeps the decrypted TGT, which indicates proof of the client's
identity.

%description -l pl.UTF-8
Kerberos V5 jest systemem uwierzytelniania rozwijanym w MIT. W tym
systemie klient (użytkownik lub usługa) wysyła żądanie biletu do
Centrum Dystrybucji Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT),
używając hasła klienta do jego zaszyfrowania i wysyła go z powrotem do
klienta. Klient następnie przystępuje do rozkodowywania kredytu przy
pomocy swojego hasła. Jeżeli zrobi to prawidłowo (tzn. poda poprawne
hasło), jego bilet uaktywnia się i będzie ważny na daną usługę.

%package common
Summary:	Common files required by Kerberos V5 servers and workstations
Summary(pl.UTF-8):	Wspólne pliki dla serwerów i klientów kerberosa
Group:		Networking
Requires:	%{name}-libs = %{version}-%{release}
Requires:	rc-scripts
Requires:	setup >= 2.4.6-2

%description common
Common configuration files, directories and programs required
for Kerberos V5 servers and clients.

Kerberos V5 is based on the Kerberos authentication system developed
at MIT. Under Kerberos, a client (generally either a user or a
service) sends a request for a ticket to the Key Distribution Center
(KDC). The KDC creates a "ticket-granting ticket" (TGT) for the
client, encrypts it using the client's password as the key, and sends
the encrypted TGT back to the client. The client then attempts to
decrypt the TGT, using its password. If the client successfully
decrypts the TGT (i.e., if the client gave the correct password), it
keeps the decrypted TGT, which indicates proof of the client's
identity.

%description common -l pl.UTF-8
Wspólne pliki konfiguracyjne, katalogi i programy niezbędne do
działania serwerów i klientów systemu Kerberos V5.

Kerberos V5 jest systemem uwierzytelniania rozwijanym w MIT. W tym
systemie klient (użytkownik lub usługa) wysyła żądanie biletu do
Centrum Dystrybucji Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT),
używając hasła klienta do jego zaszyfrowania i wysyła go z powrotem do
klienta. Klient następnie przystępuje do rozkodowywania kredytu przy
pomocy swojego hasła. Jeżeli zrobi to prawidłowo (tzn. poda poprawne
hasło), jego bilet uaktywnia się i będzie ważny na daną usługę.

%package client
Summary:	Kerberos V5 programs for use on workstations
Summary(pl.UTF-8):	Oprogramowanie klienckie dla stacji roboczej kerberosa
Group:		Networking
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Conflicts:	heimdal

%description client
Kerberos V5 Clients.

Kerberos V5 is based on the Kerberos authentication system developed
at MIT. Under Kerberos, a client (generally either a user or a
service) sends a request for a ticket to the Key Distribution Center
(KDC). The KDC creates a "ticket-granting ticket" (TGT) for the
client, encrypts it using the client's password as the key, and sends
the encrypted TGT back to the client. The client then attempts to
decrypt the TGT, using its password. If the client successfully
decrypts the TGT (i.e., if the client gave the correct password), it
keeps the decrypted TGT, which indicates proof of the client's
identity.

%description client -l pl.UTF-8
Oprogramowanie klienckie do korzystania z usług systemu Kerberos V5.

Kerberos V5 jest systemem uwierzytelniania rozwijanym w MIT. W tym
systemie klient (użytkownik lub usługa) wysyła żądanie biletu do
Centrum Dystrybucji Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT),
używając hasła klienta do jego zaszyfrowania i wysyła go z powrotem do
klienta. Klient następnie przystępuje do rozkodowywania kredytu przy
pomocy swojego hasła. Jeżeli zrobi to prawidłowo (tzn. poda poprawne
hasło), jego bilet uaktywnia się i będzie ważny na daną usługę.

%package server
Summary:	Kerberos V5 Server
Summary(pl.UTF-8):	Serwer Kerberos V5
Group:		Networking
Requires(post,postun):	sed >= 4.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires:	words
Conflicts:	heimdal-server

%description server
Common files required by Kerberos 5 servers.

Kerberos V5 is based on the Kerberos authentication system developed
at MIT. Under Kerberos, a client (generally either a user or a
service) sends a request for a ticket to the Key Distribution Center
(KDC). The KDC creates a "ticket-granting ticket" (TGT) for the
client, encrypts it using the client's password as the key, and sends
the encrypted TGT back to the client. The client then attempts to
decrypt the TGT, using its password. If the client successfully
decrypts the TGT (i.e., if the client gave the correct password), it
keeps the decrypted TGT, which indicates proof of the client's
identity.

%description server -l pl.UTF-8
Wspólne pliki wymagane przez usługi serwerowe Kerberos 5.

Kerberos V5 jest systemem uwierzytelniania rozwijanym w MIT. W tym
systemie klient (użytkownik lub usługa) wysyła żądanie biletu do
Centrum Dystrybucji Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT),
używając hasła klienta do jego zaszyfrowania i wysyła go z powrotem do
klienta. Klient następnie przystępuje do rozkodowywania kredytu przy
pomocy swojego hasła. Jeżeli zrobi to prawidłowo (tzn. poda poprawne
hasło), jego bilet uaktywnia się i będzie ważny na daną usługę.

%package server-kdc
Summary:	Kerberos V5 AS/KDC Server
Summary(pl.UTF-8):	Serwer AS/KDC Kerberos V5
Group:		Networking
Requires:	%{name}-server = %{version}-%{release}

%description server-kdc
This package constains the Kerberos version 5 Authentication Service
and Key Distribution Center (AS/KDC).

%description server-kdc -l pl.UTF-8
Ten pakiet zawiera usługę uwierzytelniającą Kerberosa 5 i centrum
dystrybucji kluczy (AS/KDC).

%package server-kadmind
Summary:	Kerberos V5 administration server
Summary(pl.UTF-8):	Serwer administracyjny Kerberos V5
Group:		Networking
Requires:	%{name}-server = %{version}-%{release}

%description server-kadmind
This package contains the KADM5 administration server.

If the database is db2, the administration server runs on the master
Kerberos server, which stores the KDC principal database and the KADM5
policy database.

If the database is LDAP, the administration server and the KDC server
need not run on the same machine.

Kadmind accepts remote requests to administer the information in these
databases. Remote requests are sent, for example, by kadmin(8) and the
kpasswd(1) command, both of which are clients of kadmind.

%description server-kadmind -l pl.UTF-8
Ten pakiet zawiera serwer administracyjny KADM5.

Jeżeli baza Kerberosa jest w formacie db2, serwer administracyjny jest
uruchamiany na głównym serwerze kerberosa, który utrzymuje bazę kluczy
KDC i KADM5.

Jeżeli baza Kerberosa jest w formacie LDAP, serwer administracyjny
może być uruchomiony na innej maszynie niż KDC.

Kadmind przyjmuje zdalne zlecenia administracyjne dla wyżej
wymienionych baz. Zdalne zlecenia są wysyłane na przykład przez
programy kadmin i kpasswd, które są klientami kadmind.

%package server-kpropd
Summary:	Kerberos V5 slave KDC update server
Summary(pl.UTF-8):	Podporządkowany serwer KDC Kerberos V5
Group:		Networking
Requires:	%{name}-server-kdc = %{version}-%{release}

%description server-kpropd
kpropd is a slave KDC update server which accepts connections from the
kprop program from the master KDC and updates the KDC database running
on the slave server.

Thus, the master Kerberos server can use kprop(8) to propagate its
database to the slave slavers. Upon a successful download of the KDC
database file, the slave Kerberos server will have an up-to-date KDC
database.
					  
%description server-kpropd -l pl.UTF-8
kpropd jest podporządkowanym serwerem odświerzającym KDC przyjmującym
połączenia od programu prop z nadrzędnego KDC i uaktualniającego bazę
danych KDC działającą na serwerze podporządkowanym.

W ten sposób nadrzędny serwer Kerberosa może używać kprop(8) do
propagowania swojej bazy danych na serwery podporządkowane. Po
pomyślnym ściągnięciu pliku bazy KDC podrzędny serwer Kerberosa będzie
zawierał aktualną bazę KDC.

%package server-ldap
Summary:	The LDAP storage plugin for the Kerberos 5 KDC
Summary(pl.UTF8):	Wtyczka przechowywania danych w LDAP dla KDC Kerberosa 5
Group:		Networking
Requires:	%{name}-server-kdc = %{version}-%{release}

%description server-ldap
Kerberos is a network authentication system. The krb5-server package
contains the programs that must be installed on a Kerberos 5 key
distribution center (KDC). If you are installing a Kerberos 5 KDC,
and you wish to use a directory server to store the data for your
realm, you need to install this package.

%description server-ldap -l pl.UTF-8
Kerberos to system uwierzytelniania sieciowego. Pakiet krb5-server
zawiera programy, które muszą być zainstalowane w centrum dystrybucji
kluczy Kerberosa 5 (KDC). W przypadku instalacji KDC Kerberosa 5 z
użyciem serwera usług katalogowych do przechowywania danych należy
zainstalować ten pakiet.

%package -n openldap-schema-krb5
Summary:	Kerberos LDAP schema
Summary(pl.UTF-8):	Schemat LDAP dla kerberosa
Group:		Networking/Daemons
Requires(post,postun):	sed >= 4.0
Requires:	openldap-servers

%description -n openldap-schema-krb5
This package contains kerberos LDAP schema for openldap.

%description -n openldap-schema-krb5 -l pl.UTF-8
Ten pakiet zawiera schemat kerberosa dla openldap-a.

%package ftpd
Summary:	The standard UNIX FTP (file transfer protocol) server
Summary(pl.UTF-8):	Serwer FTP
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	ftpd
Conflicts:	heimdal-ftpd

%description ftpd
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

%description ftpd -l pl.UTF-8
FTP jest protokołem transmisji plików szeroko rozpowszechnionym w
Internecie.

%package kshd
Summary:	Kerberized remote shell server
Summary(pl.UTF-8):	Skerberyzowany serwer zdalnego dostępu
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	rshd
Conflicts:	heimdal-rshd

%description kshd
The kshd package contains kerberized remote shell server which
provides remote execution facilities with authentication based on the
Kerberos authentication system.

%description kshd -l pl.UTF-8
Ten pakiet zawiera skerberyzowaną wersję serwer zdalnego dostępu,
który umożliwia zdalne wykonywanie poleceń w oparciu o system
uwierzytelniania Kerberos.

%package telnetd
Summary:	Server for the telnet remote login
Summary(pl.UTF-8):	Serwer protokołu telnet
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	telnetd
Obsoletes:	heimdal-telnetd

%description telnetd
Telnet is a popular protocol for remote logins across the Internet.
This package provides a telnet daemon which allows remote logins into
the machine it is running on.

%description telnetd -l pl.UTF-8
Telnet jest popularnym protokołem zdalnego logowania. Ten pakiet
zawiera serwer pozwalający na zdalne logowanie się klientów na maszynę
na której działa.

%package klogind
Summary:	Remote login server
Summary(pl.UTF-8):	Serwer zdalnego logowania
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	rlogind

%description klogind
Klogind is the server for the rlogin program. The server is based on
rlogind but uses Kerberos authentication.

%description klogind -l pl.UTF-8
Klogind jest serwerem dla programu rlogin. Oparty jest na rlogind ale
wykorzystuje system uwierzytelniania Kerberos.

%package rlogin
Summary:	rlogin is used when signing onto a system
Summary(pl.UTF-8):	Narzędzie do logowania w systemie
Group:		Networking
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Provides:	rlogin

%description rlogin
login is used when signing onto a system. It can also be used to
switch from one user to another at any time (most modern shells have
support for this feature built into them, however). This package
contain kerberized version login program.

%description rlogin -l pl.UTF-8
login jest używany przy logowaniu do systemu. Może być także użyty do
przełączenia z jednego użytkownika na innego w dowolnej chwili
(większość współczesnych shelli ma wbudowaną obsługę tego). Ten pakiet
zawiera skerberyzowaną wersję programu rlogin.

%package rsh
Summary:	Clients for remote access commands (rsh, rlogin, rcp)
Summary(pl.UTF-8):	Klient zdalnego dostępu (rsh, rlogin, rcp)
Group:		Applications/Networking
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	rcp
Obsoletes:	rsh
Obsoletes:	heimdal-rsh

%description rsh
The rsh package contains a set of programs which allow users to run
commands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp). All three of these commands
use rhosts style authentication. This package contains the clients
needed for all of these services.

%description rsh -l pl.UTF-8
Ten pakiet zawiera zestaw narzędzi pozwalających na wykonywanie
poleceń na zdalnych maszynach, logowanie na inne maszyny oraz
kopiowanie plików pomiędzy maszynami (rsh, rlogin, rcp).

%package ftp
Summary:	The standard UNIX FTP (file transfer protocol) client
Summary(pl.UTF-8):	Klient protokołu FTP
Group:		Networking
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	heimdal-ftp

%description ftp
The ftp package provides the standard UNIX command-line FTP client
with kerberos authentication support. FTP is the file transfer
protocol, which is a widely used Internet protocol for transferring
files and for archiving files.

%description ftp -l pl.UTF-8
Ten pakiet dostarcza standardowego klienta FTP z wbudowaną obsługą
kerberosa. FTP jest protokołem do przesyłania plików szeroko
rozpowszechnionym w Internecie.

%package telnet
Summary:	Client for the telnet remote login
Summary(pl.UTF-8):	Klient usługi telnet
Group:		Networking
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	telnet
Obsoletes:	heimdal-telnet

%description telnet
Telnet is a popular protocol for remote logins across the Internet.
This package provides a command line telnet client.

%description telnet -l pl.UTF-8
Telnet jest popularnym protokołem zdalnego logowania. Ten pakiet
zawiera klienta tej usługi.

%package libs
Summary:	Kerberos V5 shared libraries
Summary(pl.UTF-8):	Biblioteki dzielone dla Kerberosa V5
Group:		Libraries
Requires(post):	/sbin/ldconfig
Requires(post,preun):	grep
Requires(preun):	coreutils
Obsoletes:	krb5-configs
Obsoletes:	krb5-lib
Conflicts:	heimdal-libs < 0.8-0.rc7.2

%description libs
Libraries for Kerberos V5 Server and Client

%description libs -l pl.UTF-8
Biblioteki dynamiczne dla systemu Kerberos V5.

%package devel
Summary:	Header files for Kerberos V5 libraries and documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do bibliotek Kerberosa V5
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	keyutils-devel
Requires:	libcom_err-devel
Conflicts:	heimdal-devel

%description devel
Header files for Kerberos V5 libraries and development documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek Kerberosa V5.

%package static
Summary:	Static Kerberos V5 libraries
Summary(pl.UTF-8):	Biblioteki statyczne Kerberosa V5
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Kerberos V5 libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Kerberosa V5.

%prep
%setup -q -c
tar xf %{name}-%{version}.tar.gz
mv %{name}-%{version}/* .
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%{?with_selinux:%patch29 -p1}

%patch200 -p0
%patch201 -p0
%patch202 -p0

%build
cd src
# Get LFS support on systems that need it which aren't already 64-bit.
%ifarch %{ix86} s390 ppc sparc
CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -fPIC -I%{_includedir}/et -I%{_includedir}/ncurses"
CPPFLAGS="-D_FILE_OFFSET_BITS=64 -I%{_includedir}/et -I%{_includedir}/ncurses"
%else
CFLAGS="%{rpmcflags} -fPIC -I%{_includedir}/et -I%{_includedir}/ncurses"
CPPFLAGS="-I%{_includedir}/et -I%{_includedir}/ncurses"
%endif

top=`pwd`
for configurein in `find -name configure.in -type f` ; do
	cd `dirname $configurein`
	grep -q A._CONFIG_HEADER configure.in && %{__autoheader} -I "$top"
	%{__autoconf} -I "$top"
	cd $top
done

%configure \
	CC=%{__cc} \
	CFLAGS="$CFLAGS" \
	CPPFLAGS="$CPPFLAGS" \
	%{?with_openldap:OPENLDAP_PLUGIN=yes} \
	%{!?with_openldap:OPENLDAP_PLUGIN=""} \
	%{?with_selinux:--with-selinux} \
	--libexecdir=%{_libdir} \
	--enable-shared \
	--disable-rpath \
	--enable-dns \
	--enable-dns-for-kdc \
	--enable-dns-for-realm \
	--with-netlib=-lresolv \
	%{?with_tcl:--with-tcl=%{_prefix}} \
	%{!?with_tcl:--without-tcl} \
	--with-system-et \
	--with-system-ss

%{__make}

cd ../doc
%if %{with doc}
%{__make}
%{__make} -C api
%{__make} -C implement
%{__make} -C kadm5
%endif

%{?with_tests:%{__make} -j1 -C ../src check SKIP_NET_TESTS=1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_localstatedir},/var/log/kerberos} \
	$RPM_BUILD_ROOT{%{schemadir},%{_infodir},%{_mandir}} \
	$RPM_BUILD_ROOT/etc/{pam.d,rc.d/init.d,sysconfig/rc-inetd,shrc.d,logrotate.d}

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE7} $RPM_BUILD_ROOT%{_localstatedir}/krb5kdc
install %{SOURCE4} $RPM_BUILD_ROOT%{_localstatedir}/krb5kdc
install %{SOURCE18} $RPM_BUILD_ROOT%{_localstatedir}/krb5kdc
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/kerberos
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/kerberos
install %{SOURCE15} $RPM_BUILD_ROOT%{_sbindir}/propagation
install %{SOURCE9} %{SOURCE10} $RPM_BUILD_ROOT/etc/shrc.d

install %{SOURCE11} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/klogind
install %{SOURCE12} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install %{SOURCE13} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnetd
install %{SOURCE14} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/kshd

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/krb5kdc
install %{SOURCE16} $RPM_BUILD_ROOT/etc/rc.d/init.d/kpropd
install %{SOURCE17} $RPM_BUILD_ROOT/etc/rc.d/init.d/kadmind

install %{SOURCE19} $RPM_BUILD_ROOT/etc/pam.d/kftpd
install %{SOURCE20} $RPM_BUILD_ROOT/etc/pam.d/klogin
install %{SOURCE21} $RPM_BUILD_ROOT/etc/pam.d/kshell

%if %{with openldap}
install src/plugins/kdb/ldap/libkdb_ldap/kerberos.{schema,ldif} $RPM_BUILD_ROOT%{schemadir}
%endif

ln -sf %{_datadir}/dict/words $RPM_BUILD_ROOT%{_localstatedir}/krb5kdc/kadm5.dict
touch $RPM_BUILD_ROOT/etc/krb5.keytab

echo .so kadmin.8 > $RPM_BUILD_ROOT%{_mandir}/man8/kadmin.local.8

rm -rf $RPM_BUILD_ROOT%{_includedir}/asn.1

# fix permissions for deps generation
find $RPM_BUILD_ROOT -type f -name '*.so*' -exec chmod +x "{}" ";"

%clean
rm -rf $RPM_BUILD_ROOT

%post server-kdc
/sbin/chkconfig --add krb5kdc
%service krb5kdc restart "krb5kdc daemon"

%post server-kadmind
/sbin/chkconfig --add kadmind
%service kadmind restart "kadmind daemon"

%post server-kpropd
/sbin/chkconfig --add kpropd
%service kpropd restart "kpropd daemon"

%postun server-kdc
if [ "$1" = 0 ]; then
	%service krb5kdc stop
	/sbin/chkconfig --del krb5kdc
fi

%postun server-kadmind
if [ "$1" = 0 ]; then
	%service kadmind stop
	/sbin/chkconfig --del kadmind
fi

%postun server-kpropd
if [ "$1" = 0 ]; then
	%service kpropd stop
	/sbin/chkconfig --del kpropd
fi

%post ftpd
%service -q rc-inetd reload

%postun ftpd
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post kshd
%service -q rc-inetd reload

%postun kshd
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post telnetd
%service -q rc-inetd reload

%postun telnetd
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post klogind
%service -q rc-inetd reload

%postun klogind
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post -n openldap-schema-krb5
%openldap_schema_register %{schemadir}/kerberos.schema
%service -q ldap restart

%postun -n openldap-schema-krb5
if [ "$1" = "0" ]; then
	%openldap_schema_unregister %{schemadir}/kerberos.schema
	%service -q ldap restart
fi

%triggerpostun server -- krb5-server < 1.7
for f in principal .k5.* krb5_adm.acl kadm_old.acl kadm5.keytab; do
	if [ -f %{_localstatedir}/$f.rpmsave ]; then
		if [ -f %{_localstatedir}/krb5kdc/$f ]; then
			mv %{_localstatedir}/krb5kdc/$f{,.rpmnew}
		fi
		mv -f %{_localstatedir}/$f.rpmsave %{_localstatedir}/krb5kdc/$f
	fi
done
cp -f /etc/sysconfig/kerberos{,.rpmorig}
%{__sed} -i -e "s,/var/lib/kerberos/principal,/var/lib/kerberos/krb5kdc/principal," \
	-e "s,/var/lib/kerberos/kpropd.acl,/var/lib/kerberos/krb5kdc/kpropd.acl," \
	-e "s,/var/lib/kerberos/kadm5.keytab,/var/lib/kerberos/krb5kdc/kadm5.keytab," \
	/etc/sysconfig/kerberos

%triggerpostun server-kdc -- krb5-server-kdc < 1.7
if [ -f %{_localstatedir}/kdc.conf.rpmsave ]; then
	mv %{_localstatedir}/krb5kdc/kdc.conf{,.rpmnew}
	mv -f %{_localstatedir}/kdc.conf.rpmsave %{_localstatedir}/krb5kdc/kdc.conf
fi

%triggerpostun server-kadmind -- krb5-server-kadmind < 1.7
if [ -f %{_localstatedir}/kadm5.acl.rpmsave ]; then
	mv %{_localstatedir}/krb5kdc/kadm5.acl{,.rpmnew}
	mv -f %{_localstatedir}/kadm5.acl.rpmsave %{_localstatedir}/krb5kdc/kadm5.acl
fi

%triggerpostun server-kpropd -- krb5-server-kpropd < 1.7
for f in slave_datatrans from_master kpropd.acl; do
	if [ -f %{_localstatedir}/$f.rpmsave ]; then
		if [ -f %{_localstatedir}/krb5kdc/$f ]; then
			mv %{_localstatedir}/krb5kdc/$f{,.rpmnew}
		fi
		mv -f %{_localstatedir}/$f.rpmsave %{_localstatedir}/krb5kdc/$f
	fi
done

%triggerpostun common -- krb5-common < 1.7
if [ -f %{_localstatedir}/krb5.keytab.rpmsave ]; then
	mv /etc/krb5.keytab{,.rpmnew}
	mv -f %{_localstatedir}/krb5.keytab.rpmsave /etc/krb5.keytab
fi

%files server
%defattr(644,root,root,755)
%doc doc/krb5-{admin,install}.html %{?with_doc:doc/{admin,install}-guide.pdf}

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/kerberos

%attr(750,root,root) %dir /var/log/kerberos

%attr(700,root,root) %dir %{_localstatedir}
%attr(700,root,root) %dir %{_localstatedir}/krb5kdc

%attr(755,root,root) %{_bindir}/kadmin
%attr(755,root,root) %{_bindir}/ktutil
%attr(755,root,root) %{_bindir}/k5srvutil
%attr(755,root,root) %{_sbindir}/kadmin.local
%attr(755,root,root) %{_sbindir}/propagation
%attr(755,root,root) %{_sbindir}/kdb5_util
%attr(755,root,root) %{_sbindir}/kprop
%attr(755,root,root) %{_sbindir}/kproplog
%attr(755,root,root) %{_sbindir}/krb5-send-pr
%attr(755,root,root) %{_sbindir}/gss-server
%attr(755,root,root) %{_sbindir}/sim_server
%attr(755,root,root) %{_sbindir}/sserver
%attr(755,root,root) %{_sbindir}/uuserver

%{_mandir}/man1/krb5-send-pr.1*
%{_mandir}/man1/k5srvutil.1*
%{_mandir}/man1/kadmin.1*
%{_mandir}/man1/ktutil.1*
%{_mandir}/man8/kadmin.local.8*
%{_mandir}/man8/kdb5_util.8*
%{_mandir}/man8/kprop.8*
%{_mandir}/man8/kproplog.8*
%{_mandir}/man8/sserver.8*

%if %{with openldap}
%files server-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/krb5/plugins/kdb/kldap.so
%attr(755,root,root) %{_libdir}/libkdb_ldap.so
%attr(755,root,root) %{_libdir}/libkdb_ldap.so.*
%attr(755,root,root) %{_sbindir}/kdb5_ldap_util
%{_mandir}/man8/kdb5_ldap_util.8*

%files -n openldap-schema-krb5
%defattr(644,root,root,755)
%{schemadir}/*.ldif
%{schemadir}/*.schema
%endif

%files server-kdc
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/krb5kdc
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/krb5kdc/kdc.conf
%attr(755,root,root) %{_sbindir}/krb5kdc
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdb
%attr(755,root,root) %{_libdir}/krb5/plugins/kdb/db2.so
%dir %{_libdir}/krb5/plugins/preauth
%attr(755,root,root) %{_libdir}/krb5/plugins/preauth/pkinit.so
%attr(755,root,root) %{_libdir}/krb5/plugins/preauth/encrypted_challenge.so
%{_mandir}/man5/kdc.conf.5*
%{_mandir}/man8/krb5kdc.8*

%files server-kadmind
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/kadmind
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/krb5kdc/kadm5.acl
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/krb5kdc/kadm5.dict
%attr(755,root,root) %{_sbindir}/kadmind
%{_mandir}/man8/kadmind.8*

%files server-kpropd
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/kpropd
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/krb5kdc/kpropd.acl
%attr(755,root,root) %{_sbindir}/kpropd
%{_mandir}/man8/kpropd.8*

%files client
%defattr(644,root,root,755)
%doc doc/krb5-user.html %{?with_doc:doc/user-guide.pdf}
%attr(755,root,root) /etc/shrc.d/kerberos.*

%attr(755,root,root) %{_bindir}/kdestroy
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/klist
%attr(755,root,root) %{_bindir}/gss-client
%attr(755,root,root) %{_bindir}/sim_client
%attr(755,root,root) %{_bindir}/uuclient
%attr(4755,root,root) %{_bindir}/ksu

%attr(755,root,root) %{_bindir}/kpasswd
%attr(755,root,root) %{_bindir}/sclient
%attr(755,root,root) %{_bindir}/kvno

%{_mandir}/man1/kerberos.1*
%{_mandir}/man1/kdestroy.1*
%{_mandir}/man1/kinit.1*
%{_mandir}/man1/klist.1*
%{_mandir}/man1/ksu.1*
%{_mandir}/man1/kpasswd.1*
%{_mandir}/man1/sclient.1*
%{_mandir}/man1/kvno.1*
%{_mandir}/man5/.k5login.5*

%files rlogin
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rlogin
%{_mandir}/man1/rlogin.1*

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ftp
%{_mandir}/man1/ftp.1*

%files rsh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rcp
%attr(755,root,root) %{_bindir}/rsh
%{_mandir}/man1/rsh.1*
%{_mandir}/man1/rcp.1*

%files telnet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/telnet
%{_mandir}/man1/telnet.1*

%files telnetd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/telnetd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/telnetd
%{_mandir}/man8/telnetd.8*

%files ftpd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ftpd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/ftpd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kftpd
%{_mandir}/man8/ftpd.8*

%files kshd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/kshd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/kshd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/kshell
%{_mandir}/man8/kshd.8*

%files klogind
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/klogind
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/klogind
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/klogin
%{_mandir}/man8/klogind.8*

%files common
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/krb5.conf
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/krb5.keytab
%attr(755,root,root) %{_sbindir}/login.krb5
%{_mandir}/man8/login.krb5.8*
%{_mandir}/man5/krb5.conf.5*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgss*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgss*.so.?
%attr(755,root,root) %{_libdir}/libk5crypto.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libk5crypto.so.?
%attr(755,root,root) %{_libdir}/libkadm*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkadm*.so.?
%attr(755,root,root) %{_libdir}/libkdb5.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdb5.so.?
%attr(755,root,root) %{_libdir}/libkrb5*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkrb5*.so.?

%files devel
%defattr(644,root,root,755)
%doc doc/{kadmin,krb5-protocol} %{?with_doc:doc/{api,implement,kadm5}/*.pdf}
%attr(755,root,root) %{_bindir}/krb5-config
%attr(755,root,root) %{_libdir}/libgss*.so
%attr(755,root,root) %{_libdir}/libk5crypto.so
%attr(755,root,root) %{_libdir}/libkadm*.so
%attr(755,root,root) %{_libdir}/libkdb5.so
%attr(755,root,root) %{_libdir}/libkrb5*.so
%{_includedir}/gssapi
%{_includedir}/gssrpc
%{_includedir}/kadm5
%{_includedir}/krb5
%{_includedir}/*.h
%{_mandir}/man1/krb5-config.1*

%if 0
configure: error: Sorry, static libraries do not work in this release.
%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%endif
