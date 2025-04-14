# Generated by rust2rpm 27
%bcond check 1
%global debug_package %{nil}

%global crate struct-patch

Name:           rust-struct-patch
Version:        0.9.2
Release:        %autorelease
Summary:        Library that helps you implement partial updates for your structs

License:        MIT
URL:            https://crates.io/crates/struct-patch
Source:         %{crates_source}

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

%package     -n %{name}+box-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+box-devel %{_description}

This package contains library source intended for building other packages which
use the "box" feature of the "%{crate}" crate.

%files       -n %{name}+box-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+keep_none-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+keep_none-devel %{_description}

This package contains library source intended for building other packages which
use the "keep_none" feature of the "%{crate}" crate.

%files       -n %{name}+keep_none-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+merge-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+merge-devel %{_description}

This package contains library source intended for building other packages which
use the "merge" feature of the "%{crate}" crate.

%files       -n %{name}+merge-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+none_as_default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+none_as_default-devel %{_description}

This package contains library source intended for building other packages which
use the "none_as_default" feature of the "%{crate}" crate.

%files       -n %{name}+none_as_default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+op-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+op-devel %{_description}

This package contains library source intended for building other packages which
use the "op" feature of the "%{crate}" crate.

%files       -n %{name}+op-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+option-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+option-devel %{_description}

This package contains library source intended for building other packages which
use the "option" feature of the "%{crate}" crate.

%files       -n %{name}+option-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+status-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+status-devel %{_description}

This package contains library source intended for building other packages which
use the "status" feature of the "%{crate}" crate.

%files       -n %{name}+status-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

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
