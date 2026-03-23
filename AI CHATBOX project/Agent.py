import asyncio
import json
from dataclasses import dataclass, field
from typing import Any, Dict, List
from enum import Enum

from llm_client import LLMClient
from tools import BaseTool, CPUTool


# ===== STATE =====
class AgentState(Enum):
    IDLE = "idle"
    THINKING = "thinking"
    EXECUTING = "executing"


# ===== TASK =====
@dataclass
class Task:
    description: str
    priority: int = 1
    context: Dict[str, Any] = field(default_factory=dict)
    dependencies: List[str] = field(default_factory=list)


# ===== AGENT =====
class AIAgent:
    def __init__(self, name: str, llm_model=None):
        self.name = name
        self.llm = llm_model
        self.tools: List[BaseTool] = []
        self.task_queue = asyncio.Queue()
        self.current_state = AgentState.IDLE

        self.memory = []
        self.max_memory = 50

    def add_tool(self, tool: BaseTool):
        self.tools.append(tool)

    async def think(self, task: Task) -> Dict[str, Any]:
        SYSTEM_PROMPT = """
You are an AI agent.

Return STRICT JSON:
{
  "action": "tool" | "response",
  "analysis": "...",
  "recommendation": "...",
  "tool_name": "...",
  "params": {}
}
"""

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": json.dumps({
                    "task": task.description,
                    "context": task.context
                })
            }
        ]

        response = await self.llm.chat(messages)

        try:
            return json.loads(response)
        except Exception:
            return {
                "action": "response",
                "analysis": response,
                "recommendation": response
            }

    async def execute_tool(self, tool_name: str, **kwargs):
        for tool in self.tools:
            if tool.name == tool_name:
                return await tool.execute(**kwargs)
        raise ValueError(f"Tool {tool_name} not found")

    async def execute_plan(self, plan: Dict[str, Any]):
        action = plan.get("action")

        if action == "tool":
            return await self.execute_tool(
                plan.get("tool_name"),
                **plan.get("params", {})
            )

        elif action == "response":
            return plan.get("recommendation")

        return "Unknown action"

    async def run(self):
        while True:
            task = await self.task_queue.get()

            print(f"\n[TASK] {task.description}")

            self.current_state = AgentState.THINKING
            plan = await self.think(task)

            print(f"[PLAN] {plan}")

            self.current_state = AgentState.EXECUTING
            result = await self.execute_plan(plan)

            print(f"[RESULT] {result}")

            self.memory.append({
                "task": task.description,
                "result": result
            })

            if len(self.memory) > self.max_memory:
                self.memory.pop(0)

            self.current_state = AgentState.IDLE


# ===== MAIN TEST =====
async def main():
    agent = AIAgent("local-agent", llm_model=LLMClient())

    # add tool
    agent.add_tool(CPUTool())

    # start agent loop
    asyncio.create_task(agent.run())

    # input loop
    while True:
        q = input("\nYou: ")
        if q == "exit":
            break

        await agent.task_queue.put(Task(description=q))


if __name__ == "__main__":
    asyncio.run(main())
