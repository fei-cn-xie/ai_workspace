# gdb调试

```sh
# 在build目录构建好main.exe后
# 进入调试
gdb ./main.exe
```

```sh
# 进入gdb后
# 打断点
b main.cpp:7

# 运行
r
```


## 设置环境变量

针对windows环境，msys2的配置  

clang和ucrt64二选一
> d:\msys2\usr\bin  
> d:\msys2\ucrt64\bin


## 在vscode中使用gdb

1. 在项目目录中创建`.vscode`
2. 在`.vscode`中创建`settings.json`

```json
// 指定编译器
{
    "C_Cpp.default.compilerPath": "g++.exe"
}
```

3. 在.vscode中创建`task.json`

```json


// tasks.json
{
    // https://code.visualstudio.com/docs/editor/tasks
    "version": "2.0.0",
    "tasks": [
        {
            "label": "CMAKE",   // 任务的名字叫CMAKE，注意是大小写区分的，等会在launch中调用这个名字
            "type": "shell",    // 任务执行的是shell命令
            "command": "cmake", // 配置cmake环境变量
            "args": [
                "-S./",
                "-Bbuild",
                "-L",
                "-G\\\"MSYS Makefiles\\\"", // \需要转义
                "-DBUILD_DEBUG:BOOL=ON"
            ]
        },
        {
            "label": "MAKE",    // 任务的名字叫MAKE，注意是大小写区分的，等会在launch中调用这个名字
            "type": "shell",    // 任务执行的是shell命令
            "command": "make",  // 配置make环境变量
            "args": [
                "-C",
                "build"
            ]
        },
        {
            "label": "Buildhelloworld",   // 任务的名字叫Build，注意是大小写区分的，等会在launch中调用这个名字
            "dependsOrder": "sequence",
            "dependsOn": [
                "CMAKE",
                "MAKE"
            ]
        }
    ]
}

```

4. 在.vscode中创建`launch.json`

```json
// launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "helloworldGDB",     //这个应该是F1中出现的名字
            "preLaunchTask": "Buildhelloworld",   //在launch之前运行的任务名，这个名字一定要跟tasks.json中的任务名字大小写一致
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/build/main.exe", //需要运行的是当前打开文件的目录中，名字和当前文件相同，但扩展名为exe的程序
            "args": [],
            "stopAtEntry": true,           // 选为true则会在打开控制台后停滞，暂时不执行程序
            "cwd": "${workspaceFolder}",    // 当前工作路径：当前文件所在的工作空间
            "environment": [],
            "externalConsole": true,        // 是否使用外部控制台，选false的话，我的vscode会出现错误
            "MIMode": "gdb",
            "miDebuggerPath": "gdb",        // 调试器，gdb路径添加到环境变量
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
        }]
}

```