# TODO: use gtk4-update-icon-cache
Summary:	GNOME application to take pictures and videos
Summary(pl.UTF-8):	Aplikacja GNOME to robienia zdjęć i nagrywania filmów
Name:		gnome-snapshot
Version:	45.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	https://download.gnome.org/sources/snapshot/45/snapshot-%{version}.tar.xz
# Source0-md5:	f95c3a9d081d9670d01b7fe1309fddd2
Patch0:		snapshot-x32.patch
Patch1:		snapshot-pango.patch
URL:		https://gitlab.gnome.org/GNOME/snapshot
BuildRequires:	appstream-glib
BuildRequires:	cairo-devel >= 1.16
BuildRequires:	cargo
BuildRequires:	gdk-pixbuf2-devel >= 2.42
BuildRequires:	glib2-devel >= 1:2.77
BuildRequires:	graphene-devel >= 1.10
BuildRequires:	gstreamer-devel >= 1.20
BuildRequires:	gstreamer-plugins-base-devel >= 1.20
# camerabin
BuildRequires:	gstreamer-plugins-bad-devel >= 1.20
BuildRequires:	gtk4-devel >= 4.11
BuildRequires:	libadwaita-devel >= 1.4
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.49.2
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	rust
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.26
Requires(post,postun):	gtk-update-icon-cache
Requires:	cairo >= 1.16
Requires:	gdk-pixbuf2 >= 2.42
Requires:	glib2 >= 1:2.77
Requires:	graphene >= 1.10
Requires:	gtk4 >= 4.11
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.4
Requires:	pango >= 1:1.49.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debugsource packages don't support rust (or require adding some flags to rust/cargo)
%define		_debugsource_packages	0

%description
GNOME application to take pictures and videos.

%description -l pl.UTF-8
Aplikacja GNOME to robienia zdjęć i nagrywania filmów.

%prep
%setup -q -n snapshot-%{version}
%ifarch x32
%patch0 -p1
%endif
%patch1 -p1

%build
%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ifarch x32
export PKG_CONFIG_ALLOW_CROSS=1
%endif
%ninja_install -C build

%find_lang snapshot

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%files -f snapshot.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/snapshot
%{_datadir}/glib-2.0/schemas/org.gnome.Snapshot.gschema.xml
%{_datadir}/metainfo/org.gnome.Snapshot.metainfo.xml
%{_datadir}/snapshot
%{_desktopdir}/org.gnome.Snapshot.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Snapshot.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Snapshot-symbolic.svg
