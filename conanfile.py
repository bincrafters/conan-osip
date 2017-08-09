"""Conan receipt package for oSIP library
"""
import tempfile
import os
from conans import ConanFile, AutoToolsBuildEnvironment, VisualStudioBuildEnvironment, tools


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
    release_folder = "libosip2-5.0.0"

    def source(self):
        tools.get("https://ftp.gnu.org/gnu/osip/libosip2-5.0.0.tar.gz")

    def _run_cmd(self, command):
        if self.settings.os == "Windows":
            tools.run_in_windows_bash(self, tools.unix_path(command))
        else:
            self.run(command)

    def build(self):
        if self.settings.os == "Windows" and self.settings.compiler == "Visual Studio":
            env_build = VisualStudioBuildEnvironment(self)
            with tools.environment_append(env_build.vars):
                with tools.chdir(os.path.join(self.release_folder, "platform", "vsnet")):
                    msvc_command = tools.msvc_build_command(self.settings, "osip.sln", targets=["osip2", "osipparser2"], upgrade_project=True)
                    self.run(msvc_command)
        else:
            env_build = AutoToolsBuildEnvironment(self)
            env_build.fpic = True
            with tools.environment_append(env_build.vars):
                with tools.chdir(self.release_folder):
                    configure_args = ['--prefix=%s' % self.install_dir]
                    configure_args.append('--enable-shared' if self.options.shared else '--disable-shared')
                    configure_args.append('--enable-static' if not self.options.shared else '--disable-static')
                    self._run_cmd("./configure %s" % ' '.join(configure_args))
                    self._run_cmd("make")
                    self._run_cmd("make install")

    def _visual_platform_and_config(self):
        platform = "Win32" if self.settings.arch == "x86" else "x64"
        configuration = "Release" if self.options.shared else "ReleaseStatic"
        return platform, configuration

    def package(self):
        self.copy("COPYING", src=self.release_folder, dst=".", keep_path=False)
        self.copy(pattern="*", dst="include", src=os.path.join(self.install_dir, "include"))
        if self.settings.os == "Windows" and self.settings.compiler == "Visual Studio":
            platform, configuration = self._visual_platform_and_config()
            src = "%s/contrib/windows/%s/%s" % (self.release_folder, platform, configuration)
            if self.options.shared:
                self.copy(pattern="*.dll", dst="bin", src=src, keep_path=False)
            self.copy(pattern="*.lib", dst="lib", src=src, keep_path=False)
        else:
            self.copy(pattern="*", dst="lib", src=os.path.join(self.install_dir, "lib"))

    def package_info(self):
        self.cpp_info.libs = ["osip2", "osipparser2"]
