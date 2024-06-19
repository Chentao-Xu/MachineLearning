import os
import pandas as pd

def convert_xls_to_csv(directory):
    # 获取当前文件夹中的所有文件
    files = os.listdir(directory)
    
    # 过滤出所有的 .xls 文件
    xls_files = [file for file in files if file.endswith('.xls')]
    
    # 遍历每个 .xls 文件并转换为 .csv 文件
    for xls_file in xls_files:
        # 构建文件的完整路径
        xls_path = os.path.join(directory, xls_file)
        
        # 读取 .xls 文件
        df = pd.read_excel(xls_path, engine='xlrd')
        
        # 构建 .csv 文件的路径
        csv_file = xls_file.replace('.xls', '.csv')
        csv_path = os.path.join(directory, csv_file)
        
        # 保存为 .csv 文件
        df.to_csv(csv_path, index=False)
        print(f"Converted {xls_file} to {csv_file}")

if __name__ == "__main__":
    # 获取当前文件夹路径
    current_directory = os.getcwd()
    
    # 调用转换函数
    convert_xls_to_csv(current_directory)
