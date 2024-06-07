cmake_minimum_required(VERSION 3.18...3.22)

project(sdtw)

find_package(PythonExtensions REQUIRED)

add_library(sdtw MODULE sdtw/fast_soft_sdtw.pyx)
python_extension_module(sdtw)
install(TARGETS sdtw LIBRARY DESTINATION sdtw-lib)
