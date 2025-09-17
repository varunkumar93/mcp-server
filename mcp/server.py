# mcp/server.py

class MCPServer:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def decorator(fn):
            self.routes[path] = fn
            return fn
        return decorator

    def run(self):
        print("Server is running (simulated). Registered routes:")
        for path, func in self.routes.items():
            print(f"{path} -> {func()}")
