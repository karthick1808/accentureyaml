import yaml
import os
with open(r'C:\Users\Karthick Selvam\Desktop\Training\YAML\Samples\6.yml') as file:
    inputlist = yaml.load(file, Loader=yaml.FullLoader)
print(inputlist)
os.system("pause")
