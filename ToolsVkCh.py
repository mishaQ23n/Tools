import os
import vk_api
import time

priv = [
"""
█─█──█──█──███──████──████──█────███──████──█──█
█─█──█─█────█───█──█──█──█──█────█────█──█──█──█
█─█──██─────█───█──█──█──█──█────███──█─────████
███──█─█────█───█──█──█──█──█──────█──█──█──█──█
─█───█──█───█───████──████──███──███──████──█──█
"""
]
print(priv[0])
print("Скрипт в котором все собрано. Все скрипты, которые я писал ранее.")
print("Создатель: vk.com/chmotie \n Группа https://vk.com/scripts_xxx")
print("По вопросам писать в ЛС группы.")
print("Все инструменты.")
instr = [
"""
 ---------------------------------------------------------
| 1.VkComments                                            |
| 2.VkPost                                                |
| 3.VkSmsNakrutka                                         |
| P.S дальше еще будут))                                  |
 ---------------------------------------------------------
"""
]
print(instr[0])
navigat = input("--> ")
# os.system('cls')
if navigat == "1":
	os.chdir('VkComments')
	os.system('cls')
	os.system('python Coms.py')
if navigat == "2":
	os.chdir('VkPost')
	os.system('cls')
	os.system('python posts.py')
if navigat == "3":
	os.chdir('VkSmsNakrutka')
	os.system('cls')
	os.system('python Nakrutka.py')