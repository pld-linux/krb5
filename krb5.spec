#
# WARNING!! Please do NOT rebuild it for Th! Its place is in th-obsolete!
# These packages on ftp only confuse people uneducated in Kerberos.
# We use Heimdal implementation in Th. If someone really wants MIT,
# (s)he is on hers/his own.
#				- baggins/at/pld-linux.org
#
# Conditional build:
%bcond_without	doc             # documentation [requires TeX]
%bcond_without	audit		# audit plugin
%bcond_with	hesiod		# Hesiod support
%bcond_without	ldap		# OpenLDAP database backend module
%bcond_with	selinux		# SELinux support
%bcond_without	system_db	# system Berkeley DB (via DB 1.85 API)
%bcond_without	tcl		# build without tcl (tcl is needed for tests)
%bcond_without	tests		# don't perform make check
#
Summary:	Kerberos V5 System
Summary(pl.UTF-8):	System Kerberos V5
Name:		krb5
Version:	1.18
Release:	0.1
License:	MIT
Group:		Networking
Source0:	http://web.mit.edu/kerberos/dist/krb5/1.18/%{name}-%{version}.tar.gz
# Source0-md5:	69a5b165dac5754a5094627ee6df0def
Source2:	%{name}kdc.init
Source4:	kadm5.acl
Source5:	kerberos.logrotate
Source6:	%{name}.conf
Source7:	kdc.conf
Source8:	kerberos.sysconfig
Source9:	kerberos.sh
Source10:	kerberos.csh
Source15:	propagation
Source16:	kpropd.init
Source17:	kadmind.init
Source18:	kpropd.acl
Patch0:		%{name}-manpages.patch
Patch1:		%{name}-audit.patch
Patch2:		%{name}-db185.patch
Patch3:		%{name}-as-needed.patch
# http://lite.mit.edu/
Patch6:		%{name}-ktany.patch
Patch11:	%{name}-brokenrev.patch
Patch12:	%{name}-dns.patch
Patch13:	%{name}-enospc.patch
Patch23:	%{name}-tests.patch
Patch24:	%{name}-config.patch
Patch29:	%{name}-selinux-label.patch
URL:		http://web.mit.edu/kerberos/www/
BuildRequires:	/bin/csh
%{?with_audit:BuildRequires:	audit-libs-devel}
BuildRequires:	autoconf >= 2.50
BuildRequires:	bison
%{?with_ldap:BuildRequires:	cyrus-sasl-devel >= 2}
%{?with_system_db:BuildRequires:	db-devel}
BuildRequires:	flex
BuildRequires:	gettext-tools
BuildRequires:	ghostscript
%{?with_hesiod:BuildRequires:	hesiod-devel}
BuildRequires:	keyutils-devel
BuildRequires:	libcom_err-devel
# only for internal ss
#BuildRequires:	libedit-devel
%{?with_selinux:BuildRequires:	libselinux-devel}
# for bindir/mk_cmds
BuildRequires:	libss-devel >= 1.35
BuildRequires:	libverto-devel
BuildRequires:	lmdb-devel
BuildRequires:	ncurses-devel
%{?with_ldap:BuildRequires:	openldap-devel >= 2.4.6}
BuildRequires:	openssl-devel >= 1.0.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
%{?with_tcl:BuildRequires:	tcl-devel}
BuildRequires:	words
%if %{with doc}
BuildRequires:	doxygen
BuildRequires:	sphinx-pdg
%endif
%if %{with tests}
BuildRequires:	cmocka-devel
BuildRequires:	libverto-libev
BuildRequires:	python >= 1:2.5
# we have "online" tests disabled, so probably not needed
#BuildRequires:	resolv_wrapper >= 1.1.5
BuildRequires:	tcl-devel
%endif
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
Requires:	libverto-libev

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
Summary(pl.UTF-8):	Wtyczka przechowywania danych w LDAP dla KDC Kerberosa 5
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
Requires:	libverto-devel
Conflicts:	heimdal-devel
Obsoletes:	krb5-static

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

%package doc
Summary:	MIT Kerberos V5 documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja systemu MIT Kerberos V5 w formacie HTML
Group:		Documentation

%description doc
MIT Kerberos V5 documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja systemu MIT Kerberos V5 w formacie HTML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{?with_system_db:%patch2 -p1}
%patch3 -p1
%patch6 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch23 -p1
%patch24 -p1
%{?with_selinux:%patch29 -p1}

