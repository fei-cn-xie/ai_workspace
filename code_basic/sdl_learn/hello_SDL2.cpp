#include <iostream>
#include <SDL.h>
#include <chrono>
#include <thread>

constexpr int gWindowWidth = 800;
constexpr int gWindowHeight = 600;

int main(int argc, char* argv[]) {
    // 初始化 SDL 视频子系统
    SDL_Init(SDL_INIT_VIDEO);

    // 创建一个 SDL 窗口
    SDL_Window *window = SDL_CreateWindow("Hello SDL2", 
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, gWindowWidth, gWindowHeight, 0);
    
    // 等待 2 秒钟
    std::chrono::milliseconds ms(2000);
    std::this_thread::sleep_for(ms);

    // 销毁窗口并退出 SDL
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}