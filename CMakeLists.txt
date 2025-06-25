cmake_minimum_required(VERSION 4.0)
project(badapple)

find_package(OPENCV REQUIRED)

include_directories(${OPENCV_INCLUDE_DIRS})

add_executable(badapple badapple.cpp)

target_link_libraries(badapple $(OpenCV_LIBS))