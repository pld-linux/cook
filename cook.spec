#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
Summary:	A file construction tool
Summary(pl.UTF-8):	Narzędzie do konstrukcji plików
Name:		cook
Version:	2.25
Release:	3
License:	GPL
Group:		Development/Building
Source0:	http://www.canb.auug.org.au/~millerp/cook/%{name}-%{version}.tar.gz
# Source0-md5:	fd116da31c59c04abe41519fc131b504
URL:		http://www.canb.auug.org.au/~millerp/cook/
BuildRequires:	bison
BuildRequires:	gettext-tools
BuildRequires:	groff
BuildRequires:	sharutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cook is a tool for constructing files. It is given a set of files to
create, and recipes of how to create them. In any non-trivial program
there will be prerequisites to performing the actions necessary to
creating any file, such as include files. The cook program provides a
mechanism to define these.

When a program is being developed or maintained, the programmer will
typically change one file of several which comprise the program. Cook
examines the last-modified times of the files to see when the
prerequisites of a file have changed, implying that the file needs to
be recreated as it is logically out of date.

Cook also provides a facility for implicit recipes, allowing users to
specify how to form a file with a given suffix from a file with a
different suffix. For example, to create filename.o from filename.c

- Cook is a replacement for the traditional make(1) tool. However, it
  is necessary to convert makefiles into cookbooks using the make2cook
  utility included in the distribution.

- Cook has a simple but powerful string-based description language
  with many built-in functions. This allows sophisticated filename
  specification and manipulation without loss of readability or
  performance.

- Cook is able to use fingerprints to supplement file modification
  times. This allows build optimization without contorted rules.

- Cook is able to build your project with multiple parallel threads,
  with support for rules which must be single threaded. It is possible
  to distribute parallel builds over your LAN, allowing you to turn your
  network into a virtual parallel build engine.

If you are putting together a source-code distribution and planning to
write a makefile, consider writing a cookbook instead. Although Cook
takes a day or two to learn, it is much more powerful and a bit more
intuitave than the traditional make(1) tool. And Cook doesn't
interpret tab differently to 8 space characters!

%description -l pl.UTF-8
Cook jest narzędziem do tworzenia plików. Podaje mu się listę plików do
utworzenia oraz reguły wyjaśniające jak je utworzyć. Każdy nietrywialny
program wymaga podjęcia pewnych działań koniecznych do utworzenia
różnych plików, jak np. plików nagłówkowych. Cook udostępnia mechanizmy
pozwalający je zdefiniować.

Tworząc i rozwijając program zazwyczaj modyfikuje się pliki, z których
się składa. Cook bada daty ostatniej modyfikacji sprawdzając, czy
zmieniły się zależności; jeśli tak, pliki powinny zostać zaktualizowane.

Cook umożliwia również definiowanie niejawnych reguł, pozwalając
użytkownikom wyszczególnić metody tworzenia plików o podanym
rozszerzeniu z pliku o innym rozszerzeniu (np. jak utworzyć
plik.o z plik.c).

- Cook jest zamiennikiem tradycyjnego narzędzia make(1). Jednak przed
użyciem plików Makefile z cookiem, należy wcześniej przekształcić
je do formatu rozumianego przez cooka przy użyciu narzędzia make2cook
dostarczanego wraz z dystrybucją.

- Cook posiada prosty lecz potężny język opisowy, z wieloma wbudowanymi
  funkcjami, dzięki czemu można podawać i manipulować skomplikowanymi
  specyfikacjami nazw plików bez utraty czytelności i wydajności.

- Oprócz daty ostatniej modyfikacji, cook pozwala korzystać z fingerprintów.
  Dzięki temu można zoptymalizować proces budowania nie uciekając się
  do nienaturalnych reguł.

- Cook potrafi przeprowadzić proces budowania w wielu równoległych
  wątkach, obsługując prawidłowo reguły jednowątkowe. Można
  przeprowadzić rozproszone budowanie w sieci LAN, przekształcając
  lokalną sieć w wirtualną maszynę do budowania równoległego.

Jeśli tworzysz program od zera i planujesz napisać Makefile,
przemyśl możliwość wykorzystania zamiast niego pliku cookbook.
Choć na naukę Cooka trzeba poświęcić dzień lub dwa, jest to
narzędzie o wiele potężniejsze i znacznie bardziej intuicyjne niż
tradycyjne make(1). Poza tym Cook nie traktuje inaczej TAB-a i
ośmiu spacji!

%package doc-ps
Summary:	Cook documentation, PostScript format
Summary(pl.UTF-8):	Dokumentacja do cooka w formacie PostScript
Group:		Development/Building

%description doc-ps
Cook documentation in PostScript format.

%description doc-ps -l pl.UTF-8
Dokumentacja do cooka w formacie PostScript.

%prep
%setup -q

%build
%configure \
	NLSDIR=%{_datadir}/locale \
	ac_cv_lib_rx_main=no \
	ac_cv_header_rxposix_h=no
%{__make}

%{?with_tests:%{__make} sure}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/cook/en/LC_MESSAGES,%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_datadir}/{locale,cook/en}}

ln -s $RPM_BUILD_ROOT%{_mandir}/man1 $RPM_BUILD_ROOT%{_datadir}/cook/en/man1

%{__make} install \
	RPM_BUILD_ROOT=$RPM_BUILD_ROOT

install cook.gif $RPM_BUILD_ROOT%{_pixmapsdir}/cook.gif

mv $RPM_BUILD_ROOT%{_libdir}/cook/en $RPM_BUILD_ROOT%{_datadir}/locale/
rm -r $RPM_BUILD_ROOT%{_datadir}/cook/en

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README lib/en/*.txt
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/cook
%{_mandir}/man*/*
%{_pixmapsdir}/cook.gif

%files doc-ps
%defattr(644,root,root,755)
%doc lib/en/*.ps
