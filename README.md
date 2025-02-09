# FnTop

> 让你的窗口起到十分烦人的作用！

> 灵感来自于在COVID-19时居家学习所使用的[无限宝](https://www.kehou.com/charactFunction.htm)工具！


## 功能介绍

- 每隔几秒（或是零点几秒）激活一个窗口！可以设定多个窗口来一个一个激活。
- 令人防不胜防！只要FnTop没有关闭就可以一直使用。
- 与无限宝斗智斗勇！看看到底是FnTop更聪明，还是无限宝更NB！


## 安装与使用

可以从右侧的Release里点击最新的一栏，然后在Assets中下载对应的运行文件。
- Windows用户：下载 **"FnTop_*[版本]*_win.zip"** ，解压后运行 **"FnTop.exe"**。
- 其他系统：参见 **“从源代码运行”** 。

## 从源代码运行

> 如果我就是想特立独行，或者手滑下载的是Source Code(.zip)/Source Code(.tar.gz)，那该怎么办？
> 你可以参阅以下步骤来从源代码运行FnTop。
 
1. 下载源代码。可以从Release>最新版本>Assets>Source code下载。
2. 解压源代码到一个文件夹：我们假设你解压到了`D:\FnTop`(Windows)/`/home/FnTop`(Linux/MacOS)中。
3. 安装Python。
    - Windows: 从[Python3.12下载页面](https://www.python.org/downloads/)下载最新版本的Python安装文件。
      可以在页面最下方找到`Windows installer(64-bit)`（64位）或`Windows installer(32-bit)`（32位）下载。
    - MacOS：同样在[Python3.12下载页面](https://www.python.org/downloads/)的最下方下载`macOS 64-bit universal2 installer`。
    - Linux的发行版：自行搜索（因为太多了支持不过来）。
4. 安装完成后，打开命令行：
    - Windows：使用PowerShell输入
      ```shell
      cd D:\FnTop\  # 记得把D:\FnTop\换成你解压的位置
      pip3 install -r requirements.txt
      python3 main.py
      ```
    - MacOS/Linux：使用终端输入
      ```shell
      cd /home/FnTop/  # 记得把/home/FnTop/换成你解压的位置
      pip3 install -r ./requirements.txt
      python3 ./main.py
      ```
5. 完成！FnTop应该已经启动。不过在FnTop运行时不要关闭命令行。
