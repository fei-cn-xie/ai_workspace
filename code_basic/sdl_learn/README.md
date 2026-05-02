
> 本内容基于：https://www.bilibili.com/video/BV1iz4y1L7tA  
# 1. SDL简介

## 1.1 简介
> SDL（Simple DirectMedia Layer） 是一套开源的、跨平台的多媒体开发库，专门为游戏和多媒体应用程序提供底层硬件访问的抽象层。  
> 可以把 SDL 理解为一个 “硬件抽象层”，它屏蔽了不同操作系统之间的差异（Windows、macOS、Linux、iOS、Android 等），让你可以用同一套 C/C++ 代码实现：
> - 窗口创建与管理
> - 2D/3D 图形渲染
> - 键盘、鼠标、游戏手柄输入
> - 音频播放
> - 多线程与定时器  
> ### 核心功能模块
> - 模块: 功能
> - 视频: 渲染	创建窗口、2D 图形加速、纹理渲染，也可与 OpenGL/Vulkan/Metal 配合
> - 输入事件: 键盘、鼠标、游戏手柄、触屏、加速计
> - 音频: 音频播放、简单混音（独立音频线程）
> - 系统工具: 跨平台线程、高精度计时器、文件 I/O、字节序处理

## 1.2 SDL安装

> https://libsdl.org/  
> https://github.com/libsdl-org/SDL/releases/tag/release-3.4.8  


```sh
# 通过命令行安装，提前安装msys2，ucrt64窗口中操作
pacman -S mingw-w64-ucrt-x86_64-SDL2


# 通过源码，手动编译安装
# 1. 下载源码压缩包 SDL-release-3.4.8.tar.gz
# 2. 进入ucrt64窗口，解压
tar -zxf SDL-release-3.4.8.tar.gz
# 3. 进入目录, 创建编译目录，手动编译
cd SDL-release-3.4.8/
mkdir build
cd build
cmake .. -L -G"MSYS Makefiles"
make -j16

```