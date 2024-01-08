# 扩展市场

![classic](./script/classic.svg)
![yaml](./script/yaml.svg)
![excel](./script/excel.svg)

本仓库用于供应扩展文件内容和对应的接口

## 牌堆
### 目录结构
```
├─deck
│  ├─作者
│  │  ├─classic
│  │  │  ├─__index.json
│  │  │  ├─牌堆1.json
│  │  │  ├─牌堆2.json
│  │  │  └─...
│  │  └─resource
│  └─...
└─...
```


#### 作者空间
每一个作者可以在`deck`目录下以自己的名字直接创建一整个目录，所有的有关作品的操作都可以在自己的目录内完成。  

#### 类型牌堆
目前支持了`classic`牌堆，这是最基础的`json`格式牌堆，可以在自己的作者空间内创建对应的目录，并将对应的牌堆放入该目录。  

#### 索引文件
特别的，名为`__index.json`的文件不会被当作牌堆，而是用于描述当前目录下的牌堆的附加信息，例如`牌堆名`、`作者`、`描述`、`版本号`等等，这些信息将被用于生成扩展市场的接口数据，并最终展示在用户与扩展市场的应用界面上。  
其基本格式如下：  
```json
{
    "明日方舟-Arknights(单抽-十连).json": {
        "name": "明日方舟",
        "version": "201111",
        "version_code": 1,
        "desc": "明日方舟干员寻访，干员档案数据全部来自ArknightsWiKi，文案版权属于鹰角网络。在这里，你甚至可以抽出绝版暴行",
        "author": "lunzhiPenxil"
    },
    "明日方舟卡池-Arknight(卡池-[对应卡池名称]).json": {
        "name": "明日方舟卡池",
        "version": "201111",
        "version_code": 1,
        "desc": "明日方舟卡池寻访，干员档案数据全部来自ArknightsWiKi，文案版权属于鹰角网络。在这里，你甚至可以抽出绝版暴行",
        "author": "lunzhiPenxil"
    },
    "黑暗之魂-黑魂合集（带图版）.json": {
        "name": "黑暗之魂-黑魂合集（带图版）",
        "version": "1",
        "version_code": 1,
        "desc": "包含黑暗之魂三部曲中的武器、装备、道具、戒指、法术、生物、地点。全部文案来自黑暗之魂游戏数据解包，版权归FromSoftware所有。",
        "author": "lunzhiPenxil",
        "resource": [
            "黑暗之魂-黑魂合集（带图版）图包P1.zip",
            "黑暗之魂-黑魂合集（带图版）图包P2.zip",
            "黑暗之魂-黑魂合集（带图版）图包P3.zip",
            "黑暗之魂-黑魂合集（带图版）图包P4.zip",
            "黑暗之魂-黑魂合集（带图版）图包P5.zip"
        ]
    },
}
```


#### 资源文件
特别的，一些牌堆可能需要同时安装对应的`资源文件`，通常是一些图片文件，这些文件应当参考`OlivOS`的资源文件目录`data`下的格式以`zip`打包，放置在作者空间的`resource`目录下，并将对应的资源文件名称在`__index.json`中为对应牌堆以`resource`字段建立索引，可参考上文`黑暗之魂-黑魂合集（带图版）.json`的写法。  

## 提交的途径（给初学者的指南）
通常来说，在`Github`上我们以`Pull Request（拉取请求）`的方式来提交自己的改动，得益于`Github`完善的设计，整个提交过程你完全可以图形化的完成。

### 登录
要在`Github`上进行操作，你首先要拥有一个账号，你可以在网站的右上角进行注册后  

![image](https://github.com/OlivOS-Team/Extiverse/assets/26300331/f207650c-e686-4a87-9c5e-8abb56ef93e6)  

使用该账号登录。  

### 分支仓库
由于你并没有直接修改本仓库的权限，所以在进行修改前，你需要在你的账号名下基于本仓库创建一个分支仓库，这是一个内容与本仓库当前版本完全一致的仓库，并且会标记出分支的来源，这个仓库将是一个你真正可以随意修改的仓库。  
要创建一个分支仓库，你只需要点击右上角的`Fork`  

![image](https://github.com/OlivOS-Team/Extiverse/assets/26300331/7bb70dba-41e8-4f13-8577-26ac674801bc)  

随后你就可以开始分支流程，并最终跳转到你创建的仓库。

### 修改分支
此时你就可以对自己的分支仓库进行修改了，修改也可以以多种方式进行，你可以直接在网页上对文件进行修改，或创建和删除文件，你也可以使用`Github Desktop`来将文件克隆至本地，然后直接在本地进行修改。  
修改后，你可以在自己的分支仓库看到`Open Pull Request`的按钮  

![image](https://github.com/OlivOS-Team/Extiverse/assets/26300331/8f12ca38-72c8-455f-8c83-2f542cc495e8)  

点击它，你就可以开启`拉取请求`的流程，它最终会被提交给我们，我们进行合并后，你的修改就会自动的在扩展市场中生效了。  

#### 使用 CodeSpace 进行修改
除此之外，在你的分支仓库中，你还能使用`CodeSpace`一次性完成诸如创建文件，创建文件夹等一系列操作，对于不熟悉`Github`的用户可以考虑尝试。  

![image](https://github.com/lunzhiPenxil/Extiverse/assets/26300331/d910d588-80c0-4eab-9e75-7f485124eebe)

如上，点击后可以进入一个可以进行直观操作的网络文本编辑器其中你要注意的是左侧的`文件浏览器`与`Git版本管理器`  

![image](https://github.com/lunzhiPenxil/Extiverse/assets/26300331/e7eb0756-e52e-456f-a48c-cf54bbd4c144)

你可以通过右键菜单创建文件夹和文件  

![image](https://github.com/lunzhiPenxil/Extiverse/assets/26300331/f31a3ed8-9f8d-4f05-b367-5d245a686979)

创建完成后，可以直接在这个页面进行提交，随后，可以在原先的`Github`页面按照上文开启`拉取请求`的流程

![image](https://github.com/lunzhiPenxil/Extiverse/assets/26300331/c9f836d0-df65-429a-a230-3381f795e25d)




## 收录准则
会选择性作者自主上传至互联网的扩展文件，会优先联系作者本人。如果作者本人处于失联状态，且如果被分享的文件在发布时声明了遵守 CC-BY-NC-SA-4.0 或是其兼容的更宽松协议，则会在注明出处的前提下进行分享，并保留作者的驳回权利。
