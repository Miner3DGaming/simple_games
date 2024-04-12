import os
import time
import timeit

current_working_directory = os.getcwd()
#does file exist in current working directory

# def file_exists(path):
#     try:
#         open(path, 'r').close()
#     except IOError:
#         return False
#     return True

# def func_one(a_start, a_end, b_start, b_end):
#     for a in range(a_start, a_end+1):
#         for b in range(b_start, b_end):
#             if file_exists(f"{current_working_directory}/multiple/{a}/{b}"):
#                 pass

# def func_two(a_start, a_end, b_start, b_end):
#     for a in range(a_start, a_end+1):
#         for b in range(b_start, b_end):
#             if os.path.isfile(f"{current_working_directory}/multiple/{a}/{b}"):
#                 pass

# start = time.time()
# func_one(1, 1000, 1, 1000)
# end = time.time()
# func_two(1, 1000, 1, 1000)
# abs_end = time.time()

# print(f"Func one: {end-start} seconds")
# print(f"Func two: {abs_end-end} seconds")


# quit()




#  ³3 == 3³³ == 3*3*3*3*3*3*3*3*3




def tetration(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    temp = base
    while exponent > 1:
        temp = base**temp
        exponent -= 1
    return temp

def hexation(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    temp = base
    while exponent > 1:
        temp = tetration(base, temp)
        exponent -= 1
    return temp







os.makedirs("multiple", exist_ok=True)
os.makedirs("quadrate", exist_ok=True)
os.makedirs("tetrate", exist_ok=True)
os.makedirs("hexate", exist_ok=True)


def get_latest_file(path: str, biggest: int):
    files = os.listdir(path)  # Get a list of files in the specified directory
    max_num = -1
    latest_file = None

    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            filename, file_extension = os.path.splitext(file)
            try:
                file_number = int(filename)
                if file_number > max_num:
                    max_num = file_number
                    latest_file = file
            except ValueError:
                continue  # Skip files that don't have a valid numeric name

    if latest_file is not None:
        return latest_file
    else:
        return None  # No valid files found in the directory


#result = get_latest_file(f"{current_working_directory}/quadrate/test", 10000)






    





get_latest_file(f"{current_working_directory}/multiple/{1}", 1000)

def generate_multiple(a_start, a_end, b_start, b_end):
    b_end += 1
    print((a_end+1 - a_start) * (b_end - b_start))
    
    start = time.time()
    for a in range(a_start, a_end+1):
        #print(f"Now working on: {a} (Multiple)")
        #if not os
        os.makedirs(f"{current_working_directory}/multiple/{a}", exist_ok=True)



        for b in range(b_start, b_end):
            if not os.path.isfile(f"{current_working_directory}/multiple/{a}/{b}"):
                with open(f"{current_working_directory}/multiple/{a}/{b}", "w") as f:
                    f.write(str(a*b))
    print(f"Time it took in sec: {time.time() - start}")

def generate_quadrate(a_start, a_end, b_start, b_end):
    b_end += 1
    print((a_end+1 - a_start) ** (b_end - b_start))
    
    start = time.time()
    for a in range(a_start, a_end+1):
        #print(f"Now working on: {a} (Quadrant)")
        os.makedirs(f"{current_working_directory}/quadrate/{a}", exist_ok=True)

        for b in range(b_start, b_end):
            if not os.path.isfile(f"{current_working_directory}/quadrate/{a}/{b}"):
                with open(f"{current_working_directory}/quadrate/{a}/{b}", "w") as f:
                    f.write(str(a**b))
    print(f"Time it took in sec: {time.time() - start}")


print("\nStarting with Multiple")
generate_multiple(1, 1000, 1, 1000)
print("\nStarting with Quadrant")
generate_quadrate(1, 1000, 1, 1000)