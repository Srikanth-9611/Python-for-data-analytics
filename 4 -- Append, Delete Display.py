class ListManager:
    def __init__(self):
        self.elements = []
    def append_element(self, element):
        self.elements.append(element)
        print(f"{element} has been added to the list.")
    def delete_element(self, element):
        if element in self.elements:
            self.elements.remove(element)
            print(f"{element} has been removed from the list.")
        else:
            print(f"{element} is not in the list.")
    def display_elements(self):
        if self.elements:
            print("Current elements in the list:", self.elements)
        else:
            print("The list is currently empty.")
        
def menu():
    list_manager = ListManager()
    while True:
        print("\nMenu:")
        print("1. Append an element")
        print("2. Delete an element")
        print("3. Display elements")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            element = input("Enter an element to append: ")
            list_manager.append_element(element)
        elif choice == '2':
            element = input("Enter an element to delete: ")
            list_manager.delete_element(element)
        elif choice == '3':
            list_manager.display_elements()
        elif choice == '4':
            print("Exiting the program.")
        break
# Run the menu
menu()