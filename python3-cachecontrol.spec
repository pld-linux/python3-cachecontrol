#
# Conditional build:
%bcond_with	tests	# unit tests (not in sdist)

Summary:	httplib2 caching for requests
Summary(pl.UTF-8):	Pamięc podręczna httplib2 dla requests
Name:		python3-cachecontrol
Version:	0.14.4
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cachecontrol/
Source0:	https://files.pythonhosted.org/packages/source/c/cachecontrol/cachecontrol-%{version}.tar.gz
# Source0-md5:	37d8306a667facb1adc47a159a3733ce
URL:		https://pypi.org/project/CacheControl/
BuildRequires:	python3 >= 1:3.10
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-uv-build >= 0.9.6
BuildRequires:	python3-uv-build < 0.10
%if %{with tests}
BuildRequires:	python3-filelock >= 3.8.0
BuildRequires:	python3-msgpack >= 0.5.2
BuildRequires:	python3-msgpack < 2
BuildRequires:	python3-requests >= 2.16.0
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CacheControl is a port of the caching algorithms in httplib2 for use
with requests session object.

It was written because httplib2's better support for caching is often
mitigated by its lack of thread safety. The same is true of requests
in terms of caching.

%description -l pl.UTF-8
CacheControl to port algorytmów cache'ujących z httplib2 do użycia z
obiektami sesji requests.

Port powstał, ponieważ lepsza obsługa pamięci podręcznej w httplib2
jest zwykle niweczona przez brak dobrej obsługi wątków. Tak samo jest
w przypadku pamięci podręcznej w requests.

%prep
%setup -q -n cachecontrol-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%attr(755,root,root) %{_bindir}/doesitcache
%dir %{py3_sitescriptdir}/cachecontrol
%{py3_sitescriptdir}/cachecontrol/*.py
%{py3_sitescriptdir}/cachecontrol/__pycache__
%{py3_sitescriptdir}/cachecontrol/py.typed
%dir %{py3_sitescriptdir}/cachecontrol/caches
%{py3_sitescriptdir}/cachecontrol/caches/*.py
%{py3_sitescriptdir}/cachecontrol/caches/__pycache__
%{py3_sitescriptdir}/cachecontrol-%{version}.dist-info
