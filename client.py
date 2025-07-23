import gradio as gr
import os
import time
import traceback

from smolagents import CodeAgent, LiteLLMModel, MCPClient


def safe_agent_run(message: str, _: list) -> str:
    """Safely run the agent with timeout and error handling."""
    try:
        print(f"Processing message: {message}")
        start_time = time.time()
        result = agent.run(message)
        elapsed_time = time.time() - start_time
        print(f"Agent completed in {elapsed_time:.2f} seconds")

        return str(result)
    except Exception as e:
        error_msg = (
            f"Error running agent: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
        )
        print(error_msg)
        return error_msg


try:
    print("Initializing MCP client...")
    mcp_client = MCPClient(
        {
            "url": "https://abidlabs-mcp-tool-http.hf.space/gradio_api/mcp/sse",
            "transport": "sse",
        }
    )

    print("Getting tools...")
    tools = mcp_client.get_tools()
    print(f"Found {len(tools)} tools")

    print("Tools:")
    for tool in tools:
        print(f"-> {tool.name}: {tool.description}")

    print("Initializing model...")
    model = LiteLLMModel(
        model_id="openai/gpt-4o",
        temperature=0.2,
        max_tokens=2000,
        requests_per_minute=60,
        api_key=os.environ["OPENAI_API_KEY"],
    )

    print("Creating agent...")
    agent = CodeAgent(
        tools=[*tools],
        model=model,
    )

    print("Setting up Gradio interface...")
    demo = gr.ChatInterface(
        fn=safe_agent_run,
        type="messages",
        examples=["Give me the prime factorization of 68"],
        title="Agent with MCP Tools",
        description="This is a simple agent that uses MCP tools to answer questions.",
    )

    print("Launching demo...")
    demo.launch()
finally:
    print("Cleaning up...")
    mcp_client.disconnect()
