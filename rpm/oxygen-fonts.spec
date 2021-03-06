# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       oxygen-fonts

# >> macros
# << macros

Summary:    A desktop/gui font family for integrated use with the KDE desktop
Version:    0.4
Release:    1
Group:      System/Base
License:    GPLv2+
BuildArch:  noarch
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source1:    oxygen-fontconfig.conf
Source100:  oxygen-fonts.yaml
Source101:  oxygen-fonts-rpmlintrc
Requires:   fontpackages-filesystem
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel

%description
A desktop/gui font family for integrated use with the KDE desktop.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DOXYGEN_FONT_INSTALL_DIR=%{_fontdir}

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
%{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
%{buildroot}%{_fontconfig_confdir}/%{fontconf}
# << install post

%_font_pkg -f %{fontconf} *.ttf
%doc COPYING-GPL+FE.txt COPYING-OFL

%files devel
%defattr(-,root,root,-)
%{_kf5_cmakedir}/OxygenFont
# >> files devel
# << files devel
