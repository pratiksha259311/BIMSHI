# Orchestrator: Connects InventoryAgent & AnalyticsAgent to process data.
# Loads inventory, updates stock, generates insights, and simulates BIMSHI logic.

import json
from .inventory_agent import InventoryAgent
from .analytics_agent import AnalyticsAgent


class Orchestrator:
    """
    Orchestrator for BIMSHI.

    Responsibilities:
    - Load inventory from data file
    - Use InventoryAgent to manage stock operations
    - Use AnalyticsAgent to generate insights
    - Provide a clean interface for Streamlit or other apps to call
    """

    def __init__(self, inventory_path="agent/data/inventory.json"):
        self.inventory_path = inventory_path
        self.inventory = self.load_inventory()
        self.inventory_agent = InventoryAgent(self.inventory)
        self.analytics_agent = AnalyticsAgent(self.inventory)

    def load_inventory(self):
        """Loads inventory JSON file."""
        with open(self.inventory_path, "r") as f:
            return json.load(f)

    def update_stock(self, item_name, quantity):
        """Update stock using InventoryAgent."""
        self.inventory_agent.update_stock(item_name, quantity)
        self.save_inventory()

    def save_inventory(self):
        """Save updated inventory back to JSON."""
        with open(self.inventory_path, "w") as f:
            json.dump(self.inventory_agent.inventory, f, indent=4)

    def get_insights(self):
        """Generate analytics insights."""
        return self.analytics_agent.generate_insights()

    def get_inventory(self):
        """Return current inventory."""
        return self.inventory_agent.inventory


