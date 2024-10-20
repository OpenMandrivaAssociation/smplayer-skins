Name:		smplayer-skins
Version:	20.11.0
Release:	1
Summary:	Skins for SMPlayer
# Actually, various
License:	GPLv2
Group:		Video
URL:		https://smplayer.sourceforge.net/
Source0:	http://downloads.sourceforge.net/smplayer/%{name}-%{version}.tar.bz2
Requires:	smplayer >= 0.8.2
BuildArch:	noarch
BuildRequires:	cmake(Qt5Core)

%description
This package provides skin themes for SMPlayer.

SMPlayer intends to be a complete front-end for Mplayer, from basic features
like playing videos, DVDs, and VCDs to more advanced features like support
for Mplayer filters and more. One of the main features is the ability to
remember the state of a played file, so when you play it later it will resume
at the same point and with the same settings. smplayer is developed with
the Qt toolkit, so it's multi-platform.

%prep
%autosetup -p1

%build
export PATH=%{_libdir}/qt5/bin:$PATH
%make_build

%install
#%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_datadir}/smplayer/themes
cp -a themes/* %{buildroot}%{_datadir}/smplayer/themes

%files
%doc README.txt Changelog COPYING*.txt
%dir %{_datadir}/smplayer/themes
%{_datadir}/smplayer/themes/*

