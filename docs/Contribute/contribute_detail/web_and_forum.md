# 课程主页与论坛进度工作内容

!!! abstract "工作职责"
    **更新主页内容、维护文档与链接，及时发布论坛帖子。**

## 更新主页内容

### 概述

我们的[课程主页][homepage]托管在 Github Page 上，目前已经做到了自动部署，配置文件是 `.github\workflows\ci.yml`，一般情况下**无需更改 `ci.yml`**。

目前仓库还是归属在 [@anine09](https://github.com/anine09)，在整个项目初步完善后会移交至 [@Datawhale](https://github.com/datawhalechina)。

网站使用的框架是 [MkDocs](https://www.mkdocs.org/)，使用了 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 主题。

你可以使用如下命令来安装 `mkdocs-material`（这同时会自动安装 MkDocs）：

```bash
 pip install mkdocs-material
```

并在项目目录下使用如下命令来在本地运行网站：

```bash
mkdocs serve
```

整个 MkDocs 的配置文件是 `mkdocs.yml`。其中的配置可以酌情进行修改，参考 MkDocs 和 Material for MkDocs 的文档说明。

### 改动与添加页面

在改动与添加页面之前，请**在本地运行网站**以提供实时预览。

网站的一个页面就是一个 Markdown 文件，我们可以通过直接添加与修改对应的 Markdown 文件来实现网页内容的展示。

Material for MkDocs 提供了一些很漂亮的展示效果，推荐阅读[官方参考手册](https://squidfunk.github.io/mkdocs-material/reference/#built-in-meta-plugin)，比如这个页面就用到了 [Admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)。

!!! warning "添加页面时需注意"
    每次添加一个页面，需要修改 `mkdocs.yml` 的 `nav` 部分。

    可以参考[网站页面结构][website_tree]来进行修改，并更新这个页面的内容。

如果需要在网页 Markdown 文件内指向另一个网页 Markdown 文件，请使用**项目目录的相对路径**。并且可以使用 `#_*数字*` 来指定跳转的标题，比如点击[这个](#_1)就可以跳转到本页面的开头。点击标题旁形如 :fontawesome-solid-paragraph: 的按钮，就可以在浏览器的地址栏看到具体的地址（末尾以 `#` 开头的部分）。

By the way，如果需要输入 emoji 和 icon，请参阅：[Icons, Emojis](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/?h=icon)。

### 任务需求

在大致了解项目的结构和网站的呈现方式后，你需要做的就是定期将其他小组同学新制作的教学内容更新至课程主页，并管理课程公告，按照团队计划完善主页的其他内容，还有一点是需要根据反馈来修改文档中如错字、无效链接等小 bug。也可以逐步美化课程主页，增加更多的新功能。

## 发布论坛帖子

当新的教学内容发布后，需要在 Datawhale 论坛的相关 Tag 下发布课程讨论的帖子，例如：[[P2S] 课程讨论 - Chap 1 启航 Getting Started](http://forum.datawhale.club/t/topic/4435)。

帖子发布后请关注它，以便及时收到反馈，并更新[课程公告][course_announcement]、[项目仓库结构][repo_tree]和[网站页面结构][website_tree]等内容。

!!! note "Markdown 链接规范"
    如果需要在 Markdown 中使用链接，请遵循以下规范：

    - 外部链接直接使用 `[链接显示名](链接地址)` 语法。
    - 与本项目相关的链接，如其他 md 文件、项目网址等，需要使用 `[链接显示名][链接标签]` 语法，将引用内容放置文件末尾，且保证 `链接标签` 命名是有意义的。语法参考：[Markdown 链接语法](https://markdown.com.cn/basic-syntax/links.html#%E5%BC%95%E7%94%A8%E7%B1%BB%E5%9E%8B%E9%93%BE%E6%8E%A5)。
    - 所有图片内容保存在  `docs/images` 的相关文件夹下，并保证命名是有意义的，使用 `![][*数字标签*]`，同样将引用内容放置文件末尾，可以使用 `<figcaption>` 标签[添加图片描述](https://squidfunk.github.io/mkdocs-material/reference/images/#image-captions)，这不是强制选项。

    <figure markdown>
    ![][1]
    <figcaption>参考示例</figcaption>
    </figure>

**我们需要新的发帖模板，请指定相关可行方案。**


!!! info inline end "联系教学团队"
    如果你对这部分内容有任何问题，请联系教学团队寻求帮助。

    [联系教学团队 :fontawesome-solid-envelope:][mail_to_team]{ .md-button }
    
[mail_to_team]: ../../Team/team.md
[homepage]: https://anine09.github.io/learn-python-the-smart-way-v2/
[website_tree]: ../repo_tree.md#_3
[course_announcement]: ../../Index/announcements.md
[repo_tree]: ../repo_tree.md#_2
[1]: ../../images/contribute/markdown_link.png