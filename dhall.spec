# generated by cabal-rpm-2.0.2 --standalone --stream hackage
# https://fedoraproject.org/wiki/Packaging:Haskell

%global dhall_ver 1.30.0
%global dhall_json_ver 1.6.2
%global dhall_yaml_ver 1.0.2

%global ghc_without_dynamic 1
%global ghc_without_shared 1
# F31+
%undefine with_ghc_prof
%undefine with_haddock
# -F30
%global without_prof 1
%global without_haddock 1

%global debug_package %{nil}

%bcond_without json
%bcond_without yaml

Name:           dhall
Version:        %{dhall_ver}
Release:        1%{?dist}
Summary:        A configuration language guaranteed to terminate

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{name}-json-%{dhall_json_ver}/%{name}-json-%{dhall_json_ver}.tar.gz
Source2:        https://hackage.haskell.org/package/%{name}-yaml-%{dhall_yaml_ver}/%{name}-yaml-%{dhall_yaml_ver}.tar.gz

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-ansi-terminal-devel
#BuildRequires:  ghc-atomic-write-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-case-insensitive-devel
#BuildRequires:  ghc-cborg-devel
#BuildRequires:  ghc-cborg-json-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-cryptonite-devel
#BuildRequires:  ghc-data-fix-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-dotgen-devel
%if 0%{?fedora} >= 32
BuildRequires:  ghc-either-devel
%endif
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-types-devel
#BuildRequires:  ghc-lens-family-core-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-optparse-applicative-devel
#BuildRequires:  ghc-parsers-devel
#BuildRequires:  ghc-pretty-simple-devel
%if 0%{?fedora} >= 32
BuildRequires:  ghc-prettyprinter-devel
%endif
#BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
BuildRequires:  ghc-profunctors-devel
%if 0%{?fedora} >= 32
BuildRequires:  ghc-repline-devel
%endif
BuildRequires:  ghc-scientific-devel
#BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-th-lift-instances-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-uri-encode-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  cabal-install > 1.18
# for missing dep 'atomic-write':
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-unix-compat-devel
# for missing dep 'cborg':
BuildRequires:  ghc-array-devel
%if 0%{?fedora} >= 32
BuildRequires:  ghc-half-devel
%endif
BuildRequires:  ghc-primitive-devel
# for missing dep 'parsers':
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-charset-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-semigroups-devel
%if 0%{?fedora} < 32
# for missing dep: repline:
#BuildRequires:  ghc-fail-devel
BuildRequires:  ghc-process-devel
%endif
# for missing dep 'serialise':
BuildRequires:  ghc-array-devel
%if 0%{?fedora} >= 32
BuildRequires:  ghc-half-devel
%endif
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-time-devel

%if %{with json}
# for dhall-json
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
#BuildRequires:  ghc-aeson-yaml-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
#BuildRequires:  ghc-dhall-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-optparse-applicative-devel
%if 0%{?fedora} >= 32
BuildRequires:  ghc-prettyprinter-devel
%endif
#BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel

%if %{with yaml}
# for dhall-yaml
%if 0%{?fedora} >= 31
BuildRequires:  ghc-HsYAML-devel
%endif
#BuildRequires:  ghc-HsYAML-aeson-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
#BuildRequires:  ghc-dhall-devel
#BuildRequires:  ghc-dhall-json-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-optparse-applicative-devel
%if 0%{?fedora} >= 32
BuildRequires:  ghc-prettyprinter-devel
%endif
#BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  cabal-install > 1.18
# for missing dep 'HsYAML-aeson':
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-unordered-containers-devel
%endif
%endif

%description
Dhall is an explicitly typed configuration language that is not Turing
complete. Despite being Turing incomplete, Dhall is a real programming language
with a type-checker and evaluator.

Use this library to parse, type-check, evaluate, and pretty-print the Dhall
configuration language. This package also includes an executable which
type-checks a Dhall file and reduces the file to a fully evaluated normal form.

Read "Dhall.Tutorial" to learn how to use this library.


%if %{with json}
%package json
Summary:        Convert between Dhall and JSON or YAML
Version:        %{dhall_json_ver}

%description json
Use this package if you want to convert between Dhall expressions and JSON.


%if %{with yaml}
%package yaml
Summary:        Convert between Dhall and YAML
Version:        %{dhall_json_ver}

%description yaml
Use this package if you want to convert between Dhall expressions and YAML.
%endif
%endif


%prep
%setup -q %{?with_json:-a1 %{?with_yaml:-a2}}


%build
# Begin cabal-rpm build:
%global cabal cabal
%cabal update
%cabal sandbox init
%cabal install dhall-%{dhall_ver} %{?with_json:dhall-json-%{dhall_json_ver} %{?with_yaml:dhall-yaml-%{dhall_yaml_ver}}}


%install
mkdir -p %{buildroot}%{_bindir}
install -p .cabal-sandbox/bin/*dhall* %{buildroot}%{_bindir}

rm -r .cabal-sandbox/share/doc/*/dhall-json-%{dhall_json_ver}


%check
%cabal_test


%files
# Begin cabal-rpm files:
%license .cabal-sandbox/share/doc/*/*
%doc CHANGELOG.md
%{_bindir}/%{name}
# End cabal-rpm files


%if %{with json}
%files json
%license dhall-json-%{dhall_json_ver}/LICENSE
%doc dhall-json-%{dhall_json_ver}/CHANGELOG.md
%{_bindir}/json-to-%{name}
%{_bindir}/%{name}-to-json
%{_bindir}/%{name}-to-yaml

%if %{with yaml}
%files yaml
%license dhall-yaml-%{dhall_yaml_ver}/LICENSE
%doc dhall-yaml-%{dhall_yaml_ver}/CHANGELOG.md
%{_bindir}/yaml-to-%{name}
%{_bindir}/%{name}-to-yaml-ng
%endif
%endif


%changelog
* Tue Feb 18 2020 Tristan Cacqueray <tdecacqu@redhat.com> - 1.30.0-1
- bump to dhall version 1.30.0

* Sat Feb  8 2020 Jens Petersen <petersen@redhat.com> - 1.29.0-2
- update deps and add dhall-yaml

* Fri Feb  7 2020 Tristan Cacqueray <tdecacqu@redhat.com> - 1.29.0-1
- bump dhall-json to 1.6.1 and add json-to-dhall cli

* Wed Feb  5 2020 Jens Petersen <petersen@redhat.com> - 1.19.1-2
- add dhall-json 1.2.6

* Tue Jan 28 2020 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.19.1-1
- spec file generated by cabal-rpm-2.0.0
