#
# Conditional build:
%bcond_without	tests		# perform "make test"
#
%define	pdir	HTML
%define	pnam	Selector-XPath
Summary:	HTML::Selector::XPath - CSS Selector to XPath compiler
Summary(pl.UTF-8):	HTML::Selector::XPath - kompilator selektorów CSS do postaci języka XPath
Name:		perl-HTML-Selector-XPath
Version:	0.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bb46fc14bb6ea3169a6176db00cc68f6
URL:		http://search.cpan.org/dist/HTML-Selector-XPath/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:  perl-Test-Base
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Selector::XPath is a utility function to compile full set of
CSS2 and partial CSS3 selectors to the equivalent XPath expression.

%description -l pl.UTF-8
HTML::Selector::XPath jest modułem kompilującym pełny zestaw
selektorów CSS2 i częściowo CSS3 do postaci odpowiedniego
wyrażenia XPath.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/Selector/XPath.pm
%{_mandir}/man?/*
