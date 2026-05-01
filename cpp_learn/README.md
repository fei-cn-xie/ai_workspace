
# 1. 从零开始搭建c/c++工程
> https://www.bilibili.com/video/BV1nm4y1L73D  
> https://github.com/jinfeihan57/start_A_c_cpp_project

## 1.1 从单文件到项目工程

### 阶段1：一个main函数
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```


```sh
# 编译方法 `g++ -o 输出文件名 输入文件名`
g++ -o main main.cpp 
```

> 各个功能块耦合严重，后期维护困难，随着业务复杂度，函数体积迅速膨胀，导致逻辑不清晰，功能责任田混乱，团队合作困难。不要说大项目，连小项目也难以开发。

###   阶段2：函数抽离

```cpp
#include <iostream>

int hello() {
    std::cout << "Hello" << std::endl;
    return 0;
}

int world() {
    std::cout << "World!" << std::endl;
    return 0;
}

int main() {
    hello();
    world();
    return 0;
}
```

```sh
# 编译方法
g++ -o main main.cpp
```

### 阶段3：文件抽离

```sh
# 项目文件结构
cpp_lean
    - hello
        - hello.cpp
        - hello.h
    - world
        - world.cpp
        - world.h
mian.cpp
```


```cpp
// main.cpp
#include <iostream>
#include "hello/hello.h"
#include "world.h"


int main() {
    Hello();
    World();
    return 0;
}
```

```cpp
// hello.h
#ifndef __HELLO__ 
#define __HELLO__ // 避免重复定义

int Hello();

#endif // __HELLO__


// hello.cpp
#include <iostream> // 引入输入输出流库
#include "hello.h" // 引入头文件, 这里编译时会自动找到hello.h，把函数声明引入到当前文件中

int Hello() { // 定义Hello函数
    std::cout << "Hello" << std::endl; // 输出Hello并换行
    return 0; // 返回0表示函数执行成功
}

// world.h
#ifndef __WORLD__
#define __WORLD__ // 避免重复定义
int World();
#endif // __WORLD__

// world.cpp
#include <iostream> // <>只能引入系统库， ""可以引入用户自定义的头文件，找不到再去系统目录找
#include "world.h"
int World() {
    std::cout << "World!" << std::endl;
    return 0;
}

```


```sh
# -I ./world 表示优先在./world目录下去找头文件

# 编译方法一
g++ -o main main.cpp hello/hello.cpp world/world.cpp -I ./world

# 编译方法二 
g++ -c main.cpp -I ./world # 编译
g++ -c hello/hello.cpp # 编译
g++ -c world/world.cpp # 编译
g++ -o main main.o hello.o world.o #链接
```

> 各个功能块按照责任田划分不同的目录和文件以及函数，逻辑清晰易于管理，团队合作效率高。但是编译操作复杂，低效。


## 1.2 编译工具

### 1.2.1 阶段1：使用makefile

> 安装make： https://gnuwin32.sourceforge.net/
> 指南：https://zhuanlan.zhihu.com/p/1982583742607414813

```makefile
# makefile

# 冒号分隔
# 目标: 依赖
main: main.o hello.o world.o
    g++ -o main main.o hello.o world.o

main.o: main.cpp hello/hello.h world/world.h
    g++ -c main.cpp -I world

hello.o: hello/hello.cpp hello/hello.h
    g++ -c hello/hello.cpp

world.o: world/world.cpp world/world.h
    g++ -c world/world.cpp

# linux环境下的命令
clean:
    rm -rf main main.o hello.o world.o 
```


```sh
# 需要安装make工具
# 准备Makefile文件

# 编译
make

# 清除
make clean
```


### 1.2.2 阶段2：使用cmake

> 安装cmake: https://cmake.org


```cmake
# 定义cmake的最低版本要求
cmake_minimum_required(VERSION 3.16.3)

# 定义项目名称, 一般和项目文件夹名称一致
project(cpp_learn)

# 添加可执行文件, 参数1: 可执行文件名称, 参数2: 需要编译的源文件
add_executable(main main.cpp hello/hello.cpp world/world.cpp)

