#!/usr/bin/env python
import http.server
import socketserver
import os
import sys
import webbrowser
from urllib.parse import unquote, urlparse

# 默认端口
PORT = 8000


class MarkdownHandler(http.server.SimpleHTTPRequestHandler):
    """处理Markdown文件的HTTP处理器"""

    def do_GET(self):
        # 解码URL
        path = unquote(self.path)

        # 解析URL，分离路径和查询参数
        parsed_url = urlparse(path)
        path = parsed_url.path

        # 处理根路径请求
        if path == "/" or path == "":
            self.path = "/index.html"
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

        # 如果是.md文件，设置正确的MIME类型
        if path.endswith(".md"):
            try:
                # 移除开头的/
                if path.startswith("/"):
                    path = path[1:]

                with open(os.path.join(os.getcwd(), path), "rb") as f:
                    content = f.read()

                self.send_response(200)
                self.send_header("Content-type", "text/markdown")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return
            except FileNotFoundError:
                self.send_error(404, f"文件未找到: {path}")
                return

        # 对于其他文件类型，使用默认处理
        # 保存原始路径
        original_path = self.path
        # 设置self.path为不含查询参数的路径
        self.path = path
        # 调用父类方法处理请求
        result = http.server.SimpleHTTPRequestHandler.do_GET(self)
        # 恢复原始路径
        self.path = original_path
        return result


def run_server(port=PORT):
    """运行HTTP服务器"""
    handler = MarkdownHandler

    # 设置服务器当前目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # 尝试启动服务器
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"服务器启动在 http://localhost:{port}/")
            print("按 Ctrl+C 停止服务器")

            # 自动打开浏览器
            webbrowser.open(f"http://localhost:{port}/")

            # 启动服务器
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 98 or e.errno == 10048:  # 地址已被使用 (Linux 98, Windows 10048)
            print(f"端口 {port} 已被占用，尝试使用另一个端口")
            run_server(port + 1)
        else:
            raise


if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            run_server(port)
        except ValueError:
            print(f"错误：端口必须是一个整数")
            print(f"用法：{sys.argv[0]} [port]")
            sys.exit(1)
    else:
        run_server()
