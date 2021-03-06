#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-FindBin-libs
#    Version:           2.019002
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only FindBin\:\:libs
#

Name:           opt-perl-FindBin-libs
Version:        2.019002
Release:        1%{?dist}
Summary:        unknown
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/FindBin-libs/
BuildRoot:      /tmp/cpantorpm/FindBin-libs-2.019002-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/L/LE/LEMBARK/FindBin-libs-2.019002.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(FindBin::libs) = v2.12.01
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(File::Basename)
Requires:       opt-perl(File::Spec::Functions)
Requires:       opt-perl(File::Temp)
Requires:       opt-perl(FindBin)
Requires:       opt-perl(List::Util)
Requires:       opt-perl(Symbol)
Requires:       opt-perl(Test::More)
Requires:       opt-perl(strict)
Requires:       opt-perl(version)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(File::Basename)
BuildRequires:  opt-perl(File::Spec::Functions)
BuildRequires:  opt-perl(File::Temp)
BuildRequires:  opt-perl(FindBin)
BuildRequires:  opt-perl(List::Util)
BuildRequires:  opt-perl(Symbol)
BuildRequires:  opt-perl(Test::More)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(version)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
=head2 General Use

%prep

%setup  -n FindBin-libs-2.019002
chmod -R u+w %{_builddir}/FindBin-libs-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS" INSTALLDIRS=site SITEPREFIX=/opt/perl INSTALLSITEARCH=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi INSTALLSITELIB=/opt/perl/lib/site_perl/5.26.0 INSTALLSITEBIN=/opt/perl/bin INSTALLSITESCRIPT=/opt/perl/bin INSTALLSITEMAN1DIR=/opt/perl/man/man1 INSTALLSITEMAN3DIR=/opt/perl/man/man3 INSTALLSCRIPT=/opt/perl/bin
make %{?_smp_mflags}

#
# This is included here instead of in the 'check' section because
# older versions of rpmbuild (such as the one distributed with RHEL5)
# do not do 'check' by default.
#

if [ -z "$RPMBUILD_NOTESTS" ]; then
   make test
fi

%install

rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
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
* Thu Oct 04 2018 Rocks 2.019002-1
- Generated using cpantorpm

