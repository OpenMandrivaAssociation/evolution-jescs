%define major	2.10

Name:		evolution-jescs
Summary:	Sun Java Enterprise System Calendar Server connector for Evolution
Version:	2.10.0
Release:	%mkrel 1
License: 	GPL
Group:		Networking/Mail
Source0: 	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
URL: 		http://cvs.gnome.org/viewcvs/evolution-jescs/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	evolution-devel 
BuildRequires:  libsoup-devel 
BuildRequires:  libgtkhtml-3.8-devel 
BuildRequires:  evolution-data-server-devel
BuildRequires:	perl-XML-Parser
BuildRequires:  mono-devel

%description
This is the Evolution Connector for Sun Java Enterprise System Calendar Server 
(SJESCS), which adds support for SJESCS 5.1 and above to Evolution.

This connector supports the WCAP (Web Calendar Access Protocol) 2.0, 3.0, 3.1.

%prep
%setup -q

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

%files -f %{name}-%{major}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog 
%{_libdir}/evolution-data-server-*/camel-providers/*
%{_libdir}/evolution/*/%{name}
%{_libdir}/bonobo/servers/*.server
%{_datadir}/%{name}
%{_datadir}/evolution/*/images/*


