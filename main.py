import json

with open("defualt.json") as defualt:
    defualtObj = json.load(defualt)

while True:
    cmd = input("CMD:")
    file_name = "list.json"
    if cmd == "-add":
        nums_input = input("Add Task Number :")
        detail = input(f"Add detail to task number {nums_input} :")
        a_dict = {f"t{nums_input}": detail}
        with open(file_name, "r+") as file:
            data = json.load(file)
            data.update(a_dict)
            file.seek(0)
            json.dump(data, file)
    if cmd == "-help":
        print(
            "-add = Add New Task\n-check = check task when it is finished\n-clear = clear task\n-show = show all task"
        )
    if cmd == "-show":
        with open(file_name, "r") as file_r:
            datar = json.load(file_r)
            print(datar)
    if cmd == "-check":
        dels = input("Task To Check :")
        with open(file_name, "r") as file_del_r:
            dataDEL = json.load(file_del_r)
        dataDEL1 = dataDEL[dels] + " - (TASK CHECKED)"
        dataDEL[dels] = dataDEL1
        with open(file_name, "w") as file_del_w:
            json.dump(dataDEL, file_del_w)
            print("~~ DONE ~~")
    if cmd == "-clear":
        with open(file_name, "w") as Clear:
            json.dump(defualtObj, Clear)
            print(" ~~ Task Cleared ~~")
