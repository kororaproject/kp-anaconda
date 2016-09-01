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
#%define commit 9d2c9adeaeda6ba3f5c1e9705b24fc6e
#%define livearches %{ix86} x86_64 ppc ppc64 ppc64le
# v24.13.7
#%define commit 6d22a306e48b5c8bd3deba0a9de8c996
#%define livearches %{ix86} x86_64 ppc ppc64 ppc64le
# v25.20
%define commit 45f9dd4433c818d371e37a6121d3f7df/
%define livearches %{ix86} x86_64 ppc ppc64 ppc64le

Summary: Graphical system installer
Name:    anaconda
Version: 25.20
Release: 2%{?dist}
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

%define gettextver 0.19.8
%define pykickstartver 2.30-1
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
Requires: python3-blivet >= 1:2.0.2
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

# pwquality only "recommends" the dictionaries it needs to do anything useful,
# which is apparently great for containers but unhelpful for the rest of us
Requires: cracklib-dicts

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
Requires: python3-wrapt

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
#sed -i 's|Fedora|Korora|g' data/liveinst/gnome/fedora-welcome
#sed -i 's|Fedora|Korora|g' data/liveinst/gnome/fedora-welcome.desktop*

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

# If no langs found, keep going
%find_lang %{name} || :

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

# Allow the lang file to be empty
%define _empty_manifest_terminate_build 0

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

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 25.20-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 08 2016 Brian C. Lane <bcl@redhat.com> - 25.20-1
- Allow kickstart users to ignore the free space error (dshea)
- Stop kickstart when space check fails (bcl)
- Service anaconda-nm-config is missing type oneshot (jkonecny)
- Fix dhcpclass to work both via kickstart and the boot cmdline. (clumens)
- network: handle also ifcfg files of not activated virtual devices (#1313173)
  (rvykydal)
- network: check onboot value in ksdata, not NM connections (#1313173)
  (rvykydal)
- network: do not activate device on kickstart --onboot="yes" (#1341636)
  (rvykydal)

* Fri Jun 24 2016 Brian C. Lane <bcl@redhat.com> - 25.19-1
- hostname: don't set installer env hostname to localhost.localdomain
  (#1290858) (rvykydal)
- hostname: add tooltip to Apply button (#1290858) (rvykydal)
- hostname: fix accelerator collision (#1290858) (rvykydal)
- hostname: don't set hostname in initrafms of target system (#1290858)
  (rvykydal)
- hostname: set current hostname from target system hostname on demand
  (#1290858) (rvykydal)
- hostname: suggest current hostname for storage containers (#1290858)
  (rvykydal)
- hostname: don't set target system static hostname to current hostname
  (#1290858) (rvykydal)
- network tui: do not activate device when setting its onboot value (#1261864)
  (rvykydal)
- network tui: edit persistent configuration, not active connection (#1261864)
  (rvykydal)
- network: validate netmask in tui (#1331054) (rvykydal)
- Add wordwrap to text mode and use it by default (#1267881) (rvykydal)
- Fix adding new VG in Custom spoke can't be applied (#1263715) (jkonecny)
- Fix SimpleConfigFile file permissions (#1346364) (bcl)
- Re-configure proxy when updateBaseRepo is called (#1332472) (bcl)

* Fri Jun 17 2016 Brian C. Lane <bcl@redhat.com> - 25.18-1
- Only use <> for markup (#1317297) (bcl)
- Update iscsi dialog for Blivet 2.0 API change (bcl)
- Use the signal handlers to set initial widget sensitivies (dshea)
- Fix bad sensitivity on boxes in source spoke (jkonecny)
- Fix install-buildrequires (bcl)
- Added optional [/prefix] as pattern (kvalek)
- Require network for network-based driver disks (dshea)
- Add missing pkgs to install-buildrequires (#612) (phil)
- Increase the required version of gettext (dshea)
- Fix the name sensitivity in the custom spoke. (dshea)

* Fri Jun 10 2016 Brian C. Lane <bcl@redhat.com> - 25.17-1
- Revert "Temporarily disable translations" (bcl)
- Change where to look for the iscsi object (#1344131) (dshea)
- Fix old blivet identifiers (#1343907) (dshea)
- Fix a covscan warning about fetch-driver-net (#1269915) (bcl)
- Fix crash when NM get_setting* methods return None (#1273497) (jkonecny)
- Overwrite network files when using ks liveimg (#1342639) (bcl)
- Stop using undocumented DNF logging API (bcl)
- Use the LUKS device for encrypted swap on RAID (dshea)
- Keep the subdir in driver disk update paths (dshea)
- Warn about broken keyboard layout switching in VNC (#1274228) (jkonecny)
- Make the anaconda-generator exit early outside of the installation
  environment (#1289179) (mkolman)

* Fri Jun 03 2016 Brian C. Lane <bcl@redhat.com> - 25.16-1
- Add a button to refresh the disk list. (dlehman)
- Only try to restart payload in the Anaconda environment (mkolman)
- Make current runtime environment identifiers available via flags (mkolman)
- Display storage errors that cause no disks to be selected (#1340240) (bcl)
- Fix the SourceSwitchHandler pylint errors differently. (clumens)
- Fix pylint errors. (clumens)
- Update the disk summary on Ctrl-A (dshea)
- Revert "Refresh the view of on-disk storage state every 30 seconds."
  (dlehman)
- Refresh the view of on-disk storage state every 30 seconds. (dlehman)
- Handle unsupported disklabels. (dlehman)
- Use a blivet method to remove everything from a device. (dlehman)
- Tighten up ResizeDialog._recursive_remove a bit. (dlehman)
- Only look for partitions on partitioned disks. (dlehman)
- NFS DDs installation now works correctly (#1269915) (japokorn)
- Remove unused on_proxy_ok_clicked from Source spoke (jkonecny)
- send all layouts to localed for keymap conversion (#1333998) (awilliam)
- Small cleanup (mkolman)

* Fri May 27 2016 Brian C. Lane <bcl@redhat.com> - 25.15-1
- Resolve shortcut conflict between "Desired Capacity" and "Done" (yaneti)
- network: don't crash on devices with zero MAC address (#1334632) (rvykydal)
- Remove Authors lines from the tops of all files. (clumens)
- Related: rhbz#1298444 (rvykydal)
- New Anaconda documentation - 25.14 (bcl)
- Catch DNF MarkingError during group installation (#1337731) (bcl)
- Fix TUI ErrorDialog processing (#1337427) (bcl)
- Clean up yelp processes (#1282432) (dshea)

* Fri May 20 2016 Brian C. Lane <bcl@redhat.com> - 25.14-1
- Temporarily disable translations (bcl)
- Don't crash when selecting the same hdd ISO again (#1275771) (mkolman)

* Thu May 19 2016 Brian C. Lane <bcl@redhat.com> - 25.13-1
- Fix writeStorageLate for live installations (#1334019) (bcl)
- Remove the locale list from zanata.xml (dshea)
- Ditch autopoint. (dshea)
- Ditch intltool. (dshea)
- Rename fedora-welcome to fedora-welcome.js (dshea)
- Fix UEFI installation after EFIBase refactor (bcl)
- Fix error handling for s390 bootloader errors (sbueno+anaconda)
- Deselect all addons correctly (#1333505) (bcl)
- gui-testing needs isys to be compiled. (clumens)
- Add more to the selinux check in tests/gui/base.py. (clumens)

* Fri May 13 2016 Brian C. Lane <bcl@redhat.com> - 25.12-1
- Add single language mode (#1235726) (mkolman)
- Move default X keyboard setting out of the Welcome spoke (mkolman)
- Rerun writeBootLoader on Live BTRFS installs (bcl)
- Check for mounted partitions as part of sanity_check (#1330820) (bcl)
- Merge pull request #620 from dashea/new-canary (dshea)
- Update the required pykickstart version. (dshea)
- Implement %%packages --excludeWeakdeps (#1331100) (james)
- Fix bad addon handling when addon import failed (jkonecny)
- Add retry when downloading .treeinfo (#1292613) (jkonecny)
- Return xprogressive delay back (jkonecny)
- Change where tests on translated strings are run. (dshea)
- Merge the latest from translation-canary (dshea)
- Squashed 'translation-canary/' changes from 5a45c19..3bc2ad6 (dshea)
- Add new Makefile target for gui tests (atodorov)
- Define missing srcdir in run_gui_tests.sh and enable coverage (atodorov)
- Split gui test running out into its own script. (clumens)
- Look higher for the combobox associated with an entry (#1333530) (dshea)
- Use createrepo_c in the ci target. (dshea)
- Compile glib schema overrides with --strict. (dshea)

* Fri May 06 2016 Brian C. Lane <bcl@redhat.com> - 25.11-1
- Don't join two absolute paths (#1249598) (mkolman)
- Don't crash when taking a screenshot on the hub (#1327456) (mkolman)
- Fix pylint errors. (phil)
- Factor out common grub1/grub2 stuff into mixin, and other factoring (phil)
- Add GRUB1 (legacy) support back to Anaconda (phil)

* Fri Apr 29 2016 Brian C. Lane <bcl@redhat.com> - 25.10-1
- Handle unmounting ostree when exiting (bcl)
- ostree: Use bind mounts to setup ostree root (bcl)
- ostree: Skip root= setup when using --dirinstall (bcl)
- disable_service: Specify string format args as logging params. (clumens)
- Ignore failure when disable services that do not exist (phil)
- Get rid of an unused variable in the network spoke. (clumens)
- Revalidate source only if nm-con-ed change settings (#1270354) (jkonecny)
- Merge solutions for test source when network change (#1270354) (jkonecny)
- Changes in network state revalidate sources rhbz#1270354 (riehecky)

* Wed Apr 27 2016 Brian C. Lane <bcl@redhat.com> - 25.9-1
- Use the iutil functions for interacting with systemd services. (dshea)
- Add methods to enable and disable systemd services. (dshea)
- Do not add .service to the end of service names. (dshea)
- Remove detach-client from tmux.conf (dshea)
- Use Blivet 2.0 for set_default_fstype (#607) (sgallagh)
- Remove dnf from the list of required packages. (#605) (dshea)
- Add access to the payload from addons (#1288636) (jkonecny)
- Disable pylint warnings related to the log handler fixer. (dshea)
- Allow the metacity config dir to be overriden. (dshea)
- Do not include /usr/share/anaconda files in the gui package. (dshea)
- Work around logging's crummy lock behavior. (dshea)
- Use rm -r to remove the temporary python site directory. (dshea)
- Remove the subnet label for wired devices. (#1327615) (dshea)
- Fix how unusued network labels are hidden (#1327615) (dshea)
- Remove yum_logger (bcl)
- Remove the lock loglevel (bcl)
- Use a temporary user-site directory for the tests. (dshea)
- Build everything for make ci. (dshea)
- Ignore some E1101 no-member errors when running pylint (bcl)
- Sprinkle the code with pylint no-member disable statements (bcl)
- Catch GLib.GError instead of Exception (bcl)
- Update storage test for Blivet 2.0 API change. (bcl)
- Initialize missing private methods in BasePage class (bcl)
- Update kickstart.py for Blivet 2.0 API change. (bcl)
- Use namedtuple correctly in kexec.py (bcl)
- Add more requires to make password checking still work. (#1327411) (dshea)
- Rename isS390 to match the renames in blivet. (dshea)
- Suppress signal handling when setting zone from location (#1322648) (dshea)
- Refresh metadata when updates checkbox changes (#1211907) (bcl)

* Fri Apr 15 2016 Brian C. Lane <bcl@redhat.com> - 25.8-1
- network: handle null wireless AP SSID object (#1262556) (awilliam)
- Change new_tmpfs to new_tmp_fs. (clumens)
- Add support for kickstart %%onerror scripts. (clumens)
- Show network spoke in the TUI reconfig mode (#1302165) (mkolman)
- network: copy static routes configured in installer to system (#1255801)
  (rvykydal)
- network: fix vlan over bond in kickstart (#1234849) (rvykydal)
- network: use NAME to find ifcfg on s390 with net.ifnames=0 (#1249750)
  (rvykydal)
- Get rid of the reimport of MultipathDevice. (clumens)
- Fix iSCSI kickstart options aren't generated (#1252879) (jkonecny)
- Fix adding offload iSCSI devices (vtrefny)
- Make the list-harddrives script mode robust (mkolman)

* Fri Apr 08 2016 Brian C. Lane <bcl@redhat.com> - 25.7-1
- Blivet API change getDeviceBy* is now get_device_by_* (bcl)
- network: don't set 803-3-ethernet.name setting (#1323589) (rvykydal)
- Log non-critical user/group errors (#1308679) (bcl)
- Fix btrfs metadata raid level kwarg. (dlehman)
- docs: Add release building document (bcl)
- Minor improvements - README and test dependencies (atodorov)
- Add more matches for network connectivity (atodorov)

* Mon Apr 04 2016 Brian C. Lane <bcl@redhat.com> - 25.6-1
- Remove an unused import from anaconda-cleanup. (clumens)
- Don't use booleans in Requires (#1323314) (dshea)
- Set CSS names on all of the anaconda classes. (#1322036) (dshea)
- Don't crash if no groups are specified (#1316816) (dshea)
- Fix only one address is shown in anaconda (#1264400) (jkonecny)
- Fix call to update optical media format. (#1322943) (dlehman)
- Reset invalid disk selection before proceeding. (dlehman)
- Multiple Dogtail tests improvements (atodorov)
- Do not allow liveinst with --image or --dirinstall (#1276349) (dshea)
- New Anaconda documentation - 25.5 (bcl)

* Wed Mar 30 2016 Brian C. Lane <bcl@redhat.com> - 25.5-1
- Don't provide subclasses of the multipath or dmraid commands. (clumens)
- Add support for chunksize raid kickstart parameter. (vtrefny)
- Convert to blivet-2.0 API. (dlehman)

* Thu Mar 24 2016 Brian C. Lane <bcl@redhat.com> - 25.4-1
- Require that the English locale data be available. (#1315494) (dshea)
- Revert "Change the default locale to C.UTF-8 (#1312607)" (#1315494) (dshea)
- Make windows in metacity closable (#1319590) (dshea)
- Fix the use of CSS psuedo-classes in the widgets. (dshea)
- Add reason when logging invalid repository (#1240379) (jkonecny)

* Sat Mar 19 2016 Brian C. Lane <bcl@redhat.com> - 25.3-1
- Apply language attributes to all labels within anaconda. (dshea)
- Add a function to apply a PangoAttrLanguage to a label. (dshea)
- Add functions to watch changes to a container widget. (dshea)
- Switch to the adwaita icon theme. (dshea)
- Fix duplicate network settings in dracut (#1293539) (jkonecny)
- Fix create device with bad name when parsing KS (#1293539) (jkonecny)
- Use a lock for repoStore access (#1315414) (bcl)
- Add missing inst prefix to the nokill option in docs (mkolman)
- Merge pull request #551 from wgwoods/master-multiple-initrd-dd-fix (wwoods)
- fix multiple inst.dd=<path> args (rhbz#1268792) (wwoods)

* Fri Mar 11 2016 Brian C. Lane <bcl@redhat.com> - 25.2-1
- Load the system-wide Xresources (#1241724) (dshea)
- Use an icon that exists in Adwaita for the dasd confirmation (dshea)
- Make it possible to skip saving of kickstarts and logs (#1285519) (mkolman)
- Add a function for empty file creation (#1285519) (mkolman)
- Run actions for argparse arguments (#1285519) (mkolman)

* Wed Mar 09 2016 Brian C. Lane <bcl@redhat.com> - 25.1-1
- don't install kernel-PAE on x86_64 (#1313957) (awilliam)
- except block in py3.5 undefines the variable (bcl)
- Remove some history from the liveinst setup. (dshea)
- Do not run the liveinst setup if not in a live environment. (dshea)
- Set GDK_BACKEND=x11 before running anaconda from liveinst. (dshea)
- Run zz-liveinst as an autostart application (dshea)
- Translate the help button. (dshea)
- Translate the required space labes in resize.py (dshea)

* Fri Mar 04 2016 Brian C. Lane <bcl@redhat.com> - 25.0-1
- Add device id to dasdfmt screen. (#1269174) (sbueno+anaconda)
- Unify displayed columns in custom spoke dialogs. (#1289577) (sbueno+anaconda)
- Show some confirmation to users if adding a DASD was successful. (#1259016)
  (sbueno+anaconda)
- Hotfix for missing storage in payload class (#1271657) (jkonecny)
- Check to see if DD repo is already in addOn list (#1268357) (bcl)
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
- Fix nfs source crash when options change (#1264071) (bcl)
- makebumpver: Add a --dry-run option (bcl)
- NTP should have better behavior (#1309396) (jkonecny)
- Manually set clock shifts on UI idle (#1251044) (rmarshall)
- Don't remove selected shared part when Delete all (#1183880) (jkonecny)
- Don't delete shared/boot parts in deleteAll (#1183880) (jkonecny)

