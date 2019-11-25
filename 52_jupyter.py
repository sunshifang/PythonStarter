print('''
     Jupyter Notebook入门指南

01. 什么是Jupyter Notebook?
Jupyter Notebook是一款开放源代码的Web应用程序，可让我们创建并共享代码和文档。它提供了
一个环境，你可以在其中记录代码，运行代码，查看结果，可视化数据并在线查看输出结果。这
些特性使其成为一款执行端到端数据科学工作流程的便捷工具，可以用于数据清理，统计建模，
构建和训练机器学习模型，可视化数据以及其他许多用途。
在构建项目原型时，你的代码是被写入独立的单元并被单独执行的。这允许用户测试项目中特定
代码块，而无需从脚本的开始执行代码。还可以运行Python以外的其他语言，比如R、SQL等。由
于它们比IDE平台更具交互性，因此它们被广泛应用于教学场景。

02. 如何安装
可以使用Anaconda发行版来同时安装Python和Jupyter Notebooks
也可以通过pip install jupyter 单独安装

03. 开始使用
    1）启动
    在命令行中输入jupyter notebook并回车后，Jupyter Notebook将在默认的浏览器中打开网
    址为 http://localhost:8888/tree，无法打开时可以复制网址到浏览器地址栏手动执行。
    2）界面说明
    选项卡Files(文件): 列出当前用户的所有文件
    选项可Running(运行)：显示当前已经打开的终端和Notebooks
    选项卡Clusters(集群)：由IPython parellel包提供，用于并行计算。
    3）新建Notebook
    单击右侧的“New”选项卡(可创建Python3 TextFile Folder Terminal等)，选"Python3"
    菜单栏：File Edit View Insert Cell Kernel Help
    工具栏：保存并检查 在下面插入代码块 剪切选择的代码块 复制选择的代码块 粘贴到下
            面上移选中单元格 下移选中单元格 运行 中断服务 重启服务(带窗口) 重启服
            务然后重新运行整个代码(含窗口)
    选项：Code - 输入代码
          Markdown - 输入文本，可以在运行代码后添加结论、添加注释等。
          Raw NBConvert - 命令行工具，可将你的笔记转换为另一种格式(入HTML)
          Heading - 将标题添加到单独的小节使Notebook看起来干净整洁。这个选项已经集
          成到Markdown选项中，添加一个##，以确保输入内容被视为标题
    4）使用Magic Functions
    开发人员已经插入了预定义的magic functions，使你的工作更加方便和更具交互性。你可
    以运行以下命令来查看这些函数的列表(通常不需要输入"%"，因为Automagic默认打开的)
    magic command有两种运行方式：
    ·逐行运行(Line-wise)：执行单元格中的一行代码，命令要以%字符开始
    ·逐块运行(Cell-wise)：执行整个单元格中的代码，所有命令都必须以%%开头

04. 不仅限于Python - 在Notebooks中使用R，Julia和Javascript
    1）要在Jupyter中启用R，你需要GitHub上提供的IRKernel（R的专用内核）。这里有一份
    详细的指南(地址：https://discuss.analyticsvidhya.com/t/how-to-run-r-on-jupyter
    -ipython-notebooks/5512），总共需要八个步骤，还有截图来引导你一步一步进行操作。
    R语言可以用于数据分析。
    2）Julia可用于科学计算，可查看(https://discuss.analyticsvidhya.com/t/how-to-run
    -r-on-jupyter-ipython-notebooks/5512)
    3）使用Javascript需要IJavascript内核，可查看（地址：https://github.com/n-riesco/
    ijavascript），需要安装Node.js和npm才能使用。

05. Jupyter Notebooks中的交互式命令面板
在开始添加小插件(widget)之前，你需要导入widgets包：
    from ipywidgets import widgets
小插件的基本类型是典型的文本输入框和按钮。

06. 键盘快捷键--节省时间并提高效率！
Jupyter Notebook提供了两种不同的键盘输入模式 - 命令和编辑。命令模式将键盘与Notebook
命令绑定，并由具有蓝色左边距的带有灰色单元格边框来表示。编辑模式允许你将文本(代码)
输入活动单元格，并以绿色单元格边框表示。
使用Esc和Enter在命令和编辑模式之间切换(命令模式没有活动单元格，不可输入文本或代码)
    1）命令模式下的快捷键
    ·插入单元格：A键在选中单元格上方插入新单元格，B键在下方插入
    ·删除单元格：连续按两次D键
    ·代码单元格：Y键将当前选中的单元格变成代码单元格
    ·选择多个单元格：shift + ↑(↓)
    ·合并单元格：在多选模式下，Shift + M
    ·查找和替换：F键会弹出“查找和替换”菜单
    2）编辑模式下的快捷键
    ·Ctrl + Home 回到单元格开头
    ·Ctrl + S 保存
    ·Ctrl + Enter 执行当前单元格内的代码
    ·Alt + Enter 执行单元格的同时，在下方添加新的单元格
    ·Ctrl + Shift + F 打开命令选项板
    ·Ctrl + D 删除一行
    要查看整个键盘快捷键列表，请在命令模式下按H或转到Help菜单的Keyboard shortcuts
    请经常检查这些内容，因为经常会有新的快捷键被加进来

07. 有用的Jupyter Notebooks扩展
扩展可以有效提高你的Jupyter Notebooks的生产力。安装使用扩展的工具是Nbextensiions。
它需要两个简单的步骤来安装(还有其他方法)
    ·第1步：pip install jupyter_contrib_nbextensions  #安装nbextensions
    ·第2步：jupyter contrib nbextension install --user  #安装关联的js和css文件
完成操作后，在主页顶部会看到一个Nbextensions选项卡。列出所有扩展供使用。

07. 保存和共享你的Notebook
这是Jupyter Notebook中最重要和最棒的功能之一。当我需要写博客文章，但我的代码和注释
都保存在Jupyter文件时，我需要先将它们转换为另一种格式。请记住，这些Notebooks采用
json格式，在共享它时这并不是很有帮助。我无法在电子邮件或博客上发布不同的单元格或代
码块。可以这样做：进入Files菜单，选Download As选项：可以将你的Notebook保存为7个选项
中的任何一个(Notebook.ipynb Python.py HTML.html Markdown.md reST.rst LaTex.tex
PDF via LaTex.pdf)，就相当于另存为其他格式。
可以使用NBConvert选项，手动将你的Notebook转换为不同格式，如html或pdf.
还可以使用jupyterhub，它允许你在其服务器上托管Notebooks并与多个用户共享。许多顶尖的
研究项目都使用这个功能用于协作。

08. JupyterLab
今年(2019)2月推出，它允许以更灵活和更强大的方式处理项目，使用的是和Jupyter Notebook
相同的组件。JupyterLab环境与Jupyter Notebooks完全相同，但用户会有更高效的体验。
在JupyterLab中，你只需一个窗口即可以安排Notebook的工作区域、终端、文本文件和输出！
你要做的仅仅是将单元格拖放到你想要的位置。你还可以通过实时预览功能来编辑常用文件格
式，如Markdown、CSV和JSON，以便在实际文件中实时查看所发生的编号。安装说明在下面：
地址：http://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
开发人员的目标是JupyterLab最终可以取代Jupyter Notebooks。但是，要做到这一点还有一段
路要走，还要花些时间。

09. 最佳实践
虽然单独工作可能很有趣，但大多数时候你会发现自己是在一个团队中工作。在这种情况下，
遵循指导方针和最佳实践非常重要，这样可以确保你的代码和Jupyter Notebooks被正确标注，
以便与你的团队成员保持一致。下面列出了一些最佳实践指南：
·对于任何程序员来说，最重要的事情之一：始终确保为代码添加合适的注释！
·确保你有代码所需的文档。
·考虑一个命名方案，并坚持在所有代码中使用，以确保一致性。便于其他人读懂代码。
·无论你需要什么库，在Notebooks开始导入他们时要添加注释说明导入目的。
·确保代码中行与行之间有适当间隔，不要把循环和函数放在同一行中。
·文件多时，考虑隐藏那些对于以后参考不太重要的代码，让Notebooks看起来整洁赏心悦目。
·Matplotlib可以很漂亮整洁地展示你的Notebook，想办法使用它，地址：http://nbviewer.
  jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-
  Matplotlib.ipynb

10. 创建幻灯片
执行完View → Cell Toolbar → Slideshow操作后，每个单元格的右侧会显示一个SlideType
的下拉选项，它提供了以下5个选项：Slide Sub-Slide Fragment Skip Notes
    

''')
