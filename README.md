[![Travis Build Status](https://travis-ci.org/uilianries/conan-osip.svg?branch=release/5.0.0)](https://travis-ci.org/uilianries/conan-osip)
[![Appveyor Build status](https://ci.appveyor.com/api/projects/status/v2haakhmv2h5mgjl/branch/release/5.0.0?svg=true)](https://ci.appveyor.com/project/uilianries/conan-osip/branch/release/5.0.0)
[![License: LGPL v2.1](https://img.shields.io/badge/License-LGPL%20v2.1-blue.svg)](http://www.gnu.org/licenses/lgpl-2.1)
[![Download](https://api.bintray.com/packages/uilianries/conan/osip%3Auilianries/images/download.svg) ](https://bintray.com/uilianries/conan/osip%3Auilianries/_latestVersion)

# Conan oSIP

![Conan oSIP](conan_osip.png)

oSIP has been designed to provide the Internet Community a simple way to support the Session Initiation Protocol. SIP is described in the RFC3261

[Conan.io](https://conan.io) package for [oSIP](https://savannah.gnu.org/projects/osip/) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/uilianries/conan/osip%3Auilianries/5.0.0%3Astable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload packages to server

    $ conan upload osip/5.0.0@uilianries/stable --all

## Reuse the packages

### Basic setup

    $ conan install osip/5.0.0@uilianries/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    osip/5.0.0@uilianries/stable

    [options]
    osip:shared=True # False

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

### License
[LGPL-2.1](LICENSE)
