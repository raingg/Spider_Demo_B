# Python Spider

### Day 01

#### 创建项目

1. 安装 Anaconda

2. 命令行 Anaconda 更新源

```
C:\Users\Administrator>conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

C:\Users\Administrator>conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/

C:\Users\Administrator>conda config --set show_channel_urls yes
```

3. 创建 PyCharm scientific 项目

- 选择 Scientific
- 选择 Project Interpreter: New Conda Environment
    - Conda Environment using: Conda
    - Location
    - Python version
    - Conda execution
4. 命令行

- conda env list
- activate <conda 虚拟环境名>
- conda install numpy
- conda install matplotlib
- 复制代码到 main.py
- 运行 main.py
- 错误修复：
    - Run: `Cannot start process, the working directory does not exist.`
    - Run | Edit Configurations | working directory - Select project directory - OK 


#### 练习
使用 requests 和 pandas 库抓取一级/二级商品类目存入 csv 文件 

### Day 02
  
#### 练习
1. 修改 category 表
2. 把 csv 文件数据导入 MySQL 数据库
3. 实现二级类图图标的下载