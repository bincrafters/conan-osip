"""This script build Conan.io package to multiple platforms."""
from bincrafters import build_template_default


if __name__ == "__main__":
    builder = build_template_default.get_builder()
    builder.run()
