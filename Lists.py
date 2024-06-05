todo_list = [
  "Do homework",
  "Buy groceries",
  "Clean room",
  "Go to library",
  "Make dinner"
]

def prompt_modify_list(todo_list):
  action = input("Do you want to add, remove, or change the list?: ")
  if action == "add":
    item = input("Enter the item you want to add:")
    todo_list.append(item)
    print("Added", item)
  elif action == "remove":
    item = input("Enter the item you want to remove:")
    if item in todo_list:
      todo_list.remove(item)
      print("Removed", item)
    else:
      print(item, "is not on the todo list")
  elif action == "change":
    index = int(input("Enter the index of the item you want to change:"))
    new_value = input("Enter the new value of the item:")
    old_value = todo_list[index]
    todo_list[index] = new_value
    print("Changed", old_value, "to", new_value)

print(todo_list)
prompt_modify_list(todo_list)
print(todo_list)

#####################################################################
