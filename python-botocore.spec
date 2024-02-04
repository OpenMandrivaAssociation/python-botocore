Name:		python-botocore
Version:	1.34.34
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/botocore/botocore-%{version}.tar.gz
Summary:	Low-level, data-driven core of boto 3.
URL:		https://pypi.org/project/botocore/
License:	Apache License 2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Low-level, data-driven core of boto 3.

%prep
%autosetup -p1 -n botocore-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/botocore
%{py_sitedir}/botocore-*.*-info
