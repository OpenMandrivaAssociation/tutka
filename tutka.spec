%define name	tutka
%define version 0.12.3
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Tracker-style MIDI sequencer
Version: 	%{version}
Release: 	%{release}

Source:		http://savannah.nongnu.org/download/tutka/%{name}-%{version}.tar.bz2
URL:		http://www.nongnu.org/tutka/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig libgnomeui2-devel libxml2-devel libglade2.0-devel

%description
Tutka is a free (as in freedom) tracker style MIDI sequencer for GNU/Linux
(and other systems; only GNU/Linux is supported at this time though). It is
similar to programs like SoundTracker, ProTracker and FastTracker except that
it does not support samples and is meant for MIDI use only.

Tutka uses a custom XML based file format for storing songs. Songs in OctaMED
SoundStudio's MMD2 file format can also be loaded and saved. 

%prep
%setup -q

%build
%configure2_5x
make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="sound_section.png" needs="x11" title="Tutka" longtitle="Tracker-style sequencer" section="Multimedia/Sound"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/gconf/schemas/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%name
%{_menudir}/%name

