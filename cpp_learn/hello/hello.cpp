#include <iostream> // 引入输入输出流库
#include "hello.h" // 引入头文件, 这里编译时会自动找到hello.h，把函数声明引入到当前文件中

int Hello() { // 定义Hello函数
    std::cout << "Hello" << std::endl; // 输出Hello并换行
    return 0; // 返回0表示函数执行成功
}

int Hello_Fei() {
    return 152;
}