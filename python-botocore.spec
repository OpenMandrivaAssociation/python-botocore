%define module botocore

Name:		python-botocore
Version:	1.42.47
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Low-level, data-driven core of boto 3.
URL:		https://pypi.org/project/botocore/
License:	Apache-2.0
Group:		Development/Python
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
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
