# 定义cmake的最低版本要求
cmake_minimum_required(VERSION 3.16.3)

# 定义项目名称, 一般和项目文件夹名称一致
project(hello_world)

# 开启测试
enable_testing()

# 定义项目根路径
set(PROJECT_ROOT ${CMAKE_CURRENT_SOURCE_DIR})

# 添加子目录, 参数为子目录名称, 该目录下必须有CMakeLists.txt文件
add_subdirectory(hello)
add_subdirectory(world)




# 添加可执行文件, 参数1: 可执行文件名称, 参数2: 需要编译的源文件
add_executable(main main.cpp)


# 添加头文件搜索路径
# 参数1: 目标文件名称, 参数2: 访问权限, 参数3: 头文件路径
target_include_directories(main PUBLIC world)

# 添加链接库, 参数1: 目标文件名称, 参数2: 访问权限, 参数3: 库名称
target_link_libraries(main PUBLIC hellolib)
target_link_libraries(main PUBLIC worldlib) 

# 将 gtest 添加到项目中
add_subdirectory(test)
