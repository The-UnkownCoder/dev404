cmake_minimum_required(VERSION 3.10)
project(C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_C_FLAGS "-Wall -Wextra")

include_directories(include)

add_executable(main
    src/main.c
    src/patterns.c
    src/math_utils.c
    src/ds.c
    src/dsq.c

)