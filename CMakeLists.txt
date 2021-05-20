cmake_minimum_required(VERSION 3.9)

project(redpesk_test LANGUAGES C CXX)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/sbin)

# Executables

add_executable(rp_hello_cpp
  src/main.cpp
)

add_executable(rp_hello_c
  src/main.c
)

