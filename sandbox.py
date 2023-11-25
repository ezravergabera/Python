from icecream import ic

def add(x, y):
    return x + y

# ic(add(10, 20))
# ic(add(40, 20))
# ic(add(10, 60))

# result = ic(add(27,19))
# print(result)

def output_to_file(text):
    with open("debug_log.txt", "a") as f:
        f.write(text + '\n')


ic.configureOutput(prefix="Debug| ", outputFunction=output_to_file, includeContext=True)

ic(add(10, 20))