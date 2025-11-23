class AnalyticsAgent:
    """
    Analytics Agent for BIMSHI.
    """
    def __init__(self, inventory):
        self.inventory = inventory

    def generate_insights(self):
        """
        Generate simple analytics insights for BIMSHI store.
        Returns a dictionary of key metrics and trends.
        """
        insights = {}
        total_items = sum(self.inventory.values())
        insights["Total Items in Store"] = total_items

        # Category-wise totals
        men_items = sum(qty for item, qty in self.inventory.items() if "Men" in item)
        women_items = sum(qty for item, qty in self.inventory.items() if "Women" in item)
        kids_items = sum(qty for item, qty in self.inventory.items() if "Kids" in item)

        insights["Men's Items"] = men_items
        insights["Women's Items"] = women_items
        insights["Kids' Items"] = kids_items

        # Fast-selling vs slow-selling (simple threshold)
        fast_selling = [item for item, qty in self.inventory.items() if qty <= 20]
        slow_selling = [item for item, qty in self.inventory.items() if qty > 40]

        insights["Fast-Selling Items (<=20 pcs)"] = ", ".join(fast_selling) if fast_selling else "None"
        insights["Slow-Selling Items (>40 pcs)"] = ", ".join(slow_selling) if slow_selling else "None"

        # Simple restocking recommendation
        restock_items = [item for item, qty in self.inventory.items() if qty < 15]
        insights["Restock Recommendation (<15 pcs)"] = ", ".join(restock_items) if restock_items else "None"

        return insights


