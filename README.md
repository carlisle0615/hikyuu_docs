# 文档服务使用指南

本目录包含了项目的所有文档文件，以 Markdown 格式存储。为了更好地浏览这些文档，我们提供了一个简单的本地服务器。

## 如何启动文档服务器

1. 确保您已安装 Python（建议 Python 3.6 或更高版本）
2. 打开终端或命令提示符，进入到 docs 目录：
   ```
   cd docs
   ```
3. 运行服务器脚本：
   ```
   python server.py
   ```
4. 服务器将自动在默认浏览器中打开`http://localhost:8000`

## 功能特点

- **文档索引页面**：首页显示所有可用文档的列表，支持搜索功能
- **Markdown 渲染**：支持查看 Markdown 文件，并自动渲染为美观的格式
- **代码高亮**：所有代码块会自动高亮显示
- **自适应布局**：适合在桌面和移动设备上查看

## 可选参数

您可以指定服务器端口号（默认为 8000）：

```
python server.py 8080
```

## 问题排查

如果服务器无法启动，可能是端口已被占用。服务器会自动尝试使用下一个端口号。

如果您发现任何文档显示问题或服务器错误，请检查以下几点：

1. 确保您使用的是现代化的浏览器（Chrome、Firefox、Edge 等）
2. 检查文档文件是否为有效的 Markdown 格式
3. 确保服务器脚本有执行权限（Linux/Mac 用户可能需要运行`chmod +x server.py`）

## 关闭服务器

要停止服务器，请在终端中按`Ctrl+C`。
