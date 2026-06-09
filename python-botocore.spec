%define module botocore

Name:		python-botocore
Summary:	Low-level, data-driven core of boto 3
Version:	1.43.25
Release:	1
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/botocore/
Source0:	https://files.pythonhosted.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
Low-level, data-driven core of boto 3.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
