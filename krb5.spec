# TODO: CVE-2007-2442 CVE-2007-2443
#
# NOTE:
# making check in plugins/kdb/db2/libdb2/test... fails on x86_64
# temporarily disabled this test on x86_64 (patch33)
#	- it's problem with Th builder
#
# Conditional build:
%bcond_with	krb4		# build with Kerberos V4 support
%bcond_without	tcl		# build without tcl (tcl is needed for tests)
%bcond_without	openldap	# don't build openldap plugin
%bcond_without	tests		# don't perform make check
#
Summary:	Kerberos V5 System
Summary(pl.UTF-8):	System Kerberos V5
Name:		krb5
Version:	1.6.1
Release:	1
License:	MIT
Group:		Networking
Source0:	http://web.mit.edu/kerberos/dist/krb5/1.6/%{name}-%{version}-signed.tar
# Source0-md5:	6052c437226ea0a04a37f656f1a079b9
Source2:	%{name}kdc.init
Source3:	%{name}24d.init
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
URL:		http://web.mit.edu/kerberos/www/
Patch0:		%{name}-telnetd.patch
Patch1:		%{name}-manpages.patch
Patch2:		%{name}-netkit-rsh.patch
Patch3:		%{name}-rlogind-environ.patch
Patch4:		%{name}-ksu-access.patch
Patch5:		%{name}-ksu-path.patch
Patch6:		%{name}-tiocgltc.patch
Patch7:		%{name}-passive.patch
# http://lite.mit.edu/
Patch8:		%{name}-ktany.patch
Patch9:		%{name}-size.patch
Patch10:	%{name}-ftp-glob.patch
Patch11:	%{name}-norpath.patch
Patch12:	%{name}-paths.patch
Patch13:	%{name}-autoconf.patch
Patch14:	%{name}-api.patch
Patch15:	%{name}-brokenrev.patch
Patch16:	%{name}-dns.patch
Patch17:	%{name}-enospc.patch
Patch18:	%{name}-fclose.patch
Patch20:	%{name}-gssinit.patch
Patch21:	%{name}-io.patch
Patch22:	%{name}-kprop-mktemp.patch
Patch23:	%{name}-login-lpass.patch
Patch24:	%{name}-null.patch
Patch25:	%{name}-rcp-markus.patch
Patch26:	%{name}-rcp-sendlarge.patch
Patch27:	%{name}-reject-bad-transited.patch
Patch28:	%{name}-send-pr-tempfile.patch
Patch29:	%{name}-telnet-environ.patch
Patch30:	%{name}-as-needed.patch
Patch31:	%{name}-doc.patch
Patch32:	%{name}-tests.patch
Patch33:	%{name}-config.patch
Patch34:	%{name}-no-db-tests.patch
BuildRequires:	/bin/csh
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	e2fsprogs-devel >= 1.35
BuildRequires:	flex
BuildRequires:	ghostscript
BuildRequires:	ncurses-devel
%{?with_openldap:BuildRequires:	openldap-devel}
BuildRequires:	rpmbuild(macros) >= 1.268
%{?with_tcl:BuildRequires:	tcl-devel}
BuildRequires:	texinfo
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-format-pdflatex
BuildRequires:	tetex-latex
BuildRequires:	tetex-makeindex
BuildRequires:	words
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib/kerberos
# doesn't handle %{__cc} with spaces properly
%undefine	with_ccache
# mungles cflags
%undefine	configure_cache

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
Obsoletes:	heimdal

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
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires:	words
Obsoletes:	heimdal-server

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

%package server-krb524d
Summary:	Version 5 to Version 4 Credentials Conversion Daemon
Summary(pl.UTF-8):	Serwer tłumaczący wersję 5 na wersję 4 kerberosa
Group:		Networking
Requires:	%{name}-server-kdc = %{version}-%{release}

%description server-krb524d
This package contains the Kerberos Version 5 to Version 4 Credentials
Conversion daemon.

