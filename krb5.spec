Summary:     Kerberos V5 System
Name:        krb5
Version:     1.0.5
Release:     4d
Source:      %{name}-%{version}.src.tar.gz
Source1:     %{name}-%{version}.crypto.tar.gz
Source2:     %{name}-%{version}.doc.tar.gz
Source3:     kerberos.init
Source4:     propagation
Source5:     inetd.conf.secure
########     http://www-personal.engin.umich.edu/~itoi/index.html
Source6:     pam_krb5-1.0-1.tar.gz
Patch:       %{name}.patch
Patch1:      %{name}-select.patch
Patch2:      pam_krb5-pld.patch
Copyright:   MIT
Group:       Networking
Group(pl):   Sieci
BuildRoot:   /tmp/%{name}-%{version}-root
Summary(pl): System Kerberos V5

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

%package clients 
Summary:     Kerberos programs for use on workstations
Group:       Networking/Utilities
Group(pl):   Sieci/U¿ytki
Requires:    %{name}-lib = %{version}
Obsoletes:   telnet, rsh, ftp
Provides:    ftp, rsh, telnet 
Summary(pl): Oprogramowanie klienckie dla stacji roboczej kerberosa

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

%package daemons
Summary:     Kerberos daemons programs for use on servers
Group:       Networking/Utilities
Group(pl):   Sieci/U¿ytki
Requires:    %{name}-lib = %{version}
Summary(pl): Daemony popularnych us³ug, autoryzuj±ce przy pomocy kerberosa.

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

%package server
Summary:     Kerberos Server 
Group:       Networking/Daemons
Group(pl):   Sieci/Demony
Requires:    %{name}-lib = %{version}
Requires:    words
Prereq:	     /sbin/chkconfig
Summary(pl): Serwer Kerberosa

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

%package lib
Summary:     Kerberos shared libraries
Group:       Libraries
Group(pl):   Biblioteki
Summary(pl): Biblioteki dynamiczne dla kerberosa

%description lib
Libraries for Kerberos V5 Server and Client

%description -l pl lib
Biblioteki dynamiczne dla systemu kerberos.

%package devel
Summary:     Header files for Kerberos libraries and development documentation
Group:       Libraries
Group(pl):   Biblioteki
Requires:    %{name}-lib = %{version}
Summary(pl): Pliki nag³ówkowe i dokumentacja do bibliotek Kerberosa

%description devel
Header files for Kerberos libraries and development documentation

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do bibliotek Kerberosa

%package static
Summary:     Static Kerberos libraries
Group:       Libraries
Group(pl):   Biblioteki
Requires:    %{name}-lib = %{version}
Summary(pl): Biblioteki statyczne Kerberosa

%description static
Sattic Kerberos libraries.

%description -l pl static
Biblioteki statyczne Kerberosa.

%package pam
Summary:     PAM - Kerberos 5 module
Requires:    pam >= 0.65
Group:       Base/PAM
Group:       Podstawy/PAM
Requires:    %{name}-lib = %{version}
Summary(pl): PAM - Kerberos 5 modu³

%description pam
This is a PAM - Kerberos 5 module for PLD Linux.
It supports authentication, session, and password modules. 

%description -l pl pam
W pakiecie znajduje siê modu³ PAM wspomagaj±cy autoryzacjê przez
Kerberosa V5. 

%prep
%setup -q -b1 -b2 -b6
%patch  -p1
%patch1 -p1

#kerberos pam
(cd ../pam_krb5-1.0-1; patch -p1 < $RPM_SOURCE_DIR/pam_krb5-pld.patch)

%build
cd src
ARCH=`uname -m`
if [ "$ARCH" = "i686" ]; then
./configure \
	--prefix=/usr \
	--enable-shared \
	--with-vague-errors \
	--without-tcl \
	--sysconfdir=/etc/kerberos \
	--without-krb4 --localstatedir=/var i586-linux-gnu
else
./configure \
	--prefix=/usr \
	--enable-shared \
	--with-vague-errors \
	--without-tcl \
	--sysconfdir=/etc/kerberos \
	--without-krb4 --localstatedir=/var 
fi

# There is still problem with STREAMSPTY... 
if [ -f /lib/libc-2.0.10* ]; then
cat appl/telnet/telnetd/Makefile | sed s/-DSTREAMSPTY=1/""/g > \
appl/telnet/telnetd/Makefile
fi

install %{SOURCE5} ../doc

make CCOPTS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/rc.d/init.d,var/krb5kdc}
install -d $RPM_BUILD_ROOT/etc/kerberos
(cd src; make install DESTDIR=$RPM_BUILD_ROOT)

install src/config-files/krb5.conf $RPM_BUILD_ROOT/etc/kerberos
install src/config-files/kdc.conf $RPM_BUILD_ROOT/var/krb5kdc

install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/kerberos
install %{SOURCE4} $RPM_BUILD_ROOT/usr/sbin/propagation

