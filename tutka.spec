%define name	tutka
%define version 0.12.4
%define release %mkrel 5
%define schemas tutka

Name: 	 	%{name}
Summary: 	Tracker-style MIDI sequencer
Version: 	%{version}
Release: 	%{release}

Source:		http://savannah.nongnu.org/download/tutka/%{name}-%{version}.tar.bz2
URL:		http://www.nongnu.org/tutka/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig libgnomeui2-devel libxml2-devel libglade2.0-devel libalsa-devel desktop-file-utils ImageMagick

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
%configure2_5x --disable-schemas-install
make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --remove-category="Application" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

#icons

mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
mkdir -p $RPM_BUILD_ROOT%{_liconsdir}
mkdir -p $RPM_BUILD_ROOT%{_miconsdir}

cp %{name}.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
cp %{name}.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32 %{name}.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -scale 32 %{name}.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{name}.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert -scale 16 %{name}.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%post_install_gconf_schemas %{schemas}
%endif

%preun
%preun_uninstall_gconf_schemas %{schemas}
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/gconf/schemas/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%name
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
