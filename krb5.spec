#
# Conditional build:
# _with_krb4	- build with Kerberos V4 support
# _without_tcl	- build without tcl (needed for tests) 
#
Summary:	Kerberos V5 System
Summary(pl):	System Kerberos V5
Name:		krb5
Version:	1.3.1
Release:	0.1
License:	MIT
Group:		Networking
# warning: according to README, Source0 may require license to export outside USA
Source0:	http://www.crypto-publish.org/dist/mit-kerberos5/%{name}-%{version}.tar.gz
# Source0-md5:	73f868cf65bec56d7c718834ca5665fd
Source1:	kerberos.init
Source2:	krb524d.init
Source3:	kadm5.acl
Source4:	kerberos.logrotate
Source5:	%{name}.conf
Source6:	kdc.conf
Source7:	kerberos.sysconfig
Source8:	kerberos.sh
Source9:	kerberos.csh
Source10:	klogind.inetd
Source11:	kftpd.inetd
Source12:	ktelnetd.inetd
Source13:	kshell.inetd
Source14:	propagation
URL:		http://web.mit.edu/kerberos/www/
Patch0:		%{name}-gcc33.patch
Patch1:		%{name}-telnetd.patch
Patch2:		%{name}-manpages.patch
Patch3:		%{name}-netkit-rsh.patch
Patch4:		%{name}-rlogind-environ.patch
Patch5:		%{name}-ksu-access.patch
Patch6:		%{name}-ksu-path.patch
Patch7:		%{name}-tiocgltc.patch
Patch8:		%{name}-term.patch
Patch9:		%{name}-passive.patch
# http://lite.mit.edu/
Patch10:	%{name}-ktany.patch
Patch11:	%{name}-size.patch
Patch12:	%{name}-ftp-glob.patch
Patch13:	%{name}-check.patch
Patch14:	%{name}-double-free.patch
Patch15:	%{name}-varargs.patch
Patch16:	%{name}-norpath.patch
#Patch17:	%{name}-paths.patch
BuildRequires:	automake
BuildRequires:  autoconf
BuildRequires:	bison
BuildRequires:	e2fsprogs-devel >= 1.34
BuildRequires:	flex
BuildRequires:	mawk
%{!?_without_tcl:BuildRequires:	tcl-devel}
PreReq:		rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _localstatedir  /var/lib/kerberos

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

%description -l pl
Kerberos V5 jest systemem autentykacji rozwijanym w MIT. W tym
systemie klient (u¿ytkownik lub serwis) wysy³a ¿±danie biletu do
Centrum Dystrybucji Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT),
u¿ywaj±c has³a klienta do jego zaszyfrowania i wysy³a go spowrotem do
klienta. Klient nastêpnie przystêpuje do rozkodowywania kredytu przy
pomocy swojego has³a. Je¿eli zrobi to prawid³owo (tzn. poda poprawne
has³o), jego bilet uaktywnia siê i bêdzie wa¿ny na dan± us³ugê.

%package clients
Summary:	Kerberos programs for use on workstations
Summary(pl):	Oprogramowanie klienckie dla stacji roboczej kerberosa
Group:		Networking
Requires:	%{name}-lib = %{version}

%description clients
Kerberos Clients.

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

%description clients -l pl
Oprogramowanie klienckie do korzystania z us³ug systemu Kerberos.

Kerberos V5 jest systemem autentykacji rozwijanym w MIT. W tym
systemie klient (u¿ytkownik lub serwis) wysy³a ¿±danie biletu do
Centrum Dystrybucji Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT),
u¿ywaj±c has³a klienta do jego zaszyfrowania i wysy³a go spowrotem do
klienta. Klient nastêpnie przystêpuje do rozkodowywania kredytu przy
pomocy swojego has³a. Je¿eli zrobi to prawid³owo (tzn. poda poprawne
has³o), jego bilet uaktywnia siê i bêdzie wa¿ny na dan± us³ugê.

%package daemons
Summary:	Kerberos daemons programs for use on servers
Summary(pl):	Serwery popularnych us³ug, autoryzuj±ce przy pomocy kerberosa
Group:		Networking
Requires:	%{name}-lib = %{version}

%description daemons
Kerberos Daemons.

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

%description daemons -l pl
Daemony korzystaj±ce z systemu Kerberos do autoryzacji dostêpu.

