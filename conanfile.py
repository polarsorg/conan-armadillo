from conans import ConanFile, CMake, tools


class PolarsOrgArmadilloConan(ConanFile):
    name = "Armadillo"
    version = "9.200.1"
    license = "Apache License 2.0"
    url = "https://github.com/polarsorg/armadillo-code"
    description = "Armadillo C++ linear algebra (matrix) library"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
    }
    default_options = "shared=False"
    build_policy = "missing"
    generators = "cmake"
    build_requires = [
        "pkg-config_installer/0.29.2@bincrafters/stable",
    ]

    def build_requirements(self):
        # Or add a new requirement!
        if self.settings.os == 'Android':
            self.build_requires("android_ndk_installer/r20@bincrafters/stable")

    def requirements(self):
        # Or add a new requirement!
        if self.settings.os not in ['Macos', 'iOS']:
            self.requires("openblas/0.3.5@conan/stable")

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/polarsorg/armadillo-code.git", self.version)

    def build(self):
        tools.replace_in_file(file_path="include/armadillo_bits/config.hpp",
                              search="#define ARMA_USE_WRAPPER",
                              replace="//#define ARMA_USE_WRAPPER")

        cmake_additions = [
            "project(armadillo CXX C)",
            "include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)",
            "conan_basic_setup()",
        ]
        if self.settings.os not in ['Macos', 'iOS']:
            cmake_additions.append("list(INSERT CMAKE_FIND_ROOT_PATH 0 ${CONAN_OPENBLAS_ROOT})")

        tools.replace_in_file(file_path="CMakeLists.txt",
                              search="project(armadillo CXX C)",
                              replace='\n'.join(cmake_additions))

        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("armadillo", dst="include", src="include")
        self.copy("*.hpp", dst="include/armadillo_bits", src="include/armadillo_bits")
        self.copy("*armadillo.dll", dst="bin", keep_path=False)
        self.copy("*armadillo.lib", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.so.*", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["armadillo"]