%build
cd src
# Get LFS support on systems that need additional flags.
LFS_CFLAGS="$(getconf LFS_CFLAGS)"
CFLAGS="%{rpmcflags} $LFS_CFLAGS -fPIC -I%{_includedir}/et -I%{_includedir}/ncurses"
CPPFLAGS="$LFS_CFLAGS -I%{_includedir}/et -I%{_includedir}/ncurses"
%{__autoconf}
%{__autoheader}
%configure \
	--libexecdir=%{_libdir} \
	--disable-rpath \
	%{?with_audit:--enable-audit-plugin=simple} \
	--enable-dns-for-realm \
	--with-crypto-impl=openssl \
	%{?with_hesiod:--with-hesiod} \
	%{?with_ldap:--with-ldap} \
	--with-netlib=-lresolv \
	%{?with_selinux:--with-selinux} \
	%{?with_system_db:--with-system-db} \
	--with-system-et \
	--with-system-ss \
	--with-system-verto \
	--with-tcl=%{?with_tcl:%{_prefix}}%{!?with_tcl:no}

%{__make} \
	TCL_LIBPATH="-L%{_libdir}"

%if %{with doc}
%{__make} -C doc
%endif

%if %{with tests}
%{__make} check \
	OFFLINE=yes \
	TCL_LIBPATH="-L%{_libdir}" \
	PYTESTFLAGS="-v"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_localstatedir},/var/log/kerberos} \
	$RPM_BUILD_ROOT{%{schemadir},%{_infodir},%{_mandir}} \
	$RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig/rc-inetd,shrc.d,logrotate.d}

%{__make} -C src install \
	TCL_LIBPATH="-L%{_libdir}" \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE7} $RPM_BUILD_ROOT%{_localstatedir}/krb5kdc
install %{SOURCE4} $RPM_BUILD_ROOT%{_localstatedir}/krb5kdc
install %{SOURCE18} $RPM_BUILD_ROOT%{_localstatedir}/krb5kdc
install %{SOURCE5} $RPM_BUILD_ROOT/etc/logrotate.d/kerberos
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/kerberos
install %{SOURCE15} $RPM_BUILD_ROOT%{_sbindir}/propagation
install %{SOURCE9} %{SOURCE10} $RPM_BUILD_ROOT/etc/shrc.d

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/krb5kdc
install %{SOURCE16} $RPM_BUILD_ROOT/etc/rc.d/init.d/kpropd
install %{SOURCE17} $RPM_BUILD_ROOT/etc/rc.d/init.d/kadmind

%if %{with ldap}
install src/plugins/kdb/ldap/libkdb_ldap/kerberos.{schema,ldif} $RPM_BUILD_ROOT%{schemadir}
%endif

ln -sf %{_datadir}/dict/words $RPM_BUILD_ROOT%{_localstatedir}/krb5kdc/kadm5.dict
touch $RPM_BUILD_ROOT/etc/krb5.keytab

echo '.so man1/kadmin.1' > $RPM_BUILD_ROOT%{_mandir}/man8/kadmin.local.8

# fix permissions for deps generation
find $RPM_BUILD_ROOT -type f -name '*.so*' | xargs chmod +x

%{__rm} $RPM_BUILD_ROOT%{_libdir}/krb5/plugins/preauth/test.so

%find_lang mit-krb5

%clean
rm -rf $RPM_BUILD_ROOT

%post	server-ldap -p /sbin/ldconfig
%postun	server-ldap -p /sbin/ldconfig

%post -n openldap-schema-krb5
%openldap_schema_register %{schemadir}/kerberos.schema
%service -q ldap restart

%postun -n openldap-schema-krb5
if [ "$1" = "0" ]; then
	%openldap_schema_unregister %{schemadir}/kerberos.schema
	%service -q ldap restart
fi

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

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

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

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/kerberos
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

%{_mandir}/man1/k5srvutil.1*
%{_mandir}/man1/kadmin.1*
%{_mandir}/man1/ktutil.1*
%{_mandir}/man8/kadmin.local.8*
%{_mandir}/man8/kdb5_util.8*
%{_mandir}/man8/kprop.8*
%{_mandir}/man8/kproplog.8*
%{_mandir}/man8/sserver.8*

%if %{with ldap}
%files server-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/krb5/plugins/kdb/kldap.so
%attr(755,root,root) %{_libdir}/libkdb_ldap.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdb_ldap.so.1
%attr(755,root,root) %{_libdir}/libkdb_ldap.so
%attr(755,root,root) %{_sbindir}/kdb5_ldap_util
%{_mandir}/man8/kdb5_ldap_util.8*

%files -n openldap-schema-krb5
%defattr(644,root,root,755)
%{schemadir}/kerberos.ldif
%{schemadir}/kerberos.schema
%endif

%files server-kdc
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/krb5kdc
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/krb5kdc/kdc.conf
%attr(755,root,root) %{_sbindir}/krb5kdc
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%if %{with audit}
%dir %{_libdir}/krb5/plugins/audit
%attr(755,root,root) %{_libdir}/krb5/plugins/audit/k5audit.so
%endif
%dir %{_libdir}/krb5/plugins/kdb
%attr(755,root,root) %{_libdir}/krb5/plugins/kdb/db2.so
%attr(755,root,root) %{_libdir}/krb5/plugins/kdb/klmdb.so
%dir %{_libdir}/krb5/plugins/preauth
%attr(755,root,root) %{_libdir}/krb5/plugins/preauth/otp.so
%attr(755,root,root) %{_libdir}/krb5/plugins/preauth/pkinit.so
%attr(755,root,root) %{_libdir}/krb5/plugins/preauth/spake.so
%dir %{_libdir}/krb5/plugins/tls
%attr(755,root,root) %{_libdir}/krb5/plugins/tls/k5tls.so
%{_mandir}/man5/kdc.conf.5*
%{_mandir}/man8/krb5kdc.8*

