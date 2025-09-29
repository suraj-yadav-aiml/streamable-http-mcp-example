# Streamable HTTP MCP Server on AWS EC2

A complete demonstration of deploying a Model Context Protocol (MCP) server using streamable HTTP transport on AWS EC2 and integrating it with Claude Desktop. This project showcases how to build, deploy, and connect remote MCP servers for enhanced AI capabilities.

##  Features

This MCP server provides 4 interactive tools:

- **🤝 Greeting** - Send personalized greetings
- **🎲 Dice Roller** - Roll customizable dice with various sides and counts
- **🔐 Password Generator** - Generate secure passwords with customizable options
- **🎱 Magic 8-Ball** - Get mystical answers to your yes/no questions

##  Complete Deployment Guide

### Step 1: AWS EC2 Setup

1. **Launch EC2 Instance**
   - Instance Type: `t3.micro` (Free tier eligible)
   - AMI: Ubuntu Server 22.04 LTS
   - Security Group: Configure inbound rules for HTTP traffic

2. **Configure Security Group Inbound Rules**
   ```
   Type: Custom TCP Rule
   Port Range: 8000
   Source: 0.0.0.0/0 (or your IP for security)
   ```

3. **Connect to EC2 Instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-public-ip
   ```

### Step 2: Server Installation on EC2

1. **Install UV and Git**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   sudo apt update
   sudo apt install git -y
   ```

2. **Clone Repository**
   ```bash
   git clone https://github.com/suraj-yadav-aiml/streamable-http-mcp-example.git
   cd streamable-http-mcp-example
   ```

3. **Run the MCP Server**
   ```bash
   uv run server.py
   ```

4. **Server Output**
   ```
   INFO:     Started server process [27811]
   INFO:     Waiting for application startup.
   [09/29/25 15:15:49] INFO     StreamableHTTP session manager started
   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
   ```

### Step 3: Claude Desktop Integration

1. **Get EC2 Public IP**
   - Copy your EC2 instance's Public IPv4 address (e.g., `54.173.54.13`)

2. **Configure Claude Desktop**

   Open Claude Desktop settings and add the MCP server configuration:

   ```json
   {
     "mcpServers": {
       "streamable-http-mcp-example": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "http://YOUR_EC2_PUBLIC_IP:8000/mcp",
           "--allow-http"
         ]
       }
     }
   }
   ```

   Replace `YOUR_EC2_PUBLIC_IP` with your actual EC2 public IP address.

3. **Restart Claude Desktop**
   - Close and reopen Claude Desktop
   - The MCP tools will now be available in the interface

## Available Tools

### 1. Greeting Tool
**Function:** `greeting(name: str) -> str`
- Send personalized greetings
- **Example:** `greeting("Alice")` → `"Hi Alice!"`

### 2. Roll Dice Tool
**Function:** `roll_dice(sides: int = 6, count: int = 1) -> str`
- Roll customizable dice
- **Example:** `roll_dice(6, 3)` → `"🎲 Rolled 3 6-sided dice: [4, 2, 6] (Total: 12)"`

### 3. Generate Password Tool
**Function:** `generate_password(length: int = 12, include_symbols: bool = True) -> str`
- Generate secure passwords
- **Example:** `generate_password(16, True)` → `"🔐 Generated password: K7@mN9$pL2vXm4R"`

### 4. Magic 8-Ball Tool
**Function:** `magic_8_ball(question: str) -> str`
- Ask mystical questions
- **Example:** `magic_8_ball("Will it rain?")` → `"🎱 Question: Will it rain?\n🔮 Magic 8-Ball says: Signs point to yes"`

## Architecture Overview

```
┌─────────────────┐    HTTP Request     ┌─────────────────┐    MCP Protocol    ┌─────────────────┐
│  Claude Desktop │ ──────────────────► │   EC2 Instance  │ ─────────────────► │   MCP Server    │
│                 │                     │                 │                    │   (FastMCP)     │
│  mcp-remote     │ ◄────────────────── │  Public IP:8000 │ ◄───────────────── │   Tools         │
│  connector      │    HTTP Response    │                 │    Tool Results    │                 │
└─────────────────┘                     └─────────────────┘                    └─────────────────┘
```

**Key Components:**
- **Streamable HTTP Transport**: Enables real-time communication over HTTP
- **Remote MCP Connection**: Uses `mcp-remote` to connect Claude Desktop to remote server
- **AWS EC2 Hosting**: Provides scalable cloud infrastructure
- **FastMCP Framework**: Simplifies MCP server implementation

## Project Structure

```
streamable-http-mcp-example/
├── server.py          # Main MCP server with 4 tools
├── README.md          # This documentation
└── pyproject.toml     # UV project configuration
└── uv.lock
└── .gitignore
```

## Customization


### Adding Custom Tools
```python
@mcp.tool()
def my_custom_tool(param: str) -> str:
    """Your custom tool description."""
    return f"Custom response: {param}"
```

### Server Configuration
```python
# Modify host/port as needed
mcp = FastMCP("server", host="0.0.0.0", port=8000)
```

##  Troubleshooting

**Common Issues:**

1. **Connection Refused**
   - Check EC2 security group inbound rules
   - Verify server is running on correct port

2. **Tools Not Appearing**
   - Restart Claude Desktop after configuration
   - Check MCP server configuration syntax

3. **Server Startup Issues**
   - Ensure UV is properly installed
   - Check Python version compatibility



##  Contributing

Contributions welcome! Please feel free to submit issues and pull requests.

## License

This project is open source and available under the MIT License.

## Author

**Suraj Yadav**
- GitHub: [@suraj-yadav-aiml](https://github.com/suraj-yadav-aiml)
- Repository: [streamable-http-mcp-example](https://github.com/suraj-yadav-aiml/streamable-http-mcp-example)