It works in conjuction with a krb5kdc to allow clients to acquire
Kerberos version 4 tickets from Kerberos version 5 tickets without
specifying a password.

%description server-krb524d -l pl.UTF-8
Ten pakiet zawiera demon konwerujący uwierzytelnienia Kerberosa 5 na
wersję 4.

Demon krb524d działa w połączeniu z krb5kdc umożliwiając klientom
uzyskanie biletów Kerberosa 4 z biletów Kerberosa 5 bez konieczności
podawania hasła.

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
Requires:	%{name}-server = %{version}-%{release}

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

%package ftpd
Summary:	The standard UNIX FTP (file transfer protocol) server
Summary(pl.UTF-8):	Serwer FTP
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	ftpd
Obsoletes:	heimdal-ftpd

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
Obsoletes:	heimdal-rshd

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
Requires:	libcom_err-devel
Obsoletes:	heimdal-devel

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
cd %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
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

%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%ifarch %{x8664}
%patch34 -p1
%endif

cp src/krb524/README README.krb524

%build
cd %{name}-%{version}/src
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
	--libexecdir=%{_libdir} \
	--enable-shared \
	%{?with_krb4:--with-krb4} \
	%{!?with_krb4:--without-krb4} \
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
%{__make}
%{__make} -C api
%{__make} -C implement
%{__make} -C kadm5

%{?with_tests:%{__make} -j1 -C ../src check}

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_localstatedir},/var/log/kerberos,%{_infodir},%{_mandir}}
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig/rc-inetd,shrc.d,logrotate.d}

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE7} $RPM_BUILD_ROOT%{_localstatedir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_localstatedir}
install %{SOURCE18} $RPM_BUILD_ROOT%{_localstatedir}
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
%if %{with krb4}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/krb524d
%endif

ln -sf %{_datadir}/dict/words $RPM_BUILD_ROOT%{_localstatedir}/kadm5.dict
touch $RPM_BUILD_ROOT%{_localstatedir}/krb5.keytab

echo .so kadmin.8 > $RPM_BUILD_ROOT%{_mandir}/man8/kadmin.local.8

rm -rf $RPM_BUILD_ROOT%{_includedir}/asn.1

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

%if %{with krb4}
%post server-krb524d
/sbin/chkconfig --add krb524d
%service krb524d restart "krb524d daemon"
%endif

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

%if %{with krb4}
%postun server-krb524d
if [ "$1" = 0 ]; then
	%service krb524d stop
	/sbin/chkconfig --del krb524d
fi
%endif

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

%files server
%defattr(644,root,root,755)
%doc %{name}-%{version}/doc/krb5-{admin,install}.html %{name}-%{version}/doc/{admin,install,krb425}-guide.pdf

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/kerberos

%attr(750,root,root) %dir /var/log/kerberos

%attr(755,root,root) %{_sbindir}/kadmin
%attr(755,root,root) %{_sbindir}/kadmin.local
%attr(755,root,root) %{_sbindir}/propagation
%attr(755,root,root) %{_sbindir}/kdb5_util
%attr(755,root,root) %{_sbindir}/kprop
%attr(755,root,root) %{_sbindir}/krb5-send-pr
%attr(755,root,root) %{_sbindir}/ktutil
%attr(755,root,root) %{_sbindir}/k5srvutil
%attr(755,root,root) %{_sbindir}/gss-server
%attr(755,root,root) %{_sbindir}/sim_server
%attr(755,root,root) %{_sbindir}/sserver
%attr(755,root,root) %{_sbindir}/uuserver

%{_mandir}/man1/krb5-send-pr.1*
%{_mandir}/man8/k5srvutil.8*
%{_mandir}/man8/kadmin.8*
%{_mandir}/man8/kadmin.local.8*
%{_mandir}/man8/kdb5_util.8*
%{_mandir}/man8/kprop.8*
%{_mandir}/man8/ktutil.8*
%{_mandir}/man8/sserver.8*

