Summary:	Kerberos V5 System
Summary(pl):	System Kerberos V5
Name:		krb5
Version:	1.0.6
Release:	3
License:	MIT
Group:		Networking
# warning: according to README, Source0 and Source1 may require license to export outside USA
Source0:	ftp://athena-dist.mit.edu/pub/kerberos/dist/990511/%{name}-%{version}.src.tar.gz
Source1:	ftp://athena-dist.mit.edu/pub/kerberos/dist/990511/%{name}-%{version}.crypto.tar.gz
Source2:	ftp://athena-dist.mit.edu/pub/kerberos/dist/990511/%{name}-%{version}.doc.tar.gz
Source3:	kerberos.init
Source4:	propagation
Source5:	inetd.conf.secure
Source6:	http://www.citi.umich.edu/u/itoi/pam_krb5/pam_krb5-1.0-1.tar.gz
Source7:	kerberos.logrotate
Source8:	%{name}.conf
Source9:	kdc.conf
Source10:	kerberos.sysconfig
Source11:	kerberos.sh
Source12:	kerberos.csh
URL:		http://web.mit.edu/kerberos/www/
Patch0:		%{name}-ftp.patch
Patch1:		%{name}-telnetd.patch
Patch2:		%{name}-kadmin.patch
Patch3:		%{name}-rpc.patch
Patch4:		%{name}-paths.patch
Patch5:		pam_krb5-pld.patch
Prereq:		rc-scripts
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/athena
%define		_mandir		/usr/athena/man

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
Summary(pl):	Serwery popularnych us³ug, autoryzuj±ce przy pomocy kerberosa.
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

%package lib
Summary:	Kerberos shared libraries
Summary(pl):	Biblioteki dzielone dla kerberosa
Group:		Libraries

%description lib
Libraries for Kerberos V5 Server and Client

%description lib -l pl
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

%package pam
Summary:	PAM - Kerberos 5 module
Summary(pl):	PAM - modu³ Kerberos 5
Requires:	pam >= 0.66
Group:		Libraries
Requires:	%{name}-lib = %{version}

%description pam
This is a PAM - Kerberos 5 module for PLD Linux. It supports
authentication, session, and password modules.

%description pam -l pl
W pakiecie znajduje siê modu³ PAM wspomagaj±cy autoryzacjê przez
Kerberosa V5. 

%prep
%setup  -q -b1 -b2 -b6
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

#kerberos pam
( cd ../pam_krb5-1.0-1; patch -p1 < %{PATCH5} )

%build
cd src
ln -sf /usr/share/automake/config.sub config.sub
./configure \
	--prefix=%{_prefix} \
	--enable-shared \
	--with-vague-errors \
	--sysconfdir=/etc/athena \
	--with-krb4 \
	--localstatedir=/var %{_target_platform}

install %{SOURCE5} ../doc

%{__make} CCOPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/rc.d/init.d,var/krb5kdc}
install -d $RPM_BUILD_ROOT/etc/{athena,sysconfig,profile.d}

(cd src; make install DESTDIR=$RPM_BUILD_ROOT)

install %{SOURCE8} $RPM_BUILD_ROOT/etc/athena
install %{SOURCE9} $RPM_BUILD_ROOT/var/krb5kdc

install -d $RPM_BUILD_ROOT/etc/logrotate.d
install %{SOURCE7}			$RPM_BUILD_ROOT/etc/logrotate.d/kerberos
install %{SOURCE3}			$RPM_BUILD_ROOT/etc/rc.d/init.d/kerberos
install %{SOURCE10}			$RPM_BUILD_ROOT/etc/sysconfig/kerberos
install %{SOURCE4}			$RPM_BUILD_ROOT%{_sbindir}/propagation
install %{SOURCE11}	%{SOURCE12}	$RPM_BUILD_ROOT/etc/profile.d

echo .so kadmin.8 > $RPM_BUILD_ROOT%{_mandir}/man8/kadmin.local.8

touch $RPM_BUILD_ROOT/etc/athena/krb5.keytab

ln -sf /usr/share/dict/words $RPM_BUILD_ROOT/var/krb5kdc/kadm5.dict

touch $RPM_BUILD_ROOT/var/krb5kdc/kadm5.acl

rm -rf $RPM_BUILD_ROOT%{_includedir}/asn.1

find doc -size 0 -print | xargs rm -f

