Name:           wlvncc
Version:        0.1.0
Release:        1%{?dist}
Summary:        A Wayland VNC client

License:        ISC
URL:            https://github.com/any1/wlvncc

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(zlib)

%description
A Wayland VNC client.

%prep

%build
%meson
%meson_build

%install
%meson_install
tree %{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/wlvncc
%{_datadir}/wlvncc

%changelog
* Sun Sep 01 2024 Your Name <your.email@example.com> - 0.1.0-1
- Initial package
