#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	Strip
Summary:	String::Strip - Perl extension for fast, commonly used, string operations
Summary(pl.UTF-8):	String::Strip - rozszerzenie Perla do szybkich, często używanych operacji na łańcuchach
Name:		perl-String-Strip
Version:	1.01
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a1471ad67dbb7375dd0d288026ee7122
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
StripLTSpace	- Removes Leading and Trailing spaces from given string
StripTSpace	- Removes Trailing spaces from given string
StripLSpace	- Removes Leading spaces from given string
StripSpace	- Removes all spaces from given string

I do these things often, and these routines tend to be about 35% faster
than the corresponding regex methods.

%description -l pl.UTF-8
StripLTSpace	- usuwa wiodące i końcowe spacje z podanego łańcucha
StripTSpace	- usuwa końcowe spacje z podanego łańcucha
StripLSpace	- usuwa wiodące spacje z podanego łańcucha
StripSpace	- usuwa wszystkie spacje z podanego łańcucha

Autor modułu często wykonuje te rzeczy, a te funkcje są około 35%
szybsze od odpowiadających im metod używających wyrażeń regularnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/%{pdir}/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.so
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.ix
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.bs
%{_mandir}/man3/*