gzip -9nf doc/kadmin/* doc/krb5-protocol/* doc/*.info* \
	../pam_krb5-1.0-1/README

# Kerberos5 PAM

cd ../pam_krb5-1.0-1
%{__make} clean
%{__make} KRBINCLUDE=-I$RPM_BUILD_ROOT%{_includedir} \
	KRBLIB=-L$RPM_BUILD_ROOT%{_libdir} \
	EXTRAS="%{rpmcflags}" WANT_PWDB=no

install -d $RPM_BUILD_ROOT/lib/security
install pam_krb5.so $RPM_BUILD_ROOT/lib/security

%clean
rm -rf $RPM_BUILD_ROOT

%post lib
grep "^/usr/athena/lib$" /etc/ld.so.conf >/dev/null 2>&1
[ $? -ne 0 ] && echo "/usr/athena/lib" >> /etc/ld.so.conf
/sbin/ldconfig

%preun lib
if [ "$1" = "0" ]; then
        grep -v "/usr/athena/lib" /etc/ld.so.conf > /etc/ld.so.conf.new
	mv -f /etc/ld.so.conf.new /etc/ld.so.conf
fi

%postun lib -p /sbin/ldconfig

%files server
%defattr(644,root,root,755)
%doc doc/kadmin/* doc/krb5-install.inf* doc/krb5-admin.inf*

%attr(754,root,root) /etc/rc.d/init.d/kerberos
%attr(640,root,root) /etc/logrotate.d/*
%attr(640,root,root) /etc/sysconfig/*

%attr(700,root,root) %dir /var/krb5kdc
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) /var/krb5kdc/*

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
%attr(755,root,root) %{_sbindir}/kadmind4
%attr(755,root,root) %{_sbindir}/krb524d
%attr(755,root,root) %{_sbindir}/v5passwdd

%{_mandir}/man8/kadmin.8*
%{_mandir}/man8/kadmin.local.8*
%{_mandir}/man8/kdb5_util.8*
%{_mandir}/man8/kprop.8*
%{_mandir}/man8/kpropd.8*
%{_mandir}/man8/krb5kdc.8*
%{_mandir}/man8/kadmind.8*
%{_mandir}/man8/ktutil.8*

%files clients
%defattr(644,root,root,755)
%doc doc/krb5-user.inf*
%attr(755,root,root) /etc/profile.d/kerberos.* 

%attr(755,root,root) %{_bindir}/ftp
%attr(755,root,root) %{_bindir}/telnet
%attr(755,root,root) %{_bindir}/rsh
%attr(755,root,root) %{_bindir}/kdestroy
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/krb524init
%attr(755,root,root) %{_bindir}/v4rcp
%attr(755,root,root) %{_bindir}/v5passwd
%attr(755,root,root) %{_bindir}/klist

%attr(4711,root,root) %{_bindir}/ksu

%attr(755,root,root) %{_bindir}/kpasswd
%attr(755,root,root) %{_bindir}/rcp
%attr(755,root,root) %{_bindir}/rlogin

%{_mandir}/man1/ftp.1*
%{_mandir}/man1/telnet.1*
%{_mandir}/man1/rsh.1*
%{_mandir}/man1/kdestroy.1*
%{_mandir}/man1/kinit.1*
%{_mandir}/man1/klist.1*
%{_mandir}/man1/ksu.1*
%{_mandir}/man1/kpasswd.1*
%{_mandir}/man1/rcp.1*
%{_mandir}/man1/rlogin.1*
%{_mandir}/man5/.k5login.5*

%files daemons
%defattr(644,root,root,755)
%doc doc/inetd.conf*

%attr(755,root,root) %{_sbindir}/ftpd
%attr(755,root,root) %{_sbindir}/klogind
%attr(755,root,root) %{_sbindir}/kshd
%attr(755,root,root) %{_sbindir}/telnetd

%{_mandir}/man8/ftpd.8*
%{_mandir}/man8/klogind.8*
%{_mandir}/man8/kshd.8*
%{_mandir}/man8/telnetd.8*

%files lib
%defattr(644,root,root,755)

%dir /etc/athena
%config(noreplace) %verify(not size mtime md5) /etc/athena/krb5.conf
%attr(400,root,root) %ghost /etc/athena/krb5.keytab

%attr(755,root,root) %{_libdir}/*.so.*
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_sbindir}/login.krb5

%{_mandir}/man8/login.krb5.8*
%{_mandir}/man5/krb5.conf.5*

%files devel
%defattr(644,root,root,755)
%doc doc/krb5-protocol/*

%{_includedir}/*

%files static
%defattr(644,root,root,755)

%{_libdir}/*.a

%files pam
%defattr(644,root,root,755)
%doc ../pam_krb5-1.0-1/README.gz

%attr(755,root,root) /lib/security/pam_krb5.so
