Summary:	Kerberos V5 System
Summary(pl):	System Kerberos V5
Name:		krb5
Version:	1.0.6
Release:	1
Source0:	%{name}-%{version}.src.tar.gz
Source1:	%{name}-%{version}.crypto.tar.gz
Source2:	%{name}-%{version}.doc.tar.gz
Source3:	kerberos.init
Source4:	propagation
Source5:	inetd.conf.secure
########	http://www-personal.engin.umich.edu/~itoi/index.html
Source6:	pam_krb5-1.0-1.tar.gz
Source7:	kerberos.logrotate
Source8:	%{name}.conf
Source9:	kdc.conf
Source10:	kerberos.sysconfig
Patch0:		%{name}-ftp.patch
Patch1:		%{name}-telnetd.patch
Patch2:		%{name}-kadmin.patch
Patch3:		%{name}-rpc.patch
Patch4:		pam_krb5-pld.patch
Copyright:	MIT
Group:		Networking
Group(pl):	Sieciowe
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Kerberos V5 is based on the Kerberos authentication system developed at MIT. 
Under Kerberos, a client (generally either a user or a service) sends a
request for a ticket to the Key Distribution Center (KDC). The KDC creates
a "ticket-granting ticket" (TGT) for the client, encrypts it using the
client's password as the key, and sends the encrypted TGT back to the
client. The client then attempts to decrypt the TGT, using its password. 
If the client successfully decrypts the TGT (i.e., if the client gave the
correct password), it keeps the decrypted TGT, which indicates proof of the
client's identity.

%description -l pl
Kerberos V5 jest systemem autentykacji rozwijanym w MIT. W tym systemie
klient (u¿ytkownik lub serwis) wysy³a ¿±danie biletu do Centrum Dystrybucji
Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT), u¿ywaj±c has³a klienta do
jego zaszyfrowania i wysy³a go spowrotem do klienta. Klient nastêpnie
przystêpuje do rozkodowywania kredytu przy pomocy swojego has³a. Je¿eli
zrobi to prawid³owo (tzn. poda poprawne has³o), jego bilet uaktywnia siê i
bêdzie wa¿ny na dan± us³ugê.

%package	clients 
Summary:	Kerberos programs for use on workstations
Summary(pl):	Oprogramowanie klienckie dla stacji roboczej kerberosa
Group:		Networking
Group(pl):	Sieciowe
Requires:	%{name}-lib = %{version}

%description clients
Kerberos Clients.

Kerberos V5 is based on the Kerberos authentication system developed at MIT. 
Under Kerberos, a client (generally either a user or a service) sends a
request for a ticket to the Key Distribution Center (KDC). The KDC creates
a "ticket-granting ticket" (TGT) for the client, encrypts it using the
client's password as the key, and sends the encrypted TGT back to the
client. The client then attempts to decrypt the TGT, using its password. 
If the client successfully decrypts the TGT (i.e., if the client gave the
correct password), it keeps the decrypted TGT, which indicates proof of the
client's identity.

%description -l pl clients
Oprogramowanie klienckie do korzystania z us³ug systemu Kerberos.

Kerberos V5 jest systemem autentykacji rozwijanym w MIT. W tym systemie
klient (u¿ytkownik lub serwis) wysy³a ¿±danie biletu do Centrum Dystrybucji
Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT), u¿ywaj±c has³a klienta do
jego zaszyfrowania i wysy³a go spowrotem do klienta. Klient nastêpnie
przystêpuje do rozkodowywania kredytu przy pomocy swojego has³a. Je¿eli
zrobi to prawid³owo (tzn. poda poprawne has³o), jego bilet uaktywnia siê i
bêdzie wa¿ny na dan± us³ugê.

%package	daemons
Summary:	Kerberos daemons programs for use on servers
Summary(pl):	Serwery popularnych us³ug, autoryzuj±ce przy pomocy kerberosa.
Group:		Networking
Group(pl):	Sieciowe
Requires:	%{name}-lib = %{version}

%description daemons
Kerberos Daemons.

Kerberos V5 is based on the Kerberos authentication system developed %attr(
MIT.
Under Kerberos, a client (generally either a user or a service) sends a
request for a ticket to the Key Distribution Center (KDC). The KDC creates
a "ticket-granting ticket" (TGT) for the client, encrypts it using the
client's password as the key, and sends the encrypted TGT back to the
client. The client then attempts to decrypt the TGT, using its password.
If the client successfully decrypts the TGT (i.e., if the client gave the
correct password), it keeps the decrypted TGT, which indicates proof of the
client's identity.

%description -l pl daemons
Daemony korzystaj±ce z systemu Kerberos do autoryzacji dostêpu.

Kerberos V5 jest systemem autentykacji rozwijanym w MIT. W tym systemie
klient (u¿ytkownik lub serwis) wysy³a ¿±danie biletu do Centrum Dystrybucji
Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT), u¿ywaj±c has³a klienta do
jego zaszyfrowania i wysy³a go spowrotem do klienta. Klient nastêpnie
przystêpuje do rozkodowywania kredytu przy pomocy swojego has³a. Je¿eli
zrobi to prawid³owo (tzn. poda poprawne has³o), jego bilet uaktywnia siê i
bêdzie wa¿ny na dan± us³ugê.

