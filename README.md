# GEMINI.md

## Project Overview

This project is a simple time server that provides the current local time through a web API. It's built using Python and the `fastmcp` library. The main functionality is exposed via a single API endpoint that returns the time in different formats.

## Building and Running

To run the server, you need to have Python and the required dependencies installed. Based on the `server_fastmcp.py` file, the server can be started using the following command:

Activate venv enviroment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Stdio Test:

```bash
source /home/developer/mcp/datetime-server/venv/bin/activate
cat <<EOF | python3 /home/developer/mcp/datetime-server/server_fastmcp.py --transport stdio
{"jsonrpc": "2.0", "id": 0, "method": "initialize", "params": {"protocolVersion": "1.0", "capabilities": {}, "clientInfo": {"name": "Gemini CLI", "version": "1.0"}}}
{"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "get_local_time", "arguments": {"format": "iso"}}}
EOF
```

Http:

```bash
python3 server.py --transport http --host 127.0.0.1 --port 8000 --path /mcp
```

Http Test:

```bash
curl -X POST -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" -H "mcp-session-id: a7d450acf3264678a542130b61caeaa0" -d '{"jsonrpc": "2.0", "method": "tools/call", "params": {"name": "get_local_time", "arguments": {"format": "iso"}}, "id": 1}' http://127.0.0.1:52792/mcp
```

This will start the server on `127.0.0.1:8000`.

## Development Conventions

The code follows standard Python conventions. It uses the `argparse` module for command-line argument parsing and the `logging` module for logging. The main logic is encapsulated in the `main` function, which is called when the script is executed directly.