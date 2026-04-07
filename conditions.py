no = 20

if no >= 30:
    print(f"{no} greater than 30");
else:
    print(f"{no} lesser than 30");

if no <= 30:
    print(f"{no} greater than 30");
else:
    print(f"{no} lesser than 30");

if no >= 30:
    print(f"{no} greater than 30");
elif no ==20:
    print(f"{no} equals to 20");
else:
    print(f"{no} else");


light = "Green";

if light == "Green":
    print("Go");
elif light == "Orange":
    print("Caution");
elif light == "Red":
    print("Stop");
else:
    print("Incorrect light singal");


users = ["Pravin", "Rahul"];
if users:
    print("Users is not empty");

users = [];
if not users:
    print("Users is empty");

temp = None;
if temp == None:
    print("Its none");

if not temp:
    print("It is not none");