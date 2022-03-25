#
# Conditional build:
%bcond_with	tests		# unit tests (broken as of 1.0.1)

Summary:	Tool for managing your YubiKey configuration
Summary(pl.UTF-8):	Narzędzie do zarządzania urządzeniami YubiKey
Name:		yubikey-manager
Version:	4.0.8
Release:	3
License:	BSD
Group:		Applications/System
Source0:	https://developers.yubico.com/yubikey-manager/Releases/%{name}-%{version}.tar.gz
# Source0-md5:	490a2f5d1b49d31f6a94c9901888803c
URL:		https://developers.yubico.com/yubikey-manager/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cryptography
BuildRequires:	python3-fido2 >= 0.9.0
BuildRequires:	python3-mock
BuildRequires:	python3-pyOpenSSL
BuildRequires:	python3-pyscard
BuildRequires:	python3-pyusb
BuildRequires:	python3-six
%endif
Requires:	python3-fido2 >= 0.9.0
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python library and command line tool for configuring a YubiKey.

%description -l pl.UTF-8
Pythonowa biblioteka i narzędzie linii poleceń do konfiguracji
urządzeń YubiKey.

%prep
%setup -q

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
