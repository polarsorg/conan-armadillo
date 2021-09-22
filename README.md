# conan-armadillo
A conan wrapper for https://github.com/polarsorg/armadillo-code


### Usage

To use in your project, add `Armadillo/9.200.1/polarsorg/stable` as a conan dependency.
No binaries are pre-build at present so use `--build missing` in your project.

### Build instructions

To add Armadillo to your conan cache:
```sh
$ conan create . user/channel
```

#### Dependencies

:warning: By default, Armadillo will be built _without_ `BLAS` and `LAPACK`, therefore requires no further dependencies.
