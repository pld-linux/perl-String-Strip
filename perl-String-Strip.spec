#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	String
%define		pnam	Strip
Summary:	String::Strip - Perl extension for fast, commonly used, string operations
Summary(pl.UTF-8):	String::Strip - rozszerzenie Perla do szybkich, często używanych operacji na łańcuchach
Name:		perl-String-Strip
Version:	1.02
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/String/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af9e625b14729d3c66b3a78a208ae85c
URL:		http://search.cpan.org/dist/String-Strip/
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
%{perl_vendorarch}/String/*.pm
%dir %{perl_vendorarch}/auto/String/Strip
%attr(755,root,root) %{perl_vendorarch}/auto/String/Strip/*.so
%{perl_vendorarch}/auto/String/Strip/*.ix
%{_mandir}/man3/*
