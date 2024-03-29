%define	major	5
%define	libname	%mklibname %{name} %{major}
%define	devname	%mklibname %{name} -d

Summary:	Regular expressions library
Name:		onig
Version:	6.9.9
Release:	1
License:	BSD
Group:		System/Libraries
Url:		https://github.com/kkos/oniguruma
Source0:	https://github.com/kkos/oniguruma/archive/v%{version}.tar.gz
Patch0:		oniguruma-5.9.2-onig_new-returns-NULL-reg.patch
BuildRequires:	libtool

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
Group:		System/Libraries

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

%package -n	%{devname}
Summary:	Static library and header files for development with Oniguruma
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
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
%setup -qn oniguruma-%{version}
%patch0 -p1 -b .nullreg~

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

touch NEWS ChangeLog
autoreconf -fis

%build
%configure
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libonig.so.%{major}*

%files -n %{devname}
%doc doc/*
%doc AUTHORS COPYING HISTORY README index.html index_ja.html
%{_bindir}/*
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/oniguruma.pc
