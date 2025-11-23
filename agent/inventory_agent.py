# InventoryAgent: Manages BIMSHI store inventory

class InventoryAgent:
    """
    InventoryAgent is responsible for:
    - Receiving the stock/quantity data
    - Updating stock
    - Returning the current inventory
    """

    def __init__(self, inventory):
        self.inventory = inventory

    def update_stock(self, item_name, quantity):
        """
        Updates the stock of an item. Adds quantity if exists, else creates new entry.
        """
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