Kerberos V5 jest systemem autentykacji rozwijanym w MIT. W tym
systemie klient (u¿ytkownik lub serwis) wysy³a ¿±danie biletu do
Centrum Dystrybucji Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT),
u¿ywaj±c has³a klienta do jego zaszyfrowania i wysy³a go spowrotem do
klienta. Klient nastêpnie przystêpuje do rozkodowywania kredytu przy
pomocy swojego has³a. Je¿eli zrobi to prawid³owo (tzn. poda poprawne
has³o), jego bilet uaktywnia siê i bêdzie wa¿ny na dan± us³ugê.

%package server
Summary:	Kerberos Server
Summary(pl):	Serwer Kerberosa
Group:		Networking
Requires:	%{name}-lib = %{version}
Requires:	words

%description server
Master KDC.

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

%description server -l pl
G³ówne centrum dystrybucji kluczy (KDC).

Kerberos V5 jest systemem autentykacji rozwijanym w MIT. W tym
systemie klient (u¿ytkownik lub serwis) wysy³a ¿±danie biletu do
Centrum Dystrybucji Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT),
u¿ywaj±c has³a klienta do jego zaszyfrowania i wysy³a go spowrotem do
klienta. Klient nastêpnie przystêpuje do rozkodowywania kredytu przy
pomocy swojego has³a. Je¿eli zrobi to prawid³owo (tzn. poda poprawne
has³o), jego bilet uaktywnia siê i bêdzie wa¿ny na dan± us³ugê.

%package rlogin
Summary:	rlogin is used when signing onto a system
Summary(pl):	Narzêdzie do logowania w systemie
Group:		Networking
Requires:	%{name}-lib = %{version}
Provides:	rlogin

%description rlogin
login is used when signing onto a system. It can also be used to
switch from one user to another at any time (most modern shells have
support for this feature built into them, however). This package
contain kerberized version login program.

%description rlogin -l pl
login jest u¿ywany przy logowaniu do systemu. Mo¿e byæ tak¿e u¿yty do
prze³±czenia z jednego u¿ytkownika na innego w dowolnej chwili
(wiêkszo¶æ wspó³czesnych shelli ma wbudowan± obs³ugê tego). Ten pakiet
zawiera skerberyzowan± wersjê programu rlogin.

%package rsh
Summary:	Clients for remote access commands (rsh, rlogin, rcp)
Summary(pl):	Klient zdalnego dostêpu (rsh, rlogin, rcp)
Group:		Applications/Networking
Requires:	%{name}-lib = %{version}
Obsoletes:	rsh
Obsoletes:	rcp

%description rsh
The rsh package contains a set of programs which allow users to run
commands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp). All three of these commands
use rhosts style authentication. This package contains the clients
needed for all of these services.

%description rsh -l pl
Ten pakiet zawiera zestaw narzêdzi pozwalaj±cych na wykonywanie
poleceñ na zdalnych maszynach, logowanie na inne maszyny oraz
kopiowanie plików pomiêdzy maszynami (rsh, rlogin, rcp).

%package ftp
Summary:	The standard UNIX FTP (file transfer protocol) client
Summary(pl):	Klient protoko³u FTP
Group:		Networking
Requires:	%{name}-lib = %{version}

%description ftp
The ftp package provides the standard UNIX command-line FTP client
with kerberos authentication support. FTP is the file transfer
protocol, which is a widely used Internet protocol for transferring
files and for archiving files.

%description ftp -l pl
Ten pakiet dostarcza standardowego klienta ftp z wbudowan± obs³ug±
kerberosa. FTP jest protoko³em do przesy³ania plików szeroko
rozpowszechnionym w Internecie.

%package telnet
Summary:	Client for the telnet remote login
Summary(pl):	Klient us³ugi telnet
Group:		Networking
Requires:	%{name}-lib = %{version}
Obsoletes:	telnet

%description telnet
Telnet is a popular protocol for remote logins across the Internet.
This package provides a command line telnet client.

%description telnet -l pl
Telnet jest popularnym protoko³em zdalnego logowania. Ten pakiet
zawiera klienta tej us³ugi.

%package libs
Summary:	Kerberos shared libraries
Summary(pl):	Biblioteki dzielone dla kerberosa
Group:		Libraries
Requires(post,preun):	grep
Requires(post):		/sbin/ldconfig
Requires(preun):	fileutils
Obsoletes: 	krb5-configs, krb5-lib

