%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-vimclojure
Version:        2.3.6
Release:        1%{?dist}
Summary:        Clojure editing environment plugin for Vim
Group:          Application/Editors

License:        MIT
URL:            http://www.vim.org/scripts/script.php?script_id=2501
Source0:        %{name}-%{version}.tar.gz
# wget -O %{name}-%{version}.tar.gz https://github.com/kotarak/vimclojure/tarball/v%{version}
Patch0:         %{name}-enable-paren-rainbow.patch

Requires:       vim-common
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
%setup -q -n kotarak-vimclojure-f6a0135
%patch0 -p1

%build


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar vim/{autoload,doc,ftdetect,ftplugin,indent,plugin,syntax} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%postun
rm %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%files
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
