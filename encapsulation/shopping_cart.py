class ShoppingCart:
    def __init__(self):
        self._items: dict[str, float] = {}
        self._discount_applied = False
        self._is_checked_out = False

    def add_item(self, name: str, price: float) -> None:
        if self._is_checked_out:
            print("Cannot modify a check-out cart")
            return
        self._items[name] = price

    def apply_discount(self, code: str) -> bool:
        if code == "SAVE10" and not self._discount_applied and not self._is_checked_out:
            self._discount_applied = True
            return True
        return False

    def get_total(self) -> float:
        total = sum(self._items.values())
        if self._discount_applied:
            total *= 0.9
        return round(total, 2)

    def checkout(self) -> None:
        if self._items and not self._is_checked_out:
            self._is_checked_out = True

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 999.99)
    cart.add_item("Mouse", 29.99)

    print(f"Total: ${cart.get_total():.2f}")                     # 1029.98

    print(f"Discount: {str(cart.apply_discount('SAVE10')).lower()}")          # true
    print(f"Total: ${cart.get_total():.2f}")                     # 926.98

    print(f"Discount: {str(cart.apply_discount('SAVE10')).lower()}")          # false

    cart.checkout()
    cart.add_item("Keyboard", 79.99)  # Should be rejected
    print(f"Total: ${cart.get_total():.2f}") 