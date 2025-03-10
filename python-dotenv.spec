# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		dotenv
%define		pypi_name	python-dotenv
%define		egg_name	python_dotenv
Summary:	Add .env support to your django/flask apps in development and deployments
Name:		python-%{module}
Version:	0.17.0
Release:	6
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/python-dotenv/
Source0:	https://files.pythonhosted.org/packages/source/p/python-dotenv/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	664e1fd991a2dd109c95b743bb9eecd5
URL:		https://pypi.org/project/python-dotenv/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Add .env support to your django/flask apps in development and
deployments.

%package -n python3-%{module}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
Add .env support to your django/flask apps in development and
deployments.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG.md CONTRIBUTING.md README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
