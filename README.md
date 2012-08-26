VimClojure Fedora Package Spec
==============================

This repository contains the Fedora package spec for VimClojure.

Building
--------

Follow these steps to build the package:

* Copy the spec file to the %rpmbuild%/SPEC folder
* Copy the patch file(s) to the %rpmbuild%/SOURCES folder
* Switch to the %rpmbuild%/SOURCES folder and download the source

```
wget -O vimclojure-2.3.6.tar.gz https://github.com/kotarak/vimclojure/tarball/v2.3.6
```

* Switch to the %rpmbuild%/SPEC folder
* Make sure you have the required rpms to build

```
yum-builddep vimclojure.spec
```

* Build the vimclojure rpm

```
rpmbuild -bb vimclojure.spec
```

**WARNING:** If clojure-compat is installed, clojure-compat.jar will be used for
compilation instead of clojure.jar. This substitution produces a server.jar
that's incompatible with Clojure 1.4. The clojure-compat pom claims to provide
org.clojure:clojure:1.2, which somehow confuses the JPP depmap logic.
Looks like it's a typo in the artifactId in the clojure-compat package.

Installing
----------

Once you build the package, you can install it using this command:

    yum localinstall %rpmbuild%/RPMS/noarch/vimclojure-*.rpm

Now when you open a Clojure source file in Vim, you should see that the source is syntax highlighted.

Nailgun integration
-------------------

In order to use the REPL inside of Vim, you need to setup a nailgun server, then tell Vim you want to use it.

Setting up the nailgun server using Leiningen 2 is simple. First, add the following profile to the $HOME/.lein/profiles.clj:

    {:user {:plugins [[lein-tarsier "0.9.1"]]}}

If profiles.clj did not previously exist, this will be the only line in the file.

You can also start the server directly.

    java -cp /usr/share/java/vimclojure/server.jar:/usr/share/java/clojure.jar vimclojure.nailgun.NGServer

However, note that you will need to add any additional libraries or directories to the classpath that you intend to evaluate.

In a new terminal, create a new project using lein.

    lein new nailgun-server

Switch to the nailgun-server folder and run the nailgun server using this command:

    lein vimclojure

Switch back to the previous terminal and open a Clojure source file. Then type the following:

    :let g:vimclojure#WantNailgun = 1

Now put the cursor over a block of Clojure code and type `\et`. You should see the result appear in a result buffer.

Alternatively, you can activate nailgun integration in your .vimrc file.

    g:vimclojure#WantNailgun = 1
