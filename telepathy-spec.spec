Summary:	Telepathy specication
Summary(pl.UTF-8):	Specyfikacja Telepathy
Name:		telepathy-spec
Version:	0.27.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://telepathy.freedesktop.org/releases/telepathy-spec/%{name}-%{version}.tar.gz
# Source0-md5:	acb1b820d3254a410ad994c7ac698c12
URL:		https://telepathy.freedesktop.org/spec/
BuildRequires:	libxslt-progs
BuildRequires:	python3 >= 1:3
BuildRequires:	python3-jinja2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
telepathy-spec is the canonical description of the Telepathy D-Bus
API, on which all other Telepathy projects are based.

Telepathy is a D-Bus framework for unifying real time communication,
including instant messaging, voice calls and video calls. It abstracts
differences between protocols to provide a unified interface for
applications.

%description -l pl.UTF-8
telepathy-spec to kanoniczny opis API D-Busowego Telepathy, na którym
oparte są wszystkie pozostałe projekty Telepathy.

Telepathy to szkielet D-Busowy ujednolicający komunikację w czasie
rzeczywistym, w tym komunikatory, połączenia głosowe i wideo.
Abstrahuje różnice między protokołami w celu udostępnienia jednolitego
interfejsu dla aplikacji.

%prep
%setup -q

%build
%{__make}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYRIGHT ChangeLog NEWS README doc/spec
