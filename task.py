import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('chocolate_house.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    is_seasonal BOOLEAN NOT NULL,
    allergy_info TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    flavor_suggestion TEXT NOT NULL,
    allergy_concern TEXT
)
''')

conn.commit()

# Function to add a seasonal flavor
def add_flavor(name, is_seasonal, allergy_info):
    cursor.execute('''
    INSERT INTO flavors (name, is_seasonal, allergy_info)
    VALUES (?, ?, ?)
    ''', (name, is_seasonal, allergy_info))
    conn.commit()
    print(f'Flavor "{name}" added!')

# Function to view all flavors
def view_flavors():
    cursor.execute('SELECT * FROM flavors')
    for row in cursor.fetchall():
        print(row)

# Function to add an ingredient to inventory
def add_ingredient(ingredient, quantity):
    cursor.execute('''
    INSERT INTO inventory (ingredient, quantity)
    VALUES (?, ?)
    ''', (ingredient, quantity))
    conn.commit()
    print(f'Ingredient "{ingredient}" added with quantity {quantity}!')

# Function to view inventory
def view_inventory():
    cursor.execute('SELECT * FROM inventory')
    for row in cursor.fetchall():
        print(row)

# Function to submit a flavor suggestion
def submit_suggestion(customer_name, flavor_suggestion, allergy_concern):
    cursor.execute('''
    INSERT INTO suggestions (customer_name, flavor_suggestion, allergy_concern)
    VALUES (?, ?, ?)
    ''', (customer_name, flavor_suggestion, allergy_concern))
    conn.commit()
    print(f'Suggestion from "{customer_name}" submitted!')

# Main application loop
def main():
    while True:
        print("\nChocolate House Management System")
        print("1. Add Seasonal Flavor")
        print("2. View All Flavors")
        print("3. Add Ingredient to Inventory")
        print("4. View Inventory")
        print("5. Submit Flavor Suggestion")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter flavor name: ")
            is_seasonal = input("Is it seasonal? (yes/no): ").lower() == 'yes'
            allergy_info = input("Enter allergy information (if any): ")
            add_flavor(name, is_seasonal, allergy_info)

        elif choice == '2':
            print("All Flavors:")
            view_flavors()

        elif choice == '3':
            ingredient = input("Enter ingredient name: ")
            quantity = int(input("Enter quantity: "))
            add_ingredient(ingredient, quantity)

        elif choice == '4':
            print("Inventory:")
            view_inventory()

        elif choice == '5':
            customer_name = input("Enter customer name: ")
            flavor_suggestion = input("Enter flavor suggestion: ")
            allergy_concern = input("Enter allergy concern (if any): ")
            submit_suggestion(customer_name, flavor_suggestion, allergy_concern)

        elif choice == '6':
            print("Exiting the application...")
            break

        else:
            print("Invalid option. Please try again.")

# Run the application
if __name__ == "__main__":
    main()

# Close the database connection at the end
conn.close()
