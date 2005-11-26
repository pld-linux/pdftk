Summary:	pdftk - the pdf tool kit
Summary(pl):	pdftk - Zestaw narzêdzi dla plików PDF
Name:		pdftk
Version:	1.12
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.pdfhacks.com/pdftk/%{name}-%{version}.tar.bz2
# Source0-md5:	ec1b6d9e06109c6f05e19033f1d91d8a
URL:		http://www.accesspdf.com/pdftk/
BuildRequires:	gcc-java
BuildRequires:	libgcj-devel
BuildRequires:	libwmf-devel
BuildRequires:	jasper-devel
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

%description -l pl
pdftk to proste narzêdzie do pracy codziennej z dokumentami PDF.
Umo¿liwia ³±czenie dokumentów PDF, dzielenie stron PDF na nowe
dokumenty, odszyfrowywanie wej¶cia w razie potrzeby (wymaga has³a),
opcjonalne szyfrowanie wyj¶cia, dodawanie znaku wodnego, wype³nianie
formularzy PDF z danymi FDF i/lub tworzenie raportów z formularzy na
metrykach PDF wraz z metadanymi i zak³adkami, uaktualnianie metadanych
PDF, do³±czanie plików do stron lub dokumentów PDF, rozpakowywanie
za³±czników PDF, rozk³adanie dokumentu PDF na pojedyncze strony,
dekompresjê lub ponown± kompresjê strumieni stron, naprawianie
uszkodzonych plików PDF (w miarê mo¿liwo¶ci).

%prep
%setup -q

%build
unset CLASSPATH
%{__make} -f Makefile.RedHat -C pdftk

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install pdftk/pdftk $RPM_BUILD_ROOT%{_bindir}/pdftk
install debian/pdftk.1 $RPM_BUILD_ROOT%{_mandir}/man1/pdftk.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc pdftk.1.html pdftk.1.notes pdftk.1.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
