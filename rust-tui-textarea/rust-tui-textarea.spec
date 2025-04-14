# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate tui-textarea

Name:           rust-tui-textarea
Version:        0.7.0
Release:        %autorelease
Summary:        Simple yet powerful text editor widget for ratatui and tui-rs

License:        MIT
URL:            https://crates.io/crates/tui-textarea
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop features and dependencies for unused termwiz support
# * drop features and dependencies for unused tui support
Patch:          tui-textarea-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Tui-textarea is a simple yet powerful text editor widget for ratatui and
tui-rs. Multi-line text editor can be easily put as part of your TUI
application.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+arbitrary-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arbitrary-devel %{_description}

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%files       -n %{name}+arbitrary-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+crossterm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+crossterm-devel %{_description}

This package contains library source intended for building other packages which
use the "crossterm" feature of the "%{crate}" crate.

%files       -n %{name}+crossterm-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no-backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no-backend-devel %{_description}

This package contains library source intended for building other packages which
use the "no-backend" feature of the "%{crate}" crate.

%files       -n %{name}+no-backend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ratatui-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ratatui-devel %{_description}

This package contains library source intended for building other packages which
use the "ratatui" feature of the "%{crate}" crate.

%files       -n %{name}+ratatui-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+search-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+search-devel %{_description}

This package contains library source intended for building other packages which
use the "search" feature of the "%{crate}" crate.

%files       -n %{name}+search-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+termion-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+termion-devel %{_description}

This package contains library source intended for building other packages which
use the "termion" feature of the "%{crate}" crate.

%files       -n %{name}+termion-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
%autochangelog
