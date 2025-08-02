# AI for QA

## Getting Started

### Things to remember:

1. LLM (Large Language Model)
    - AI trained on massive text data to understand and generate human language
    - Text in => Text out
    - Learns patterns from billions of text examples
    - Understands the context
2. AI Agent = LLM + Tools + Autonomy
    - An AI Agent is an autonomous system that perceives its environment, makes decisions and takes actions to achieve specific goals
    - Goal Oriented
    - Tool Access
    - Decision-Making
    - Iterative Execution

| Traditional LLM      | AI Agents                     |
|----------------------|-------------------------------|
| Text in -> Text out  | Text in -> Actions -> Results |
| Passive responder    | Active problem solver         |
| No external access   | Connected to tools/systems    |
| One-shot interaction | Multi-step reasoning          |

🧠 LLM (Brain) + 🔧Tools (Hands) + 🤖 Autonomy (Decision Making)

3. MCP (Model Context Protocol)
    - Claude
        - Download Desktop App
        - Goto settings of claude
        - Click on Developers
        - Click on edit configurations
        - Opens the configration file path
        - Now choose the desired MCP server from "[smithery](https://smithery.ai/)"
        - Copy the JSON and Paste it into Claude configuration JSON
        - Now you can notice those tools inside the Claude

4. Multi-Agent workflow Patterns
    1. Sequential Workflow
    2. Parallel Workflow
    3. Hierarchical Workflow
    4. Collaborative Workflow

5. Agentic AI
    - Agentic AI refers to AI systems that can autonomously take actions and make decisions to achieve goals, rather than just responding to prompts
    - Installation
      - Install Python
      - Install IDE - PyCharm Community Edition
      - Install packages using PIP command
        - Navigate to "[AutoGen](https://microsoft.github.io/autogen/stable//user-guide/agentchat-user-guide/installation.html)"
        - Install ```pip install -U "autogen-agentchat"```
        - Install ``` pip install "autogen-ext[openai]"```
        - Install ```pip install -U "autogen-ext[mcp]"```


| Traditional AI       | Agentic AI           |
|----------------------|----------------------|
| Answer this question | Solves the problem   |
| Single Interaction   | Multi-step execution |
| Reactive             | Proactive            |
| Human-guided         | Self-directed        |
| Tool less            | Tool enabled         |

