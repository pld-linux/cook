Summary:	A file construction tool
Summary(pl):	Narzêdzie do konstrukcji plików
Name:		cook
Version:	2.19
Release:	2
License:	GPL
Group:		Development/Building
Source0:	http://www.canb.auug.org.au/~millerp/cook/%{name}-%{version}.tar.gz
URL:		http://www.canb.auug.org.au/~millerp/cook/
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
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} RPM_BUILD_ROOT=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/cook/en

install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install cook.gif $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README lib/en/*.{ps,txt}

%files
%defattr(644,root,root,755)
%doc *.gz lib/en/*.txt.gz 
%attr(0755,root,root) %{_bindir}/*
%{_libdir}/cook
%{_datadir}/cook
%{_mandir}/man*/*
%{_pixmapsdir}/cook.gif

%files doc-ps
%defattr(644,root,root,755)
%doc lib/en/*.ps.gz

%clean
rm -rf $RPM_BUILD_ROOT
