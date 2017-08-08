"""Receipt validation for oSIP
"""
from os import getenv
from conans import ConanFile, CMake


class TestOSIPConan(ConanFile):
    """Build test using target package and execute all tests
    """
    channel = getenv("CONAN_CHANNEL", "testing")
    user = getenv("CONAN_USERNAME", "uilianries")
    settings = "os", "compiler", "build_type", "arch"
    requires = "osip/5.0.0@%s/%s" % (user, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.conanfile_directory, build_dir="./")
        cmake.build()

    def imports(self):
        self.copy(pattern="*.so*", dst="bin", src="lib")
        self.copy(pattern="*.dll", dst="bin", src="bin")

    def test(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.conanfile_directory, build_dir="./")
        cmake.build()
        cmake.test()
