# SPDX-License-Identifier: GPL-3.0-or-later
%global debug_package %{nil}

Name:		xmrig
Version:	6.22.2
Release:	3%{?dist}
Summary:	unified CPU/GPU miner

License:	GPL-3.0-or-later
URL:		https://xmrig.com
Source0:	https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz

Patch0:		disable-auto-donate.patch

BuildRequires:	cmake
BuildRequires:	ninja-build
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
%patch 0

%build
%cmake -G Ninja -DWITH_HTTP=OFF -DWITH_MSR=OFF -DWITH_ENV_VARS=OFF -DWITH_OPENCL=OFF -DWITH_CUDA=OFF
%cmake_build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{_vpath_builddir}/xmrig %{buildroot}%{_bindir}/xmrig

%files
%license LICENSE
%{_bindir}/xmrig

%changelog
%autochangelog
