Name:           python-jsonpatch
Version:        1.9
Release:        1
Summary:        Applying JSON Patches in Python
License:        Modified BSD License
Group:          Development/Languages/Python
Url:            https://pypi.python.org/packages/source/j/jsonpatch/jsonpatch-%{version}.tar.gz
Source0:        jsonpatch-%{version}.tar.gz

BuildRequires: python2
BuildRequires: python2-libs
BuildRequires: python-setuptools

Requires: python-jsonpointer

BuildArch:      noarch

%description
Library to apply JSON Patches according to RFC 6902.

%prep
%setup -n jsonpatch-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/*
%{_bindir}/jsondiff
%{_bindir}/jsonpatch

%changelog
* Wed Mar 04 2015 Mahmoud Bassiouny <mbassiouny@vmware.com>
- Initial packaging for Photon