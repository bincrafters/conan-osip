"""Conan receipt package for oSIP library
"""
import tempfile
import os
from conans import ConanFile, AutoToolsBuildEnvironment, tools


class LibOSIPConan(ConanFile):
    """Download oSIP source, build and create package
    """
    name = "osip"
    version = "5.0.0"
    generators = "cmake", "txt"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False] }
    default_options = "shared=True"
    url = "http://github.com/uilianries/conan-osip"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "https://www.gnu.org/licenses/lgpl-2.1.html"
    description = "A library to provide the Internet Community a simple way to support the Session Initiation Protocol"
    install_dir = tempfile.mkdtemp(suffix=name)

    def source(self):
        tools.get("https://ftp.gnu.org/gnu/osip/libosip2-5.0.0.tar.gz")

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        env_build.fpic = True
        with tools.environment_append(env_build.vars):
            with tools.chdir("libosip2-5.0.0"):
                configure_args = ['--prefix=%s' % self.install_dir]
                configure_args.append('--enable-shared' if self.options.shared else '--disable-shared')
                configure_args.append('--enable-static' if not self.options.shared else '--disable-static')
                env_build.configure(args=configure_args)
                env_build.make(args=["all"])
                env_build.make(args=["install"])

    def package(self):
        self.copy("COPYING", src="libosip2-5.0.0", dst=".", keep_path=False)
        self.copy(pattern="*", dst="include", src=os.path.join(self.install_dir, "include"))
        self.copy(pattern="*.a", dst="lib", src=os.path.join(self.install_dir, "lib"), keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=os.path.join(self.install_dir, "lib"), keep_path=False)
        self.copy(pattern="*.la", dst="lib", src=os.path.join(self.install_dir, "lib"), keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", src=os.path.join(self.install_dir, "lib"), keep_path=False)
        self.copy(pattern="*.pc", dst=os.path.join("lib", "pkgconfig"), src=os.path.join(self.install_dir, "lib", "pkgconfig"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["osip2", "osipparser2"]
