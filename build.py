"""This script build Conan.io package to multiple platforms."""
from os import getenv
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="osip:shared", pure_c=True)
    builder.run()
