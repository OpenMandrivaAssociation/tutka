%define name	tutka
%define version 0.12.5
%define release 3
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
BuildRequires:	pkgconfig libgnomeui2-devel libxml2-devel libglade2.0-devel libalsa-devel desktop-file-utils imagemagick

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


%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.12.5-2mdv2011.0
+ Revision: 677841
- rebuild to add gconftool as req

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.12.5-1
+ Revision: 645464
- update to new version 0.12.5

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.12.4-6mdv2010.0
+ Revision: 434471
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.12.4-5mdv2009.0
+ Revision: 261674
- rebuild
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.12.4-2mdv2008.1
+ Revision: 140921
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jun 02 2007 Adam Williamson <awilliamson@mandriva.org> 0.12.4-2mdv2008.0
+ Revision: 34748
- correct category removal

* Thu May 31 2007 Adam Williamson <awilliamson@mandriva.org> 0.12.4-1mdv2008.0
+ Revision: 33035
- BuildRequires libalsa-devel
- generate MDV-style and fd.o icons
- remove old menu, correct XDG menu
- install gconf schemas correctly (with macro)
- new release 0.12.4


* Wed Nov 30 2005 Lenny Cartier <lenny@mandriva.com> 0.12.3-2mdk
- do not use parallel build

* Fri Nov 04 2005 Austin Acton <austin@mandriva.org> 0.12.3-1mdk
- New release 0.12.3

* Wed Mar 30 2005 Austin Acton <austin@mandrake.org> 0.12.2-1mdk
- New release 0.12.2

* Fri Jan 14 2005 Austin Acton <austin@mandrake.org> 0.12.0-1mdk
- 0.12.0
- source URL
- configure 2.5

* Tue Oct 14 2003 Austin Acton <aacton@yorku.ca> 0.11.1-1mdk
- initial package

