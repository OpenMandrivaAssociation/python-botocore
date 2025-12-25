Name:		python-botocore
Version:	1.42.16
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/botocore/botocore-%{version}.tar.gz
Summary:	Low-level, data-driven core of boto 3.
URL:		https://pypi.org/project/botocore/
License:	Apache License 2.0
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Low-level, data-driven core of boto 3.

%files
%{py_sitedir}/botocore
%{py_sitedir}/botocore-*.*-info
