# v21.48.22
#%define commit ddeac82e13aa889964c31e732f7cf52e
# v22.20.13
#%define commit 0960631ea56171af883e1caec8a1a8dd
# v23.19
#%define commit 3cbd24759aead17e4172998e5f350faa
# v23.19.5
#%define commit 78577f83ece00062d3de6d4183274f80
# v23.19.6
#%define commit 2b513a78747c89f53608e97096b22c7b
# v23.19.9
#%define commit 9b1a0d289c3fa4871a3ae1c4d9c12eda
# v23.19.10
#%define commit 03d4b336be46df720f808783b6d71da3
# v24.13.4
%define commit 9d2c9adeaeda6ba3f5c1e9705b24fc6e
%define livearches %{ix86} x86_64 ppc ppc64 ppc64le

Summary: Graphical system installer
Name:    anaconda
Version: 24.13.4
Release: 1%{?dist}
License: GPLv2+ and MIT
Group:   Applications/System
URL:     http://fedoraproject.org/wiki/Anaconda
Epoch:   1

# To generate Source0 do:
# git clone https://github.com/rhinstaller/anaconda
# git checkout -b archive-branch anaconda-%%{version}-%%{release}
# ./autogen.sh
# make dist
Source0: http://pkgs.fedoraproject.org/repo/pkgs/anaconda/%{name}-%{version}.tar.bz2/%{commit}/%{name}-%{version}.tar.bz2
Source1: install-button.png
#Patch0: 0001-fedora-welcome-rebranding.patch


# Versions of required components (done so we make sure the buildrequires
# match the requires versions of things).

# Also update in AM_GNU_GETTEXT_VERSION in configure.ac
%define gettextver 0.19.1
%define intltoolver 0.31.2-3
%define pykickstartver 2.20
%define dnfver 0.6.4
%define partedver 1.8.1
%define pypartedver 2.5-2
%define nmver 0.9.9.0-10.git20130906
%define dbusver 1.2.3
%define mehver 0.23-1
%define firewalldver 0.3.5-1
%define utillinuxver 2.15.1
%define dracutver 034-7
%define isomd5sum 1.0.10
%define fcoeutilsver 1.0.12-3.20100323git
%define iscsiver 6.2.0.873-26
%define rpmver 4.10.0
%define libarchivever 3.0.4
%define langtablever 0.0.34
%define libxklavierver 5.4
%define libtimezonemapver 0.4.1-2
%define helpver 22.1-1

BuildRequires: audit-libs-devel
BuildRequires: gettext >= %{gettextver}
BuildRequires: gtk3-devel
BuildRequires: gtk-doc
BuildRequires: gtk3-devel-docs
BuildRequires: glib2-doc
BuildRequires: gobject-introspection-devel
BuildRequires: glade-devel
BuildRequires: intltool >= %{intltoolver}
BuildRequires: libgnomekbd-devel
BuildRequires: libxklavier-devel >= %{libxklavierver}
BuildRequires: pango-devel
BuildRequires: python3-kickstart >= %{pykickstartver}
%if ! 0%{?rhel}
BuildRequires: python3-bugzilla
%endif
BuildRequires: python3-devel
BuildRequires: python3-nose
BuildRequires: systemd
# rpm and libarchive are needed for driver disk handling
BuildRequires: rpm-devel >= %{rpmver}
BuildRequires: libarchive-devel >= %{libarchivever}
%ifarch %livearches
BuildRequires: desktop-file-utils
%endif
%ifarch s390 s390x
BuildRequires: s390utils-devel
%endif
BuildRequires: libtimezonemap-devel >= %{libtimezonemapver}

# Tools used by the widgets resource bundle generation
BuildRequires: gdk-pixbuf2-devel
BuildRequires: libxml2

Requires: anaconda-core = 1:%{version}-%{release}
Requires: anaconda-gui = 1:%{version}-%{release}
Requires: anaconda-tui = 1:%{version}-%{release}

%description
The anaconda package is a metapackage for the Anaconda installer.

%package core
Summary: Core of the Anaconda installer
Epoch:   1
Requires: python3-dnf >= %{dnfver}
Requires: python3-blivet >= 1:1.12
Requires: python3-meh >= %{mehver}
Requires: libreport-anaconda >= 2.0.21-1
Requires: libselinux-python3
Requires: rpm-python3 >= %{rpmver}
Requires: parted >= %{partedver}
Requires: python3-pyparted >= %{pypartedver}
Requires: python3-requests
Requires: python3-requests-file
Requires: python3-requests-ftp
Requires: python3-kickstart >= %{pykickstartver}
Requires: langtable-data >= %{langtablever}
Requires: langtable-python3 >= %{langtablever}
Requires: authconfig
Requires: firewalld >= %{firewalldver}
Requires: util-linux >= %{utillinuxver}
Requires: python3-dbus
Requires: python3-pwquality
Requires: python3-pytz
Requires: realmd
Requires: teamd
%ifarch %livearches
Requires: usermode
%endif
%ifarch s390 s390x
Requires: openssh
%endif
Requires: isomd5sum >= %{isomd5sum}
Requires: createrepo_c
Requires: NetworkManager >= %{nmver}
Requires: NetworkManager-glib >= %{nmver}
Requires: NetworkManager-team
Requires: dhclient
Requires: kbd
Requires: chrony
Requires: python3-ntplib
Requires: rsync
Requires: systemd
%ifarch %{ix86} x86_64
Requires: fcoe-utils >= %{fcoeutilsver}
%endif
Requires: python3-iscsi-initiator-utils >= %{iscsiver}
%ifarch %{ix86} x86_64
%if ! 0%{?rhel}
Requires: hfsplus-tools
%endif
%endif
%ifnarch aarch64
Requires: kexec-tools
%endif
Requires: python3-pid
Requires: python3-ordered-set >= 2.0.0

Requires: python3-coverage >= 4.0-0.12.b3

# required because of the rescue mode and VNC question
Requires: anaconda-tui = 1:%{version}-%{release}

# Make sure we get the en locale one way or another
Requires: glibc-langpack-en

Obsoletes: anaconda-images <= 10
Provides: anaconda-images = %{version}-%{release}
Obsoletes: anaconda-runtime < %{version}-%{release}
Provides: anaconda-runtime = %{version}-%{release}
Obsoletes: booty <= 0.107-1

%description core
The anaconda-core package contains the program which was used to install your
system.

%package gui
Summary: Graphical user interface for the Anaconda installer
Epoch: 1
Requires: anaconda-core = 1:%{version}-%{release}
Requires: anaconda-widgets = 1:%{version}-%{release}
Requires: python3-meh-gui >= %{mehver}
Requires: adwaita-icon-theme
Requires: system-logos
Requires: tigervnc-server-minimal
Requires: libxklavier >= %{libxklavierver}
Requires: libgnomekbd
Requires: libtimezonemap >= %{libtimezonemapver}
Requires: nm-connection-editor
%ifarch %livearches
Requires: zenity
%endif
Requires: keybinder3
%ifnarch s390 s390x
Requires: NetworkManager-wifi
%endif
Requires: anaconda-user-help >= %{helpver}
Requires: yelp
Requires: python3-gobject-base

# Needed to compile the gsettings files
BuildRequires: gsettings-desktop-schemas
BuildRequires: metacity

%description gui
This package contains graphical user interface for the Anaconda installer.

%package tui
Summary: Textual user interface for the Anaconda installer
Epoch: 1
Requires: anaconda-core = 1:%{version}-%{release}

%description tui
This package contains textual user interface for the Anaconda installer.

%package widgets
Summary: A set of custom GTK+ widgets for use with anaconda
Epoch: 1
Group: System Environment/Libraries
Requires: python3

%description widgets
This package contains a set of custom GTK+ widgets used by the anaconda installer.

%package widgets-devel
Summary: Development files for anaconda-widgets
Epoch: 1
Group: Development/Libraries
Requires: glade
Requires: %{name}-widgets%{?_isa} = %{version}-%{release}

%description widgets-devel
This package contains libraries and header files needed for writing the anaconda
installer.  It also contains Python and Glade support files, as well as
documentation for working with this library.

%package dracut
Summary: The anaconda dracut module
Requires: dracut >= %{dracutver}
Requires: dracut-network
Requires: dracut-live
Requires: xz
Requires: python3-kickstart
Epoch: 1

%description dracut
The 'anaconda' dracut module handles installer-specific boot tasks and
options. This includes driver disks, kickstarts, and finding the anaconda
runtime on NFS/HTTP/FTP servers or local disks.

%prep
%setup -q
#convert Fedora name to Korora.
find . -name *.po -print0 | xargs -0 sed -i 's/Fedora/Korora/g'
sed -i 's|Fedora|Korora|g' data/liveinst/gnome/fedora-welcome
sed -i 's|Fedora|Korora|g' data/liveinst/gnome/fedora-welcome.desktop*

mv ./pyanaconda/installclasses/fedora.py ./pyanaconda/installclasses/korora.py
sed -i s/fedora/korora/g ./pyanaconda/installclasses/korora.py
sed -i s/Fedora/Korora/g ./pyanaconda/installclasses/korora.py
sed -i 's/efi_dir = "korora"/efi_dir = "fedora"/g' ./pyanaconda/installclasses/korora.py

cp -f %{SOURCE1} data/liveinst/gnome/

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{make_install}
find %{buildroot} -type f -name "*.la" | xargs %{__rm}

# Create an empty directory for addons
mkdir %{buildroot}%{_datadir}/anaconda/addons