%description libs
Libraries for Kerberos V5 Server and Client

%description libs -l pl
Biblioteki dynamiczne dla systemu kerberos.

%package devel
Summary:	Header files for Kerberos libraries and documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do bibliotek Kerberosa
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}

%description devel
Header files for Kerberos libraries and development documentation.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do bibliotek Kerberosa.

%package static
Summary:	Static Kerberos libraries
Summary(pl):	Biblioteki statyczne Kerberosa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Kerberos libraries.

%description static -l pl
Biblioteki statyczne Kerberosa.

%prep
%setup -q
%patch0  -p1
%patch1  -p1
%patch2  -p1
%patch3  -p1
%patch4  -p1
%patch5  -p1
%patch6  -p1
%patch7  -p0
%patch8  -p1
%patch9  -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
#patch17 -p1

%build
cd src
CC=%{__cc}
CFLAGS="%{rpmcflags} -fPIC -I%{_includedir}/et"
%configure \
	--libexecdir=%{_libdir} \
        --enable-shared \
        --enable-static \
	%{?_with_krb4:--with-krb4}%{?!_with_krb4:--without-krb4} \
        --with-vague-errors \
        --enable-dns \
        --enable-dns-for-kdc \
        --enable-dns-for-realm \
        --with-netlib=-lresolv \
        %{!?_without_tcl:--with-tcl=%{_prefix}} \
	--with-system-et \
	--with-system-ss \
        %{_target_platform}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_localstatedir},/var/log/kerberos,%{_infodir},%{_mandir}}
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig/rc-inetd,profile.d,logrotate.d}

cd src
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE6} $RPM_BUILD_ROOT%{_localstatedir}/
install %{SOURCE3} $RPM_BUILD_ROOT%{_localstatedir}/
install %{SOURCE4}                      $RPM_BUILD_ROOT/etc/logrotate.d/kerberos
install %{SOURCE1}                      $RPM_BUILD_ROOT/etc/rc.d/init.d/kerberos
install %{SOURCE7}                      $RPM_BUILD_ROOT/etc/sysconfig/kerberos
install %{SOURCE14}                     $RPM_BUILD_ROOT%{_sbindir}/propagation
install %{SOURCE8}      %{SOURCE9}      $RPM_BUILD_ROOT/etc/profile.d

install %{SOURCE10}                     $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/klogind
install %{SOURCE11}                     $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install %{SOURCE12}                     $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnetd
install %{SOURCE13}                     $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/kshell
%if %{?_with_krb4:1}%{!?_with_krb4:0}
install %{SOURCE2}			$RPM_BUILD_ROOT/etc/rc.d/init.d/krb524d
%endif

ln -sf /usr/share/dict/words $RPM_BUILD_ROOT%{_localstatedir}/kadm5.dict
touch $RPM_BUILD_ROOT%{_localstatedir}/krb5.keytab

echo .so kadmin.8 > $RPM_BUILD_ROOT%{_mandir}/man8/kadmin.local.8

rm -rf $RPM_BUILD_ROOT%{_includedir}/asn.1

find doc -size 0 -print | xargs rm -f

# rpath fix
sed "s/^CC_LINK=.*/CC_LINK='\$(CC) \$(PROG_LIBPATH)'/g" src/krb5-config > $RPM_BUILD_ROOT%{_bindir}/krb5-config

%clean
rm -rf $RPM_BUILD_ROOT

%post server
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/chkconfig --add kerberos
%{?_with_krb4:/sbin/chkconfig --add krb524d}

%post libs -p /sbin/ldconfig

%postun server
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
if [ "$1" = 0 ]; then
	if [ -f /var/lock/subsys/kerberos ]; then
                /etc/rc.d/init.d/kerberos stop 1>&2
	fi
	/sbin/chkconfig --del kerberos

	%if %{?_with_krb4:1}%{!?_with_krb4:0}
	if [ -f /var/lock/subsys/krb524d ]; then
		/etc/rc.d/init.d/krb524d stop 1>&2
	fi
	/sbin/chkconfig --del krb524d
	%endif
fi

%postun libs -p /sbin/ldconfig

