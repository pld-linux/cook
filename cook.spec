#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
Summary:	A file construction tool
Summary(pl):	Narzêdzie do konstrukcji plików
Name:		cook
Version:	2.25
Release:	1
License:	GPL
Group:		Development/Building
Source0:	http://www.canb.auug.org.au/~millerp/cook/%{name}-%{version}.tar.gz
# Source0-md5:	fd116da31c59c04abe41519fc131b504
URL:		http://www.canb.auug.org.au/~millerp/cook/
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	groff
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

%description -l pl
Cook jest narzêdziem do tworzenia plików. Podaje mu siê listê plików do
utworzenia oraz regu³y wyja¶niaj±ce jak je utworzyæ. Ka¿dy nietrywialny
program wymaga podjêcia pewnych dzia³añ koniecznych do utworzenia
ró¿nych plików, jak np. plików nag³ówkowych. Cook udostêpnia mechanizmy
pozwalaj±cy je zdefiniowaæ.

Tworz±c i rozwijaj±c program zazwyczaj modyfikuje siê pliki, z których
siê sk³ada. Cook bada daty ostatniej modyfikacji sprawdzaj±c, czy
zmieni³y siê zale¿no¶ci; je¶li tak, pliki powinny zostaæ zaktualizowane.

Cook umo¿liwia równie¿ definiowanie niejawnych regu³, pozwalaj±c
u¿ytkownikom wyszczególniæ metody tworzenia plików o podanym
rozszerzeniu z pliku o innym rozszerzeniu (np. jak utworzyæ
plik.o z plik.c).

- Cook jest zamiennikiem tradycyjnego narzêdzia make(1). Jednak przed
u¿yciem plików Makefile z cookiem, nale¿y wcze¶niej przekszta³ciæ
je do formatu rozumianego przez cooka przy u¿yciu narzêdzia make2cook
dostarczanego wraz z dystrybucj±.

- Cook posiada prosty lecz potê¿ny jêzyk opisowy, z wieloma wbudowanymi
  funkcjami, dziêki czemu mo¿na podawaæ i manipulowaæ skomplikowanymi
  specyfikacjami nazw plików bez utraty czytelno¶ci i wydajno¶ci.

- Oprócz daty ostatniej modyfikacji, cook pozwala korzystaæ z fingerprintów.
  Dziêki temu mo¿na zoptymalizowaæ proces budowania nie uciekaj±c siê
  do nienaturalnych regu³.

- Cook potrafi przeprowadziæ proces budowania w wielu równoleg³ych
  w±tkach, obs³uguj±c prawid³owo regu³y jednow±tkowe. Mo¿na
  przeprowadziæ rozproszone budowanie w sieci LAN, przekszta³caj±c
  lokaln± sieæ w wirtualn± maszynê do budowania równoleg³ego.

Je¶li tworzysz program od zera i planujesz napisaæ Makefile,
przemy¶l mo¿liwo¶æ wykorzystania zamiast niego pliku cookbook.
Choæ na naukê Cooka trzeba po¶wiêciæ dzieñ lub dwa, jest to
narzêdzie o wiele potê¿niejsze i znacznie bardziej intuicyjne ni¿
tradycyjne make(1). Poza tym Cook nie traktuje inaczej TAB-a i
o¶miu spacji!

%package doc-ps
Summary:	Cook documentation, PostScript format
Summary(pl):	Dokumentacja do cooka w formacie PostScript
Group:		Development/Building

%description doc-ps
Cook documentation in PostScript format.

%description doc-ps -l pl
Dokumentacja do cooka w formacie PostScript.

%prep
%setup -q

%build
%configure \
	NLSDIR=%{_datadir}/locale
%{__make}

%{?with_tests:%{__make} sure}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/cook/en/LC_MESSAGES
install -d $RPM_BUILD_ROOT%{_datadir}/locale
install -d $RPM_BUILD_ROOT%{_datadir}/cook/en
ln -s $RPM_BUILD_ROOT%{_mandir}/man1 $RPM_BUILD_ROOT%{_datadir}/cook/en/man1
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	RPM_BUILD_ROOT=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_libdir}/cook/en $RPM_BUILD_ROOT%{_datadir}/locale/
rm -r $RPM_BUILD_ROOT%{_datadir}/cook/en
install -D cook.gif $RPM_BUILD_ROOT%{_pixmapsdir}/cook.gif

%find_lang %{name} --with-gnome --all-name

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

%clean
rm -rf $RPM_BUILD_ROOT
