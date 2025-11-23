# AnalyticsAgent: Processes BIMSHI store data to generate insights,
# demand trends, product performance, and simple restocking predictions.
class AnalyticsAgent:
    """
    Analytics Agent for BIMSHI.
    Generates insights on sales, stock levels, category performance,
    and predicts restocking needs using simple heuristic rules.
    """

    def __init__(self, inventory_data, sales_data):
        self.inventory_data = inventory_data   # {item: quantity}
        self.sales_data = sales_data           # {item: units_sold}

    def top_selling_items(self, top_n=5):
        sorted_items = sorted(self.sales_data.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[:top_n]

    def low_stock_items(self, threshold=10):
        return {item: qty for item, qty in self.inventory_data.items() if qty < threshold}

    def demand_prediction(self):
        """Simple prediction: if sold units > remaining stock → needs restock"""
        prediction = {}
        for item, sold in self.sales_data.items():
            stock = self.inventory_data.get(item, 0)
            if sold > stock:
                prediction[item] = "High demand – restock needed soon"
            elif sold == 0:
                prediction[item] = "No demand – review item"
            else:
                prediction[item] = "Stable"
        return prediction

    def category_performance(self, category_map):
        """
        category_map example:
        { 'Sweaters': ['Men Sweater', 'Women Sweater'], 'Kids': ['Kids Hoodie'] }
        """
        category_sales = {}
        for category, items in category_map.items():
            category_sales[category] = sum(self.sales_data.get(i, 0) for i in items)
        return category_sales

    def generate_summary(self):
        return {
            "top_sellers": self.top_selling_items(),
            "low_stock": self.low_stock_items(),
            "demand_prediction": self.demand_prediction(),
        }

