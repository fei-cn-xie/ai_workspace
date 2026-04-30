cmake_minimum_required(VERSION 3.16.3)
project(test)

# 将 gtest 添加到项目中， 参数1: gtest所在路径, 参数2: gtest编译后输出路径（自定义）
add_subdirectory(${PROJECT_ROOT}/thirdpart/googletest-1.17.0 googletest)


add_executable(test_hello ${CMAKE_CURRENT_SOURCE_DIR}/test_hello.cpp)

# 添加头文件搜索路径
target_include_directories(test_hello PUBLIC ${PROJECT_ROOT}/thirdpart/googletest-1.17.0/googletest/include)
# 添加头文件搜索路径
target_include_directories(test_hello PUBLIC ${PROJECT_ROOT})

# 添加链接库, 参数1: 目标文件名称, 参数2: 访问权限, 参数3: 库名称
target_link_libraries(test_hello PUBLIC hellolib gtest gtest_main)

# # 添加测试, 参数1: 测试名称, 参数2: 可执行文件名称
# add_test(NAME test_hello COMMAND test_hello)
