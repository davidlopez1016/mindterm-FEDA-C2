from phone.directory import Directory

directory = Directory()

directory.add_contact("Alice", "Smith", "TechCorp", "12345", "Street1, CityA")
directory.add_contact("Bob", "Johnson", "Innovate Inc.", "67890", "Avenue2, CityB")
directory.add_contact("Carol", "Brown", "Creative LLC", "54321", "Street3, CityC")

directory.list_contacts()