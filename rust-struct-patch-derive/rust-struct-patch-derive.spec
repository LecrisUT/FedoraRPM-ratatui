# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate struct-patch-derive

Name:           rust-struct-patch-derive
Version:        0.9.2
Release:        %autorelease
Summary:        Library that helps you implement partial updates for your structs

License:        MIT
URL:            https://crates.io/crates/struct-patch-derive
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Drop pretty_assertions_sorted dependency
Patch:          struct-patch-derive-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A library that helps you implement partial updates for your structs.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%package     -n %{name}+merge-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+merge-devel %{_description}

This package contains library source intended for building other packages which
use the "merge" feature of the "%{crate}" crate.

%files       -n %{name}+merge-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+op-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+op-devel %{_description}

This package contains library source intended for building other packages which
use the "op" feature of the "%{crate}" crate.

%files       -n %{name}+op-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+status-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+status-devel %{_description}

This package contains library source intended for building other packages which
use the "status" feature of the "%{crate}" crate.

%files       -n %{name}+status-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Remove pretty_assertions_sorted usage
sed -i '/use pretty_assertions_sorted/d' src/patch.rs
sed -i 's/assert_eq_sorted/assert_eq/' src/patch.rs

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
