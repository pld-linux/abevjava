Summary:	Electronic formfill application (APEH, Hungary)
Summary(hu.UTF-8):	Elektronikus APEH nyomtatványkitöltő
Name:		abevjava
Version:	2.17.0
Release:	0.2
License:	GPL v2, Apache License v2, MPL
Group:		Applications
Source0:	http://www.apeh.hu/data/cms36637/%{name}_install.jar
# Source0-md5:	766c5cce1764e92c388609bdecb4cf15
Source1:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-forms.tar.xz
# Source1-md5:	d42d3d4e43c68841fb1040e6f98192e6
Source2:	%{name}
Source3:	%{name}.desktop
URL:		http://www.apeh.hu/bevallasok/nyomtatvany/keretprogramok/abevjava_install.html
Requires:	jre-X11
Suggests:	%{name}-forms = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Electronic formfill application (APEH, Hungary).

%description -l hu.UTF-8
Ez a programcsomag számítógéppel támogatott nyomtatványkitöltést
megvalósító eszköz. Ezzel a programmal tudja elektronikus
adóbevallását elkészíteni és feladásra megjelölni. Amennyiben Ön
internet kapcsolattal rendelkezik, segítséget nyújt az elektronikus
feladásban is.

%package forms
Summary:	Forms for abevjava
Summary(hu.UTF-8):	Nyomtatványok az abevjava nyomtatványkitöltőhöz
Group:		Applications

%description forms
Forms for abevjava.

%description forms -l hu.UTF-8
Nyomtatványok az abevjava nyomtatványkitöltőhöz.

%prep
%setup -q -c %{name}-%{version} -a1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_iconsdir}/hicolor/32x32}
install application/abevjava.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32
install application/{abevjava.jar,cfg.enyk} $RPM_BUILD_ROOT%{_datadir}/%{name}
install %SOURCE2 $RPM_BUILD_ROOT%{_bindir}
install %SOURCE3 $RPM_BUILD_ROOT%{_desktopdir}
cp -r application/{segitseg,xsd} $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r nyomtatvanyok $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/32x32/%{name}.png
%{_datadir}/%{name}/abevjava.jar
%{_datadir}/%{name}/cfg.enyk
%{_datadir}/%{name}/segitseg
%{_datadir}/%{name}/xsd

%files forms
%defattr(644,root,root,755)
%{_datadir}/%{name}/nyomtatvanyok
