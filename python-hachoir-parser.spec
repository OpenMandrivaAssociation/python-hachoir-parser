%define module_name hachoir-parser

Summary:	Python library to parse file format for the hachoir framework
Name: 		python-%{module_name}
Version: 	1.2.1
Release: 	%mkrel 2
Source0: 	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
URL: 		http://hachoir.org/wiki/hachoir-parser
BuildArch:	noarch
Requires:	python-hachoir-core
%{py_requires -d}
BuildRequires:	python-setuptools

%description
hachoir-parser is a package of most common file format parsers written 
using hachoir-core. Not all parsers are complete, some are very good and 
other are poor: only parse first level of the tree for example.

A perfect parser have no "raw" field: with a perfect parser you are able 
to know *each* bit meaning. Some good (but not perfect ;-)) parsers:

    * Matroska video
    * Microsoft RIFF (AVI video, WAV audio, CDA file)
    * PNG picture
    * TAR and ZIP archive 

%prep
%setup -q -n %{module_name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%dir %{py_puresitedir}/hachoir_parser
