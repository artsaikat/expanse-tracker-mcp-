from fastmcp import FastMCP

mcp = FastMCP("Test")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello {name}"

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000,
    )