Name:		nrg2iso
Version:	0.4
Release:	9
Summary:	Convert Nero CD Images to ISO
Source0:	http://gregory.kokanosky.free.fr/v4/linux/%{name}-%{version}.tar.bz2
URL:		http://gregory.kokanosky.free.fr/v4/linux/nrg2iso.en.html
License:	GPL
Group:		Archiving/Other

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

%files
%defattr(-,root,root)
%doc CHANGELOG
%{_bindir}/nrg2iso
