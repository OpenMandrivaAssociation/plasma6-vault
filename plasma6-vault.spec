%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20231014

Name: plasma6-vault
Version: 5.240.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/plasma-vault/-/archive/master/plasma-vault-master.tar.bz2#/plasma-vault-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
%endif
Summary: Plasma Vault - a tool for encrypted storage
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6Activities)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6Plasma)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KSysGuard) >= 5.27.80
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: cryfs

%description
Plasma Vault - a tool for encrypted storage.

%prep
%autosetup -p1 -n plasma-vault-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_qtdir}/plugins/kf6/kfileitemaction/plasmavaultfileitemaction.so
%{_qtdir}/plugins/kf6/kded/plasmavault.so
%{_qtdir}/plugins/plasma/applets/org.kde.plasma.vault.so
%{_datadir}/metainfo/org.kde.plasma.vault.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.vault
