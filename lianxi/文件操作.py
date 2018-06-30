
# 文件自动关闭
with open("text.txt", "w") as textfile:
  textfile.write("Success!")
if not textfile.closed:
  textfile.close()

print(textfile.closed)