%package	server
Summary:	Kerberos Server 
Summary(pl):	Serwer Kerberosa
Group:		Networking
Group(pl):	Sieciowe
Requires:	%{name}-lib = %{version}
Requires:	words
Prereq:		/sbin/chkconfig

%description server
Master KDC.

Kerberos V5 is based on the Kerberos authentication system developed at MIT. 
Under Kerberos, a client (generally either a user or a service) sends a
request for a ticket to the Key Distribution Center (KDC). The KDC creates
a "ticket-granting ticket" (TGT) for the client, encrypts it using the
client's password as the key, and sends the encrypted TGT back to the
client. The client then attempts to decrypt the TGT, using its password. 
If the client successfully decrypts the TGT (i.e., if the client gave the
correct password), it keeps the decrypted TGT, which indicates proof of the
client's identity.

%description -l pl server
G³ówne centrum dystrybucji kluczy (KDC).

Kerberos V5 jest systemem autentykacji rozwijanym w MIT. W tym systemie
klient (u¿ytkownik lub serwis) wysy³a ¿±danie biletu do Centrum Dystrybucji
Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT), u¿ywaj±c has³a klienta do
jego zaszyfrowania i wysy³a go spowrotem do klienta. Klient nastêpnie
przystêpuje do rozkodowywania kredytu przy pomocy swojego has³a. Je¿eli
zrobi to prawid³owo (tzn. poda poprawne has³o), jego bilet uaktywnia siê i
bêdzie wa¿ny na dan± us³ugê.

%package	lib
Summary:	Kerberos shared libraries
Summary(pl):	Biblioteki dzielone dla kerberosa
Group:		Libraries
Group(pl):	Biblioteki
Prereq:		/sbin/ldconfig

%description lib
Libraries for Kerberos V5 Server and Client

%description -l pl lib
Biblioteki dynamiczne dla systemu kerberos.

%package	devel
Summary:	Header files for Kerberos libraries and documentation
Summary(pl):	Pliki nag³ówkowe i dokumentacja do bibliotek Kerberosa
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name}-lib = %{version}

%description devel
Header files for Kerberos libraries and development documentation

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do bibliotek Kerberosa

%package	static
Summary:	Static Kerberos libraries
Summary(pl):	Biblioteki statyczne Kerberosa
Group:		Libraries
Group(pl):	Biblioteki
Requires:	%{name}-lib = %{version}

%description static
Sattic Kerberos libraries.

%description -l pl static
Biblioteki statyczne Kerberosa.

%package	pam
Summary:	PAM - Kerberos 5 module
Summary(pl):	PAM - Kerberos 5 modu³
Requires:	pam >= 0.66
Group:		Libraries
Group:		Libraries
Requires:	%{name}-lib = %{version}

%description pam
This is a PAM - Kerberos 5 module for PLD Linux.
It supports authentication, session, and password modules. 

%description -l pl pam
W pakiecie znajduje siê modu³ PAM wspomagaj±cy autoryzacjê przez
Kerberosa V5. 

%prep
%setup -q -b1 -b2 -b6
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

#kerberos pam
(cd ../pam_krb5-1.0-1; patch -p1 < $RPM_SOURCE_DIR/pam_krb5-pld.patch)

%build
cd src
./configure \
	--prefix=/usr/athena \
	--enable-shared \
	--with-vague-errors \
	--sysconfdir=/etc/athena \
	--with-krb4 \
	--localstatedir=/var %{_target_platform}

install %{SOURCE5} ../doc

make CCOPTS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/rc.d/init.d,var/krb5kdc}
install -d $RPM_BUILD_ROOT/etc/{athena,sysconfig}

(cd src; make install DESTDIR=$RPM_BUILD_ROOT)

install %{SOURCE8} $RPM_BUILD_ROOT/etc/athena
install %{SOURCE9} $RPM_BUILD_ROOT/var/krb5kdc

install -d $RPM_BUILD_ROOT/etc/logrotate.d
install %{SOURCE7} $RPM_BUILD_ROOT/etc/logrotate.d/kerberos

