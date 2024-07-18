# seek() function
# with open ('file.txt', 'r') as f:
#     print(type(f))
#     # Move to the 10th byte in the file
#     f.seek(10)

#     # Read the next 5 bytes
#     data = f.read(5)
#     print(data)

# tell() function
# with open('file.txt','r') as f:
#     print(type(f))

#     f.seek(10)
#     print(f.tell())
#     data=f.read(5)
#     print(data)

# with open('file.txt', 'r') as f:
#   # Read the first 10 bytes
#   data = f.read(10)
#   print(data)
#   # Save the current position
#   current_position = f.tell()

#   # Seek to the saved position
#   f.seek(current_position)
#   print(current_position)

# truncate() function
# with open ('sample.txt','w') as f:
#     f.write('Hello World!')
#     f.truncate(5)

# with open ('sample.txt','r') as f:
#     print(f.read())