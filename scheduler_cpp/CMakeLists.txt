cmake_minimum_required(VERSION 3.20)
project(factoryos_scheduler CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Core library: pure C++, no Python dependency
add_library(scheduler_core src/scheduler.cpp)
target_include_directories(scheduler_core PUBLIC src)

# Python bindings (Phase 5): pip install pybind11
find_package(pybind11 CONFIG QUIET)
if(pybind11_FOUND)
  pybind11_add_module(factoryos_scheduler bindings/bindings.cpp)
  target_link_libraries(factoryos_scheduler PRIVATE scheduler_core)
endif()

# Unit tests with GoogleTest
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.15.2.zip
)
FetchContent_MakeAvailable(googletest)
enable_testing()
add_executable(scheduler_tests tests/test_scheduler.cpp)
target_link_libraries(scheduler_tests PRIVATE scheduler_core GTest::gtest_main)
include(GoogleTest)
gtest_discover_tests(scheduler_tests)
