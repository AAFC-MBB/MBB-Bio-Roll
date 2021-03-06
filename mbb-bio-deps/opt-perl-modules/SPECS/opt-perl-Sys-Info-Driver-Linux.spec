#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Sys-Info-Driver-Linux
#    Version:           0.7903
#    cpantorpm version: 1.08
#    Date:              Wed Nov 14 2018
#    Command:
# /opt/perl/bin/cpantorpm --NO-TESTS --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Sys\:\:Info\:\:Driver\:\:Linux
#

Name:           opt-perl-Sys-Info-Driver-Linux
Version:        0.7903
Release:        1%{?dist}
Summary:        Linux driver for Sys::Info
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sys-Info-Driver-Linux/
BuildRoot:      /tmp/cpantorpm/Sys-Info-Driver-Linux-0.7903-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/B/BU/BURAK/Sys-Info-Driver-Linux-0.7903.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Sys::Info::Driver::Linux) = 0.7903
Provides:       opt-perl(Sys::Info::Driver::Linux::Constants) = 0.7903
Provides:       opt-perl(Sys::Info::Driver::Linux::Device) = 0.7903
Provides:       opt-perl(Sys::Info::Driver::Linux::Device::CPU) = 0.7903
Provides:       opt-perl(Sys::Info::Driver::Linux::OS) = 0.7903
Provides:       opt-perl(Sys::Info::Driver::Linux::OS::Distribution) = 0.7903
Provides:       opt-perl(Sys::Info::Driver::Linux::OS::Distribution::Conf) = 0.7903
Requires:       opt-perl
Requires:       opt-perl(Config::General)
Requires:       opt-perl(Unix::Processors)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Config::General)
BuildRequires:  opt-perl(Unix::Processors)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This document describes version 0.7903 of Sys::Info::Driver::Linux
released on 8 May 2013.

%prep

%setup  -n Sys-Info-Driver-Linux-0.7903
chmod -R u+w %{_builddir}/Sys-Info-Driver-Linux-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Build.PL optimize="$RPM_OPT_FLAGS" --installdirs site --install_path arch=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi --install_path lib=/opt/perl/lib/site_perl/5.26.0 --install_path script=/opt/perl/bin --install_path bin=/opt/perl/bin --install_path libdoc=/opt/perl/man/man3 --install_path bindoc=/opt/perl/man/man1
./Build


%install

rm -rf $RPM_BUILD_ROOT
./Build pure_install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%clean

rm -rf $RPM_BUILD_ROOT

%files

%defattr(-,root,root,-)
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man3/*

%changelog
* Wed Nov 14 2018 Rocks 0.7903-1
- Generated using cpantorpm

