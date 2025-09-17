from mcp.server import MCPServer

# Global server object (MCP will detect this)
mcp = MCPServer()

@mcp.route("/")
def hello():
    return "Hello from my-mcp-server!"

# Optional: only needed if running directly
if __name__ == "__main__":
    mcp.run()
