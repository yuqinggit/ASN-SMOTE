import pandas as pd  

# 读取DAT文件，假设文件中的数据是以空格分隔的  
df = pd.read_csv('pima.dat', sep=',', header=0)  
# 注意：header=None 表示文件中没有列名，你需要自己指定列名（如上例中的Column1, Column2等）  
# 如果文件中有列名，则可以去掉header=None，并省略names参数  
# 将DataFrame保存为XLSX文件  
df.to_excel('pima.xlsx', index=False)



# 有空格符的处理
df = pd.read_csv('iris0.dat', sep=',', skipinitialspace=True, header=0)  
df.to_excel('iris0.xlsx', index=False)

df = pd.read_csv('vehicle1.dat', sep=',', skipinitialspace=True, header=0)  
df.to_excel('vehicle1.xlsx', index=False)