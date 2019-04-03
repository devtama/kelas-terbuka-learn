import sys

data_list = [1,2,3,4,5,6,7,8,9,10,"sayati","cedok","bihbul", False, 3.14]
data_tuple = (1,2,3,4,5,6,7,8,9,10,"sayati","cedok","bihbul", False, 3.14)

besar_dataList = sys.getsizeof(data_list)
besar_dataTuple = sys.getsizeof(data_tuple)

print(f"besar data list = {besar_dataList}")
print(f"besar data Tuple = {besar_dataTuple}")