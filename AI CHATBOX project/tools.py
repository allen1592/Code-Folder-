from abc import ABC, abstractmethod
from typing import Dict, Any
import aiohttp

class BaseTool(ABC):
    name: str

    @abstractmethod
    async def execute(self, **kwargs) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


# 🔹 Example Tool: Fake CPU API (demo)
class CPUTool(BaseTool):
    name = "cpu_check"

    async def execute(self, device: str = "router1") -> Dict[str, Any]:
        # giả lập API
        return {
            "device": device,
            "cpu": "75%",
            "status": "high"
        }

    def get_description(self) -> str:
        return "Check CPU usage of device"