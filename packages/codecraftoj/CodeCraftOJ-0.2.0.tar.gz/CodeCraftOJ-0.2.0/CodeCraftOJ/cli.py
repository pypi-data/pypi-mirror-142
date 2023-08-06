import http
import http.server
import pathlib
import socketserver
from pathlib import Path
from CodeCraftOJ.server.serve import backend
import threading

__version__ = '0.2.0'


def entry():
    print(f"=== CodeCraft Offline Judge v{__version__} ===")
    back_thread = threading.Thread(target=backend, args=[find_record_dir()])
    front_thread = threading.Thread(target=frontend)
    front_thread.start()
    back_thread.start()
    front_thread.join()
    back_thread.join()


def find_record_dir():
    now = Path(".")
    print("Working on:", now.absolute())
    if (now / "task").exists():
        return now / "task"
    else:
        raise FileNotFoundError("""
        未在当前目录找到 task 文件夹
        请在项目根目录建立 task 文件夹,并在根目录运行CLI
        """)


def handler_from(directory):
    def _init(self, *args, **kwargs):
        return http.server.SimpleHTTPRequestHandler.__init__(self, *args, directory=self.directory, **kwargs)

    return type(f'HandlerFrom<{directory}>',
                (http.server.SimpleHTTPRequestHandler,),
                {'__init__': _init, 'directory': directory})


def frontend():
    PORT = 21573

    Handler = http.server.SimpleHTTPRequestHandler

    Handler.extensions_map = {
        '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg': 'image/svg+xml',
        '.css': 'text/css',
        '.js': 'application/x-javascript',
        '': 'application/octet-stream',  # Default
    }

    httpd = socketserver.TCPServer(("", PORT), handler_from(str(pathlib.Path(__file__).parent.resolve())))

    print(f"Done! Web Serving at --> http://localhost:{PORT} <--")
    httpd.serve_forever()


if __name__ == '__main__':
    entry()
