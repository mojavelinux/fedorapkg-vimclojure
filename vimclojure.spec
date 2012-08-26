%global vimfiles_root %{_datadir}/vim/vimfiles
%global commithash f6a0135

Name:           vimclojure
Version:        2.3.6
Release:        1%{?dist}
Summary:        Clojure editing environment plugin for Vim
Group:          Application/Editors

License:        MIT
URL:            http://www.vim.org/scripts/script.php?script_id=2501
Source0:        %{name}-%{version}.tar.gz
# wget -O %{name}-%{version}.tar.gz https://github.com/kotarak/vimclojure/tarball/v%{version}
Source1:        %{name}-%{version}-server-pom.xml
Patch0:         %{name}-enable-paren-rainbow.patch

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  clojure-maven-plugin

Requires:       vim-common
# should nailgun be required, or optional?
Requires:       nailgun
Requires(post): vim
Requires(postun): vim

BuildArch:      noarch

%description
VimClojure is one of the most sophisticated editing environments for Clojure.
It provides syntax highlighting, indenting and command completion. It's not
intended to be an easy to use Clojure IDE, but a plugin to make life easier for
people already familiar with Vim.

%prep
%setup -q -n kotarak-vimclojure-%{commithash}
%patch0 -p1
cp -p %{SOURCE1} server/pom.xml

%build
mvn-rpmbuild -f server/pom.xml install

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
install -pm 644 server/target/server-%{version}.jar %{buildroot}%{_javadir}/%{name}/server.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 server/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-server.pom
%add_maven_depmap JPP.%{name}-server.pom %{name}/server.jar

mkdir -p %{buildroot}%{vimfiles_root}
cp -ar vim/{autoload,doc,ftdetect,ftplugin,indent,plugin,syntax} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%postun
rm %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%files
%{_javadir}/%{name}/*.jar
%{_mavenpomdir}/JPP.%{name}-*.pom
%{_mavendepmapfragdir}/%{name}

%doc README.markdown
%doc %{vimfiles_root}/doc/*
%{vimfiles_root}/autoload/*
%{vimfiles_root}/ftdetect/*
%{vimfiles_root}/ftplugin/*
%{vimfiles_root}/indent/*
%{vimfiles_root}/plugin/*
%{vimfiles_root}/syntax/*

%changelog
* Sat Aug 25 2012 Dan Allen <dallen@redhat.com> - 2.3.6-1
- Initial package.
