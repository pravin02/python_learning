name = "Pravin Patil";
print(len(name), " is the lenth of the employee name ", name);

print("First character of string ", name[0]);
print("Last character of string ", name[-1]);
print("First three characters of string ", name[0:3]);
print("All the characters of string ", name[0:]);
print("All the characters of string ", name[:]);

print("------------------------");
para = "This is the demonstration of the \"python\"";
print(para);

print("Concat strings");

first_name=  "Pravin";
last_name ="Patil";
full_name = first_name +" "+last_name;
print(full_name);
full_name = f"{first_name} {last_name}"
print(full_name);

print("First Name in upper ", first_name.upper());
print("First Name in lower ", first_name.lower());
print("First Name in title ", first_name.title());
print("Strip white spaces ", first_name.strip());
print("Find index of text or character ", first_name.find("Pr"));
print("Replace ", first_name.replace("P", "R"))

print("If contains return true/false ->", "Pr" in first_name)
print("If not contains return true/false ->", "Pr" not in first_name)