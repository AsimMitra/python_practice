print("Hello Folks there in codespaces, I am {}, first time here".format("Asim Mitra"))
my_List=["Asim Mitra",20,"from CGEC"]
print(f"I am {my_List[0]}, {my_List[1]}, I am {my_List[2]}") #formatted string with print statement
#After first commit
#Dictionary practice
my_dict={"a":1,'b':2,"c":3,'d':4}   #initialization of dictionary
# Check if a key exists
if 'a' in my_dict:
    print("Found a")

# Loop through keys (default behavior)
for key in my_dict.keys():  # can be used as "for key in my_dict: " without keys()
    print(key)

# Loop through values
for value in my_dict.values():  #uses of my_dict.values()
    print(value)

# Loop through both keys and values simultaneously
for key, value in my_dict.items():      #uses of my_dict.items()
    print(f"key : {key}, value : {value}")