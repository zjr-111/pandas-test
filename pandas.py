import pandas as pd
import random
# 读取文件
df = pd.read_excel(r'works.xlsx')
# df_1 = pd.read_excel(r'works.xlsx')
# 纵合并表格
# df = pd.concat([df, df_1])
# 横向合并表格
# df = pd.merge(df, df_1, how='属性')
# 创建数字和文字相对应的字典
digit_dict={
    '1': '一',
    '2': '二',
    '3': '三',
}
# 定义改变数字的函数change_digit
def change_digit(list):
    result = []
    for i in list:
        num_str = str(i)
        chines_num = ''.join([digit_dict[digit] for digit in num_str])
        result.append(chines_num)
    return result
# fillna()的作用是将空的填上，文件里的名字都是两个字的，可以进一步改善
df['姓名'] = df['姓名'].fillna('').apply(lambda x: x[-2:])
# 检查文件的大概信息
# print(df.info)
if '年龄' not in df.columns:    
    # 随机生成年龄
    age = [random.randint(18,70)for i in range(len(df['姓名']))]
    # 检查年龄列表
    #print(age)
    # 更新年龄列表
    df['年龄'] = age
# 新增学历列，并给其赋值，判断是否列存在需要用到df.columns，df.columns用来获取DataFrame对象的列标签的属性
if '学历' not in df.columns:
    df['学历'] = ''
    df['学历'] = df['学历'].apply(lambda x: random.randint(1,3) if x is not None else None) # 这里需要先进行创建列，才能进行这一步的操作，lamba函数不支持赋值，但支持返回值
    df['学历'] = change_digit(df['学历'])
    df['学历'] = df['学历'].apply(lambda x: str(x)+'本')
# 所属人群
df['人群'] = pd.cut(df['年龄'],bins=[0,25,50,70],labels=['青年','中年','老年'])
# 工资
df['薪资'] = ''
df['薪资'] = df['薪资'].apply(lambda x: random.randint(3000, 7000) if x is not None else None)
df['薪资水平'] = pd.cut(df['薪资'],bins=[3000,4000,5000,7000],labels=['小薪','小康','赋予'])
# 平均薪资
if '平均薪资' not in df.columns:
    df['平均薪资'] = ''
    mean = df['薪资'].mean()
    df.loc[0,'平均薪资'] = mean
'''
# 年龄平均值 df.index用来获取DataFrame对象的横标签的属性
if '平均' not in df.index:    
    df.loc['平均'] = ''
    # 'pd.to_numeric’函数用于将一个Series或DataFrame的数据类型转换为数值类型，'coerce’表示将无法转换的数据设置为NaN。
    df['年龄'] = pd.to_numeric(df['年龄'], errors='coerce') 
    mean = df['年龄'].mean()
    #print(mean)
    df.loc['平均','年龄'] = '平均年龄' + str(mean)
'''
#检查文档文件
print(df)
print('============================================================')
# 检查文档最后几行
print(df.tail(2))
print('============================================================')
# 展示高工资的人
print(df.loc[df['薪资']>6700])
print('============================================================')
print(df.loc[df['薪资'] == df['薪资'].max()])
# 保存文件
df.to_excel(r'work.xlsx',index=False)
