from QuickSort import QuickSort
from BubbleSort import BubbleSort

data_input = input("ป้อนตัวเลข(เช่น 5 2 7 1 9): ")

data_list = list(map(int, data_input.split()))

print("เลือกวิธีเรียงลำดับ:")
print("1. QuickSort")
print("2. BubbleSort")
choice = input("พิมพ์หมายเลข (1/2): ")

if choice == "1":
    result = QuickSort(data_list)
elif choice == "2":
    result = BubbleSort(data_list)
else:
    exit()

print("Result Sort:", result)
