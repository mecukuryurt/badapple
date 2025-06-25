cmake_minimum_required(VERSION 4.0)
project(badapple)

find_package(OpenCV REQUIRED PATHS C:\\opencv NO_DEFAULT_PATH)

include_directories(${OPENCV_INCLUDE_DIRS})

add_executable(badapple badapple.cpp)

target_link_libraries(badapple $(OpenCV_LIBS))