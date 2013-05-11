#
# Conditional build:
%bcond_without	static_libs	# static library build
#
Summary:	A pipeline manipulation library
Summary(pl.UTF-8):	Biblioteka operacji na linii potoków
Name:		libpipeline
Version:	1.2.3
Release:	1
License:	GPL v3+
Group:		Development/Libraries
Source0:	http://download.savannah.gnu.org/releases/libpipeline/%{name}-%{version}.tar.gz
# Source0-md5:	f4866aa3a84f2852c78f87ff619dfc60
URL:		http://libpipeline.nongnu.org/
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
# Fedoraish Dep: http://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries
Provides:	bundled(gnulib)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpipeline is a C library for setting up and running pipelines of
processes, without needing to involve shell command-line parsing which
is often error-prone and insecure. This alleviates programmers of the
need to laboriously construct pipelines using lower-level primitives
such as fork(2) and execve(2).

%description -l pl.UTF-8
libpipeline to biblioteka C do ustanawiania i uruchamiania linii
potoków procesów bez potrzeby wykonywania analizy linii poleceń, która
jest zwykle błędogenna i niebezpieczna. Ogranicza konieczność
pracochłonnego tworzenia linii potoków przez programistów przy użyciu
niskopoziomowych wywołań, takich jak fork(2) i execve(2).

%package devel
Summary:	Header file for pipeline manipulation library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki operacji na linii potoków
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libpipeline-devel contains the header file needed to develop programs
that use libpipeline library.

%description devel -l pl.UTF-8
Ten pakiet zawiera plik nagłówkowy potrzebny do tworzenia programów
wykorzystujących bibliotekę libpipeline.

%package static
Summary:	Static libpipeline library
Summary(pl.UTF-8):	Statyczna biblioteka libpipeline
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpipeline library.

%description static -l pl.UTF-8
Statyczna biblioteka libpipeline.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	prefix=%{_prefix} \
	INSTALL='install -p' \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpipeline.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libpipeline.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpipeline.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpipeline.so
%{_includedir}/pipeline.h
%{_mandir}/man3/libpipeline.3*
%{_mandir}/man3/pipecmd_*.3*
%{_mandir}/man3/pipeline_*.3*
%{_pkgconfigdir}/libpipeline.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpipeline.a
%endif
