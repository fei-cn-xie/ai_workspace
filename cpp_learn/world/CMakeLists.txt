# 定义cmake的最低版本要求
cmake_minimum_required(VERSION 3.16.3)

# 定义项目名称, 一般和项目文件夹名称一致
project(world)

# 设置源文件路径
set(WORLD_SRC ${CMAKE_CURRENT_SOURCE_DIR}/world.cpp)

# 添加库文件, 参数1: 库名称, 参数2: 库类型, 参数3: 需要编译的源文件
# 共享库: SHARED，动态库是共享库的一种，区别在于动态库在运行时加载，而共享库在编译时链接
# 静态库: STATIC，在编译时将库文件的代码直接复制到可执行文件中，生成一个独立的可执行文件
add_library(worldlib STATIC ${WORLD_SRC})

# 添加头文件搜索路径， 只要添加了头文件搜索路径，就可以在源文件中直接使用#include "world.h"来包含头文件，而不需要指定完整路径
target_include_directories(worldlib SYSTEM INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})