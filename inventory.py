# MY VERSION

def calculate_total_cost():
    """"Calculate total cost of a product based on information gave by the user"""
    try:
        # Product info gave it by the user
        name: str = input("Enter product name: ")
        price: float = float(input("Enter product price: "))
        quantity: int = int(input("Enter product quantity: "))

        # Calculate total
        total_cost = price * quantity

        # Return value in a nice format
        return f"\nProuct info\n{"-"*20}\nProduct: {name}\nPrice: {price}\nQuantity: {quantity}\n{"-"*20}\nTotal cost: {total_cost: .0f}\n{"-"*20}\n"
    
    # Handle exception if not there number
    except ValueError:
        print("You must enter just numbers")

# Call of the function
print(calculate_total_cost())

# -----------------------------------------------------------------------------------------------------------------------------------------------------

# CHATGPT VERSION

def calculate_total_cost() -> str:
    """Calculate total cost of a product with input validation and styled output."""
    
    # Ask for product name
    name = input("🛍️ Enter product name: ").strip()
    while not name:
        name = input("⚠️ Product name cannot be empty. Please try again: ").strip()

    # Ask for product price
    while True:
        try:
            price = float(input("💰 Enter product price: "))
            if price <= 0:
                print("⚠️ Price must be greater than zero.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number for the price.")

    # Ask for quantity
    while True:
        try:
            quantity = int(input("📦 Enter product quantity: "))
            if quantity <= 0:
                print("⚠️ Quantity must be greater than zero.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid integer for quantity.")

    # Calculate total
    total_cost = price * quantity

    # Pretty output
    summary = (
        f"\n🧾 PURCHASE SUMMARY\n"
        f"{'-'*25}\n"
        f"📘 Product: {name}\n"
        f"💵 Price: ${price:,.2f}\n"
        f"🔢 Quantity: {quantity}\n"
        f"{'-'*25}\n"
        f"✅ Total Cost: ${total_cost:,.2f}\n"
    )

    return summary

# Run the function
# print(calculate_total_cost())

# SUMMARY OF IMPROVEMENTS

# | Problem                  | Fix                                                 |
# | ------------------------ | --------------------------------------------------- |
# | Mixed logic & validation | Split into clear input loops                        |
# | No type hint on function | Added `-> str` for clarity                          |
# | Weak validation          | Added checks for empty, negative, or invalid values |
# | Poor UI readability      | Styled output with emojis, lines, and formatting    |
# | Inconsistent formatting  | Used f-string formatting for consistent results     |

