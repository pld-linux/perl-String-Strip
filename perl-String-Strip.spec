#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Strip
Summary:	String::Strip - Perl extension for fast, commonly used, string operations
Summary(pl):	String::Strip - rozszerzenie do szybkich, cz�sto u�ywanych operacji na �a�cuchach
Name:		perl-String-Strip
Version:	1.01
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
 StripLTSpace - Removes Leading and Trailing spaces from given string
 StripTSpace  - Removes Trailing spaces from given string
 StripLSpace  - Removes Leading spaces from given string
 StripSpace   - Removes all spaces from given string

I do these things often, and these routines tend to be about 35% faster
than the corresponding regex methods.

%description -l pl
 StripLTSpace - usuwa wiod�ce i ko�cowe spacje z podanego �a�cucha
 StripTSpace  - usuwa ko�cowe spacje z podanego �a�cucha
 StripLSpace  - usuwa wiod�ce spacje z podanego �a�cucha
 StripSpace   - usuwa wszystkie spacje z podanego �a�cucha

Autor modu�u cz�sto wykonuje te rzeczy, a te funkcje s� oko�o 35%
szybsze od odpowiadaj�cych im metod u�ywaj�cych wyra�e� regularnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/%{pdir}/*.pm
%dir %{perl_sitearch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_sitearch}/auto/%{pdir}/%{pnam}/*.so
%{perl_sitearch}/auto/%{pdir}/%{pnam}/*.ix
%{perl_sitearch}/auto/%{pdir}/%{pnam}/*.bs
%{_mandir}/man3/*
