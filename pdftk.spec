# TODO:		build system-wire itext.jar.so and use it here
#%define		itextvers 2.1.7
Summary:	pdftk - the PDF tool kit
Summary(pl.UTF-8):	pdftk - zestaw narzędzi dla plików PDF
Name:		pdftk
Version:	2.02
Release:	2
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/%{name}-%{version}-src.zip
# Source0-md5:	6534365fd6727724f288a556ede33faa
#Patch0:		%{name}-use-internal-itext.patch
#Patch1:		%{name}-classpath.patch
URL:		http://www.pdflabs.com/tools/pdftk-server/
BuildRequires:	gcc-java
BuildRequires:	jar
#BuildRequires:	jasper-devel
#BuildRequires:	java-itext >= %{itextvers}
BuildRequires:	libgcj-devel
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
#Requires:	java-itext >= %{itextvers}
Requires:	libgcj
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pdftk is a simple tool for doing everyday things with PDF documents.
It allows you to merge PDF documents, split PDF pages into a new
document, decrypt input as necessary (password required), encrypt
output as desired, apply a background watermark, fill PDF forms with
FDF data and/or flatten forms report on PDF metrics including Metadata
and Bookmarks, update PDF metadata, attach files to PDF pages or the
PDF document, unpack PDF attachments, burst a PDF document into single
pages, uncompress and re-compress page streams, repair corrupted PDF
(where possible).

%description -l pl.UTF-8
pdftk to proste narzędzie do pracy codziennej z dokumentami PDF.
Umożliwia łączenie dokumentów PDF, dzielenie stron PDF na nowe
dokumenty, odszyfrowywanie wejścia w razie potrzeby (wymaga hasła),
opcjonalne szyfrowanie wyjścia, dodawanie znaku wodnego, wypełnianie
formularzy PDF z danymi FDF i/lub tworzenie raportów z formularzy na
metrykach PDF wraz z metadanymi i zakładkami, uaktualnianie metadanych
PDF, dołączanie plików do stron lub dokumentów PDF, rozpakowywanie
załączników PDF, rozkładanie dokumentu PDF na pojedyncze strony,
dekompresję lub ponowną kompresję strumieni stron, naprawianie
uszkodzonych plików PDF (w miarę możliwości).

%prep
%setup -q -n %{name}-%{version}-dist
#%patch0 -p1
#%patch1 -p0

# remove bundled libraries from source tree
#%{__rm} -rf java

%build
unset CLASSPATH
%{__make} -j1 -f Makefile.Redhat -C pdftk \
	GJAR=jar \
	LIBDIR="%{_libdir}" \
#	ITEXTVERS="%{itextvers}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -p pdftk/pdftk $RPM_BUILD_ROOT%{_bindir}/pdftk
cp -p pdftk.1 $RPM_BUILD_ROOT%{_mandir}/man1/pdftk.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog.*
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
