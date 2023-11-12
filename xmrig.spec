%global debug_package %{nil}

Name:		xmrig
Version:	6.20.0
Release:	1%{?dist}
Summary:	unified CPU/GPU miner

License:	GPLv3
URL:		https://xmrig.com
Source0:	https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	hwloc-devel
BuildRequires:	libstdc++-static
BuildRequires:	libuv-static
BuildRequires:	openssl-devel

%description
XMRig is a high performance, open source, cross platform
unified CPU/GPU miner

%prep
%autosetup
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
* Sat Nov 11 2023 zpc <dev@zpc.st>
- initial release.
