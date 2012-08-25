VimClojure Fedora Package Spec
==============================

This repository contains the Fedora package spec for VimClojure.

Building
--------

Follow these steps to build the package:

1. Copy the spec file to the %rpmbuild%/SPEC folder
2. Copy the patch file(s) to the %rpmbuild%/SOURCES folder
3. Switch to the %rpmbuild%/SOURCES folder and download the source:
    wget -O vim-vimclojure-2.3.6.tar.gz https://github.com/kotarak/vimclojure/tarball/v2.3.6
4. Switch to the %rpmbuild%/SPEC folder and build the RPM
    rpmbuild -bb vim-vimclojure.spec

Installing
----------

Once you build the package, you can install it using this command:

    yum localinstall %rpmbuild%/RPMS/noarch/vim-vimclojure-*.rpm

Now when you open a Clojure source file in Vim, you should see that the source is syntax highlighted.

Repl
----

In order to use the REPL inside of Vim, you need to setup a nailgun server, then tell Vim you want to use it.

Setting up the nailgun server using Leiningen is simple. First, add the following profile to the $HOME/.lein/profiles.clj:

    {:user {:plugins [[lein-tarsier "0.9.1"]]}}

If this file did not previously exist, this will be the only line in the file.

In a new terminal, create a new project using lein.

    lein new nailgun-server

Switch to the nailgun-server folder and run the nailgun server using this command:

    lein vimclojure

Switch back to the previous terminal and open a Clojure source file. Then type the following:

    :let g:vimclojure#WantNailgun = 1

Now put the cursor over a block of Clojure code and type `\et`. You should see the result appear in a result buffer.

Alternatively, you can activate nailgun integration in your .vimrc file.

    g:vimclojure#WantNailgun = 1
