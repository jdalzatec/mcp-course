import asyncio
import json
from typing import TypedDict, List, Dict

from huggingface_hub import Agent


class AgentConfig(TypedDict):
    model: str
    provider: str
    servers: List[Dict]


def load_agent_config(config_path: str = "agent.json") -> AgentConfig:
    with open(config_path, "r") as f:
        return json.load(f)


async def main():
    agent_config = load_agent_config()
    async with Agent(
        model=agent_config["model"],
        provider=agent_config["provider"],
        servers=agent_config["servers"],
    ) as agent:
        await agent.load_tools()
        tools = agent.available_tools
        for tool in tools:
            print(f"-> {tool.function.name}: {tool.function.description}")

        result = agent.run("What is the sentiment of the following text: 'I love you'")
        async for chunk in result:
            if hasattr(chunk, "role") and chunk.role == "tool":
                print(chunk.content)


if __name__ == "__main__":
    asyncio.run(main())
