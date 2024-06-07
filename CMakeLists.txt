cmake_minimum_required(VERSION 3.15...3.26)

project(sdtw)

find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

add_subdirectory(sdtw)
