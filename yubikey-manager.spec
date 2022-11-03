#
# Conditional build:
%bcond_with	tests		# unit tests (broken as of 1.0.1)

Summary:	Tool for managing your YubiKey configuration
Summary(pl.UTF-8):	Narzędzie do zarządzania urządzeniami YubiKey
Name:		yubikey-manager
Version:	5.0.0
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://developers.yubico.com/yubikey-manager/Releases/yubikey_manager-%{version}.tar.gz
# Source0-md5:	0c4be1b791faf267c2bb29ca33f28fcf
URL:		https://developers.yubico.com/yubikey-manager/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with tests}
BuildRequires:	python3-cryptography
BuildRequires:	python3-fido2 >= 1.0.0
BuildRequires:	python3-mock
BuildRequires:	python3-pyOpenSSL
BuildRequires:	python3-pyscard
BuildRequires:	python3-pyusb
BuildRequires:	python3-six
%endif
Requires:	python3-fido2 >= 1.0.0
Requires:	python3-modules >= 1:3.6
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
%{__python3} -m unittest discover -s tests
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
