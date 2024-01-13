# Constants
kerf_in_inches = 0.067  # Default kerf width in inches
min_index_length_in_inches = 3  # Default minimum index length in inches

# Function to calculate the number of parts and drop length from stock length
def calculate_parts_and_drop(stock_length, part_length, kerf, min_index):
    working_stock_length = stock_length - min_index
    working_part_length = part_length + kerf
    part_count = int(working_stock_length / working_part_length)
    used_length = part_count * working_part_length
    drop_length = stock_length - used_length
    return part_count, drop_length

# Settings menu
def settings_menu():
    global kerf_in_inches, min_index_length_in_inches
    kerf_in_inches = float(input("kerf (in):"))
    min_index_length_in_inches = float(input("Index (in):"))

# Function to show credits
def show_credits():
    print("Credits:")
    print("Dev: James Slater")
    print("Help: ChatGPT-4")
    print("From: OpenAI")
    input("Press any key...")

# Main program with menu
def main_menu():
    while True:
        print("\\nMain Menu")
        print("1. Calculate")
        print("2. Settings")
        print("3. Credits")
        print("4. Exit")
        choice = input("Choice: ")

        if choice == '1':
            stock_length = float(input("Stock (in): "))
            part_length = float(input("Part (in): "))
            part_count, drop_length = calculate_parts_and_drop(stock_length, part_length, kerf_in_inches, min_index_length_in_inches)
            print("Parts: {}".format(part_count))
            print("Drop: {:.4f}".format(drop_length))

            while True:
                user_choice = input("'1' Main '2' Exit:").upper()
                if user_choice == '1':
                    break
                elif user_choice == '2':
                    print("Exiting program.")
                    return(0)
                else:
                    print("'1' Main")
                    print("'2' Exit.")

        elif choice == '2':
            settings_menu()

        elif choice == '3':
            show_credits()

        elif choice == '4':
            print("Exiting program.")
            return(0)

main_menu()
