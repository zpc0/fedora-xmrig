%global debug_package %{nil}

# prevent buffer overflow error
%define _fortify_level 2

Name:		xmrig
Version:	6.20.0
Release:	2%{?dist}
Summary:	unified CPU/GPU miner

License:	GPLv3
URL:		https://xmrig.com
Source0:	https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz

Patch0:		disable-auto-donate.patch

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	hwloc-devel
BuildRequires:	libstdc++-static
BuildRequires:	libuv-static
BuildRequires:	openssl-devel

%description
XMRig is a high performance, open source, cross platform
unified CPU/GPU miner

%prep
%setup -q
%patch0
%cmake

%build
%cmake_build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{__cmake_builddir}/xmrig %{buildroot}%{_bindir}/xmrig

%files
%license LICENSE
%{_bindir}/xmrig

%changelog
* Sat Nov 25 2023 zpc <dev@zpc.st>
- set fortify level 2 to prevent buffer overflow error.
- disable automatic donation by default.

* Sat Nov 11 2023 zpc <dev@zpc.st>
- initial release.
