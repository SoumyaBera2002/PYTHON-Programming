class BubbleSort:
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(n - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp

class Main:
    def main(self):
        arr = [5, 4, 3, 2, 1]
        bsort = BubbleSort()
        bsort.sort(arr)
        for i in arr:
            print(i)

# Create an instance of the Main class and call the main method
main_instance = Main()
main_instance.main()
