class SalesPerson:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.sales = []

    # Getters
    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    def get_sales(self):
        return self.sales

    # Setters
    def set_name(self, name):
        self.name = name

    def set_title(self, title):
        self.title = title

    def add_sale(self, sale):
        self.sales.append(sale)

    # Iterator implementation
    def __iter__(self):
        return iter(self.sales)

    # Calculate total sales
    def get_total_sales(self):
        return sum(self.sales)

    # Calculate minimum sales
    def get_min_sales(self):
        return min(self.sales) if self.sales else 0

    # Calculate maximum sales
    def get_max_sales(self):
        return max(self.sales) if self.sales else 0

    # Calculate average sales
    def get_average_sales(self):
        return self.get_total_sales() / len(self.sales) if self.sales else 0


def generate_sales_report(sales_people):
    company_total = 0

    print("\n----- Sales Report -----")

    for person in sales_people:
        print(f"\nSalesperson: {person.get_name()}")
        print(f"Title: {person.get_title()}")

        print("Sales Figures (using iterator):")
        for sale in person:
            print(f"  {sale}")

        total_sales = person.get_total_sales()
        min_sales = person.get_min_sales()
        max_sales = person.get_max_sales()
        average_sales = person.get_average_sales()

        print(f"Total Sales: {total_sales}")
        print(f"Minimum Sale: {min_sales}")
        print(f"Maximum Sale: {max_sales}")
        print(f"Average Sales: {average_sales}")

        company_total += total_sales

    print(f"\nTotal Sales for the Company: {company_total}")
    print("------------------------")


if __name__ == "__main__":
    sales_people = []

    # Get input for 3 salespeople, including "Randall"
    for i in range(3):
        if i == 0:
            name = "Randall"
            title = "Senior Sales Associate"  # Example title
        else:
            name = input(f"Enter name for salesperson {i + 1}: ")
            title = input(f"Enter title for salesperson {i + 1}: ")

        person = SalesPerson(name, title)

        print(f"Enter at least 3 sales figures for {name}:")
        for j in range(3):
            sale = float(input(f"  Sale {j + 1}: "))
            person.add_sale(sale)

        sales_people.append(person)

    # Generate sales report
    generate_sales_report(sales_people)