# EudictObsidianBridge 欧路词典到Obsidian转换工具

这个工具的用途是将欧路词典（eudic）中的生词本和笔记整合到Obsidian库。

需要你将欧陆词典中的词库导出后，这个脚本会将其从CSV格式转为Markdown格式。



## 操作方法

### 在欧路词典中

在单词详情页中标星即可把单词记录于生词本。

在单词详情页中添加笔记后则单词自动记录于笔记本。

打开欧路词典主界面。

点击笔记本图标。

点击“管理”。

**选中“生词本”选项卡**。

点击“导出”。

将导出格式调整为“CSV格式”。

点击“导出”，选择路径。

即可导出生词本。

点击“管理”。

**选中“我的笔记”选项卡**。

点击“导出”。

将导出格式调整为“CSV格式”。

点击“导出”，选择路径。

即可导出笔记。

在新窗口中点击“导出”。



## Py脚本的使用

将脚本中的文件名替换后，直接运行。

ver1.2修复了问题，可以适用于全新md文档和附加md文档的内容。

若缺少pandas包，则尝试运行以下命令。

```
pip install pandas
```



## 样例

![obsidian主界面](D:\Program_Myself\Program_Software_Project_Upload\EudictObsidianBridge\example_image\obsidian主界面.png)