%ifarch %livearches
desktop-file-install ---dir=%{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/liveinst.desktop
%endif
# NOTE: If you see "error: Installed (but unpackaged) file(s) found" that include liveinst files,
#       check the IS_LIVEINST_ARCH in configure.ac to make sure your architecture is properly defined

%find_lang %{name}

%post widgets -p /sbin/ldconfig
%postun widgets -p /sbin/ldconfig


%ifarch %livearches
%post
update-desktop-database &> /dev/null || :
%endif

%ifarch %livearches
%postun
update-desktop-database &> /dev/null || :
%endif

%files

%files core -f %{name}.lang
%license COPYING
%{_unitdir}/*
%{_prefix}/lib/systemd/system-generators/*
%{_bindir}/instperf
%{_bindir}/anaconda-disable-nm-ibft-plugin
%{_sbindir}/anaconda
%{_sbindir}/handle-sshpw
%{_datadir}/anaconda
%{_prefix}/libexec/anaconda
%exclude %{_prefix}/libexec/anaconda/dd_*
%{python3_sitearch}/pyanaconda/*
%exclude %{python3_sitearch}/pyanaconda/rescue.py*
%exclude %{python3_sitearch}/pyanaconda/__pycache__/rescue.*
%exclude %{python3_sitearch}/pyanaconda/ui/gui/*
%exclude %{python3_sitearch}/pyanaconda/ui/tui/*
%{_bindir}/analog
%{_bindir}/anaconda-cleanup
%ifarch %livearches
%{_bindir}/liveinst
%{_sbindir}/liveinst
%config(noreplace) %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/security/console.apps/*
%{_libexecdir}/liveinst-setup.sh
%{_datadir}/applications/*.desktop
%{_sysconfdir}/xdg/autostart/*.desktop
%endif

%files gui
%{python3_sitearch}/pyanaconda/ui/gui/*
%{_datadir}/anaconda/window-manager/glib-2.0/schemas/*
%{_datadir}/themes/Anaconda/*

%files tui
%{python3_sitearch}/pyanaconda/rescue.py
%{python3_sitearch}/pyanaconda/__pycache__/rescue.*
%{python3_sitearch}/pyanaconda/ui/tui/*

%files widgets
%{_libdir}/libAnacondaWidgets.so.*
%{_libdir}/girepository*/AnacondaWidgets*typelib
%{python3_sitearch}/gi/overrides/*

%files widgets-devel
%{_libdir}/libAnacondaWidgets.so
%{_includedir}/*
%{_datadir}/glade/catalogs/AnacondaWidgets.xml
%{_datadir}/gtk-doc

%files dracut
%dir %{_prefix}/lib/dracut/modules.d/80%{name}
%{_prefix}/lib/dracut/modules.d/80%{name}/*
%{_prefix}/libexec/anaconda/dd_*

%changelog
* Mon Apr 18 2016 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 24.13.4-1
- Refresh metadata when updates checkbox changes (#1211907) (bcl)
- network: handle null wireless AP SSID object (#1262556) (awilliam)
- Show network spoke in the TUI reconfig mode (#1302165) (mkolman)
- Fix iSCSI kickstart options aren't generated (#1252879) (jkonecny)
- Make the list-harddrives script mode robust (mkolman)
- network: don't set 803-3-ethernet.name setting (#1323589) (rvykydal)
- Log non-critical user/group errors (#1308679) (bcl)

* Mon Apr 04 2016 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 24.13.3-1
- Don't use booleans in Requires (#1323314) (dshea)
- Set CSS names on all of the anaconda classes. (#1322036) (dshea)
- Don't crash if no groups are specified (#1316816) (dshea)
- Fix only one address is shown in anaconda (#1264400) (jkonecny)
- Use an icon that exists in Adwaita for the dasd confirmation (#1316601)
  (dshea)

* Thu Mar 31 2016 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 24.13.2-1
- Require that the English locale data be available. (#1315494) (dshea)
- Revert "Change the default locale to C.UTF-8 (#1312607)" (#1315494) (dshea)
- Make windows in metacity closable (#1319590) (dshea)
- Fix the use of CSS psuedo-classes in the widgets. (dshea)
- Use a lock for repoStore access (#1315414) (bcl)

* Wed Mar 09 2016 Samantha N. Bueno <sbueno+anaconda@redhat.com> - 24.13.1-1
- don't install kernel-PAE on x86_64 (#1313957) (awilliam)
- except block in py3.5 undefines the variable (bcl)
- Remove some history from the liveinst setup. (#1313098) (dshea)
- Do not run the liveinst setup if not in a live environment. (#1313098) (dshea)
- Set GDK_BACKEND=x11 before running anaconda from liveinst. (#1313098) (dshea)
- Run zz-liveinst as an autostart application (#1313098) (dshea)
- Translate the help button. (dshea)
- Translate the required space labes in resize.py (dshea)
- Add device id to dasdfmt screen. (#1269174) (sbueno+anaconda)
- Unify displayed columns in custom spoke dialogs. (#1289577) (sbueno+anaconda)
- Show some confirmation to users if adding a DASD was successful. (#1259016) (sbueno+anaconda)
- Hotfix for missing storage in payload class (#1271657) (jkonecny)
- Use the default levelbar offset values. (dshea)
- Do not change the GUI language to a missing locale. (#1312607) (dshea)
- Don't crash when setting an unavailable locale (#1312607) (dshea)
- Change the default locale to C.UTF-8 (#1312607) (dshea)
- Update the libtool version-info. (dshea)
- Use CSS to style the internal widgets. (dshea)
- Move the widgets pixmaps into resources. (dshea)
- Add a resource bundle to libAnacondaWidgets (dshea)
- Rename show_arrow and chosen_changed to show-arrow and chosen-changed (dshea)
- Remove an invalid transfer notation. (dshea)
- Stop using SGML in the docs. (dshea)
- Change the install test URL. (dshea)
- NTP should have better behavior (#1309396) (jkonecny)
- Update zanata.xml file for f24-branch. (sbueno+anaconda)
- Manually set clock shifts on UI idle (#1251044) (rmarshall)
- Don't remove selected shared part when Delete all (#1183880) (jkonecny)
- Don't delete shared/boot parts in deleteAll (#1183880) (jkonecny)

* Fri Feb 19 2016 Brian C. Lane <bcl@redhat.com> - 24.13-1
- tests/gui enhancements (atodorov)
- Fix gui tests for anaconda move to anaconda.py (atodorov)
- Use a different ipmi command to log events. (clumens)
- Clarify that a string in list-screens is actually a regex. (clumens)
- Merge pull request #513 from wgwoods/update-dd-docs (wwoods)
- updated driver updates docs (wwoods)
- Add specification for the user interaction config file (mkolman)
- Update zanata webui URL in translation doc. (dlehman)
- Tweak partition removal in Custom spoke (jkonecny)
- Do not skip evaluation after removing partitions (jkonecny)
- Import iutil earlier so we can use ipmi_report from check_for_ssh. (clumens)
- Make disconnect_client_callbacks more resilient (#1307063). (clumens)
- Move the langpacks install into to a separate function. (dshea)
- Fix _find_by_title method in Accordion (jkonecny)

* Fri Feb 12 2016 Brian C. Lane <bcl@redhat.com> - 24.12-1
- Use host storage for directory or image install dnf download (bcl)
- Log payloadError so we know why installation failed. (bcl)
- Add the addons directory to the rpm. (dshea)
- Use the packaged version of ordered-set (dshea)
- Remove an unused import (dshea)
- Add an uninstall hook for the renamed anaconda (dshea)
- Make langpack work in DNF (#1297823) (jsilhan)
- New Anaconda documentation - 24.11 (bcl)

* Fri Feb 05 2016 Brian C. Lane <bcl@redhat.com> - 24.11-1
- Fix makeupdates for anaconda move to anaconda.py (bcl)
- Rename ./anaconda to ./anaconda.py to work around coverage.py #425 (atodorov)
- Remove special handling for interruptible system calls. (dshea)
- Handle PEP 3101 strings in the gettext context check (dshea)
- Improve RHS summary strings in multiselection (#1265620) (jkonecny)
- Increase GI version required of AnacondaWidgets (jkonecny)
- Increment version of g-introspection for widgets (jkonecny)
- Increment the AnacondaWidgets version (jkonecny)
- Switch to the new Initial Setup unit name (#1299210) (mkolman)
- Uncomment self.check_lang_locale_views in tests/gui/ (atodorov)
- Add dogtail to test requirements (atodorov)
- Add config for easier combining of kickstart and Jenkins coverage data
  (atodorov)
- Apply the fallback style to anaconda selectors. (dshea)
- Redo the stylesheet for Gtk 3.19+ (dshea)
- Directly overwrite /usr/share/anaconda/anaconda-gtk.css (dshea)
- Merge pull request #463 from dashea/translation-tests (dshea)
- Display the name of the addon while executing it (bcl)
- Add page selection summary to the right side (#1265620) (jkonecny)
- Ask when removing new items in multiselection (#1265620) (jkonecny)
- Add multiselection with SHIFT key (#1265620) (jkonecny)
- Use show_arrow feature implemented in Selector (#1265620) (jkonecny)
- Add new property to show/hide arrow in Selector (#1265620) (jkonecny)
- Change selection logic when opening Page (#1265620) (jkonecny)
- Add new BasePage class (#1265620) (jkonecny)
- Add signal and methods to MountpointSelector (#1265620) (jkonecny)
- Fix errors with multiselection (#1265620) (jkonecny)
- Accordion class now process events for selectors (#1265620) (jkonecny)
- Change cammel case for accordion.py to new pep8 (jkonecny)
- Move selection logic from custom spoke to accordion (#1265620) (jkonecny)
- Modify ConfirmDeleteDialog now the checkbox is optional (#1265620) (jkonecny)
- Multiselection works in GUI with remove (#1265620) (jkonecny)
- Add multiselection to Accordion with control key (#1265620) (jkonecny)
- Remove bad translations from the source tarball. (dshea)
- Treat warnings from xgettext as errors. (dshea)
- Run translation-canary tests from make check. (dshea)
- Do not run pylint on translation-canary (dshea)
- Squashed 'translation-canary/' content from commit 5a45c19 (dshea)

* Fri Jan 29 2016 Brian C. Lane <bcl@redhat.com> - 24.10-1
- Add a finished method to spokes (#1300499) (bcl)
- Handle DeviceConfiguration with con = None (#1300499) (bcl)
- Log detailed information about installed packages (bcl)
- s/KickstartValueError/KickstartParseError. (clumens)
- Move requiredDeviceSize to the main Payload class (#1297905) (dshea)

* Fri Jan 08 2016 Brian C. Lane <bcl@redhat.com> - 24.9-1
- Handle unexpected DNF exit (bcl)
- Fix bad space needed messages (jkonecny)
- nosetests-3.5 is now the right version. (clumens)
- Ignore a pylint error about how we're using Popen (dshea)
- Mark an unused variable as unused (dshea)
- Ignore type-related errors for types pylint can't figure out (dshea)
- Import errors are just regular errors now (dshea)
- Replace the remaining log.warn calls with log.warning. (dshea)
- Fix an erroneously bare raise statement (dshea)
- Replace the deprecated assertEquals with assertEqual (dshea)
- Don't add a None to the list of things to unmount on ostree installs.
  (clumens)

* Wed Dec 02 2015 Brian C. Lane <bcl@redhat.com> - 24.8-1
- Fix pylint problems in the gui testing code. (clumens)
- Merge 9c5e02392d0401a3bd0adecedea03535595773ef into
  67b569253c724639c2490f5fab70f7111f699b3f (atodorov)
- Fix the replacement suggestion for "hostname" (dshea)
- Automatically generate sr (dshea)
- Fix PropertyNotFoundError PermHwAddress (#1269298) (jkonecny)
- Make sure python3.5 code can run in early initrd (bcl)
- Replace <list>.delete() with <list>.remove() in user.py (sujithpandel)
- Rename everything that still refers to LiveCD (atodorov)
- Updates to progress and storage tests (atodorov)
- Multiple changes to DogtailTestCase (atodorov)
- Move all Python files into the main gui/ directory (atodorov)
- Simplify tests by removing OutsideMixin and update Creator (atodorov)
- Modify existing tests to match latest anaconda behavior and environment
  (atodorov)
- Temporary disable test code which doesn't work (atodorov)
- Make tests/gui/ execute ./anaconda from git (atodorov)
- Add window title (#1280077) (mkolman)
- Replace execReadlines with check_output in parse-kickstart_test.py (bcl)
- Fix a spelling error in the hardware error message (#1284165). (clumens)

* Wed Nov 18 2015 Brian C. Lane <bcl@redhat.com> - 24.7-1
- Collect test-suite.log from all 'make check' invocations. Closes #452
  (atodorov)
- Fix parse-kickstart_test.py. (clumens)
- Remove mkdud.py. (clumens)
- Remove the kickstart_tests directory. (clumens)
- Always quote values in ifcfg- files (#1279131) (bcl)
- Include original kickstart in /root/original-ks.cfg (#1227939) (bcl)
- strip spaces from extlinux label and default (#1185624) (bcl)
- Report kernel failures during kickstart tests. (clumens)
- Make sure unicode in kickstart works. (dshea)
- Set the window icon (dshea)
- Only run space check in TUI if spokes are complete. (#1279413)
  (sbueno+anaconda)
- Allow a user's primary group to be created in --groups (#1279041) (dshea)
- Remove uses of broad-except. (dshea)
- Add a test for all that container minimization stuff. (clumens)
- Use the partition command in one of the kickstart_tests. (clumens)
- Don't clear the _currentIsoFile if another iso was selected (bcl)
- makeupdates: Include utils/handle-sshpw (bcl)
- Add --sshkey to kickstart sshpw command (#1274104) (bcl)
- Split exception description from exception traceback (jkonecny)
- Show DNF exception instead of silent exit (jkonecny)
- Combine results from all gettext_tests into one log file (atodorov)
- Try to run make ci with real translations. (dshea)
- Untranslate undisplayed TreeView column headers. (dshea)
- Add a test for hidden translatable strings (dshea)
- Add the translated string to markup error messages. (dshea)
- Test glade translations by default (dshea)
- Change the way glade tests are run. (dshea)
- Remove the accelerator test. (dshea)
- Add the test lib directory to $PYTHONPATH in the commit hook (dshea)
- network: create ifcfg files in tui if needed (#1268155) (rvykydal)
- Do not limit ONBOOT default setting to url and nfs installation methods
  (#1269264) (rvykydal)
- ibft: fix setting dracut boot args for static ibft nic configuration
  (#1267526) (rvykydal)
- network: Don't set --device link default for hostname only network cmd
  (#1272274) (rvykydal)
- network: assume --device=link as default also for ks on hd (#1085310)
  (rvykydal)
- network: use ibftx interface for iSCSI from iBFT in dracut (#1077291)
  (rvykydal)
- network: add s390 options to default ifcfg files (#1074570) (rvykydal)

* Fri Nov 06 2015 Brian C. Lane <bcl@redhat.com> - 24.6-1
- Fix a pylint error in the previous commits. (clumens)
- Honor ANACONDA_WIDGETS_OVERRIDES (atodorov)
- Load anaconda-gtk.css from ANACONDA_DATA if specified (atodorov)
- Use the correct path for ui categories (atodorov)
- Typo fix, it's ANACONDA_WIDGETS_DATA not ANACONDA_WIDGETS_DATADIR (atodorov)
- Allow wired network properties more grid space. (dshea)
- Improve language selection at low resolutions. (dshea)
- Make reclaim work with small screens and big labels (dshea)
- allow repo with only a name if it's a pre-defined one (#1277638) (awilliam)
- Only raise thread exceptions once (#1276579) (bcl)
- Use py3.4 crypt and salt (bcl)
- Be more careful with incomplete device types (#1256582) (dshea)
- Fix an import error in rpmostreepayload.py. (clumens)
- Fix Testing docs inclusion in Sphinx (bcl)
- Ignore interfaces with invalid VLAN IDs. (dshea)
- Cleaner logging of .treeinfo return conditions in dependant function.
  (riehecky)
- Update link to upstream kickstart docs (opensource)
- rpmostreepayload: Also unmount internal mounts during shutdown (walters)
- rpmostreepayload: Fix two issues with mounting (walters)
- Add a README for kickstart tests. (clumens)
- Make the documentation match the environment variable. (clumens)
- Check that cache PVs (if any) are in the VG the LV belongs to (#1263258)
  (vpodzime)
- Fix the alignment of the "Label" label in custom (dshea)
- Use unsafe caching during kickstart tests. (clumens)

* Wed Oct 28 2015 Brian C. Lane <bcl@redhat.com> - 24.5-1
- Improve install space required estimation (#1224048) (jkonecny)
- Update the on-disk snapshot of storage when adv. disks are added (#1267944)
  (vpodzime)
- Check that ipv6 kickstart outputs the right ip= (dshea)
- Change a variable name for pylint. (dshea)
- Do not run time_initialize for image and directory installations (#1274103)
  (bcl)
- Remove unused properties (dshea)
- Do not modify the kickstart user data until apply() (dshea)
- Make AdvancedUserDialog.run() more readable (dshea)
- Improve the behavior of the home directory input. (dshea)
- Stop setting inappropriate properties in ksdata. (dshea)
- Update the password strength bar during the password strength check. (dshea)
- Remove unnecessary grab_focus and set_sensitive calls (dshea)
- Use signal handlers in the user spoke more sensibly. (dshea)
- Fix potential issues with the username guesser. (dshea)
- Make kickstart tests growing LVs stricter (vpodzime)
- Point coverage.py to the full path of pyanaconda/ (atodorov)
- Don't set BOOTPROTO= when it isn't set (jbacik)
- Pass strings to blockdev.dasd_format, not a DASDDevice object. (#1273553)
  (sbueno+anaconda)
- Revert "Use yum to install the mock buildroot for now." (dshea)
- decode package name for /etc/sysconfig/kernel (RHBZ #1261569) (awilliam)
- Add tests for the more complicated command line options (dshea)
- Store fewer kinds of things in the dirinstall option. (dshea)
- Fix the parsing of selinux=0 (#1258569) (dshea)
- Include a local $ANACONDA_DATADIR in the test environment. (dshea)
- Move the command line arguments to anaconda_argparse. (dshea)
- Don't crash while logging binary output. (dshea)
- Decode program output even if there is no output (#1273145) (dshea)
- Add a test for _run_program with binary output (dshea)
- Test execWithCapture when the command outputs nothing. (dshea)
- Fix a long line in kickstart_tests/functions.sh. (clumens)
- Merge pull request #414 from vpodzime/master-lvm_log (vpodzime)
- Save the lvm.log Blivet may produce (vpodzime)

* Fri Oct 16 2015 Brian C. Lane <bcl@redhat.com> - 24.4-1
- Hide the places sidebar in the ISO chooser widget. (dshea)
- Use GtkResponseType values in the iso chooser dialog (dshea)
- Do not use deprecated getDevicesByInstance method (vtrefny)
- By default, skip those kickstart tests we know to be failing. (clumens)
- Fix pylint unused import (jkonecny)
- network: handle bridge device appearing before its connection (#1265593)
  (rvykydal)
- Use $KSTEST_URL in tests that still had dl.fp.o hardcoded. (dshea)
- Support CONNECT in the test proxy server. (dshea)
- Extract the file used by liveimg as a prereq (dshea)
- Convert the proxy script to a prereq. (dshea)
- Add a prereqs function to kickstart tests. (dshea)
- Fix traceback when trying to create list of unformatted DASDs. (#1268764)
  (sbueno+anaconda)
- network: handle missing connections of a device configured in GUI better
  (rvykydal)
- network: don't set NM_CONTROLLED=no for root on SAN. (rvykydal)
- Add support for other systemd units to kickstart service command (bcl)
- Merge pull request #388 from wgwoods/dd-in-initrd-fix (wwoods)
- Set the password checkbox for empty kickstart passwords. (dshea)
- Do not set the password input text with unencrypted passwords. (dshea)
- Install input checks before modifying the user GUI (#1256065) (dshea)
- Fix a lying error message in style_guide.py (dshea)
- Use "Enter" instead of "Return" for the keyboard key. (dshea)
- New Anaconda documentation - 24.3 (bcl)
- Include missing test files and scripts in Makefile.am/tarball (atodorov)
- dracut: accept inst.dd=[file:]/dd.iso (#1268792) (wwoods)
- Do not override StorageChecker.errors in StorageSpoke (#1252596) (vtrefny)
- Lookup IPv6 address without brackets (#1267872) (bcl)
- Mangle the boot device differently for systemd (#1241704) (dshea)
- Fail the media check if the systemd service failed to start. (dshea)

* Fri Oct 02 2015 Brian C. Lane <bcl@redhat.com> - 24.3-1
- Properly translate c-to-continue on the root selection screen (mkolman)
- Check minimal memory requirements properly (#1267673) (jstodola)
- Allow users to be created with an existing GID. (dshea)
- Add a test for creating a user with an existing GID. (dshea)
- Add tests for gids embmedded in the user groups list. (dshea)
- Allow the kickstart --groups list to specify GIDs. (dshea)
- Add a --groups argument to the user ks test. (dshea)
- Fix the locale pattern packages-instlangs-3 looks for. (dshea)
- Raise an error if osimg cannot be found (#1248673) (bcl)
- Use the bootloader raid levels for bootloader installation (#1266898) (bcl)
- Use otps.display_mode during early startup (#1267140) (mkolman)
- Mount stage2 cdrom after running driver-updates (#1266478) (bcl)
- Get rid of an unused import in the user spoke. (clumens)
- Log crashes from the signal handler. (dshea)
- Save a core file when anaconda crashes. (dshea)
- Keep environment selection when reentering the software spoke (#1261393)
  (mkolman)
- Only show the user spoke if no users are specified in kickstart (#1253672)
  (mkolman)
- Fix 'cat: /tmp/dd_disk: No such file or directory' (#1251394) (jkonecny)
- Do not display curl 404 errors that can be safely ignored (vtrefny)
- Catch blkid failure in driver-updates (#1262963) (bcl)
- Add kickstart tests for %%packages --instLangs (dshea)
- Do not display markup in showDetailedError. (dshea)
- Skip OEMDRV if interactive DD is requested (#1254270) (bcl)
- Drivers are simply under /run/install/DD-x/ (#1254270) (bcl)
- Fix branding when iso is downloaded from nfs or hd (#1252756) (jkonecny)
- Use yum to install the mock buildroot for now. (dshea)
- Rename the gettext tests (dshea)
- Bring back the KSTEST_HTTP_ADDON_REPO substitution in nfs-repo-and-addon.sh
  (clumens)
- Run substitution checks on the right kickstart file. (clumens)
- Tell gettext that anaconda is not a GNU package. (dshea)
- Ignore environment modification warnings in docs/conf.py (dshea)
- Check for unsubstituted strings before running a test. (dshea)
- Autopart use 90%% of disk capacity for required space compare (#1224048)
  (jkonecny)
- Fix include packages install size when downloading on root (#1224048)
  (jkonecny)
- Enable and improve the check for swap LV size in LVM cache kickstart tests
  (vpodzime)
- make-sphinx-docs: Add modules needed to document tests (bcl)
- Add test documentation (atodorov)
- Fix how the reqpart test checks for /boot, again. (clumens)
- Add a way to get default settings when running the kickstart_tests. (clumens)
- Change how we ignore non-tests in kickstart_tests. (clumens)
- Various fixes to substitution strings in kickstart_tests. (clumens)
- Move kickstart_test .ks files to .ks.in. (clumens)

* Fri Sep 11 2015 Brian C. Lane <bcl@redhat.com> - 24.2-1
- Handle driver rpms retrieved via network (#1257916) (bcl)
- Fix the types passed to chown_dir_tree (#1260318) (dshea)
- Add a test for home directory reuse (dshea)
- Use MDRaidArrayDevice.members instead of .devices (dshea)
- Make sure anaconda reads in ks file from OEMDRV device. (#1057271)
  (sbueno+anaconda)
- Try to deal with expected errors from devicetree.populate (#1257648)
  (vpodzime)
- Revert "Temporarily disable generating a coverage report." (clumens)
- Fix a DBus InvalidProperty handling (jkonecny)
- Fix another bash syntax problem in kickstart-genrules.sh (#1057271)
  (sbueno+anaconda)
- Add a test for the rootpw kickstart command (dshea)
- Add tests for setRootPassword (dshea)
- Add a /boot partition to the reqpart test. (clumens)
- Fix up a statement that's not assigned to anything. (clumens)
- Temporarily disable generating a coverage report. (clumens)
- Don't try to concatenate a list with a string (#1252444) (mkolman)
- Activate coverage for tests executed with sudo (atodorov)
- set sysroot correctly when setting root password (#1260875) (awilliam)
- Add a test for kickstarts that %%include a URL (dshea)
- Add missing python dependencies for requests. (#1259506) (dshea)
- Serve the http addon repos from the test tmpdir (dshea)
- Make make-addon-pkgs easier to use from within a test (dshea)
- Add a simple http server for use in kickstart tests. (dshea)
- Add a script to print an IP address for the host. (dshea)
- Add a cleanup hook that can be defined by kickstart tests (dshea)
- Move kickstart test support files into a separate directory. (dshea)
- Fix a python3 related error in the pre-commit hook (dshea)
- network: gui spoke TODO cleanup (rvykydal)
- libnm in spoke: add missing connection for eth device with Configure
  (rvykydal)
- libnm in spoke: allow adding missing connection for eth device externally
  (rvykydal)
- libnm in spoke: wait for valid state of added device before adding to list
  (rvykydal)
- libnm in spoke: use libmn objects instead of names an uuids (device on/off)
  (rvykydal)
- libnm in spoke: to check if device is activated just use its object
  (rvykydal)
- libnm in spoke: use connnection objects instead of uuids (edit connection)
  (rvykydal)
- libnm in spoke: refresh early when device is added (rvykydal)
- libnm in spoke: use connection object instead of uuid (DeviceConfiguration)
  (rvykydal)
- libnm in spoke: share nm client in standalone and normal spoke (rvykydal)
- libnm in spoke: add enterprise wpa connection using libnm client (rvykydal)
- libnm in spoke: use AccessPoint object in place of ssid bytearray (rvykydal)
- libnm in spoke: delete connection using libnm client (rvykydal)
- libnm in spoke: replace python-dbus workaround calls for ap security flags
  (rvykydal)
- libnm in spoke: call get_data() on ap.get_ssid() result to get ssid bytes
  (rvykydal)
- libnm in spoke: showing ip configuration of a device (rvykydal)
- libnm in spoke: NMClient -> NM.Client (rvykydal)
- libnm in spoke: gi.NetworkManager -> gi.NM (rvykydal)
- libnm in spoke: Revert "Fix crash when new device appear in Welcome screen
  (#1245960)" (rvykydal)
- libnm in spoke: Revert "Fix crash when connections are changing (#1245960)"
  (rvykydal)
- Add an ignoredisk --drives= test. (clumens)
- Add a test for the reqpart command. (clumens)
- Grab anaconda.coverage on tests that reimplement validate(). (clumens)
- Install driver-updates (dshea)
- Fix a typo in service enablement in kickstart.py. (clumens)
- Get rid of the extraneous cats and greps in user.ks. (clumens)
- Add sshkey testing to the user kickstart_test. (clumens)
- Add a kickstart test in Arabic. (clumens)
- Verify Initial Setup services are present before turning them ON/OFF
  (#1252444) (mkolman)
- Don't crash if the Japanese PC-98 keyboard is selected (#1190589) (mkolman)
- Report on all local files and exclude what we don't need instead of
  explicitly including paths we may not be aware of. (atodorov)
- Change "failed to download" messages from critical to warning. (clumens)
- getcode -> status_code in a live payload error message. (clumens)
- Fix a bash error in kickstart-genrules.sh (#1057271) (sbueno+anaconda)
- specify if=virtio,cache=none for VM drives (atodorov)
- update the test b/c latest anaconda doesn't allow weak passwords (atodorov)
- Specify format=raw to avoid warning from qemu (atodorov)
- update for Python3 nose (atodorov)
- Add a services.sh file to match the existing services.ks. (clumens)
- Add types to all existing kickstart tests. (clumens)
- Add the ability to mark kickstart tests with a type. (clumens)
- Run nm-connection-editor with the --keep-above flag (#1231856) (mkolman)

* Mon Aug 31 2015 Brian C. Lane <bcl@redhat.com> - 24.1-1
- Add a test for the user and group creation functions. (dshea)
- Get rid of libuser. (#1255066) (dshea)
- s/$releasever/rawhide/ (clumens)
- LVM on RAID kickstart test (vpodzime)
- unbuffered read in python3 only works for binary (bcl)
- don't crash if no environment set in interactive (#1257036) (awilliam)
- network: compare with ssid bytes, not str (rvykydal)
- Add dependencies for running the tests/gui tests (atodorov)
- Fix first run environment setup in software spoke (#1257036) (jkonecny)
- Stop pretending liveinst+rescue is supported (#1256061). (clumens)
- Defer to Fedora distro-wide settings for password strength (#1250746) (dshea)
- New Anaconda documentation - 24.0 (bcl)
- Do a better job reporting failures from kickstart_tests. (clumens)
- Preserve coverage results from running the kickstart_tests. (clumens)

* Mon Aug 24 2015 Brian C. Lane <bcl@redhat.com> - 24.0-1
- Remove from the docs repo=hd installation with installable tree (jkonecny)
- Fix a race between a window continuing and the next starting (#1004477)
  (dshea)
- Start hubs with the buttons insensitive. (dshea)
- Do not replace the standard streams if not necessary. (dshea)
- Fix inst.repo=hd: is not working (#1252902) (jkonecny)
- Kickstart: Added SELinux test. (kvalek)
- Kickstart tests related to SELinux. (kvalek)
- Package install and debug message logging. (kvalek)
- Don't crash if incorrect environment is set in kickstart (#1234890) (mkolman)
- Fix I/O issues when anaconda is started without a locale. (dshea)
- Move locale environment logic into localization.py (dshea)
- network: fix configuring team in kickstart pre (#1254929) (rvykydal)
- Merge pull request #311 from atodorov/add_local_coverage (clumens)
- Merge pull request #308 from atodorov/rawhide_missing_deps (clumens)
- Enable test coverage in CI (atodorov)
- Fix the single-spoke TUI message for Python 3. (dshea)
- Merge pull request #291 from atodorov/update_coverage_switch (clumens)
- Add missing requirements (atodorov)
- Add basic kickstart tests for LVM Thin Provisioning (vpodzime)
- Use the default mirrorlist instead of fixed repo URL in kickstart tests
  (vpodzime)
- Destroy the keyboard layout dialog when finished (#1254150) (dshea)
- Do not encode the geoloc timezone to bytes (#1240812) (dshea)
- use inst.debug as alternative option to start coverage (atodorov)

* Mon Aug 17 2015 Brian C. Lane <bcl@redhat.com> - 23.20-1
- Skip source url checks when network is off (#1251130) (bcl)
- Don't set net.device to link if there is no ksdevice (#1085310) (bcl)
- Reading carrier while link is down raises IOError (#1085310) (bcl)
- Don't write nfs repos to the target system (#1246212) (bcl)
- Make sure username entered in TUI if create a user chosen. (#1249660)
  (sbueno+anaconda)
- Write the empty dnf langpacks.conf to the right directory (#1253469) (dshea)
- Add pyanaconda test for network.check_ip_address (jkonecny)
- Replace IPy package by ipaddress (jkonecny)
- Correctly check return code when running rpm from makeupdates (mkolman)
- Fix crash when new device appear in Welcome screen (#1245960) (jkonecny)
- Fix crash when connections are changing (#1245960) (jkonecny)
- Make LVM cache kickstart tests more robust (vpodzime)
- product.img buildstamp should override distribution buildstamp (#1240238)
  (bcl)
- On incomplete ks, don't automatically proceed with install. (#1034282)
  (sbueno+anaconda)
- Update the translation doc with zanata branching incantations.
  (sbueno+anaconda)
- Merge pull request #287 from kparal/patch-1 (clumens)
- boot-options.rst: add a note about nfsiso (kamil.paral)
- Few fixes and amendments for the boot_options.rst file (vpodzime)
- Prevent issues with encrypted LVs on renamed VGs (#1224045) (vpodzime)
- Create and use snapshot of on-disk storage with no modifications (#1166598)
  (vpodzime)
- Implement the class for storage snapshots (vpodzime)
- Prevent any changes in the StorageSpoke if just going back (vpodzime)
- Make StorageSpoke's on_back_clicked less complicated (vpodzime)
- Add kickstart tests for the LVM cache kickstart support (vpodzime)
- Disable packages-multilib, for now. (clumens)
- Make sure the liveimg test shuts down when it finishes. (clumens)
- Change how success is checked for the basic-ostree test. (clumens)

* Fri Aug 07 2015 Brian C. Lane <bcl@redhat.com> - 23.19-1
- Add basic support for LVM cache creation in kickstart (vpodzime)
- Use labels for the rest of the non-autopart test results. (dshea)
- Use a disk label to find the filesystem for escrow results (dshea)
- Use someone else's code for PID file management. (dshea)
- Prevent incomplete translations from making the TUI unusable (#1235617)
  (mkolman)
- Apply the environment substitutions more liberally in nfs-repo-and-addon
  (dshea)
- Use stage2=hd: instead of stage2=live: (dshea)
- Add test for liveimg kickstart command (bcl)
- Fix pre-install script execution (bcl)
- test pre-install kickstart section (bcl)
- Use sys.exit() instead of the exit() created by site.py. (dshea)
- Call ipmi_report before sys.exit (dshea)
- Add a test for proxy authentication (dshea)
- Add optional authentication to the proxy server (dshea)
- Add more tests to proxy-kickstart (dshea)
- Show an alternative prompt if a hub contains only a single spoke (#1199234)
  (mkolman)
- Add few docs and improvement in check_ip_address (jkonecny)
- Check whether files actually contain translatable strings. (dshea)
- Add specific error string to TUI user dialog (#1248421) (bcl)
- Make EditTUIDialog error generic (#1248421) (bcl)
- Fix and expand nfs-repo-and-addon.ks (dshea)
- Added a script to make the packages used by nfs-repo-and-addon (dshea)
- Implement the rest of the repo options in dnfpayload. (dshea)
- Fix kickstart test for bond interface creation (jkonecny)

* Fri Jul 31 2015 Brian C. Lane <bcl@redhat.com> - 23.18-1
- Move the proxy server script into a common file. (dshea)
- Use python3 for the proxy server and remove python2 compatibility (dshea)
- makePickle now needs to return bytes (bcl)
- gi.require_version raises ValueError (bcl)
- Remove duplicate signal setup block (bcl)
- Fix three bugs discovered by driverdisk-disk.ks (clumens)
- Fix error with OEMDRV ks auto-load check. (#1057271) (sbueno+anaconda)
- Make sure TUI is readable for non-latin languages (#1182562) (mkolman)
- Equalize capacity & mount point entries (#1212615) (dshea)
- Disable GRUB os_prober on POWER (#1193281) (rmarshall)
- Cancel Container Edit Sensitizes Update (#1168656) (rmarshall)
- Fix SoftwareSpoke._kickstarted. (dshea)
- Disable a Pylint false-positive (#1234896) (mkolman)
- Add support for autostep and --autoscreenshot (#1234896) (mkolman)
- Escape \'s in doc strings (dshea)
- Ellipsize the file system type combo box (#1212615) (dshea)
- Add graphviz to make-sphinx-doc script (jkonecny)
- Remove many of a documentation compilation errors (jkonecny)
- Add class diagrams to existing spokes and hubs (jkonecny)
- Add class diagram settings to documentation (jkonecny)
- Fix the UnusuableConfigurationError dialog (#1246915) (dshea)
- Chase pygobject's stupid moving target (dshea)
- Add missing translation contexts (dshea)
- Actually translate the container type labels (dshea)
- Check whether a translated string requires a context or comment. (dshea)
- Clean up the temporary pools virt-install makes. (clumens)
- Return the same object for repeated calls to __get__ (#1245423) (dshea)
- Use sys.exit instead of os._exit. (clumens)
- Add parentheses around the IPV6 regex fragment. (dshea)
- Add tests for IPv6 literals in URLs (dshea)
- Modify Installation Source Proxy Label (#11688554) (rmarshall)

* Fri Jul 24 2015 Brian C. Lane <bcl@redhat.com> - 23.17-1
- Fix Initial PPC PReP Boot Selector Name (#1172755) (rmarshall)
- Require a newer version of pykickstart (vpodzime)
- Use dictionaries is thread-safe manner. (dshea)
- Merge pull request #234 from wgwoods/master (wwoods)
- Auto-load ks.cfg if OEMDRV volume available. (#1057271) (sbueno+anaconda)
- Check the encrypt checkbox when encrypted specified in KS (vtrefny)
- Do not raise KickstartValueError for missing passphrase (vtrefny)
- Ask for encryption passphrase when not specified in ks (#1213096) (vtrefny)
- dracut: minor cleanup (wwoods)
- dracut: fix missing messages for inst.ks=cdrom (wwoods)
- Wait forever for kickstarts on CDROM (#1168902) (wwoods)
- Use abs_builddir instead of builddir so paths will look more reasonable.
  (clumens)
- Add a new makefile target that does everything needed for jenkins. (clumens)
- Merge pull request #228 from AdamWill/logind (dshea)
- Fix crash when mirrorlist checkbox is checked (jkonecny)
- Fix crash when user start typing proxy credentials (jkonecny)
- Check repository URL before leaving Source Spoke (jkonecny)
- Add IDs to identify addon repositories (jkonecny)
- Repositories can be checked without a selection (jkonecny)
- Consolidate the language environment variables. (dshea)
- Change the generated API indices slightly (dshea)
- Ignore "mountpoint" used a format specifier (dshea)
- filesystems -> file systems, per the style guide (dshea)
- Properly parameterize a translated string (dshea)
- Fix pylint errors in rescue.py. (dshea)
- Remove unused imports (dshea)
- Remove text.py from spec file (#965985) (sbueno+anaconda)
- Merge pull request #220 from AdamWill/1243962 (dshea)
- Fix adding 'boot=' option in FIPS mode (vtrefny)
- anaconda.target: Wants systemd-logind.service (#1222413) (awilliam)
- Remove the last usage of newt and get rid of it as a dependency (#965985)
  (sbueno+anaconda)
- Enable anaconda to use the new rescue mode. (#965985) (sbueno+anaconda)
- Get rid of unnecessary constants in constants_text. (#965985)
  (sbueno+anaconda)
- Get rid of some unnecessary files. (#965985) (sbueno+anaconda)
- Display verbose packaging errors to the user (bcl)
- Show source errors from refresh method (bcl)
- Fix the validate functions in the btrfs kickstart_tests. (clumens)
- Connect kickstart lang data to dnf-langpacks (#1051816) (dshea)
- Add simple_replace config file function (bcl)
- Remove some vestiges of the old packaging module (dshea)
- Remove window boot block detection functions. (dshea)
- Remove iutil.xprogressive_delay. (dshea)
- Simplify iutil.mkdirChain. (dshea)
- Decode wifi SSIDs into strings. (#1240398) (dshea)
- Actually use the temp directory so test files get cleaned up (dshea)
- Disable the output from rpmbuild (dshea)
- Remove stray references to python2. (dshea)
- Fix possible to start installation without network (#1221109) (jkonecny)
- Fix 'q' (to quit) do not work in TUI hub (jkonecny)
- act on the right objects when stripping URL protocols (#1243962) (awilliam)
- Fix 'App' object has no attribute 'queue' (#1243316) (jkonecny)

* Thu Jul 16 2015 Brian C. Lane <bcl@redhat.com> - 23.16-1
- fix storage writing for live and ostree installs (#1236937) (awilliam)
- Add O_CREAT to the open flags when extracting rpm files. (dshea)
- Move ostree gobject version check next to the import (#1243543) (bcl)
- Remove rpmfluff from the buildrequires. (dshea)
- Only import readline if readline is necessary. (dshea)
- use the right baseurl in run_install_test.sh. (clumens)
- Don't copy the environment when starting metacity. (dshea)
- Fix the use of a temporary file in SimpleConfig.write (dshea)
- Add a test for SimpleConfig.write(use_tmp=True). (dshea)
- Remove an unnecessary chmod when creating chrony.conf (dshea)
- Fix some bad uses of chmod. (dshea)
- Add a function to open a file with specific permission bits (dshea)
- Don't ask to start vnc if user specifies text mode. (#1202277)
  (sbueno+anaconda)
- New Anaconda documentation - 23.15 (bcl)
- Add a helper for building Sphinx docs using mock. (bcl)
- Update Sphinx configuration for python3 (bcl)
- Running without a GUI can also raise ValueError in errors.py (bcl)
- parse-kickstart_test.py: fix driverdisk_test() (wwoods)
- Fix the spelling of "version" (dshea)

* Mon Jul 13 2015 Brian C. Lane <bcl@redhat.com> - 23.15-1
- Some dracut modules anaconda needs have been split into their own package.
  (clumens)
- User operation kickstart tests. (kvalek)
- Kickstart tests for UTC and LOCAL hwclock. (kvalek)
- Kickstart firewall tests. (kvalek)
- Fix Repository New_Repository has no mirror or baseurl (#1215963) (jkonecny)

* Fri Jul 10 2015 Brian C. Lane <bcl@redhat.com> - 23.14-1
- Catch blivet formatDevice ValueError in custom (#1240226) (bcl)
- There's now a python3-rpmfluff, so revert this. (clumens)
- Fix a couple other pylint problems in the driver disk tests. (clumens)
- Merge pull request #194 from wgwoods/master (wwoods)
- dracut: fix boot failure waiting for finished/dd.sh (wwoods)
- Use builddir instead of srcdir to find the dd utils (dshea)
- Fix the dd_test for python3. (dshea)
- Fix %%files to deal with compiled python3 modules (dshea)
- Add a bunch of gi.require_version calls (dshea)
- Temporarily disable the error about not importing rpmfluff. (clumens)
- Don't try to iterate over threads directly in wait_all. (clumens)
- Update the btrfs kickstart tests to use functions.sh. (clumens)
- Merge pull request #182 from wgwoods/dd-refactor (wwoods)
- driver_updates: fixes from patch review (wwoods)
- Don't be too picky about what name is --device=link (dshea)
- Ignore stderr output from parse-kickstart. (dshea)
- Add an option to execReadlines to filter out stderr. (dshea)
- Ignore interruptible system calls in the dd test (dshea)
- Fix an undefined variable in writeStorageLate (dshea)
- Connect zfcp entries to the discovery buttons (dshea)
- Connect iscsi activations to buttons (dshea)
- Connect the dasd number entry to the discovery buttons. (dshea)
- Add keyboard layouts on the row-activated signal. (dshea)
- Connect dialog inputs to default actions. (dshea)
- Remove unnecessary GtkNotebooks. (dshea)
- Re-save some dialog glade files. (dshea)
- Merge pull request #181 from wgwoods/master (wwoods)
- dd-refactor: dracut + build bits (wwoods)
- Add kickstart test for RAID1 (bcl)
- pass PYTHONPATH to the kickstart test framework (bcl)
- Write servers to chronyd.conf even if it's off (#1197575) (wwoods)
- Refresh advanced disks after disk summary dialog (#1226354) (bcl)
- parse-kickstart: just emit 'inst.dd=XXX' for driverdisk (wwoods)
- parse-kickstart: pylint fixes (wwoods)
- dd-refactor: new driver_updates.py + tests (wwoods)
- payload: fix driverdisk repos (wwoods)
- dracut: fix boot with inst.ks and no inst.{repo,stage2} (#1238987) (wwoods)
- Use the most recent versions of the btrfs, logvol, part, and raid commands.
  (clumens)
- Allow /boot partition on iscsi with ibft (#1164195) (jkonecny)
- Add kickstart tests to test btrfs installation (vtrefny)
- Fix broken test by infiniband patch (#1177032) (jkonecny)

* Thu Jul 02 2015 Brian C. Lane <bcl@redhat.com> - 23.13-1
- Add a switch for the Airplane Mode label (dshea)
- Connect labels with keyboard accelerators to a widget (dshea)
- Add a test for dangling keyboard accelerators. (dshea)
- Use pocketlint for translation and markup checking (dshea)
- Flatten the glade test directory. (dshea)
- Add support for specifying arbitrary mkfs options. (clumens)
- Fix kickstart install with infiniband (#1177032) (jkonecny)
- anaconda-dracut: Fix sysroot mount for netroot (#1232411) (bcl)
- Add RAID swaps to /etc/fstab (#1234469) (bcl)
- network: catch another race when calling dbus methods on invalid devices
  (rvykydal)
- network: GUI, add connection even when virtual device activation failed
  (#1179276) (rvykydal)
- Fix IP / hostname mismatches when showing VNC server address (#1186726)
  (rvykydal)
- Check also ipv6 default routes when looking for onboot=yes device (#1185280)
  (rvykydal)
- Merge pull request #157 from wgwoods/master_dd_fixes (wwoods)
- Do not check dependencies on invalid payloads (dshea)
- network: don't set onboot=False for default autoconnections (#1212009)
  (rvykydal)
- Fix the types used to write anaconda-tb-all.log (dshea)
- dd: drop unnecessary archive_read_data_skip (wwoods)
- dd_extract: -l should not extract modules+firmware (wwoods)
- dd: fix permissions on extracted files (#1222056) (wwoods)
- tests: add dd_tests (wwoods)

* Fri Jun 26 2015 Brian C. Lane <bcl@redhat.com> - 23.12-1
- Revert "Add an optional conditional to progress_report." (bcl)
- Fix inconsistencies in the payload messages. (dshea)
- Fix install-requires and install-buildrequires (dshea)
- anaconda-dracut: Mount /dev/mapper/live-rw (#1232411) (bcl)
- Eliminate some false test results when running glade tests. (atodorov)
- Move the knowledge about network packages into ksdata.network. (clumens)
- Add an optional conditional to progress_report. (clumens)
- Move the big block of late storage writing out of install.py. (clumens)
- The attribute is named ostreesetup.nogpg. (clumens)
- Use the index in grubenv (#1209678) (bcl)
- Do not raise an exception on EINTR from os.close or os.dup2 (dshea)
- Merge pull request #154 from mulkieran/master-959701 (mulkieran)
- Improve focus behavior in the advanced user dialog (dshea)
- Re-save advanced_user.glade (dshea)
- Depsolve kickstarted packages on the summary hub (#961280) (dshea)
- Add a kickstart test for %%packages --ignoremissing (dshea)
- Remove descriptions for RAID levels (#959701) (amulhern)
- No kexec-tools on aarch64 (bcl)

* Fri Jun 19 2015 Brian C. Lane <bcl@redhat.com> - 23.11-1
- Do not import iutil from flags (dshea)
- Ignore EINTR errors in files unlikely to encounter them (dshea)
- Reimplement the open override for the dracut scripts (dshea)
- Wrap the only non-open call found by the new pocketlint checks (dshea)
- Redefine open to retry on EINTR (dshea)
- Remove __future__ imports (dshea)
- Use python 3's OSError subclasses instead of checking errno (dshea)
- Allow kwargs in eintr_retry_call (dshea)
- Remove explicit uses of /dev/null (dshea)
- Do not retry calls to close or dup2 (dshea)
- Remove another function from isys (dshea)
- Make dialogs behave better with timed input validation (dshea)
- Fix the password/confirm checks to work with delayed validation (dshea)
- Move the URL protocol removal out of the input check (dshea)
- Remove the vestigal capslock label from the password spoke (dshea)
- Re-saved a few glade files (dshea)
- Run set_status unconditionally from update_check_status (dshea)
- Do not run input checks for every keystroke of input (#1206307) (dshea)
- Add a method to execute timed actions early (dshea)
- Use comps.environments instead of comps.environments_iter (#1221736) (dshea)
- Merge pull request #83 from mulkieran/master-requires (mulkieran)
- Only show supported autopart choices in choices combo. (amulhern)
- Strip out device types that blivet is not able to support. (amulhern)
- Update blivet required version. (amulhern)
- Fix nfs4 stage2 and repo handling (#1230329) (bcl)
- Update upd-kernel so that it actually works (#1166535) (bcl)
- Fix passing ,nfsvers=3 to dracut (#1161820) (bcl)
- Require the python3 version of iscsi-initiator-utils (dshea)
- Fix the pylint pre-commit hook for python3 and pocketlint (dshea)
- Fix a type check to work with python 3. (dshea)
- Do not log Xorg output to tty5 (dshea)

* Wed Jun 10 2015 Brian C. Lane <bcl@redhat.com> - 23.10-1
- Deal with encrypted partitions not being readable by virt-cat. (clumens)
- Make use of the restore_signals Popen argument (dshea)
- Don't allow /boot on iSCSI. (#1164195) (sbueno+anaconda)
- Merge pull request #127 from mulkieran/master-kickstart (mulkieran)
- Actually distribute the clickable message test, too (dshea)
- Fix disk argument passing to virt-cat in the ostree test. (clumens)
- Relabel all password and group files in %%post (#1228489) (dshea)
- Deal with the order of ifcfg files not being guaranteed. (clumens)
- Add a __init__.py to fix up an error when running iutil_test.py. (clumens)
- Actually run the clickable message test (dshea)
- Add a false positive to pylint checking for S390Error. (clumens)
- Let the excludedocs test pass if there are only directories left. (clumens)
- Allow successful kstest results to provide more details. (clumens)
- The escrow_cert test cannot use autopart. (clumens)
- Don't warn on PyInit__isys being unused. (clumens)
- Test that root LV is encrypted. (amulhern)
- Deal with subprocess returning bytes in tests/lib/filelist.py, too. (clumens)
- Make anaconda+python3+pocketlint work. (clumens)
- Start using our new shared pylint framework in anaconda. (clumens)
- Remove our extra pylint checkers. (clumens)
- Remove a duplicate libselinux-python3 requires. (clumens)
- Run makeupdates with Python 2 for now (mkolman)
- Don't use the _safechars private property (#1014220) (mkolman)
- Make sure directory size is returned as int (#1014220) (mkolman)
- Only warn about missing yum-utils (#1014220) (mkolman)
- Make sure set_system_time() gets an integer (#1014220) (mkolman)
- Make sure the column number in TUI is an integer (#1141242) (mkolman)
- Python 3 compatible sorting fixes (#1014220) (mkolman)
- Make version comparison Python 3 compatible (#1014220) (mkolman)
- Don't apply numeric comparison on None (#1141242) (mkolman)
- Avoid comparing None to an integer (#1141242) (mkolman)
- Handle urllib split (#1014220) (mkolman)
- Don't try to decode strings (#1014220) (mkolman)
- Rename function attributes (#1014220) (mkolman)
- Replace raw_input() with input() (#1014220) (mkolman)
- Make iterators and their usage Python 3 compatible (#1014220) (mkolman)
- Convert Python 2 metaclass magic to Python 3 metaclass magic (#1014220)
  (mkolman)
- Make the raise syntax Python 3 compatible (#1014220) (mkolman)
- Python 3 no longer does tuple parameter unpacking (#1014220) (mkolman)
- Make isys Python 3 compatible (#1014220) (mkolman)
- Set a correct mode for the tempfile (#1014220) (mkolman)
- Python 3 temp files no longer reflect external changes (#1014220) (mkolman)
- Make print usage Python 3 compatible (#1014220) (mkolman)
- Rename the warnings spoke to warnings_spoke (#1014220) (mkolman)
- Replace list comprehension with for at class level (mkolman)
- Make gettext usage Python 3 compatible (#1014220) (mkolman)
- Do not open tty5 for writing in the "a" mode (#1014220) (vpodzime)
- Do not use pykickstart's RepoData as a key in a dict (#1014220) (vpodzime)
- Do not run repo attrs' checks if they are not set up yet (#1014220)
  (vpodzime)
- Don't depend on side effects of map() (#1141242) (mkolman)
- Don't use exceptions' message attribute (#1014220) (vpodzime)
- Addapt to string type changes (#1014220) (mkolman)
- Handle modules returning bytes in Python 3 (#1014220) (mkolman)
- Add and use function that makes sure we work with strings (#1014220)
  (vpodzime)
- Handle modules requiring different string types in Python 3 (#1014220)
  (mkolman)
- Remove sitecustomize (#1014220) (mkolman)
- Make ASCII conversions Python compatible (#1014220) (mkolman)
- Remove "is Unicode" tests (#1014220) (mkolman)
- Fix ASCII conversion tests (#1014220) (mkolman)
- Return a string when calling a program (#1014220) (mkolman)
- Handle subprocess returning bytes (#1014220) (mkolman)
- Handle latin-1 strings in locale -a output (#1014220) (mkolman)
- Open the VNC password file for binary writing (#1014220) (mkolman)
- Update parse-kickstart for python3 (#1014220) (bcl)
- Update driver-updates for python3 (#1014220) (bcl)
- Update python-deps for python3 (#1014220) (bcl)
- Add a test for parse-kickstart (#1014220) (bcl)
- Make the import Python 3 compatible (#1014220) (mkolman)
- Change configparser and queue imports (#1014220) (mkolman)
- Remove imports from the __future__ (#1014220) (mkolman)
- Use the imp module directly (#1014220) (mkolman)
- Use Python 3 versions of Python dependencies  (#1014220) (mkolman)
- Use /usr/bin/python3 in scripts (#1014220) (mkolman)
- Use Python 3 versions of nose and Pylint (#1014220) (mkolman)
- Build the Anaconda widgets for Python 3 (#1014220) (mkolman)
- Update makebumpver for python3 (#1014220) (bcl)
- Fix Kickstart installation without default gateway errors out (jkonecny)
- Fix results checking in a couple ks tests. (clumens)

* Wed Jun 03 2015 Brian C. Lane <bcl@redhat.com> - 23.9-1
- Fix a usage typo in run_once_ks script. (sbueno+anaconda)
- Add kickstart tests for keyboard settings. (sbueno+anaconda)
- Add a kickstart test for lang settings. (sbueno+anaconda)
- Fix a %% call inside _(). (clumens)
- Convert ntp-pools.* to using the new kstest functions and autopart. (clumens)
- Fix up the expected output in parse-kickstart_test.py. (clumens)
- Fix a couple more pylint problems in the s390 code. (clumens)
- Use the adapted Timezone class for kickstart data (vpodzime)
- Add a kickstart test for processing NTP servers/pools configuration
  (vpodzime)
- Show error on invalid username attempts in TUI. (#1171778) (sbueno+anaconda)
- Fix dracut reads ksdevice from missing os enviromnent (jkonecny)
- Run kickstart tests through an LMC-like program, not LMC itself. (clumens)
- Move common kickstart_test code out into its own functions.sh file. (clumens)
- Switch to using autopart in the kickstart tests. (clumens)
- Fix a couple pylint errors. (sbueno+anaconda)
- Make anaconda changes necessary for libblockdev s390 plugin.
  (sbueno+anaconda)
- Add a kickstart test for lvm with percentage-based sizes. (dlehman)
- Add kickstart test for basic fixed-size lvm layout. (dlehman)
- Add a kickstart test to validate the default fstype. (dlehman)
- Add kickstart test to test bond interface creation (jkonecny)
- Add kickstart test to test vlan creation (jkonecny)
- Fix --device=link and --device not specified (#1085310) (rvykydal)
- Add kickstart test to test hostname (jkonecny)
- Add a /boot to tmpfs-fixed_size.ks. (clumens)
- Fix bad warning message when user set illegal IP (jkonecny)
- Fix bad check of illegal ip address (jkonecny)
- Add a simple tmpfs kickstart test (mkolman)
- Add a kickstart test for escrow packets and backup passphrases (dshea)
- Fix a typo that caused us to discard corrected target sizes. (#1211746)
  (dlehman)
- Don't pass anything to ./configure. (dshea)
- Fix a pylint problem in parse-kickstart_test.py. (clumens)
- Fix 0 choice in Language and Storage in TUI mode (jkonecny)
- Update html documentation for new boot-options section (bcl)
- Convert boot-options to ReST and include it in the Sphinx documents. (bcl)

* Fri May 15 2015 Brian C. Lane <bcl@redhat.com> - 23.8-1
- Clean up after processKickstart in parse-kickstart_test.py. (clumens)
- Add support to dnfpayload.py for addon NFS repos. (clumens)
- Fix IndexError: list index out of range (#1219004) (jkonecny)
- Fix a typo in proxy-kickstart.sh that was causing a test time out. (clumens)
- iSCSI Name Validation using regexes (sujith_pandel)
- Add kickstart tests for proxy usage. (dshea)
- In dracut, do not display a warning for network lines with just a hostname.
  (clumens)
- Add transport adapters to support ftp and file fetching (dshea)
- Fix for "Kickstart installation fails..." (#1197960) (jkonecny)
- Allow passing kickstart tests to be run on the command line. (clumens)
- Automatically collect environment variables to be passed to ks tests.
  (clumens)
- Use isinstance instead of type for doing type checks. (clumens)
- Remove yumpayload.py, its support files, and most references to yum.
  (clumens)
- Fix the packages-and-group wildcard exclusion test (dshea)
- Set the GUI-selected environment in the ksdata (#1192100) (dshea)
- Don't crash if the disk model is None (#1215251) (dshea)
- Correct an error message in packages-and-groups-1.ks. (clumens)
- Switch from testing for emacs* to kacst*. (clumens)
- Tests that end in a traceback are failures, not successes. (clumens)
- Don't run run_report.sh from within run_kickstart_tests.sh. (clumens)
- If a kickstart test failed due to a traceback, display that. (clumens)
- Wrap device labels earlier (#1212586) (dshea)
- Remove the angle property from the device label (dshea)
- Get rid of the find button in the filter spoke. (dshea)
- Rearrange filter.glade (dshea)
- Fix errors in the vendor column renderers. (dshea)
- Fix some minor inconsistencies in filter.glade (dshea)
- Fix issues with advanced storage searching. (dshea)
- Remove duplicate entries from search combo boxes (dshea)
- Use named IDs for the filter type combo boxes. (dshea)
- Rearrange filter.glade the way glade wants it now (dshea)
- Add a reporting support script to kickstart tests. (clumens)
- Return a specific error code when a test times out. (clumens)
- Fix indentation in run_one_ks.sh. (clumens)
- Also remove all the fonts in the packages-and-groups-1 test. (clumens)
- Enable the basic-ftp and basic-ftp-yum kickstart tests. (clumens)
- Fix a typo in groups-and-envs-2.ks (clumens)
- Get NTP pools and servers from ksdata for the runtime config (vpodzime)
- Adapt to the new argument list for save_servers_to_config. (clumens)
- Remove the restriction that /boot be below 2TB for grub (#1082331) (dshea)
- Distinguish between NTP pools and servers in GUI (vpodzime)
- Add support for chrony pool directive (mlichvar)
- Add a readme pointing to the documentation (bcl)
- Sphinx docs - use source order (bcl)
- Add html documentation for Anaconda v23.7 (bcl)
- Place html docs under ./docs/html/ (bcl)
- Configure proxy settings for dnf payload (#1211122) (bcl)
- Change online action to change (bcl)
- Check for images/install.img first for netboot (bcl)
- Ignore addon and anaconda sections in handle-sshpw (bcl)
- Ignore %%anaconda section in parse-kickstart (bcl)
- Change of label in iscsi storage spoke (jkonecny)

* Wed Apr 22 2015 Brian C. Lane <bcl@redhat.com> - 23.7-1
- Fix doReqPartition import from autopart (bcl)
- Add support for reboot --kexec kickstart command (bcl)
- Add inst.kexec and --kexec support to reboot with kexec (bcl)
- Add setup_kexec method to prepare the system for a reboot with kexec (bcl)
- Add kickstart %%pre-install section support (bcl)
- Remove the custom help button from the toolbar (bcl)
- Use multiple streams for zRAM instead of multiple devices (vpodzime)
- iscsi: pass rd.* options of devices to be mouted in dracut (#1192398)
  (rvykydal)
- Remove the unused productName import from custom_storage_helpers.py.
  (clumens)
- Remove the old custom partitioning help dialog (mkolman)
- Implement the new reqpart command. (clumens)
- Sort disks by name when checking disk selection (vpodzime)
- Set both .format's and .originalFormat's passphrase on unlock (vpodzime)
- Make the Encrypt checkbox insensitive for encrypted non-BTRFS devices
  (#1210254) (vpodzime)
- Check for Gtk before importing escape_markup (bcl)
- If the network is disabled, also disable the network part of the source
  spoke. (#1192104) (clumens)
- Add handling for unusable storage configurations. (dlehman)
- Allow markup in the label/message of DetailedErrorDialog. (dlehman)
- Allow passing an optional button list to showDetailedError. (dlehman)
- Allow kwargs with gtk_action_wait, gtk_action_nowait decorators. (dlehman)
- Fix makeupdates handling of Release: (bcl)
- Make sure we unmount the path we mounted (bcl)
- Fix up one more back_clicked reference that got missed. (clumens)
- Don't unconditionally set ksdata.lang.seen to True (#1209927) (mkolman)
- Reset the back_clicked flag if we stay on the Storage spoke (#1210003)
  (vpodzime)
- Mark the back_clicked attribute of the Storage spoke as private (vpodzime)
- TUI pwpolicy setup was supposed to be in __init__ not refresh (#1208607)
  (bcl)
- Preserve the order of boot args added by kickstart. (clumens)
- Revert "allow /boot on btrfs subvol or filesystem" (bcl)
- Connect scroll adjustments in the right class (#1206472) (dshea)

* Thu Apr 02 2015 Brian C. Lane <bcl@redhat.com> - 23.6-1
- Enforce sane disk selections. (dlehman)
- Add a test for parse-kickstart (bcl)
- Add --tmpdir to parse-kickstart for testing (bcl)
- Use the correct format for IPMI messages. (clumens)
- Do not use min_luks_entropy with pre-existing devices (#1206101) (dshea)
- Remove the dnf cache directory when resetting the repo (dshea)
- Do not add separators to the addon list when not needed (dshea)
- Only use the instclass environment if it actually exists. (dshea)

* Fri Mar 27 2015 Brian C. Lane <bcl@redhat.com> - 23.5-1
- Mock external module dependencies for readthedocs (bcl)
- Generate the pyanaconda module documentation (bcl)
- Reformat kickstart.rst using better ReST markup (bcl)
- Add some deprecation-related false positives. (clumens)
- Add Sphinx documentation support (bcl)
- Add documentation on %%anaconda kickstart command (bcl)
- Prevent Storage spoke Done button method from multiple launch (jkonecny)
- Prevent spokes from being exited more times. (jkonecny)
- Only depend on pygobject3-base in anaconda-core (#1204469) (mkolman)
- Use proxy when configured for the base repo (#1196953) (sjenning)
- Assume UTC if setting the system time without a timezone (#1200444) (dshea)
- Add boolean as return to ThreadManager.wait (jkonecny)
- Make sure LANG is always set to something (#1201896) (dshea)
- Fix pylint/translation issues from the pwpolicy patches. (clumens)

* Fri Mar 20 2015 Brian C. Lane <bcl@redhat.com> - 23.4-1
- Clean out the mock chroot before attempting to run the rest of the test.
  (clumens)
- Implement %%anaconda kickstart section for pwpolicy (bcl)
- Add pwpolicy support to TUI interface (bcl)
- Add pwpolicy for the LUKS passphrase dialog. (bcl)
- Add pwpolicy for the user spoke. (bcl)
- Use pwpolicy for the root password spoke. (bcl)
- Add the text for weak passwords to constants (bcl)
- Add tests with an FTP instrepo (dshea)
- Add kickstart tests for an NFS instrepo and addon repos. (dshea)
- Handle /boot on btrfs for live (#1200539) (bcl)
- rpmostreepayload: write storage config after shared var is mounted (#1203234)
  (rvykydal)
- Tweak tmux configuration file (jkonecny)
- Remove --device= from the new kickstart tests. (clumens)
- Add more kickstart-based packaging tests. (clumens)
- Fix enlightbox call in ZFCPDialog. (#1151144) (sbueno+anaconda)
- fix crash with bare 'inst.virtiolog' in boot args (wwoods)
- Do not attempt to set None as a warning (dshea)
- fix inst.ks.sendmac for static ip=XXX (#826657) (wwoods)

* Fri Mar 13 2015 Brian C. Lane <bcl@redhat.com> - 23.3-1
- Only insert strings into the environment (#1201411) (dshea)
- Fix the rescue kernel version list in writeBootLoader (#1201429) (dshea)
- Missing local variable check (omerusta)
- Fix the handling of nfs:// URLs. (dshea)
- Add glob support for the -a/--add option in makeupdates (mkolman)
- White Space fixes (omerusta)
- Put all mock results into the top-level source dir. (clumens)
- Merge pull request #31 from dcantrell/master (david.l.cantrell)
- Require newt-python in anaconda-core (dshea)
- Make merge-pr executable (dshea)
- Display an error for exceptions during GUI setup (dshea)
- Remove unused invisible char properties (dshea)
- Add a check for invisible_char validity (dshea)
- Connect viewport adjustments to child focus adjustments (#1192155) (dshea)
- Support '%%packages --multilib' in dnfpayload.py (#1192628) (dcantrell)

* Fri Mar 06 2015 Brian C. Lane <bcl@redhat.com> - 23.2-1
- Add rc-release target (bcl)
- Change --skip-tx to --skip-zanata in scratch-bumpver (bcl)
- Add --newrelease to makebumpver (bcl)
- Improve the addon repo name collision code (#1125322) (bcl)
- Fix the import of mountExistingSystem (vpodzime)
- Fix import error in anaconda-cleanup. (sbueno+anaconda)
- Use the new static method to get possible PE sizes (vpodzime)
- Try using the global LUKS passphrase if none is given for LV/part (#1196112)
  (vpodzime)
- Fix the help button mnemonic display on spokes (dshea)
- Only set the hub message if the message has changed (dshea)
- Wrap the info bar in a GtkRevealer (dshea)
- Add links to clickable warning and error messages. (dshea)
- Add a test to look for clickable messages that aren't clickable enough.
  (dshea)
- Increment the widgets version number (dshea)
- Allow markup and links in the info bar. (dshea)
- Add more links to gtk-doc comments (dshea)
- Handle New_Repository name collision source spoke (#1125322) (bcl)
- Fix a bad usage of execWithRedirect (#1197290) (dshea)
- Have to be root to delete /var/tmp/kstest-* on the remote machines. (clumens)
- Use the LUKS device for swap in fstab (#1196200) (vpodzime)
- Clear TUI source spoke errors that may have been leftover from a prior
  attempt. (#1192259) (sbueno+anaconda)

* Fri Feb 27 2015 Brian C. Lane <bcl@redhat.com> - 23.1-1
- Make sure python2 dnf is required (bcl)
- Fix pykickstart requirement. (clumens)
- Extract xattrs from tar payload (#1195462) (bcl)
- Add a script to rebase and merge pull requests (dshea)
- Update translation documentation for Zanata (bcl)
- Switch translation support to fedora.zanata.org (bcl)
- install.py: fix the 'is team device' check (awilliam)
- Explain why Anaconda requires rpm-devel and libarchive-devel during build
  (mkolman)
- Revert "Switch to temporary transifex branch" (bcl)
- Revert "makebumpver needs to know about anaconda-1 transifex name" (bcl)
- Commit 23.0 anaconda.pot file (bcl)
- Rename queue.py to queuefactory.py. (clumens)
- Remove references to old_tests, which no longer exists. (clumens)
- Fix package and group removing with the dnf payload. (clumens)
- Don't try to run new-kernel-pkg if it doesn't exist. (clumens)

* Fri Feb 20 2015 Brian C. Lane <bcl@redhat.com> - 23.0-1
- Remove unused imports (dshea)
- Check for unused imports in __init__ files (dshea)
- Remove timestamp-based version support. (dshea)
- Add test lib methods to check regexes (dshea)
- Cleanup BuildRequires (mkolman)
- Remove obsolete imports. (amulhern)
- Make print statement print output w/out surrounding parentheses. (amulhern)
- Remove an unused import (dshea)
- rpmostreepayload: Honor noverifyssl (walters)
- typo: packaging: Don't vary name of "verified" (walters)
- Disable the metacity mouse-button-modifier setting (dshea)
- Fix completion setting in TUI language spoke. (#1192230) (sbueno+anaconda)
- Remove the pylint false positives for the GLib module (dshea)
- Use ExtendAction for --ignore flag (amulhern)
- Use a simple ExtendAction for add_rpms option. (amulhern)
- Fix log message formating (mkolman)
- Don't clear nonexistent DNF package download location (#1193121) (mkolman)