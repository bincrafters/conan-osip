"""Conan receipt package for oSIP library
"""
import os
from conans import ConanFile, AutoToolsBuildEnvironment, CMake, tools


class LibOSIPConan(ConanFile):
    """Download oSIP source, build and create package
    """
    name = "osip"
    version = "5.0.0"
    generators = "cmake", "txt"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False] }
    default_options = "shared=False"
    url = "http://github.com/bincrafters/conan-osip"
    author = "Bincrafters <bincrafters@gmail.com>"
    homepage = "https://savannah.gnu.org/projects/osip/"
    license = "https://git.savannah.gnu.org/cgit/osip.git/tree/COPYING"
    description = "A library to provide the Internet Community a simple way to support the Session Initiation Protocol"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://ftp.gnu.org/gnu/osip"
        tools.get("{0}/libosip2-{1}.tar.gz".format(source_url, self.version))
        extracted_dir = "libosip2-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        if self.settings.os == "Windows":
            self._cmake_build()
        else:
            self._linux_osx_build()

    def _cmake_build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def _linux_osx_build(self):
        env_build = AutoToolsBuildEnvironment(self)
        env_build.fpic = True
        with tools.environment_append(env_build.vars):
            with tools.chdir(self.source_subfolder):
                configure_args = ['--prefix=%s' % self.package_folder]
                configure_args.append('--enable-shared' if self.options.shared else '--disable-shared')
                configure_args.append('--enable-static' if not self.options.shared else '--disable-static')
                env_build.configure(args=configure_args)
                env_build.make(args=["-s", "all"])
                env_build.make(args=["-s", "install"])

    def package(self):
        self.copy("COPYING", dst="licenses", src=self.source_subfolder, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
