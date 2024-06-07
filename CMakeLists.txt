cmake_minimum_required(VERSION 3.15...3.26)

project(sdtw)

find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

# Add NumPy include directory
execute_process(
    COMMAND "${PYTHON_EXECUTABLE}" -c "import numpy as np; print(np.get_include())"
    OUTPUT_VARIABLE NUMPY_INCLUDE_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
include_directories(${NUMPY_INCLUDE_DIR})

add_subdirectory(sdtw)
