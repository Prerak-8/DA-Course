import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:
    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)

            required_columns = ["Date", "Product", "Category", "Price", "Quantity Sold", "Total Sales"]

            for column in required_columns:
                if column not in self.data.columns:
                    print("Missing column:", column)
                    return False

            missing_values = self.data.isnull().sum().sum()

            if missing_values > 0:
                print("Missing values found.")
                self.data = self.data.dropna()
            else:
                print("No missing values found.")

            self.data["Date"] = pd.to_datetime(self.data["Date"])

            return True

        except FileNotFoundError:
            print("File not found.")
            return False

        except Exception as e:
            print("Error loading file:", e)
            return False

    def calculate_metrics(self):
        if self.data is None:
            print("No data has been loaded. Please load a dataset.")
            return

        total_sales = self.data["Total Sales"].sum()
        average_sales = np.mean(self.data["Total Sales"])

        self.data["Sales Percentage"] = (self.data["Total Sales"] / total_sales) * 100

        print("\n--- Sales Metrics ---\n")
        print("Total sales:", round(total_sales, 3))
        print("Average sales:", round(average_sales, 3))

    def filter_data(self, condition):
        if self.data is None:
            print("No data has been loaded. Please load a dataset.")

        filtered_data = self.data[self.data["Category"].str.lower() == condition.lower()]

        if len(filtered_data) == 0:
            print("No records found.")
        else:
            print("\nFiltered Data:")
            print(filtered_data)

    def display_summary(self):
        if self.data is None:
            print("No data has been loaded. Please load a dataset.")
            return

        print("\n**** Dataset Summary ****\n")
        print(self.data.describe())

        print("\nSales by category:")
        print(self.data.groupby("Category")["Total Sales"].sum())

    def visulaize_data(self):
        if self.data is None:
            print("No data has been loaded. Please load a dataset.")
            return

        category_sales = self.data.groupby("Category")["Total Sales"].sum()

        category_sales.plot(kind = "bar")
        plt.title("Total Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.tight_layout()
        plt.show()

        daily_sales = self.data.groupby("Date")["Total Sales"].sum()

        daily_sales.plot(kind = "line", marker = "o")
        plt.title("Sales Trend over Time")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.tight_layout()
        plt.show()

        num_data = self.data[["Price", "Quantity Sold", "Total Sales"]]

        sns.heatmap(num_data.corr(), annot = True)
        plt.title("Sales Correlation Heatmap")
        plt.tight_layout()
        plt.show()

file_name = input("Enter CSV file name: ")
print()

analyzer = RetailAnalyzer()

if analyzer.load_data(file_name):
    analyzer.calculate_metrics()
    analyzer.display_summary()

    category = input("\nEnter a category to filter: ")
    analyzer.filter_data(category)
    analyzer.visulaize_data()