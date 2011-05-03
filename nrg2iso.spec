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

