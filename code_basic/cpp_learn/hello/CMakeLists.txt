# 定义cmake的最低版本要求
cmake_minimum_required(VERSION 3.16.3)

# 定义项目名称, 一般和项目文件夹名称一致
project(hello)

# 设置源文件路径
set(HELLO_SRC ${CMAKE_CURRENT_SOURCE_DIR}/hello.cpp)

# 添加库文件, 参数1: 库名称, 参数2: 库类型, 参数3: 需要编译的源文件
# 共享库: SHARED，动态库是共享库的一种，区别在于动态库在运行时加载，而共享库在编译时链接
# 静态库: STATIC，在编译时将库文件的代码直接复制到可执行文件中，生成一个独立的可执行文件
add_library(hellolib SHARED ${HELLO_SRC})

if(CMAKE_SYSTEM_NAME MATCHES "Windows")
    set(LIBRARY_OUTPUT_PATH ${PROJECT_BIN_DIR})
endif ()