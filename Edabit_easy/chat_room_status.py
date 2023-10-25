def chatroom_status(users):
    if len(users) == 0:
        return "No one online"
    elif len(users) == 1:
        return users[0] + " is online"
    elif len(users) == 2:
        return users[0] + " and " + users[1] + " are online"
    else:
        txt = users[0] + ", " + users[1] + " and another " + str(len(users) - 2) + " members are online"
        return txt

print(chatroom_status([]))                                      # ➞ No one online
print(chatroom_status(["Jane"]))                                # ➞ Jane is online
print(chatroom_status(["Jane", "Kate"]))                        # ➞ Jane and Kate are online
print(chatroom_status(["Jane", "Kate", "Bash", "Lush"]))        # ➞ Jane, Kate and another 2 members are online


