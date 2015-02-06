Name:		smplayer-skins
Version:	20121029
Release:	3
Summary:	Skins for SMPlayer
# Actually, various
License:	GPLv2
Group:		Video
URL:		http://smplayer.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Requires:	smplayer >= 0.8.2
BuildArch:	noarch

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

%build
# nothing

%install
%makeinstall_std PREFIX=%{_prefix}

%files
%doc README.txt Changelog COPYING*.txt
%dir %{_datadir}/smplayer/themes
%{_datadir}/smplayer/themes/*

