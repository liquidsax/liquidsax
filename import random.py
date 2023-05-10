import random
print (random.random())#random.random()用于输出一个0-1的随机小数
print (random.uniform(10,20))#用于生产一个范围内数字（小数）
print (random.randint(10,20))#用于生存一个整数
print (random.choice("无双大黄瓜"))
print (random.choice(["focxk","djkdk","shjdiu"]))#用于选取
p = ["fuck","my","little","pussy"]
random.shuffle(p)#像洗牌一样打乱顺序
print (p)
list=[1,2,3,4,5,6,77]
slice=random.sample(list,4)#创建一个容量为4的样本
print(slice)
print(list)