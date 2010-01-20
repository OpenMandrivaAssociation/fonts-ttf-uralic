Summary: Truetype fonts for Cyrillic-based Uralic languages
Name: fonts-ttf-uralic
Version: 0
Release: %mkrel 2.20040829.3
License: GPLv2+
Group: System/Fonts/True type
URL: http://peoples.org.ru/eng_uralic.html
Source0: http://www.peoples.org.ru/font/BookmanUralic.zip
Source1: http://www.peoples.org.ru/font/ChanceryUralic.zip
Source2: http://www.peoples.org.ru/font/GothicUralic.zip
Source3: http://www.peoples.org.ru/font/MonoUralic.zip
Source4: http://www.peoples.org.ru/font/PalladioUralic.zip
Source5: http://www.peoples.org.ru/font/RomanUralic.zip
Source6: http://www.peoples.org.ru/font/SansCondUralic.zip
Source7: http://www.peoples.org.ru/font/SansUralic.zip
Source8: http://www.peoples.org.ru/font/SchoolbookUralic.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: freetype-tools

%description
The Uralic fonts contain additional letters used in most Uralic languages
with Russian-based writing systems - Khanty (all dialects), Komi, Mansi 
(without marking long vowels), Mari, Nenets, Selkup and Udmurt. 

The fonts also support Altai, Chukchi, Even, Evenki, Koryak and Nanai.

Font list:

   * Bookman Uralic (regular, bold, italic)
   * Chancery Uralic - Decorative calligraphic font
   * Gothic Uralic (regular, bold) - Futura-like sans serif
   * Mono Uralic (regular) - Courier-like fixed width font
   * Palladio Uralic (regular, bold, italic) - Palatino-like typeface
   * Roman Uralic (regular, bold, italic) - Times-like typeface
   * Sans Uralic (regular, bold, italic, bold italic) - Helvetica-like
     sans serif typeface
   * Sans Condensed Uralic (regular, bold) - Narrow version of Sans Uralic
   * Schoolbook Uralic (regular, bold, italic)

These fonts cover ISO10646-1 and CP1251 charsets.

%prep
%setup -q -c 
unzip -qq -o %{SOURCE1}
unzip -qq -o %{SOURCE2}
unzip -qq -o %{SOURCE3}
unzip -qq -o %{SOURCE4}
unzip -qq -o %{SOURCE5}
unzip -qq -o %{SOURCE6}
unzip -qq -o %{SOURCE7}
unzip -qq -o %{SOURCE8}
chmod 0644 license.txt

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/uralic

install -m 644 *.TTF $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/uralic
ttmkfdir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/uralic > $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/uralic/fonts.dir
ln -s fonts.dir $RPM_BUILD_ROOT%{_datadir}/fonts/TTF/uralic/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/uralic \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-uralic:pri=50

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc license.txt
%dir %{_datadir}/fonts/TTF/uralic
%{_datadir}/fonts/TTF/uralic/*.TTF
%verify(not mtime) %{_datadir}/fonts/TTF/uralic/fonts.dir
%{_datadir}/fonts/TTF/uralic/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-uralic:pri=50
