#相对路径
# 绝对路径
#

from pathlib import Path
path = Path('内置模块')
print(path.exists())#查找路径是否存在，布尔类型，可以实现自动化
for file in path.glob("*.py"):
    print(file)#查找py类型的文件







