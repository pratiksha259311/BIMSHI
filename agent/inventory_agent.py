from typing import Dict, Any

class InventoryAgent:
    """
    InventoryAgent is responsible for:
    - Receiving the stock/quantity data
    - Deciding what needs to be reordered
    - Returning structured results for downstream agents
    """

    def __init__(self):
        pass

    def analyze_inventory(self, inventory_data: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Main logic for inventory analysis.

        Args:
            inventory_data: Example:
                {
                    "paracetamol": {"quantity": 12, "threshold": 20},
                    "dettol": {"quantity": 3, "threshold": 10}
                }

        Returns:
            {
                "to_reorder": [
                    {"item": "paracetamol", "need": 8},
                    {"item": "dettol", "need": 7}
                ],
                "status": "success"
            }
        """

        reorder_list = []

        for item, data in inventory_data.items():
            qty = data.get("quantity", 0)
            thr = data.get("threshold", 0)

            # Check if stock is low
            if qty < thr:
                reorder_list.append({
                    "item": item,
                    "need": thr - qty
                })

        return {
            "to_reorder": reorder_list,
            "status": "success"
        }

