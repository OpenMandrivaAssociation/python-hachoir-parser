%define module_name hachoir-parser

Summary:	Python library to parse file format for the hachoir framework
Name: 		python-%{module_name}
Version: 	1.3.4
Release: 	%mkrel 2
Source0: 	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group: 		Development/Python
BuildRoot: 	%{_tmppath}/%{name}-buildroot
URL: 		http://hachoir.org/wiki/hachoir-parser
BuildArch:	noarch
Requires:	python-hachoir-core
%{py_requires -d}
BuildRequires:	python-setuptools python-hachoir-core

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
python setup.py install --root=%{buildroot} 

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc AUTHORS COPYING 
%{py_puresitedir}/hachoir_parser
%{py_puresitedir}/*.egg-info


%changelog
* Mon Nov 08 2010 Funda Wang <fwang@mandriva.org> 1.3.4-2mdv2011.0
+ Revision: 594925
- rebuild for py 2.7

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.4-1mdv2011.0
+ Revision: 569668
- update to new version 1.3.4

* Sun Apr 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.3-1mdv2010.1
+ Revision: 538755
- update to new version 1.3.3

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.2-1mdv2010.1
+ Revision: 515895
- update to 1.3.2

* Sun Feb 07 2010 Michael Scherer <misc@mandriva.org> 1.3.1-1mdv2010.1
+ Revision: 501619
- do not use --record, as this can lead to unoawned directory problem
- update to 1.3.1
- fix Url

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-2mdv2010.0
+ Revision: 442162
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.1-1mdv2009.1
+ Revision: 320021
- rebuild with python 2.6
- clean spec
- new release 1.2.1

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 242413
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 17 2007 Michael Scherer <misc@mandriva.org> 1.0-1mdv2008.0
+ Revision: 52798
- version 1.0

