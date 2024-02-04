#
# Conditional build:
%bcond_without	tests		# unit tests

Summary:	Tool for managing your YubiKey configuration
Summary(pl.UTF-8):	Narzędzie do zarządzania urządzeniami YubiKey
Name:		yubikey-manager
# versions 5.1+ use poetry buildsystem
Version:	5.0.1
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://developers.yubico.com/yubikey-manager/Releases/yubikey_manager-%{version}.tar.gz
# Source0-md5:	8686ea7e4d633da9e9318e5e8c22c699
URL:		https://developers.yubico.com/yubikey-manager/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with tests}
BuildRequires:	python3-click >= 8.0
BuildRequires:	python3-click < 9
BuildRequires:	python3-cryptography >= 3.0
BuildRequires:	python3-cryptography < 42
BuildRequires:	python3-fido2 >= 1.0
BuildRequires:	python3-fido2 < 2
BuildRequires:	python3-keyring >= 23.4
BuildRequires:	python3-keyring >= 24
BuildRequires:	python3-makefun >= 1.9.5
BuildRequires:	python3-pyscard >= 2.0
BuildRequires:	python3-pyscard < 3
BuildRequires:	python3-pytest >= 7.2
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python library and command line tool for configuring a YubiKey.

%description -l pl.UTF-8
Pythonowa biblioteka i narzędzie linii poleceń do konfiguracji
urządzeń YubiKey.

%prep
%setup -q -n yubikey_manager-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.adoc
%attr(755,root,root) %{_bindir}/ykman
%{py3_sitescriptdir}/ykman
%{py3_sitescriptdir}/yubikit
%{py3_sitescriptdir}/yubikey_manager-%{version}-py*.egg-info
