# Python Practice Tasks

这个仓库用来记录CS小白从0-1 借助AI 完成 Python 基础练习和小工具任务。

## 当前任务

### Task 01:  图片重命名预览工具
练习内容：
- os.listdir()
- for 循环
- endswith()
- os.path.splitext()
- f-string
- 函数拆分

### Task 02： 图片重命名执行工具
练习内容：
- execute 参数控制预览/执行
- os.path.join()
- os.rename()
- 默认参数
- 代码安全意识：先预览，再执行

### Task 03:  返回重命名计划
练习内容：
- list 列表
- append()
- tuple 元组
- return 返回结果
- 将打印式脚本改成可复用函数

### Task 04:  统计文件类型数量
练习内容：
- 字典
- 文件后缀统计
- 键值对

### Task 05： 统计图片的总数量
练习内容：
- dict.values()
- sum

### Task 06: 汇报图片内容
练习内容： 
- with open () as f
- f.write

### Task 07 : 读取外部配置文件
练习内容
- readlines()
-  .strip  （去掉 这一行末尾恶心的换行符\n）
-  split('=')
-  字典名[键盘] = value

### Task 08 : 流水线的封装
练习内容
- def
- return
- 封装独立变量与函数隔离

### Task 09 : 防弹衣的穿戴
练习内容
- try:
- except:

### Task 10: Json 初步
练习内容
- import json
- json.load() 将外部json 文件变成字典

### Task 11: 深层目录文件搜索
练习内容
- os.walk()
- 复习 endswith(('',''))
- 复习 os.join() 

### 开始 学习 ai-engineering-from-scratch

### Task 12 : 手搓一个贝叶斯计算器 
P(A|B) = [P(B|A) * P(A)]/P(B) :注意这个B不是单一一个数字 而是需要你计算

### Task13 :蒙特卡洛与大数定律
练习内容：
蒙特卡洛算法 = 生成随机数模拟 + 统计发生的频率
- random.randint(1,6)
- for _ in range(1000) 占位符的规范
- range() list[ ] 都是[,) 包头不包尾
- 而random.randint( )是两边都包

### Task 14:计算均值和方差
练习内容：
- dict.items()
- 均值和方差的计算公式
- (x** 2) 这个** 是x的的指数 ！注意 而不是^ 这个是异或符号。

### Task 15: 计算正态分布
练习内容：
- math 库的使用：math.exp() / math.sqrt() / math.pi
- 概率密度和概率的区别

### Task 16: 微积分与概率面积的计
练习内容：
- 利曼和的暴力求积分
- dx

### Task 17：马尔科夫链与状态转移矩阵
练习内容
- 高内聚低耦合的思想
- 嵌套字典（字典里再套一层字典）
- 累计分布函数

### Task 18:中心极限定理
练习内容
- 双重for循环
- 大样本均值逼近正态分布的验证

### Task19:蒙特卡洛模拟
练习内容
- random.uniform()生成浮点数
- 面积逼近法的物理代码优化

### Task20:大数定律
练习内容
- range(1,1+num_toss) 防止分母为0
- 动态均值 (前5次 后5次)
