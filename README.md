# conan-armadillo
A conan wrapper for https://github.com/felix-org/armadillo-code

### Build instructions


To add Armadillo to your conan cache:
```sh
$ conan create . user/channel -s cppstd=14
```

#### Dependencies

:warning: By default, Armadillo will be built _without_ `BLAS` and `LAPACK`, therefore requires no further dependencies.