%files server-kadmind
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/kadmind
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/krb5kdc/kadm5.acl
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/krb5kdc/kadm5.dict
%attr(755,root,root) %{_sbindir}/kadmind
%{_mandir}/man5/kadm5.acl.5*
%{_mandir}/man8/kadmind.8*

%files server-kpropd
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/kpropd
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/krb5kdc/kpropd.acl
%attr(755,root,root) %{_sbindir}/kpropd
%{_mandir}/man8/kpropd.8*

%files client
%defattr(644,root,root,755)
%attr(755,root,root) /etc/shrc.d/kerberos.*

%attr(755,root,root) %{_bindir}/gss-client
%attr(755,root,root) %{_bindir}/kdestroy
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/klist
%attr(755,root,root) %{_bindir}/kpasswd
%attr(4755,root,root) %{_bindir}/ksu
%attr(755,root,root) %{_bindir}/kswitch
%attr(755,root,root) %{_bindir}/kvno
%attr(755,root,root) %{_bindir}/sclient
%attr(755,root,root) %{_bindir}/sim_client
%attr(755,root,root) %{_bindir}/uuclient

%{_mandir}/man1/kdestroy.1*
%{_mandir}/man1/kinit.1*
%{_mandir}/man1/klist.1*
%{_mandir}/man1/kpasswd.1*
%{_mandir}/man1/ksu.1*
%{_mandir}/man1/kswitch.1*
%{_mandir}/man1/kvno.1*
%{_mandir}/man1/sclient.1*
%{_mandir}/man5/.k5identity.5*
%{_mandir}/man5/.k5login.5*
%{_mandir}/man5/k5identity.5*
%{_mandir}/man5/k5login.5*

%files common
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/krb5.conf
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/krb5.keytab
%{_mandir}/man5/krb5.conf.5*
%{_mandir}/man7/kerberos.7*

%files libs -f mit-krb5.lang
%defattr(644,root,root,755)
%doc NOTICE README
%attr(755,root,root) %{_libdir}/libgssapi_krb5.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgssapi_krb5.so.2
%attr(755,root,root) %{_libdir}/libgssrpc.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libgssrpc.so.4
%attr(755,root,root) %{_libdir}/libk5crypto.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libk5crypto.so.3
%attr(755,root,root) %{_libdir}/libkadm5clnt_mit.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkadm5clnt_mit.so.12
%attr(755,root,root) %{_libdir}/libkadm5srv_mit.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkadm5srv_mit.so.12
%attr(755,root,root) %{_libdir}/libkdb5.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkdb5.so.10
%attr(755,root,root) %{_libdir}/libkrad.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkrad.so.0
%attr(755,root,root) %{_libdir}/libkrb5.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkrb5.so.3
%attr(755,root,root) %{_libdir}/libkrb5support.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libkrb5support.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krb5-config
%attr(755,root,root) %{_libdir}/libgssapi_krb5.so
%attr(755,root,root) %{_libdir}/libgssrpc.so
%attr(755,root,root) %{_libdir}/libk5crypto.so
%attr(755,root,root) %{_libdir}/libkadm5clnt_mit.so
%attr(755,root,root) %{_libdir}/libkadm5clnt.so
%attr(755,root,root) %{_libdir}/libkadm5srv_mit.so
%attr(755,root,root) %{_libdir}/libkadm5srv.so
%attr(755,root,root) %{_libdir}/libkdb5.so
%attr(755,root,root) %{_libdir}/libkrad.so
%attr(755,root,root) %{_libdir}/libkrb5.so
%attr(755,root,root) %{_libdir}/libkrb5support.so
%{_includedir}/gssapi
%{_includedir}/gssrpc
%{_includedir}/kadm5
%{_includedir}/krb5
%{_includedir}/gssapi.h
%{_includedir}/kdb.h
%{_includedir}/krad.h
%{_includedir}/krb5.h
%{_includedir}/profile.h
%{_pkgconfigdir}/gssrpc.pc
%{_pkgconfigdir}/kadm-client.pc
%{_pkgconfigdir}/kadm-server.pc
%{_pkgconfigdir}/kdb.pc
%{_pkgconfigdir}/krb5.pc
%{_pkgconfigdir}/krb5-gssapi.pc
%{_pkgconfigdir}/mit-krb5.pc
%{_pkgconfigdir}/mit-krb5-gssapi.pc
%{_mandir}/man1/krb5-config.1*

%files doc
%defattr(644,root,root,755)
%doc doc/html/*