# 添加头文件搜索路径
# 参数1: 目标文件名称, 参数2: 访问权限, 参数3: 头文件路径
target_include_directories(main PUBLIC world)
```

- 构建build
```sh
# 准备好CMakeLists.txt文件
# cpp_learn/CMakeLists.txt

# 创建编译目录
mkdir build
cd build

# 执行cmake 生成makefile
# -G "MinGW Makefiles" 表示使用MinGw生成器, 否则微软默认选择visual studio
# ..表示对上一级目录编译
cmake -G "MinGW Makefiles" ..

# 执行make 
make

# make VERBOSE=1 #编译时生成详细信息
```

```sh
# 开启多个线程编译， 8表示开启8个线程
make -j8
```

```sh

# 列出所有缓存变量, 例如自定义的option(BUILD_TEST, "test", OFF), 会显示BUILD_TEST的值
cmake .. -L

# 列出所有缓存变量（包含高级变量）
cmake .. -LA

# 只列出调用 -L 之后新增的变量
cmake .. -LN

# 列出缓存变量以及详细信息描述
cmake .. -LH


```
- 跨平台的编译与构建
```sh
##############################################
# 配置项目，生成构建系统（如 Makefile、Ninja 等），并列出配置选项
cmake -S./ -Bsb_build -L
      ↑     ↑        ↑
      │     │        └── 参数3: -L (List)
      │     └── 参数2: -B (Build)
      └── 参数1: -S (Source)
# 编译项目，调用底层的构建工具（如 make、ninja、MSBuild）来实际编译代码。
cmake --build sb_build
```


### 1.2.3 阶段3：使用分级cmake项目

```sh
# 项目目录
cpp_learn
    - build
    - hello
        hello.h
        hello.cpp
        CMakeLists.txt
    - world
        world.h
        world.cpp
        CMakeLists.txt
    main.cpp
    CmakeLists.txt
```

```cmake
# 根目录下的CmakeLists.txt
# 定义cmake的最低版本要求
cmake_minimum_required(VERSION 3.16.3)

# 定义项目名称, 一般和项目文件夹名称一致
project(hello_world)

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

################################################################################################
# hello 目录下的CmakeLists.txt
# 定义cmake的最低版本要求
cmake_minimum_required(VERSION 3.16.3)

# 定义项目名称, 一般和项目文件夹名称一致
project(hello)

# 设置源文件路径
set(HELLO_SRC ${CMAKE_CURRENT_SOURCE_DIR}/hello.cpp)

# 添加库文件, 参数1: 库名称, 参数2: 库类型, 参数3: 需要编译的源文件
# 共享库: SHARED，动态库是共享库的一种，区别在于动态库在运行时加载，而共享库在编译时链接
# 静态库: STATIC，在编译时将库文件的代码直接复制到可执行文件中，生成一个独立的可执行文件
add_library(hellolib STATIC ${HELLO_SRC})

########################################################################################
# world 目录下的CmakeLists.txt

# 定义cmake的最低版本要求
cmake_minimum_required(VERSION 3.16.3)

# 定义项目名称, 一般和项目文件夹名称一致
project(hello)

# 设置源文件路径
set(HELLO_SRC ${CMAKE_CURRENT_SOURCE_DIR}/hello.cpp)

# 添加库文件, 参数1: 库名称, 参数2: 库类型, 参数3: 需要编译的源文件
# 共享库: SHARED，动态库是共享库的一种，区别在于动态库在运行时加载，而共享库在编译时链接
# 静态库: STATIC，在编译时将库文件的代码直接复制到可执行文件中，生成一个独立的可执行文件
add_library(hellolib STATIC ${HELLO_SRC})
```

```sh
# 编译
# cpp_learn目录下
mkdir build
cd build

cmake ..
make