%files server
%defattr(644,root,root,755)
%doc doc/kadmin/* doc/krb5-install.inf* doc/krb5-admin.inf*

%attr(754,root,root) /etc/rc.d/init.d/kerberos
%{?_with_krb4:%attr(754,root,root) /etc/rc.d/init.d/krb524d}

%attr(640,root,root) /etc/logrotate.d/*
%attr(640,root,root) /etc/sysconfig/kerberos

%attr(750,root,root) %dir /var/log/kerberos
%attr(700,root,root) %dir %{_localstatedir}
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_localstatedir}/*

%attr(755,root,root) %{_sbindir}/kadmin
%attr(755,root,root) %{_sbindir}/kadmin.local
%attr(755,root,root) %{_sbindir}/propagation
%attr(755,root,root) %{_sbindir}/kdb5_util
%attr(755,root,root) %{_sbindir}/kprop
%attr(755,root,root) %{_sbindir}/kpropd
%attr(755,root,root) %{_sbindir}/krb5-send-pr
%attr(755,root,root) %{_sbindir}/krb5kdc
%attr(755,root,root) %{_sbindir}/kadmind
%attr(755,root,root) %{_sbindir}/ktutil
%attr(755,root,root) %{_sbindir}/k5srvutil
%attr(755,root,root) %{_sbindir}/v5passwdd
%attr(755,root,root) %{_sbindir}/gss-server
%attr(755,root,root) %{_sbindir}/sserver
%{?_with_krb4:%attr(755,root,root) %{_sbindir}/kadmind4}
%{?_with_krb4:%attr(755,root,root) %{_sbindir}/krb524d}

%{_mandir}/man8/kadmin.8*
%{_mandir}/man8/kadmin.local.8*
%{_mandir}/man8/kdb5_util.8*
%{_mandir}/man8/kprop.8*
%{_mandir}/man8/kpropd.8*
%{_mandir}/man8/krb5kdc.8*
%{_mandir}/man8/kadmind.8*
%{_mandir}/man8/ktutil.8*
%{_mandir}/man8/k5srvutil.8*
%{_mandir}/man8/sserver.8*

%files clients
%defattr(644,root,root,755)
%doc doc/krb5-user.inf*
%attr(755,root,root) /etc/profile.d/kerberos.*

%attr(755,root,root) %{_bindir}/kdestroy
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/v5passwd
%attr(755,root,root) %{_bindir}/klist
%attr(755,root,root) %{_bindir}/gss-client
%attr(4755,root,root) %{_bindir}/ksu
%{?_with_krb4:%attr(755,root,root) %{_bindir}/krb524init}

%attr(755,root,root) %{_bindir}/kpasswd
%attr(755,root,root) %{_bindir}/sclient
%attr(755,root,root) %{_bindir}/kvno

%{_mandir}/man1/v5passwd.1*
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
%{?_with_krb4:%attr(755,root,root) %{_bindir}/v4rcp}

%{_mandir}/man1/rsh.1*
%{_mandir}/man1/rcp.1*
%{?_with_krb4:%{_mandir}/man1/v4rcp.1*}

%files telnet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/telnet
%{_mandir}/man1/telnet.1*


%files daemons
%defattr(644,root,root,755)

%attr(755,root,root) %{_sbindir}/ftpd
%attr(755,root,root) %{_sbindir}/klogind
%attr(755,root,root) %{_sbindir}/kshd
%attr(755,root,root) %{_sbindir}/telnetd

/etc/sysconfig/rc-inetd/telnetd
/etc/sysconfig/rc-inetd/ftpd
/etc/sysconfig/rc-inetd/kshell
/etc/sysconfig/rc-inetd/klogind

%{_mandir}/man8/ftpd.8*
%{_mandir}/man8/klogind.8*
%{_mandir}/man8/kshd.8*
%{_mandir}/man8/telnetd.8*

%files libs
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/krb5.conf
%attr(400,root,root) %ghost %{_localstatedir}/krb5.keytab

%attr(755,root,root) %{_libdir}/*.so.*
%attr(755,root,root) %{_sbindir}/login.krb5

%{_mandir}/man8/login.krb5.8*
%{_mandir}/man5/krb5.conf.5*
%{_mandir}/man5/kdc.conf.5*

%files devel
%defattr(644,root,root,755)
%doc doc/krb5-protocol/*
%attr(755,root,root) %{_bindir}/krb5-config
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
