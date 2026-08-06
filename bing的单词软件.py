import random

# 定义一个字典，用来存储单词和它们的含义
words = {}

# 定义一个函数，用来录入单词
def add_word():
    word = input("请输入单词：")
    meaning = input("请输入含义：")
    words[word] = meaning

# 定义一个函数，用来查找单词的含义
def lookup_word():
    word = input("请输入要查找的单词：")
    if word in words:
        print(f"{word}的含义是{words[word]}")
    else:
        print(f"抱歉，{word}不在字典中。")

# 定义一个函数，用来随机测试
def test_words():
    correct = 0
    total = 0
    for i in range(5):
        word = random.choice(list(words.keys()))
        meaning = words[word]
        if random.randint(0, 1) == 0:
            # 中文翻英文
            answer = input(f"{meaning}的英文是什么？")
            if answer == word:
                print("回答正确！")
                correct += 1
            else:
                print(f"回答错误，正确答案是{word}。")
        else:
            # 英文翻中文
            answer = input(f"{word}的中文是什么？")
            if answer == meaning:
                print("回答正确！")
                correct += 1
            else:
                print(f"回答错误，正确答案是{meaning}。")
        total += 1
    print(f"测试结束，你一共回答了{total}道题，其中{correct}道题回答正确，准确率为{correct/total*100:.2f}%。")

# 主程序循环
while True:
    print("欢迎使用背单词软件！请选择以下功能：")
    print("1. 录入单词")
    print("2. 查找单词的含义")
    print("3. 随机测试")
    print("4. 退出程序")

    choice = input("请输入功能编号：")

    if choice == "1":
        add_word()
    elif choice == "2":
        lookup_word()
    elif choice == "3":
        test_words()
    elif choice == "4":
        break
    else:
        print("输入有误，请重新输入。")

print("谢谢使用背单词软件！")