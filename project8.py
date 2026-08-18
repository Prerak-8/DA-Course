import numpy as np

print("==============================")
print("Welcome to the Numpy Analyzer!")
print("==============================\n")

class DataAnalytics:

    def __init__(self):
        self.original_array = []
        self.__current_array = None

    @classmethod
    def project_name(cls):
        print("Numpy Analyzer")

    @staticmethod
    def input_hint():
        print("Enter integers separated by spaces.")

    def create_1d_array(self):
        elements = int(input("Enter number of elements: "))
        print()

        data = list(map(int, input(f"Enter {elements} elements separated by space: ").split()))
        print()

        if len(data) != elements:
            print("Wrong number of elements.\n")
            return
        else:
            self.__current_array = np.array(data)
            self.original_array.append(self.__current_array)
            print("1D Array created successfully:\n", self.__current_array, "\n")

        mode = input("index or slice? : ").lower()

        if mode == "index":
            idx = int(input("Enter index: "))
            print("\nElement:", self.__current_array[idx], "\n")

        elif mode == "slice":
            start = int(input("Slice start: "))
            end = int(input("Slice end: "))
            print("\nSlice:", self.__current_array[start:end], "\n")

    def create_2d_array(self):
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
        print()

        elements = rows * columns
        data = list(map(int, input(f"Enter {elements} elements separated by space: ").split()))
        print()

        if len(data) != elements:
            print("Wrong number of elements.\n")
            return
        else:
            self.__current_array = np.array(data).reshape(rows, columns)
            self.original_array.append(self.__current_array)
            print("2D Array created successfully:\n", self.__current_array, "\n")

        mode = input("index or slice? : ").lower()

        if mode == "index":
            row = int(input("Row index: "))
            col = int(input("Column index: "))
            print("\nElement:", self.__current_array[row, col], "\n")

        elif mode == "slice":
            row1 = int(input("Row start: "))
            row2 = int(input("Row end: "))
            col1 = int(input("Column start: "))
            col2 = int(input("Column end: "))
            print("\nSlice:\n", self.__current_array[row1:row2, col1:col2], "\n")

    def create_3d_array(self):
        layers = int(input("Enter number of layers: "))
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
        print()

        elements = layers * rows * columns
        data = list(map(int, input(f"Enter {elements} elements separated by space: ").split()))
        print()

        if len(data) != elements:
            print("Wrong number of elements.\n")
            return
        else:
            self.__current_array = np.array(data).reshape(layers, rows, columns)
            self.original_array.append(self.__current_array)
            print("3D Array created successfully:\n", self.__current_array, "\n")

        mode = input("index or slice? : ").lower()

        if mode == "index":
            dep = int(input("Depth index: "))
            row = int(input("Row index: "))
            col = int(input("Column index: "))
            print("\nElement:", self.__current_array[dep, row, col], "\n")

        elif mode == "slice":
            dep1 = int(input("Depth start: "))
            dep2 = int(input("Depth end: "))
            row1 = int(input("Row start: "))
            row2 = int(input("Row end: "))
            col1 = int(input("Column start: "))
            col2 = int(input("Column end: "))
            print("\nSlice:\n", self.__current_array[dep1:dep2, row1:row2, col1:col2], "\n")

    def addition(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        input_math = list(map(int, input(f"Enter {self.__current_array.size} elements for second array separated by space: ").split()))
        print()

        if len(input_math) != self.__current_array.size:
            print("Wrong number of elements.\n")
        else:
            second_arr = np.array(input_math).reshape(self.__current_array.shape)
            print("Original array:\n", self.__current_array)
            print("Second array:\n", second_arr)
            print("Result of addition:\n", np.add(self.__current_array, second_arr), "\n")

    def subtraction(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        input_math = list(map(int, input(f"Enter {self.__current_array.size} elements for second array separated by space: ").split()))
        print()
        
        if len(input_math) != self.__current_array.size:
            print("Wrong number of elements.\n")
        else:
            second_arr = np.array(input_math).reshape(self.__current_array.shape)
            print("Original array:\n", self.__current_array)
            print("Second array:\n", second_arr)
            print("Result of subtraction:\n", np.subtract(self.__current_array, second_arr), "\n")

    def multiplication(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        input_math = list(map(int, input(f"Enter {self.__current_array.size} elements for second array separated by space: ").split()))
        print()
        
        if len(input_math) != self.__current_array.size:
            print("Wrong number of elements.\n")
        else:
            second_arr = np.array(input_math).reshape(self.__current_array.shape)
            print("Original array:\n", self.__current_array)
            print("Second array:\n", second_arr)
            print("Result of multiplication:\n", np.multiply(self.__current_array, second_arr), "\n")

    def division(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        input_math = list(map(int, input(f"Enter {self.__current_array.size} elements for second array separated by space: ").split()))
        print()
        
        if len(input_math) != self.__current_array.size:
            print("Wrong number of elements.\n")
        else:
            second_arr = np.array(input_math).reshape(self.__current_array.shape)
            print("Original array:\n", self.__current_array)
            print("Second array:\n", second_arr)
            print("Result of division:\n", np.divide(self.__current_array, second_arr), "\n")

    def array_combine(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        input_combine = list(map(int, input(f"Enter the elements of another array to combine ( {self.__current_array.size} elements separated by space): ").split()))
        print()

        if len(input_combine) != self.__current_array.size:
            print("Wrong number of elements.\n")
        else:
            second_arr = np.array(input_combine).reshape(self.__current_array.shape)
            print("Original array:\n", self.__current_array)
            print("Second array:\n", second_arr)
            print("Vertical stack:\n", np.vstack((self.__current_array, second_arr)), "\n")
            print("Horizontal stack:\n", np.hstack((self.__current_array, second_arr)), "\n")

    def array_split(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        print("Original array:\n", self.__current_array)
        print("Split array:\n", np.array_split(self.__current_array, 2), "\n")

    def search_value(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        value = int(input("Enter value to search: "))
        result = np.where(self.__current_array == value)

        if result[0].size == 0:
            print("Value not found.\n")
        else:
            print("Search result:", result, "\n")

    def sort_array(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        print("Sorted array:", np.sort(self.__current_array, axis=None), "\n")

    def filter_values(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        threshold = int(input("Enter threshold value: "))
        flat = self.__current_array.flatten()
        print("Filtered values:", flat[flat > threshold], "\n")

    def sum_values(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        print("Sum:", np.sum(self.__current_array), "\n")

    def mean_values(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        print("Mean:", np.mean(self.__current_array), "\n")

    def median_values(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        print("Median:", np.median(self.__current_array), "\n")

    def std_values(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        print("Standard Deviation:", np.std(self.__current_array), "\n")

    def variance_values(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        print("Variance:", np.var(self.__current_array), "\n")

    def min_max_values(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        print("Minimum:", np.min(self.__current_array))
        print("Maximum:", np.max(self.__current_array), "\n")

    def percentile_values(self):
        if self.__current_array is None:
            print("Create an array first.\n")
            return

        percentile = float(input("Enter percentile value (0-100): "))
        print(f"{percentile}th Percentile:", np.percentile(self.__current_array, percentile), "\n")

analytics = DataAnalytics()

while True:
    print("Choose an option:") 
    print("1. Create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit\n")

    choice = int(input("Enter your choice: "))
    print()

    match choice:
        case 1:
            while True:
                print("Select the type of array to create:")
                print("1. 1D Array")
                print("2. 2D Array")
                print("3. 3D Array")
                print("4. Back to Main Menu\n")

                choice_array = int(input("Enter your choice: "))
                print()

                match choice_array:
                    case 1:
                        arr_1d = analytics
                        arr_1d.create_1d_array() 

                    case 2:
                        arr_2d = analytics
                        arr_2d.create_2d_array()

                    case 3:
                        arr_3d = analytics
                        arr_3d.create_3d_array()

                    case 4:
                        break

                    case _:
                        print("Invalid choice entered. Please enter a valid choice.\n")

        case 2:
            while True:
                print("Choose a mathematical operation:")
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. Back to Main Menu\n")

                choice_math = int(input("Enter your choice: "))
                print()

                match choice_math:
                    case 1:
                        math_add = analytics
                        math_add.addition()

                    case 2:
                        math_sub = analytics
                        math_sub.subtraction()

                    case 3:
                        math_mul = analytics
                        math_mul.multiplication()

                    case 4:
                        math_div = analytics
                        math_div.division()

                    case 5:
                        break

                    case _:
                        print("Invalid choice entered. Please enter a valid choice.\n")

        case 3:
            while True:
                print("Choose an option:")
                print("1. Combine Arrays")
                print("2. split Array")
                print("3. Back to Main Menu\n")

                choice_combine_split = int(input("Enter your choice: "))
                print()
                
                match choice_combine_split:
                    case 1:
                        combine_arr = analytics
                        combine_arr.array_combine()
                
                    case 2:
                        split_arr = analytics
                        split_arr.array_split()
                
                    case 3:
                        break
                
                    case _:
                        print("Invalid choice entered. Please enter a valid choice.\n")

        case 4:
            while True:
                print("Choose an option:")
                print("1. Search a value")
                print("2. Sort the array")
                print("3. Filter values")
                print("4. Back to Main Menu\n")

                choice_search_sort_filter = int(input("Enter your choice: "))
                print()
                
                match choice_search_sort_filter:
                    case 1:
                        search_arr = analytics
                        search_arr.search_value()
                
                    case 2:
                        sort_arr = analytics
                        sort_arr.sort_array()
                
                    case 3:
                        filter_arr = analytics
                        filter_arr.filter_values()
                
                    case 4:
                        break
                
                    case _:
                        print("Invalid choice entered. Please enter a valid choice.\n")

        case 5:
            while True:
                print("Choose an aggregate/ statistical operation:")
                print("1. Sum")
                print("2. mean")
                print("3. Median")
                print("4. Standard Deviation")
                print("5. Variance")
                print("6. Minimum and Maximum")
                print("7. Percentile")
                print("8. Back to Main Menu\n")

                choice_aggregate_statistics = int(input("Enter your choice: "))
                print()
                
                match choice_aggregate_statistics:
                    case 1:
                        operation_sum = analytics
                        operation_sum.sum_values()
                
                    case 2:
                        operation_mean = analytics
                        operation_mean.mean_values()
                
                    case 3:
                        operation_median = analytics
                        operation_median.median_values()
                
                    case 4:
                        operation_std_div = analytics
                        operation_std_div.std_values()
                
                    case 5:
                        operation_variance = analytics
                        operation_variance.variance_values()

                    case 6:
                        operation_min_max = analytics
                        operation_min_max.min_max_values()

                    case 7:
                        operation_percentile = analytics
                        operation_percentile.percentile_values()

                    case 8:
                        break

                    case _:
                        print("Invalid choice entered. Please enter a valid choice.\n")

        case 6:
            break

        case _:
            print("Invalid choice entered. Please enter a valid choice.\n")

print("Thank you for using Numpy Analyzer!\nHave a nice day.\nGoodbye.")