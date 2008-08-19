%define major	2.24

Name:		evolution-jescs
Summary:	Sun Java Enterprise System Calendar Server connector for Evolution
Version:	2.23.1
Release:	%mkrel 1
License: 	GPLv2+
Group:		Networking/Mail
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
URL: 		http://cvs.gnome.org/viewcvs/evolution-jescs/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	evolution-devel >= 2.11
BuildRequires:  libsoup-devel 
BuildRequires:	perl-XML-Parser
BuildRequires:  mono-devel

%description
This is the Evolution Connector for Sun Java Enterprise System Calendar Server 
(SJESCS), which adds support for SJESCS 5.1 and above to Evolution.

This connector supports the WCAP (Web Calendar Access Protocol) 2.0, 3.0, 3.1.

%prep
%setup -q
touch *

%build

%configure2_5x 

make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall_std

rm -f $RPM_BUILD_ROOT%{_libdir}/evolution/*/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/evolution-data-server-*/*/*.a

%{find_lang} %{name}-%{major}

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%if %mdvver < 200900
%post
%update_icon_cache hicolor
%postun
%clean_icon_cache hicolor
%endif

%files -f %{name}-%{major}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog 
%{_libdir}/evolution-data-server-*/camel-providers/*
%{_libdir}/evolution/*/%{name}
%{_libdir}/bonobo/servers/*.server
%{_datadir}/%{name}
%_datadir/evolution/*/icons/hicolor/*/*/*
%_datadir/icons/hicolor/*/apps/*
