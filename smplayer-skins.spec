%define name    smplayer-skins
%define version 20121029
%define release 1

Name:           %{name}
Summary:        Skins for SMPlayer
License:        GPL
Group:		Video
URL:            http://smplayer.sourceforge.net/
Version:        %{version}
Release:        %{release}

Source0:        %{name}-%{version}.tar.bz2

BuildArch:	noarch
Autoreqprov:    On
Requires:		smplayer >= 0.8.2

%description
This package provides skin themes for SMPlayer.
SMPlayer intends to be a complete front-end for Mplayer, from basic features 
like playing videos, DVDs, and VCDs to more advanced features like support 
for Mplayer filters and more. One of the main features is the ability to 
remember the state of a played file, so when you play it later it will resume 
at the same point and with the same settings. smplayer is developed with 
the Qt toolkit, so it's multi-platform.

%prep
%setup -q

%install
make PREFIX=/usr DESTDIR=%{?buildroot:%{buildroot}} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.txt Changelog
%dir %{_datadir}/smplayer/themes
%{_datadir}/smplayer/themes/*

%changelog