%if %{with openldap}
%files server-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/krb5/plugins/kdb/kldap.so
%attr(755,root,root) %{_libdir}/libkdb_ldap.so
%attr(755,root,root) %{_libdir}/libkdb_ldap.so.*
%attr(755,root,root) %{_sbindir}/kdb5_ldap_util
%{_mandir}/man8/kdb5_ldap_util.8*
%endif

%files server-kdc
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/krb5kdc
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/kdc.conf
%attr(755,root,root) %{_sbindir}/krb5kdc
%attr(755,root,root) %{_libdir}/krb5/plugins/kdb/db2.so
%{_mandir}/man5/kdc.conf.5*
%{_mandir}/man8/krb5kdc.8*

%files server-kadmind
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/kadmind
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/kadm5.acl
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/kadm5.dict
%attr(755,root,root) %{_sbindir}/kadmind
%{_mandir}/man8/kadmind.8*

%files server-kpropd
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/kpropd
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/kpropd.acl
%attr(755,root,root) %{_sbindir}/kpropd
%{_mandir}/man8/kpropd.8*

%if %{with krb4}
%files server-krb524d
%defattr(644,root,root,755)
%doc %{name}-%{version}/doc/krb425.html
%attr(754,root,root) /etc/rc.d/init.d/krb524d
%attr(755,root,root) %{_sbindir}/kadmind4
%attr(755,root,root) %{_sbindir}/krb524d
%endif

%files client
%defattr(644,root,root,755)
%doc %{name}-%{version}/doc/krb5-user.html %{name}-%{version}/doc/user-guide.pdf
%attr(755,root,root) /etc/shrc.d/kerberos.*

%attr(755,root,root) %{_bindir}/kdestroy
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/klist
%attr(755,root,root) %{_bindir}/gss-client
%attr(755,root,root) %{_bindir}/sim_client
%attr(755,root,root) %{_bindir}/uuclient
%attr(4755,root,root) %{_bindir}/ksu
%{?with_krb4:%attr(755,root,root) %{_bindir}/krb524init}

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
%{?with_krb4:%attr(755,root,root) %{_bindir}/v4rcp}
%{_mandir}/man1/rsh.1*
%{_mandir}/man1/rcp.1*
%{?with_krb4:%{_mandir}/man1/v4rcp.1*}

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
%{_mandir}/man8/ftpd.8*

%files kshd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/kshd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/kshd
%{_mandir}/man8/kshd.8*

%files klogind
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/klogind
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/klogind
%{_mandir}/man8/klogind.8*

%files common
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/krb5.conf
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdb
%attr(700,root,root) %dir %{_localstatedir}
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/krb5.keytab

%attr(755,root,root) %{_sbindir}/login.krb5
%{_mandir}/man8/login.krb5.8*
%{_mandir}/man5/krb5.conf.5*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdes425.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libdes425.so.?
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
%doc %{name}-%{version}/doc/{kadmin,krb5-protocol} %{name}-%{version}/doc/{api,implement,kadm5}/*.pdf
%attr(755,root,root) %{_bindir}/krb5-config
%attr(755,root,root) %{_libdir}/libdes425.so
%attr(755,root,root) %{_libdir}/libgss*.so
%attr(755,root,root) %{_libdir}/libk5crypto.so
%attr(755,root,root) %{_libdir}/libkadm*.so
%attr(755,root,root) %{_libdir}/libkdb5.so
%attr(755,root,root) %{_libdir}/libkrb5*.so
%{_includedir}/gssapi
%{_includedir}/gssrpc
%{_includedir}/krb5
%{?with_krb4:%{_includedir}/kerberosIV}
%{_includedir}/*.h
%{_mandir}/man1/krb5-config.1*

%if 0
configure: error: Sorry, static libraries do not work in this release.
%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%endif
