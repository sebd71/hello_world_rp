cmake_minimum_required(VERSION 3.9)

project(redpesk_test LANGUAGES C CXX)

# Executables

add_executable(rp_hello_cpp
  src/main.cpp
)

add_executable(rp_hello_c
  src/main.c
)

install(TARGETS rp_hello_cpp DESTINATION ${CMAKE_INSTALL_BINDIR})
install(TARGETS rp_hello_c DESTINATION ${CMAKE_INSTALL_BINDIR})
