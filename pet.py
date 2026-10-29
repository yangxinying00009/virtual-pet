"""
文字宠物养成小游戏
适合Python课程作业
玩法：
1. 给宠物取名
2. 选择功能：喂食 / 玩耍 / 睡觉 / 查看状态 / 退出
3. 饱食度、快乐值太低宠物会生病扣血
"""
import random
import time

class Pet:
    def __init__(self, name):
        self.name = name
        self.hp = 100      # 生命值
        self.full = 80     # 饱食度
        self.happy = 80    # 快乐值

    def show_status(self):
        print(f"\n===== 🐾 {self.name} 的状态 =====")
        print(f"生命值：{self.hp}")
        print(f"饱食度：{self.full}")
        print(f"快乐值：{self.happy}")
        if self.hp <= 0:
            print(f"😢 {self.name} 离开了你，游戏结束！")
        elif self.full <= 20 or self.happy <= 20:
            print(f"🤒 {self.name} 状态不太好，快照顾它！")
        else:
            print(f"😊 {self.name} 现在很健康！")
        print("=" * 25)

    def feed(self):
        add = random.randint(10, 25)
        self.full += add
        if self.full > 100:
            self.full = 100
        print(f"🍚 你喂了 {self.name}，饱食度 +{add}")
        self.check_sick()

    def play(self):
        add = random.randint(15, 30)
        self.happy += add
        self.full -= random.randint(5,10)
        if self.happy > 100:
            self.happy = 100
        print(f"🎈 你陪 {self.name} 玩耍，快乐值 +{add}")
        self.check_sick()

    def sleep(self):
        add = random.randint(15, 25)
        self.hp += add
        self.full -= random.randint(3,8)
        if self.hp > 100:
            self.hp = 100
        print(f"💤 {self.name} 睡了一觉，生命值 +{add}")
        self.check_sick()

    def check_sick(self):
        if self.full <= 20 or self.happy <= 20:
            lose = random.randint(5,12)
            self.hp -= lose
            print(f"⚠️  {self.name} 不舒服！生命值 -{lose}")

    def auto_decay(self):
        self.full -= random.randint(2,6)
        self.happy -= random.randint(2,6)
        if self.full < 0:
            self.full = 0
        if self.happy < 0:
            self.happy = 0

def random_event(pet):
    event_list = [
        f"✨ {pet.name} 捡到小零食！饱食度+10",
        f"🌈 {pet.name} 看到彩虹，开心极了！快乐值+10",
        f"🌧️ 外面下雨，{pet.name} 有点不开心，快乐值-5",
    ]
    if random.random() < 0.25:
        event = random.choice(event_list)
        print("\n【随机事件】" + event)
        if "饱食度+10" in event:
            pet.full +=10
            if pet.full>100:
                pet.full=100
        elif "快乐值+10" in event:
            pet.happy +=10
            if pet.happy>100:
                pet.happy=100
        elif "快乐值-5" in event:
            pet.happy -=5

def main():
    print("="*40)
    print("欢迎来到文字宠物养成小游戏！")
    print("="*40)
    pet_name = input("请给你的小宠物起名字：")
    my_pet = Pet(pet_name)
    print(f"\n🎉 你的宠物 {pet_name} 诞生啦！好好照顾它！")

    while True:
        if my_pet.hp <= 0:
            my_pet.show_status()
            print("游戏结束！")
            break
        print("\n-------- 操作菜单 --------")
        print("1. 喂食 🍚")
        print("2. 玩耍 🎈")
        print("3. 睡觉 💤")
        print("4. 查看状态 📊")
        print("5. 退出游戏 ❌")
        choice = input("\n请输入你的选择(1-5)：")

        if choice == "1":
            my_pet.feed()
        elif choice == "2":
            my_pet.play()
        elif choice == "3":
            my_pet.sleep()
        elif choice == "4":
            my_pet.show_status()
            continue
        elif choice == "5":
            print(f"👋 再见，下次再来陪 {my_pet.name}！")
            break
        else:
            print("❌ 输入错误，请输入1~5之间的数字！")
            continue

        my_pet.auto_decay()
        random_event(my_pet)
        time.sleep(0.6)

if __name__ == "__main__":
    main()