strip $RPM_BUILD_ROOT/usr/sbin/* || :
strip $RPM_BUILD_ROOT/usr/bin/* || :

echo .so kadmin.8.bz2 > $RPM_BUILD_ROOT%{_mandir}/man8/kadmin.local.8

ln -s /usr/dict/linux.words $RPM_BUILD_ROOT/var/krb5kdc/kadm5.dict
touch $RPM_BUILD_ROOT/var/krb5kdc/kadm5.acl

rm -rf $RPM_BUILD_ROOT/usr/include/asn.1.bz2

find doc -size 0 -print | xargs rm -f

chmod 755 $RPM_BUILD_ROOT%{_libdir}/*.so.*

bzip2 -9 $RPM_BUILD_ROOT%{_mandir}/{man1/*,man8/*}
bzip2 -9 $RPM_BUILD_ROOT%{_mandir}/{man5/*,man5/.*}

# Kerberos5 PAM

cd ../pam_krb5-1.0-1
make clean
make COPTFLAGS="$RPM_OPT_FLAGS" WANT_PWDB=no

install -d $RPM_BUILD_ROOT/lib/security
install pam_krb5.so $RPM_BUILD_ROOT/lib/security

%clean
rm -rf $RPM_BUILD_ROOT

%post   lib -p /sbin/ldconfig
%postun lib -p /sbin/ldconfig

%files server
%defattr(644,root,root,755)
%doc doc/kadmin/* doc/krb5-install.inf* doc/krb5-admin.inf*

%attr(700,root,root) %config /etc/rc.d/init.d/kerberos
%attr(700,root,root) %dir /var/krb5kdc
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) /var/krb5kdc/*

%attr(711,root,root) /usr/sbin/kadmin
%attr(711,root,root) /usr/sbin/kadmin.local
%attr(711,root,root) /usr/sbin/propagation
%attr(711,root,root) /usr/sbin/kdb5_util
%attr(711,root,root) /usr/sbin/kprop
%attr(711,root,root) /usr/sbin/kpropd
%attr(755,root,root) /usr/sbin/krb5-send-pr
%attr(711,root,root) /usr/sbin/krb5kdc
%attr(711,root,root) /usr/sbin/kadmind
%attr(711,root,root) /usr/sbin/ktutil

%{_mandir}/man8/kadmin.8.bz2
%{_mandir}/man8/kadmin.local.8.bz2
%{_mandir}/man8/kdb5_util.8.bz2
%{_mandir}/man8/kprop.8.bz2
%{_mandir}/man8/kpropd.8.bz2
%{_mandir}/man8/krb5kdc.8.bz2
%{_mandir}/man8/kadmind.8.bz2
%{_mandir}/man8/ktutil.8.bz2

%files clients
%defattr(644,root,root,755)
%doc doc/inetd.conf* doc/krb5-user.inf*

%attr(711,root,root) /usr/bin/ftp
%attr(711,root,root) /usr/bin/telnet
%attr(711,root,root) /usr/bin/rsh
%attr(711,root,root) /usr/bin/kdestroy
%attr(711,root,root) /usr/bin/kinit
%attr(711,root,root) /usr/bin/klist

%attr(4711,root,root) /usr/bin/ksu

%attr(711,root,root) /usr/bin/kpasswd
%attr(711,root,root) /usr/bin/rcp
%attr(711,root,root) /usr/bin/rlogin

%{_mandir}/man1/ftp.1.bz2
%{_mandir}/man1/telnet.1.bz2
%{_mandir}/man1/rsh.1.bz2
%{_mandir}/man1/kdestroy.1.bz2
%{_mandir}/man1/kinit.1.bz2
%{_mandir}/man1/klist.1.bz2
%{_mandir}/man1/ksu.1.bz2
%{_mandir}/man1/kpasswd.1.bz2
%{_mandir}/man1/rcp.1.bz2
%{_mandir}/man1/rlogin.1.bz2
%{_mandir}/man5/.k5login.5.bz2

%files daemons
%defattr(644,root,root,755)
%doc doc/inetd.conf*

%attr(711,root,root) /usr/sbin/ftpd
%attr(711,root,root) /usr/sbin/klogind
%attr(711,root,root) /usr/sbin/kshd
%attr(711,root,root) /usr/sbin/telnetd

%{_mandir}/man8/ftpd.8.bz2
%{_mandir}/man8/klogind.8.bz2
%{_mandir}/man8/kshd.8.bz2
%{_mandir}/man8/telnetd.8.bz2

%files lib
%defattr(644,root,root,755)
%dir /etc/kerberos
%config(noreplace) %verify(not size mtime md5) /etc/kerberos/krb5.conf

%attr(755,root,root) %{_libdir}/*.so.*
%attr(755,root,root) %{_libdir}/*.so
%attr(711,root,root) /usr/sbin/login.krb5

%{_mandir}/man8/login.krb5.8.bz2
%{_mandir}/man5/krb5.conf.5.bz2

%files devel
%defattr(644,root,root,755)
%doc doc/krb5-protocol/*
/usr/include/*

%files static
%attr(644,root,root) %{_libdir}/*.a

%files pam
%defattr(644,root,root,755)
%doc ../pam_krb5-1.0-1/README 
%attr(755,root,root) /lib/security/pam_krb5.so

%changelog
* Sun Dec 13 1998 Willy The Hacker <willy@the.hacker.ogr>
[1.0.5-4d]
- splited workstation package into two (clients and daemons),
  by Jolly Roger <roger@hell.gov> 
- fixed stupid pam_krb5.so source code error...
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
- firs try RPM.