install %{SOURCE3}  $RPM_BUILD_ROOT/etc/rc.d/init.d/kerberos
install %{SOURCE10} $RPM_BUILD_ROOT/etc/sysconfig/kerberos
install %{SOURCE4}  $RPM_BUILD_ROOT/usr/athena/sbin/propagation

strip $RPM_BUILD_ROOT/usr/athena/{bin/*,sbin/*} || :

echo .so kadmin.8 > $RPM_BUILD_ROOT/usr/athena/man/man8/kadmin.local.8

touch $RPM_BUILD_ROOT/etc/athena/krb5.keytab

ln -s /usr/dict/linux.words $RPM_BUILD_ROOT/var/krb5kdc/kadm5.dict

touch $RPM_BUILD_ROOT/var/krb5kdc/kadm5.acl

rm -rf $RPM_BUILD_ROOT/usr/include/asn.1

find doc -size 0 -print | xargs rm -f

strip $RPM_BUILD_ROOT/usr/athena/lib/*.so.*.*
chmod 755 $RPM_BUILD_ROOT/usr/athena/lib/*.so.*

gzip -9fn $RPM_BUILD_ROOT/usr/athena/man/man[158]/*
gzip -9fn $RPM_BUILD_ROOT/usr/athena/man/man5/.k5login.5
gzip -9fn doc/kadmin/* doc/krb5-protocol/* doc/*.info* 

gzip -9fn ../pam_krb5-1.0-1/README 

# Kerberos5 PAM

cd ../pam_krb5-1.0-1
make clean
make COPTFLAGS="$RPM_OPT_FLAGS" WANT_PWDB=no

install -d $RPM_BUILD_ROOT/lib/security
install -s pam_krb5.so $RPM_BUILD_ROOT/lib/security

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

%attr(750,root,root) /etc/rc.d/init.d/kerberos
%attr(640,root,root) /etc/logrotate.d/*
%attr(640,root,root) /etc/sysconfig/*

%attr(700,root,root) %dir /var/krb5kdc
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) /var/krb5kdc/*

%attr(755,root,root) /usr/athena/sbin/kadmin
%attr(755,root,root) /usr/athena/sbin/kadmin.local
%attr(755,root,root) /usr/athena/sbin/propagation
%attr(755,root,root) /usr/athena/sbin/kdb5_util
%attr(755,root,root) /usr/athena/sbin/kprop
%attr(755,root,root) /usr/athena/sbin/kpropd
%attr(755,root,root) /usr/athena/sbin/krb5-send-pr
%attr(755,root,root) /usr/athena/sbin/krb5kdc
%attr(755,root,root) /usr/athena/sbin/kadmind
%attr(755,root,root) /usr/athena/sbin/ktutil
%attr(755,root,root) /usr/athena/sbin/kadmind4
%attr(755,root,root) /usr/athena/sbin/krb524d
%attr(755,root,root) /usr/athena/sbin/v5passwdd

/usr/athena/man/man8/kadmin.8.gz
/usr/athena/man/man8/kadmin.local.8.gz
/usr/athena/man/man8/kdb5_util.8.gz
/usr/athena/man/man8/kprop.8.gz
/usr/athena/man/man8/kpropd.8.gz
/usr/athena/man/man8/krb5kdc.8.gz
/usr/athena/man/man8/kadmind.8.gz
/usr/athena/man/man8/ktutil.8.gz

%files clients
%defattr(644,root,root,755)
%doc doc/krb5-user.inf*

%attr(755,root,root) /usr/athena/bin/ftp
%attr(755,root,root) /usr/athena/bin/telnet
%attr(755,root,root) /usr/athena/bin/rsh
%attr(755,root,root) /usr/athena/bin/kdestroy
%attr(755,root,root) /usr/athena/bin/kinit
%attr(755,root,root) /usr/athena/bin/krb524init
%attr(755,root,root) /usr/athena/bin/v4rcp
%attr(755,root,root) /usr/athena/bin/v5passwd
%attr(755,root,root) /usr/athena/bin/klist

%attr(4711,root,root) /usr/athena/bin/ksu

%attr(755,root,root) /usr/athena/bin/kpasswd
%attr(755,root,root) /usr/athena/bin/rcp
%attr(755,root,root) /usr/athena/bin/rlogin

/usr/athena/man/man1/ftp.1.gz
/usr/athena/man/man1/telnet.1.gz
/usr/athena/man/man1/rsh.1.gz
/usr/athena/man/man1/kdestroy.1.gz
/usr/athena/man/man1/kinit.1.gz
/usr/athena/man/man1/klist.1.gz
/usr/athena/man/man1/ksu.1.gz
/usr/athena/man/man1/kpasswd.1.gz
/usr/athena/man/man1/rcp.1.gz
/usr/athena/man/man1/rlogin.1.gz
/usr/athena/man/man5/.k5login.5.gz

%files daemons
%defattr(644,root,root,755)
%doc doc/inetd.conf*

%attr(755,root,root) /usr/athena/sbin/ftpd
%attr(755,root,root) /usr/athena/sbin/klogind
%attr(755,root,root) /usr/athena/sbin/kshd
%attr(755,root,root) /usr/athena/sbin/telnetd

/usr/athena/man/man8/ftpd.8.gz
/usr/athena/man/man8/klogind.8.gz
/usr/athena/man/man8/kshd.8.gz
/usr/athena/man/man8/telnetd.8.gz

%files lib
%defattr(644,root,root,755)

%dir /etc/athena
%config(noreplace) %verify(not size mtime md5) /etc/athena/krb5.conf
%attr(400,root,root) %ghost /etc/athena/krb5.keytab

%attr(755,root,root) /usr/athena/lib/*.so.*
%attr(755,root,root) /usr/athena/lib/*.so
%attr(755,root,root) /usr/athena/sbin/login.krb5

/usr/athena/man/man8/login.krb5.8.gz
/usr/athena/man/man5/krb5.conf.5.gz

%files devel
%defattr(644,root,root,755)
%doc doc/krb5-protocol/*

/usr/athena/include

%files static
%defattr(644,root,root,755)

/usr/athena/lib/*.a

%files pam
%defattr(644,root,root,755)
%doc ../pam_krb5-1.0-1/README.gz

%attr(755,root,root) /lib/security/pam_krb5.so

%changelog
* Tue May 18 1999 Road Runner <runner@wb.com>
  [1.0.6-1]
- update to 1.0.6
- fixed slave_propagation script,
- added some patches,
- 1st prepare to use on 1.0 PLD Linux System
  -- /dev/pts for telnetd most wanted
  -- PAM support for klogind && krb5.login needed
  
* Thu Feb 18 1999 Road Runner <runner@wb.com>
  [1.0.5-5d]
- changed prefix to /usr/athena -- conflicts with other shared libs ;(
- modified %post, %preun & %postun scripts,
- added config for logrotate,
- fixed all config files,
- added %ghost /etc/athena/krb5.keytab && fixed default $KEYTAB_FILE,
- added stripping shared libs, 
- compressed documentation,
- fixed Group && Group(pl).


* Sun Dec 13 1998 Willy The Hacker <willy@the.hacker.org>
  [1.0.5-4d]
- splited workstation package into two (clients and daemons),
  
  by Jolly Roger <roger@hell.gov> 

- fixed stupid pam_krb5.so source code bug...

  by Road Runner <runner@wb.com>

- moved all shared libraries & symlinks into krb5-lib,
- cosmetic changes,
- final build for 1.1 PLD Linux -> I hoppe ;)
  
* Tue Oct 20 1998 Road Runner <runner@wb.com>
  [1.0.5-3d]
- fixed localstatedir,
- fixed initscript,
- other -- minor changes.

* Wed Sep 23 1998 Road Runner <runner@wb.com>
  [1.0.5-2d]
- fixed pl translation,
- removed ccopts & cppopts from configure,
- restricted files permissions,
- patching ftp & ftpd against empty macros,
- fixed telnet client,
- added $ARCH - to possibility build on i686, 
- again fixed shared libraries permissions to 755,
- localstatedir moved to /var/krb5kdc,
- fixed propagation script,
- fixed & moved inetd.conf.secure to %doc,
- removed stripping of shared libraries,
- added more docs,
- added Conflicts: e2fsprogs-devel with devel & static subpackages,
- added Provides: ftp, telnet, rsh in workstation subpackages.

* Mon Sep 21 1998 Bugs Bunny <bugs@wb.com>
  [1.0.5-2]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added removing 0 bytes length files,
- added using %%{name} and %%{version} in Source,
- added devel and static subpackages,
- added making some man page as nroff include instead
  making sym links to other  (this allow compress man pages in future),
- added full %attr description in %files,
- added striping shared libraries,
- fixed passing $RPM_OPT_FLAGS,
- documentation ios now installade in usual place,
- added "Obsoletes: telnet, rsh, ftp" for server (for security) and
  worstation packages (for easy replace standard telnet, rsh, ftp client and
  servers),
- some %description propagatet from main to subpackages,
- added "%dir /var/krb5kdc" for worstation subpackage,
- many simplifications in %files, %install and %build.

* Mon Aug 9 1998 Road Runner <runner@wb.com>
  [1.0.5-1d]
- translation modified for pl,
- changed permissions of shared libraries to 755,
- removed simple-client and server,
- build without kerberos IV support (we don't need it),

* Fri Jun 26 1998 Road Runner <runner@wb.com>
  [1.0.5-1]
- first try RPM.
