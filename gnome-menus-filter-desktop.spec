Summary:	Clean gnome-menus for an average user
Summary(pl.UTF-8):	gnome-menus dla zwykłego użytkownika
Name:		gnome-menus-filter-desktop
Version:	2.10.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	%{name}-applications.menu
Source1:	%{name}-preferences.menu
Source2:	%{name}-settings.menu
URL:		http://www.gnome.org/
Requires:	gnome-menus
Provides:	gnome-menus-filter
Obsoletes:	gnome-menus-filter-default
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clean gnome-menus for an average desktop user. Removes rarely used
applications.

%description -l pl.UTF-8
Wyczyszczone gnome-menus dla zwykłego użytkownika. Usuwa rzadko
używane aplikacje.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus

install %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications.menu
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/preferences.menu
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/settings.menu

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/menus
