#!/usr/bin/env python3
from fastmcp import FastMCP
from datetime import datetime
import argparse
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("local-time-mcp")

mcp = FastMCP(name="Local Time Server")

@mcp.resource("time://now")
def time_now() -> dict:
    now = datetime.now().astimezone()
    return {
        "iso": now.isoformat(),
        "human": now.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "tz": str(now.tzname())
    }

@mcp.tool()
def get_local_time(format: str = "iso") -> str:
    now = datetime.now().astimezone()
    if format == "iso":
        return now.isoformat()
    if format == "human":
        return now.strftime("%Y-%m-%d %H:%M:%S %Z")
    return now.strftime(format)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--transport", choices=["stdio", "http"], default="stdio")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--path", default="/mcp")
    args = parser.parse_args()

    log.info("Starting Local Time MCP server (%s)", args.transport)
    if args.transport == "stdio":
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="http", host=args.host, port=args.port, path=args.path)

if __name__ == "__main__":
    main()
