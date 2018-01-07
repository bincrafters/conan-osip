"""Conan receipt package for oSIP library
"""
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
    default_options = "shared=False"
    url = "http://github.com/bincrafters/conan-osip"
    author = "Bincrafters <bincrafters@gmail.com>"
    homepage = "https://savannah.gnu.org/projects/osip/"
    license = "https://git.savannah.gnu.org/cgit/osip.git/tree/COPYING"
    description = "A library to provide the Internet Community a simple way to support the Session Initiation Protocol"
    exports = ["LICENSE.md"]
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://ftp.gnu.org/gnu/osip"
        tools.get("{0}/libosip2-{1}.tar.gz".format(source_url, self.version))
        extracted_dir = "libosip2-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure(self):
        del self.settings.compiler.libcxx

    def _run_cmd(self, command):
        if self.settings.os == "Windows":
            tools.run_in_windows_bash(self, tools.unix_path(command))
        else:
            self.run(command)

    def build(self):
        if self.settings.os == "Windows" and self.settings.compiler == "Visual Studio":
            self._msvc_build()
        elif self.settings.os == "Windows" and self.settings.compiler == "gcc":
            self._mingw_build()
        else:
            self._linux_osx_build()

    def _msvc_build(self):
        env_build = VisualStudioBuildEnvironment(self)
        with tools.environment_append(env_build.vars):
            with tools.chdir(os.path.join(self.source_subfolder, "platform", "vsnet")):
                msvc_command = tools.msvc_build_command(self.settings, "osip.sln", targets=["osip2", "osipparser2"], upgrade_project=True)
                self.run(msvc_command)

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

    def _mingw_build(self):
        env_build = AutoToolsBuildEnvironment(self)
        env_build.fpic = True
        with tools.environment_append(env_build.vars):
            with tools.chdir(self.source_subfolder):
                configure_args = ['--prefix=%s' % self.package_folder]
                configure_args.append('--enable-shared' if self.options.shared else '--disable-shared')
                configure_args.append('--enable-static' if not self.options.shared else '--disable-static')
                if self.settings.os == "Windows" and self.settings.compiler == "gcc" and self.settings.arch == "x86_64":
                    configure_args.append('--host=x86_64-w64-mingw32')
                if self.settings.os == "Windows" and self.settings.compiler == "gcc" and self.settings.arch == "x86":
                    configure_args.append('--build=i686-w64-mingw32')
                    configure_args.append('--host=i686-w64-mingw32')
                tools.run_in_windows_bash(self, tools.unix_path("./configure %s" % ' '.join(configure_args)))
                tools.run_in_windows_bash(self, "make -s")
                tools.run_in_windows_bash(self, "make -s install")

    def _visual_platform_and_config(self):
        platform = "Win32" if self.settings.arch == "x86" else "x64"
        configuration = "Release" if self.options.shared else "ReleaseStatic"
        return platform, configuration

    def package(self):
        self.copy("COPYING", dst="licenses", src=self.source_subfolder, keep_path=False)
        if self.settings.os == "Windows" and self.settings.compiler == "Visual Studio":
            self.copy(pattern="*", dst="include", src=os.path.join(self.source_subfolder, "include"))
            platform, configuration = self._visual_platform_and_config()
            src = "%s/contrib/windows/%s/%s" % (self.source_subfolder, platform, configuration)
            if self.options.shared:
                self.copy(pattern="*.dll", dst="bin", src=src, keep_path=False)
                self.copy(pattern="*.lib", dst="lib", src=src, keep_path=False)
            else:
                src = os.path.join(self.build_folder, "libosip2-%s" % self.version)
                self.copy(pattern="*.lib", dst="lib", src=src, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
