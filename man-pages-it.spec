Summary: Italian man (manual) pages from the Linux Documentation Project
Name: man-pages-it
Version: 2.80
Release: 6%{?dist}
License: IEEE
Group: Documentation
URL: http://www.pluto.linux.it/ildp/man/
%define extra_name %{name}-extra
%define extra_ver 0.5.0
Source0: ftp://ftp.pluto.it/pub/pluto/ildp/man/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: man
BuildArch: noarch
Obsoletes: %{extra_name} < 2.80
Provides: %{extra_name} = %{version}-%{release}
Summary(it): Pagine del manuale in italiano

%description
Manual pages from the Linux Documentation Project, translated into Italian.

%description -l it
Questo pacchetto è la traduzione a cura dell'Italian Linux Documentation
Project (ILDP) del pacchetto man page ufficiale mantenuto e distribuito da
Michael Kerrisk. La versione di questo pacchetto garantisce che le man page
contenute sono state aggiornate alla versione corrispondente del pacchetto
ufficiale. 

%prep
%setup -q
#%patch0 -p1

for i in *; do
    if [ -f $i ]; then
        iconv -f ISO8859-15 -t UTF-8 $i -o $i.utf8
        %__mv $i.utf8 $i
    fi
done
for i in man*/*; do
    if [ -f $i ]; then
        iconv -f ISO8859-15 -t UTF-8 $i -o $i.utf8
        %__mv $i.utf8 $i
    fi
done

%build


%install
%__rm -rf $RPM_BUILD_ROOT
%__make prefix=$RPM_BUILD_ROOT
%__mkdir -p $RPM_BUILD_ROOT/%{_mandir}/it
%__cp -R man* $RPM_BUILD_ROOT/%{_mandir}/it
%__rm -rf $RPM_BUILD_ROOT/%{_mandir}/it/'man??'
%__rm -rf $RPM_BUILD_ROOT/share/man

%clean
%__rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CHANGELOG HOWTOHELP POSIX-COPYRIGHT readme
%{_mandir}/it/man*/*


%changelog
* Wed Mar 03 2010 Ding-Yi Chen <dchen@redhat.com> - 2.80-6
- Resolves: #560507 [man-pages-it] Package wrangler fix

* Wed Mar 03 2010 Ding-Yi Chen <dchen@redhat.com> - 2.80-5
- Resolves: #560507 [man-pages-it] Package wrangler fix
- Fixed Fedora 569443 [man-pages-it] Wrong directory ownership

* Mon Feb 01 2010 Ding-Yi Chen <dchen@redhat.com> - 2.80-4
- Resolves: #560507
  [man-pages-it] Package wrangler fix
- Remove comments of extra subpackage, as upstream already merge them.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.80-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 26 2008 Ding-Yi Chen <dchen@redhat.com> - 2.80-1
- [Bug 451982] New: RFE: New version of man-pages-it available
- Obsoletes man-pages-it-extra

* Thu Dec 06 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-7
- [Bug 226125] Merge Review: man-page-it (Comment 13)

* Thu Dec 06 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-6
- [Bug 226125] Merge Review: man-page-it (Comment 8)

* Thu Dec 06 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-5
- Fix improper format of SPEC

* Wed Dec 05 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-4
- Change the Licence from "Freely redistributable without restriction" to IEEE

* Tue Dec 04 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-3
- [Bug 226125] Merge Review: man-page-it

* Thu Oct 25 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-2
- [Bug 335931] man-pages-it package is 6 years old
- Add Italian summaries and descriptions

* Mon Oct 22 2007 Ding-Yi Chen <dchen@redhat.com> - 2.65-0
- [Bug 335931] man-pages-it package is 6 years old

* Wed Oct 10 2007 Ding-Yi Chen <dchen@redhat.com> - 0.3.0-18
- [Bug 236116] Unsupported programs in man-pages-it
- remove celibacy.1 and sex.6

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.3.0-17.1.gz
- rebuild

* Thu Mar 23 2006 Karsten Hopp <karsten@redhat.de> 0.3.0-17
- remove vim.1, provided by the vim-common package

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Apr 07 2005 Peter Vrabec <pvrabec@redhat.com> 0.3.0-16
- newgrp man page removed, will be provided by shadow-utils

* Tue Sep 28 2004 Leon Ho <llch@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 10 2004 Akira TAGOH <tagoh@redhat.com> 0.3.0-13
- removed apropos.1, man.1, whatis.1, man.config.5, and makewhatis.8, because the latest man contains those manpages.

* Tue Feb 11 2003 Phil Knirsch <pknirsch@redhat.com> 0.3.0-12
- Convert all manpages to utf-8.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 0.3.0-11
- rebuilt

* Fri Nov 29 2002 Tim Powers <timp@redhat.com> 0.3.0-10
- remove unpackaged files from the buildroot

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 0.3.0-7
- Add URL

* Wed Apr  4 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add patch to fix roff errors in multiple man pages

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 20 2000 Jeff Johnson <jbj@redhat.com>
- rebuild to compress man pages.

* Mon Jun 19 2000 Matt Wilson <msw@redhat.com>
- defattr root

* Sun Jun 11 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%{_mandir}/it and %%{_tmppath} 

* Mon May 15 2000 Trond Eivind Glomsrød <teg@redhat.com>
- first build
