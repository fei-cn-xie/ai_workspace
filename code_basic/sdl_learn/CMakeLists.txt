cmake_minimum_required(VERSION 3.16.3)
project(sdl_learn)

enable_testing()

option(BUILD_DEBUG "Build Debug" OFF)
if(BUILD_DEBUG)
    add_compile_options("-g")
endif()

set(SDL_LEARN_PROJECT_ROOT ${CMAKE_CURRENT_SOURCE_DIR})
set(SDL_LEARN_BIN_ROOT ${CMAKE_CURRENT_BINARY_DIR})

add_executable(sdl_learn
    ${CMAKE_CURRENT_SOURCE_DIR}/hello_SDL2.cpp
)

find_package(SDL2)

if(${SDL2_FOUND})
    message(STATUS "SDL2 found: ${SDL2_INCLUDE_DIRS}")
    message(STATUS "SDL2 libraries: ${SDL2_STATIC_LIBRARIES}")
    target_include_directories(sdl_learn PUBLIC ${SDL2_INCLUDE_DIRS})
    target_link_libraries(sdl_learn PUBLIC ${SDL2_STATIC_LIBRARIES})
else()
    message(STATUS "SDL2 not found, building from source" )
    add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/lib/SDL-release-2.28.3)
    target_link_libraries(sdl_learn PUBLIC SDL2::SDL2-static SDL2::SDL2main)
endif()


# 设置编译测试选项

option(BUILD_TESTS "Build Tests" OFF)
if(BUILD_TESTS)
    add_subdirectory(tests)
endif()