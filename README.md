我近期开始学习pandas，为我的数据分析生涯做准备，目前准备先从表格的基础操作做起，并不断完善。
pd.read_excel('文件地址') 阅读文档,还有read_csv、read_html等等。
df['标签'] 选择列
df['标签'].apply(lambda x: x[-2:])
apply() 这个方法的第一个参数时函数将用于列表里的每一个元素。 ‘lambda x: x[-2:]’ 是匿名函数，lamba是关键字 x是函数参数 ‘:’是函数的冒号，冒号后面的语句是表达式。
df.to_excel('文件',index=False) 保存后缀为excel文件，如果要保存别的后缀的文件就需要改变to_excel的函数。