# 操作指南

## 克隆仓库到本地

1. 在电脑任意文件夹中，右键，点击**在终端中打开**，依次输入：

```
git clone https://github.com/Sunzhuoran-bit/business_intelligence
cd business_intelligence
```

## 本地修改文件

2. 每次在修改代码之前，都请同步代码为最新的代码，在终端中输入：

```
 git pull origin main
```

2. 如果要进行文件的修改和编写，请在终端中输入：

```
git checkout -b feat/代码的功能
```

其中，feat/代码的功能 ，总共可以有7类，请对应修改：

- feat：新功能（feature）
- fix：修补bug
- docs：文档（documentation）
- style： 格式（不影响代码运行的变动）
- refactor：重构（即不是新增功能，也不是修改bug的代码变动）
- test：增加测试
- chore：构建过程或辅助工具的变动

代码的功能，自己想起什么名字就起什么。

3. 接下来，您可以在本地进行任何修改、添加或删除操作。在完成修改之后，您可以将更改记录到本地分支。如果要查看您修改的文件，在终端中输入：

   ```
   git status
   ```

## 向仓库提交修改

4. 请先配置您的邮箱和名字（只需要配置一次），邮箱请务必设置为和github注册时相同的邮箱。在终端中输入：

```
git config --global user.email "you@example.com"

git config --global user.name "Your Name"
```

4. 如果您想将修改的代码提交到GitHub仓库中，请依次输入：

```
git add .

git commit -m "对您工作的简要描述"

git push -u origin feat/代码的功能
```

5. 合并到 `main`分支 ：浏览器中打开：https://github.com/Sunzhuoran-bit/business_intelligence。

点击Pull requests，再点击页面中的绿色按钮：Compare & pull request。设置页面中的base:main。compare:feat/代码的功能。设置好之后，点击create_pull_request，等待审核。



如果仍有不懂的地方，请询问AI工具。