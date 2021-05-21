Name: hello_world_rp
Version: 0
Release: 1%{?dist}
Summary: hello_world_rp summary

License: No license to be set
URL: https://github.com/ab491/hello_world_rp
Source0: %{name}-%{version}.tar.gz

BuildRequires: afm-rpm-macros
BuildRequires: gcc gcc-c++
BuildRequires: cmake

%description
The helloworld

%prep
%autosetup -p 1


%build
%cmake
%cmake_build
# Equivalent to
#cmake -DCMAKE_INSTALL_PREFIX=/usr
#make

%install
%cmake_install
# Equivalent to
#make install DESTDIR=%{buildroot}/

%files
%{_bindir}/*

%check

%clean
