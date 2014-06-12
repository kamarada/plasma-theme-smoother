#
# spec file for package plasma-theme-smoother
#
# Copyright (c) 2014 Kamarada Project, Aracaju, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


%define tarname Smoother
Name:           plasma-theme-smoother
Version:        1.1
Release:        1
Summary:        Plasma Smoother Theme
License:        GPL
Group:          System/GUI/KDE
Source0:        %{tarname}.tar.gz
Url:            http://half-left.deviantart.com/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:	kde4-filesystem

%description
A nice smooth plasma theme designed by Sean Wilson

http://half-left.deviantart.com/art/KDE4-Smoother-354277055

%prep
%setup -q -n %{tarname}

%build

%install
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme
cp -R $RPM_BUILD_DIR/%{tarname} %{buildroot}%{_kde4_appsdir}/desktoptheme

%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%{_kde4_appsdir}/desktoptheme/Smoother/

%changelog
* Tue Jun 12 2014 kamaradalinux@gmail.com
- Initial import from version 1.1
