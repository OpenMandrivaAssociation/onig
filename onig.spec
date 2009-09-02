%define	major 2
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Regular expressions library
Name:		onig
Version:	5.9.1
Release:	%mkrel 3
License:	BSD
Group:		System/Libraries
URL:		http://www.geocities.jp/kosako3/oniguruma/
Source0:	http://www.geocities.jp/kosako3/oniguruma/archive/%{name}-%{version}.tar.gz
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Oniguruma is a regular expressions library. The characteristics of this library
is that different character encoding for every regular expression object can be
specified. (supported APIs: GNU regex, POSIX and Oniguruma native)

Supported character encodings:

 o ASCII, UTF-8, UTF-16BE, UTF-16LE, UTF-32BE, UTF-32LE,
 o EUC-JP, EUC-TW, EUC-KR, EUC-CN,
 o Shift_JIS, Big5, GB18030, KOI8-R, CP1251,
 o ISO-8859-1, ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-5,
 o ISO-8859-6, ISO-8859-7, ISO-8859-8, ISO-8859-9, ISO-8859-10,
 o ISO-8859-11, ISO-8859-13, ISO-8859-14, ISO-8859-15, ISO-8859-16
 o (GB18030 encoding was contributed by KUBO Takehiro)
 o (CP1251 encoding was contributed by Byte)

%package -n	%{libname}
Summary:	Regular expressions library
Group:          System/Libraries

%description -n	%{libname}
Oniguruma is a regular expressions library. The characteristics of this library
is that different character encoding for every regular expression object can be
specified. (supported APIs: GNU regex, POSIX and Oniguruma native)

Supported character encodings:

 o ASCII, UTF-8, UTF-16BE, UTF-16LE, UTF-32BE, UTF-32LE,
 o EUC-JP, EUC-TW, EUC-KR, EUC-CN,
 o Shift_JIS, Big5, GB18030, KOI8-R, CP1251,
 o ISO-8859-1, ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-5,
 o ISO-8859-6, ISO-8859-7, ISO-8859-8, ISO-8859-9, ISO-8859-10,
 o ISO-8859-11, ISO-8859-13, ISO-8859-14, ISO-8859-15, ISO-8859-16
 o (GB18030 encoding was contributed by KUBO Takehiro)
 o (CP1251 encoding was contributed by Byte)

This package provides the shared Oniguruma library.

%package -n	%{develname}
Summary:	Static library and header files for development with Oniguruma
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel

%description -n	%{develname}
Oniguruma is a regular expressions library. The characteristics of this library
is that different character encoding for every regular expression object can be
specified. (supported APIs: GNU regex, POSIX and Oniguruma native)

Supported character encodings:

 o ASCII, UTF-8, UTF-16BE, UTF-16LE, UTF-32BE, UTF-32LE,
 o EUC-JP, EUC-TW, EUC-KR, EUC-CN,
 o Shift_JIS, Big5, GB18030, KOI8-R, CP1251,
 o ISO-8859-1, ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-5,
 o ISO-8859-6, ISO-8859-7, ISO-8859-8, ISO-8859-9, ISO-8859-10,
 o ISO-8859-11, ISO-8859-13, ISO-8859-14, ISO-8859-15, ISO-8859-16
 o (GB18030 encoding was contributed by KUBO Takehiro)
 o (CP1251 encoding was contributed by Byte)

This package is only needed if you plan to develop or compile applications
which requires the Oniguruma library.

%prep

%setup -q -n %{name}-%{version}

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

%build
touch NEWS ChangeLog
autoreconf -fis

%configure2_5x

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING HISTORY README README.ja index.html index_ja.html
%attr(0755,root,root) %{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc doc/*
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_includedir}/*.h
%attr(0755,root,root) %{_libdir}/*.so
%attr(0644,root,root) %{_libdir}/*.a
%attr(0644,root,root) %{_libdir}/*.la
