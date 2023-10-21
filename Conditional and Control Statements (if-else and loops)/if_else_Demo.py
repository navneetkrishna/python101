movies_list = ["Rocky", "Batman", "Captain America", "The Godfather"]
show_list = ["Breaking Bad", "The Office", "Friends", "Hannibal", "GOT"]


my_choice = input("Enter your choice: ")

if my_choice in show_list:
    print("Your choice is a show")

elif my_choice in movies_list:                      # similar to else-if
    print("Your choice is a movie")

else:
    print("Unknown")

# ----------------------------------------------------------------

# my_tuple = ("John", "Doe", 23, ["Sr. Software Eng.", "LG"])
# if ("John" in my_tuple) and ("GOT" in show_list):
#     print("OK")