# 执行, 回到根目录运行时路径使用./build找到hello.dll和world.dll
cd ..
./build/main.exe
```


### 1.2.4 库类型

- STATIC
  - `.lib` (Windows)
  - `.a` (Linux/MinGW)
  - 代码复制进 exe
  - 文件更大
  - 不需要额外 dll
- SHARED
  - 代码运行时加载
  - 文件更小
  - 需要带 `dll` 文件
- MODULE
  - `.dll` (Windows)
  - `.so` (Linux)
  - 运行时动态加载（插件）

## 1.3 gtest测试框架

> 如何在我们的项目中引入三方库(开源库，合作开发)。项目在开发过程中，如何保证开发的代码是正确的?答案是“测试”，不是开发。  
> 任何一个完整的项目都必须引入测试框架，以保证各个模块提供的能力是正确可靠的。googletest 是当下最流行的c/c++测试框架。

> 熟练掌握gtest，并目真实的去开发测试用例。能为我们的项目提前屏蔽很多不必要的问题(尤其项目有一定规模时)。
> 例如:项目选代过程中，常常会出现修复一个bug，又引入了多个bug的情况，如果此时对应的api有完整的测试用例，则可以提前暴露解决上述bug。一个优秀的开发，必定也是一个好的测试。

> https://ggdocs.cn/googletest/primer.html
> https://github.com/google/googletest/releases/tag/v1.17.0




### 1.3.1 入门

```sh
# 1. 下载源码
# 2. 将源码放在thirdpart目录下
# 3. 将gtest添加到项目中，CMakeLists.txt
# 
cd build
cmake ..
make # 可以看到生成了libgtest.a等内容

# # 执行测试用例 任选其一
# 方式一 # 需要 cpp_learn/CMakeLists.txt中添加 enable_testing()， 
# cpp_learn/test/CMakeLists.txt中添加add_test(NAME test_hello COMMAND test_hello)
ctest 

# 方式二 # 需要 cpp_learn/CMakeLists.txt中添加 enable_testing()， 
# cpp_learn/test/CMakeLists.txt中添加add_test(NAME test_hello COMMAND test_hello)
make test 

# 方式三
# 找到cpp_learn/build/test/test_hello.exe文件执行 
./test/test_hello.exe
```

### 1.3.2 多个测试工程

> 如果只使用上一小节的方式三，当工程项目很多，项目内模块很多，我们对某个模块测试时却需要对整个测试项目编译和执行，极不方便  
> 因此使用方式一或方式二，可实现对多个测试项目进行编译和管理

`CMakeLists.txt`中开启ctest

```cmake
# 项目根目录下的CMakeLists.txt
# # 开启cmake测试能力
enable_testing()

# # 将 test 添加到项目中, test目录下有CMakeLists.txt
add_subdirectory(test)

##################################################
# 测试工程test文件夹下的CMakeLists.txt
# 添加测试, 参数1: 测试名称, 参数2: 测试命令
add_test(NAME test_hello COMMAND test_hello)

# 添加测试, 参数1: 测试名称, 参数2: 测试命令
add_test(NAME test_world COMMAND test_world)

```

```sh
# build目录下
cmake ..
make -j8

#执行测试
ctest

# 测试详细日志在cpp_learn\build\Testing\Temporary\LastTest.log

```

### 1.3.3 测试项目的编译选择

- 设置编译测试选项
```cmake
# 根目录下的CMakeLists.txt

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

#########################################################
# test目录下的CMakeLists.txt
# 设置 gmock 选项为 OFF，避免编译 gmock 库，因为我们只需要 gtest 库
set(BUILD_GMOCK OFF) # 一定要在add之前

# 将 gtest 添加到项目中， 参数1: gtest所在路径, 参数2: gtest编译后输出路径（自定义）
add_subdirectory(${PROJECT_ROOT}/thirdpart/googletest-1.17.0 googletest)

```

```sh
# 指定编译选项
cmake .. -LH -DBUILD_TEST=ON
```

### 1.3.4 单独编译gtest
> 对于第三方库的文件，其实不用每次都去编译构建，而是下载好源码，编译之后使用即可。  

```sh
# 进入到thirdpart/googletest-1.17.0
mkdir my_gbuild
cd my_gbuild
cmake .. -LH
make
```


```cmake
# 方便直接引入.h文件
# world/CMakeLists.txt
add_library(worldlib STATIC ${WORLD_SRC})

# 添加头文件搜索路径， 只要添加了头文件搜索路径，就可以在源文件中直接使用#include "world.h"来包含头文件，而不需要指定完整路径
target_include_directories(worldlib SYSTEM INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})
```

> 从零开始搭建c/c++工程完结




