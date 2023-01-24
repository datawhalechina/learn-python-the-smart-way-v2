# 项目结构

## 项目仓库结构

```bash
learn-python-the-smart-way-v2
 ├── docs # P2S 网站相关内容
 │   ├── aims.md # 学习目标
 │   ├── background.md # 课程背景
 │   ├── contribute.md # 参与贡献
 │   ├── contribute_detail # 贡献细则
 │   │   └── repo_tree.md # Repo 结构
 │   ├── datawhale.md # 关于 Datawhale
 │   ├── images # 图片资源
 │   │   ├── datawhale_logo.png # Datawhale Logo
 │   │   └── datawhale_wechat_qrcode.jpeg # Datawhale 公众号二维码
 │   ├── index.md # 简介
 │   ├── method.md # 授课形式
 │   ├── question.md # 答疑交流
 │   ├── reference.md # 课程资源
 │   ├── schedule.md # 课程进度
 │   ├── schedule_detail # 课程进度详情
 │   │   ├── chap0.md
 │   │   ├── chap1.md
 │   │   ├── ...
 │   └── team.md # 教学团队
 ├── homework # 作业相关文件夹
 │   ├── chapter_0-Install
 │   │   ├── hw0_info.md
 │   │   ├── p2s.yaml
 │   │   └── requirements.txt
 │   └── hw1.py
 ├── LICENSE # 项目协议
 ├── mkdocs.yml # P2S 网站配置
 ├── README.md 
 ├── resources # Slides 的资源
 │   ├── datawhale_logo.png
 │   ├── datawhale_wechat_qrcode.jpeg
 │   ├── icon
 │   │   └── video.svg
 │   └── slides
 │       └── chap1
 │           └── pic
 │               ├── chap1_1_464px-Brian-Kernighan-2017.png
 │               ├── chap1_1_AIMaster.jpg
 │               └── reference.md
 └── slides # 幻灯片
     ├── chapter_0-Installation.ipynb
     ├── chapter_1-Getting_Started.ipynb
     ├── chapter_2-Data_Types_and_Operators.ipynb
     ├── chapter_3-Variables_and_Functions.ipynb
     ├── chapter_4-Conditionals.ipynb
     ├── datawhale_logo.png
     └── rise.css # Jupyter Notebook RISE 插件配置
```
## 网站页面结构
```yaml
nav:
    - 简介:
          - 课程简介: index.md
          - 课程背景: Index/background.md
          - 课程公告: Index/announcements.md
    - 教学团队: Team/team.md
    - 课程进度:
          - 课程进度列表: Schedule/schedule.md
          - 进度详情:
                - Chap 0 安装: Schedule/schedule_detail/chap0.md
                - Chap 1 启航: Schedule/schedule_detail/chap1.md
                - Chap 2 数据类型和操作: Schedule/schedule_detail/chap2.md
                - Chap 3 变量与函数: Schedule/schedule_detail/chap3.md
    - 学习目标: Aims/aims.md
    - 授课形式: Method/method.md
    - 答疑交流: Question/question.md
    - 课程资源: Reference/reference.md
    - 参与贡献:
          - 如何贡献: Contribute/contribute.md
          - 项目结构: Contribute/repo_tree.md
          - 教学团队工作流: Contribute/workflows.md
          - 贡献细则:
                - 课程主页、论坛进度: Contribute/contribute_detail/web_and_forum.md
                - 作业发布、作业验证: Contribute/contribute_detail/homework.md
                - 直播辅助、视频剪辑: Contribute/contribute_detail/live_and_video.md
                - 文字教程、反馈收集: Contribute/contribute_detail/textbook_and_feedback.md
                - 进度跟进、答疑讨论: Contribute/contribute_detail/progress_and_discuss.md
                - 课程大纲、课程内容: Contribute/contribute_detail/outline_and_content.md
    - 关于 Datawhale: About/datawhale.md
```