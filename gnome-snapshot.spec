# TODO: use gtk4-update-icon-cache
Summary:	GNOME application to take pictures and videos
Summary(pl.UTF-8):	Aplikacja GNOME to robienia zdjęć i nagrywania filmów
Name:		gnome-snapshot
Version:	44.2
Release:	1
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	https://download.gnome.org/sources/snapshot/44/snapshot-%{version}.tar.xz
# Source0-md5:	b9f8b08abe7390f74383840ae9bd2f8b
URL:		https://gitlab.gnome.org/GNOME/snapshot
BuildRequires:	appstream-glib
BuildRequires:	cargo
BuildRequires:	glib2-devel >= 1:2.75
BuildRequires:	gstreamer-devel >= 1.20
BuildRequires:	gstreamer-plugins-base-devel >= 1.20
# camerabin
BuildRequires:	gstreamer-plugins-bad-devel >= 1.20
BuildRequires:	gtk4-devel >= 4.9.0
BuildRequires:	libadwaita-devel >= 1.4
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	rust
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.26
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.75
Requires:	hicolor-icon-theme
Requires:	gtk4 >= 4.9.0
Requires:	libadwaita >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME application to take pictures and videos.

%description -l pl.UTF-8
Aplikacja GNOME to robienia zdjęć i nagrywania filmów.

%prep
%setup -q -n snapshot-%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

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
