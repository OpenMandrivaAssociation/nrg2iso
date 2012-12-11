%define name	nrg2iso
%define version	0.4
%define release	%mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Convert Nero CD Images to ISO
Source:		http://gregory.kokanosky.free.fr/v4/linux/%{name}-%{version}.tar.bz2
URL:		http://gregory.kokanosky.free.fr/v4/linux/nrg2iso.en.html
License:	GPL
Group:		Archiving/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description 
Nrg2Iso is a linux utility for converting cd images generated
by Nero Burning Rom to ISO format.

%prep
%setup -q

%build
%{__cc} %{optflags} -o nrg2iso nrg2iso.c

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install nrg2iso %{buildroot}%{_bindir}/nrg2iso

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG
%{_bindir}/nrg2iso



%changelog
* Tue May 03 2011 Michael Scherer <misc@mandriva.org> 0.4-7mdv2011.0
+ Revision: 664791
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.4-5mdv2010.0
+ Revision: 430182
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.4-4mdv2009.0
+ Revision: 254066
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.4-2mdv2008.1
+ Revision: 130699
- kill re-definition of %%buildroot on Pixel's request
- import nrg2iso


* Sat Apr 15 2006 Luca Berra <bluca@vodka.it> 0.4-2mdk
- Rebuild
- use %%mkrel

* Wed Jan 12 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4-1mdk
- 0.4
 
* Sat Jun 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2-1mdk
- 0.2

* Sun Nov 09 2003 Luca Berra <bluca@vodka.it> 0.1-2mdk
- fix summary

* Sun Sep 28 2003 Luca Berra <bluca@vodka.it> 0.1-1mdk
- initial cooker contrib
