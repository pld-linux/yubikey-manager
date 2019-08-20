#
# Conditional build:
%bcond_with	tests		# unit tests (broken as of 1.0.1)

Summary:	Tool for managing your YubiKey configuration
Summary(pl.UTF-8):	Narzędzie do zarządzania urządzeniami YubiKey
Name:		yubikey-manager
Version:	3.1.0
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://developers.yubico.com/yubikey-manager/Releases/%{name}-%{version}.tar.gz
# Source0-md5:	0546eca40e78e689cda7e69c194f51b5
URL:		https://developers.yubico.com/yubikey-manager/
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-cryptography
BuildRequires:	python-enum34
BuildRequires:	python-fido2 >= 0.7.0
BuildRequires:	python-mock
BuildRequires:	python-pyOpenSSL
BuildRequires:	python-pyscard
BuildRequires:	python-pyusb
BuildRequires:	python-six
%endif
Requires:	python-fido2 >= 0.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python library and command line tool for configuring a YubiKey.

%description
Pythonowa biblioteka i narzędzie linii poleceń do konfiguracji
urządzeń YubiKey.

%prep
%setup -q

# integration tests, require device
%{__rm} -r test/on_yubikey

%build
%py_build

%if %{with tests}
%{__python} -m unittest discover -s test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.adoc
%attr(755,root,root) %{_bindir}/ykman
%{py_sitescriptdir}/ykman
%{py_sitescriptdir}/yubikey_manager-%{version}-py*.egg-info
