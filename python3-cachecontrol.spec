Summary:	httplib2 caching for requests
Name:		python3-cachecontrol
Version:	0.14.2
Release:	1
License:	Apache v2
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cachecontrol/
Source0:	https://files.pythonhosted.org/packages/source/c/cachecontrol/cachecontrol-%{version}.tar.gz
# Source0-md5:	1c7bd3fcebd1877270fb662c1ede2f75
URL:		https://pypi.org/project/CacheControl/
BuildRequires:	python3 >= 1:3.8
BuildRequires:	python3-build
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-flit_core >= 3.2
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CacheControl is a port of the caching algorithms in httplib2 for use
with requests session object.

It was written because httplib2’s better support for caching is often
mitigated by its lack of thread safety. The same is true of requests
in terms of caching.

%prep
%setup -q -n cachecontrol-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/doesitcache
%dir %{py3_sitescriptdir}/cachecontrol
%{py3_sitescriptdir}/cachecontrol/*.py
%{py3_sitescriptdir}/cachecontrol/__pycache__
%{py3_sitescriptdir}/cachecontrol/py.typed
%dir %{py3_sitescriptdir}/cachecontrol/caches
%{py3_sitescriptdir}/cachecontrol/caches/*.py
%{py3_sitescriptdir}/cachecontrol/caches/__pycache__
%{py3_sitescriptdir}/cachecontrol-%{version}.dist-info
