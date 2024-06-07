cmake_minimum_required(VERSION 3.0)

project(sdtw)

# Find Python and its libraries
find_package(Python3 COMPONENTS Interpreter Development)
find_package(Python3 REQUIRED)

# Find Cython
find_program(CYTHON_EXECUTABLE cython)
if(NOT CYTHON_EXECUTABLE)
    message(FATAL_ERROR "Cython not found. Please install it.")
endif()

# Add Cython source file
set(CYTHON_SOURCES sdtw/soft_dtw_fast.pyx)

# Compile Cython source file to C++/C
set_source_files_properties(${CYTHON_SOURCES} PROPERTIES CYTHON_IS_CXX TRUE)
add_custom_command(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/soft_dtw_fast.cpp
    COMMAND ${CYTHON_EXECUTABLE} --cplus -3 ${CMAKE_CURRENT_SOURCE_DIR}/sdtw/soft_dtw_fast.pyx -o ${CMAKE_CURRENT_BINARY_DIR}/soft_dtw_fast.cpp
    DEPENDS ${CYTHON_SOURCES}
)

# Add the compiled C++/C file to the project
set(CYTHON_CPP_SOURCES ${CMAKE_CURRENT_BINARY_DIR}/soft_dtw_fast.cpp)

# Include directories
include_directories(${Python3_INCLUDE_DIRS})

# Add the executable/library
add_library(my_module SHARED ${CYTHON_CPP_SOURCES})
target_link_libraries(my_module ${Python3_LIBRARIES})

# Install target
install(TARGETS sdtw DESTINATION sdtw-lib)
