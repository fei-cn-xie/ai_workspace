# 定义cmake的最低版本要求
cmake_minimum_required(VERSION 3.16.3)

# 定义项目名称, 一般和项目文件夹名称一致
project(hello_world)

# # 开启cmake测试能力
enable_testing()


option(BUILD_DEBUG "是否构建调试版本" OFF)
if(BUILD_DEBUG)
    message(STATUS "构建调试版本")
    add_compile_options("-g") # 添加编译选项, -g表示生成调试信息
endif()


# 定义项目根路径
set(PROJECT_ROOT ${CMAKE_CURRENT_SOURCE_DIR})

# 添加子目录, 参数为子目录名称, 该目录下必须有CMakeLists.txt文件
add_subdirectory(hello)
add_subdirectory(world)




# 添加可执行文件, 参数1: 可执行文件名称, 参数2: 需要编译的源文件
add_executable(main main.cpp)


# 添加头文件搜索路径
# 参数1: 目标文件名称, 参数2: 访问权限, 参数3: 头文件路径
# world目录下的CMakeLists.txt中已经添加了头文件搜索路径(target_include_directories(worldlib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})), 所以这里不需要再添加一次了
# target_include_directories(main PUBLIC world)

# 添加链接库, 参数1: 目标文件名称, 参数2: 访问权限, 参数3: 库名称
target_link_libraries(main PUBLIC hellolib)
target_link_libraries(main PUBLIC worldlib) 

# 添加测试选项, 参数1: 选项名称, 参数2: 选项描述, 参数3: 默认值
# 一般自定义选线不要用CMAKE_开头, 以免和cmake内置选项冲突
option(BUILD_TEST "是否构建测试" OFF)

if(BUILD_TEST)
    message(STATUS "构建测试")
    # 将 test 添加到项目中, test目录下有CMakeLists.txt
    add_subdirectory(test)
else()
    message(STATUS "不构建测试")
endif()

