
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
add_library(hellolib SHARED ${HELLO_SRC})
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


## 1.3 gtest测试框架







