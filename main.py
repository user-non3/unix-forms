import re
import os
import time
from colorama import *

logo_text = '''  / / / /___  (_)  __      / ____/___  _________ ___  _____
 / / / / __ \/ / |/_/_____/ /_  / __ \/ ___/ __ `__ \/ ___/
/ /_/ / / / / />  </_____/ __/ / /_/ / /  / / / / / (__  ) 
\____/_/ /_/_/_/|_|     /_/    \____/_/  /_/ /_/ /_/____/  
                                                    '''
                                                    
def main():
    os.system('cls')
    os.system('title Проверка пакетов...')
    print('Запускаю программу...')
    time.sleep(1)
    os.system('cls')
    os.system('title Unix Systems / Build: 1.0 ')
    print(Fore.GREEN + f'\n{logo_text}\n\nДобро пожаловать в скрипт UnixForms для Arizona RP\nРазработчик - Nevermore_Nightmare [05] | VK: @user.none | VK Public: @unix.tech | Discord: user.none\n')
    option_choice = input(Fore.GREEN + f'[1] Сбор через файл {Fore.RED}Arizona Tools{Fore.GREEN}\n[2] Сбор через файл Чат-лога\n[3] FAQ\n\n> Выберите метод сбора: ')
    choiceOption(option_choice)
    
    
def choiceOption(option):
    if option == '1':
        file = input(Fore.GREEN + '> Введите путь к файлу TXT (Без ковычек): ')
        
        dataTransformByFile(file)
        
    elif option == '2':
        file = input(Fore.GREEN + '> Введите путь к файлу TXT (Без ковычек): ')
        dataTransformByChat(file)
    
    elif option == '3':
        os.system('cls')
        threads = input(Fore.GREEN + f'\n{logo_text}\n\n[1] Откуда взять файл от {Fore.RED}Arizona Tools{Fore.GREEN}?\n[2] Откуда взять файл от Чат-лога\n[3] В главное меню\n\n> Какой пункт вас интересует?: ')
        help(threads)
        
    else:
        print(Fore.RED + '[ERROR] Укажите правильный метод сбора!')
        
def help(threads_choice):
    if threads_choice == '1':
        print(Fore.GREEN + f'\nДля того что бы взять файл для формы вы должны зайти в папку moonloader в корневой директории вашей игры.\nЗатем нужно перейти в папку {Fore.RED}Arizona Tools{Fore.GREEN} > Выданные наказания, дальше ищете нужный вам файл по дате\nПример - bin/Arizona/moonloader')
    
    elif threads_choice == '2':
        print(Fore.GREEN + '\nЧто бы получить путь к файлу с чатлогом перейдите в директорию: \nДокументы > GTA San Andreas User Files > SAMP > arizona > chatlog - дальше выберите папку по дате')
    
    elif threads_choice == '3':
        main()
        

def dataTransformByFile(file_name):
    tag = input(Fore.GREEN + '> Введите ваш тег (Напишите 0 если он вам не нужен): ')
    choice = input(Fore.GREEN + '\n[1] Парсить баны (banoff)\n[2] Парсить муты (muteoff)\n[3] Парсить джайлы (jailoff)\n\n> Выберите опцию: ')
    with open(file_name, 'r') as file:
        data = file.read()
        
    input_file = open("output.txt", "w+", encoding='utf-8')
    pattern = r"(.*)\s\|\s\/a\s(\S+)\s(\S+)\s(\S+)\s(.*)"
    
    
    if choice == '1':
        form_reason = input(Fore.GREEN + '> Укажите причину (Напишите 0 если не нужно): ')
        matches = re.findall(pattern, data)
        try:
            for match in matches:
                hour, cmd, nick, days, reason = match
                
                if nick.isdigit():
                    pass
                
                else:
                    if tag == '0':
                        if form_reason == '0':
                            input_file.write(f'/banoff 0 {nick} 2000 Напишите_Сюда_Причину\n')
                            
                        else:
                            input_file.write(f'/banoff 0 {nick} 2000 Чит\n')
                            
                    else:
                        if form_reason == '0':
                            input_file.write(f'/banoff 0 {nick} 2000 Напишите_Сюда_Причину // {tag}\n')
                            
                        else:
                            input_file.write(f'/banoff 0 {nick} 2000 {form_reason} // {tag}\n')
                
            print(Fore.GREEN + '\n> Сортировка данных была успешно закончена, спасибо за использование!')
            time.sleep(5)
            os.system('exit')
                
        except Exception as ex:
            print(Fore.RED + f'> Произошла ошибка в скрипте, отпишите разработчику!\n\n{ex}')
    
    elif choice == '2':
        form_reason = input(Fore.GREEN + '> Укажите причину (Напишите 0 если не нужно): ')
        matches = re.findall(pattern, data)
        try:
            for match in matches:
                hour, cmd, nick, days, reason = match
                
                if nick.isdigit():
                    pass
                
                else:
                    if tag == '0':
                        if form_reason == '0':
                            input_file.write(f'/muteoff {nick} 30 Напишите_Сюда_Причину\n')
                            
                        else:
                            input_file.write(f'/muteoff {nick} 30 {form_reason}\n')
                        
                    else:
                        if form_reason == '0':
                            input_file.write(f'/muteoff {nick} 30 Напишите_Сюда_Причину // {tag}\n')
                            
                        else:
                            input_file.write(f'/muteoff {nick} 30 {form_reason} // {tag}\n')
                
            print(Fore.GREEN + '\n> Сортировка данных была успешно закончена, спасибо за использование!')
            time.sleep(5)
            os.system('exit')
                
        except Exception as ex:
            print(Fore.RED + f'> Произошла ошибка в скрипте, отпишите разработчику!\n\n{ex}')
            
    elif choice == '3':
        form_reason = input(Fore.GREEN + '> Укажите причину (Напишите 0 если не нужно): ')
        matches = re.findall(pattern, data)
        try:
            for match in matches:
                hour, cmd, nick, days, reason = match
                
                if nick.isdigit():
                    pass
                
                else:
                    if tag == '0':
                        if form_reason == '0':
                            input_file.write(f'/jailoff {nick} 30 Напишите_Сюда_Причину\n')
                            
                        else:
                            input_file.write(f'/jailoff {nick} 30 {form_reason}\n')
                        
                    else:
                        if form_reason == '0':
                            input_file.write(f'/jailoff {nick} 30 Напишите_Сюда_Причину // {tag}\n')
                            
                        else:
                            input_file.write(f'/jailoff {nick} 30 {form_reason} // {tag}\n')
                
            print(Fore.GREEN + '\n> Сортировка данных была успешно закончена, спасибо за использование!')
            time.sleep(5)
            os.system('exit')
                
        except Exception as ex:
            print(Fore.RED + f'> Произошла ошибка в скрипте, отпишите разработчику!\n\n{ex}')

def dataTransformByChat(file_name):
    tag = input(Fore.GREEN + '> Введите ваш тег (Напишите 0 если он вам не нужен): ')
    choice = input(Fore.GREEN + '\n[1] Парсить баны (banoff)\n[2] Парсить муты (muteoff)\n[3] Парсить джайлы (jailoff)\n\n> Выберите опцию: ')
    with open(file_name, 'r') as file:
        data = file.read()
        
    input_file = open("output.txt", "w+", encoding='utf-8') 
    
    if choice == '1':
        form_reason = input(Fore.GREEN + '> Укажите причину (Напишите 0 если не нужно): ')
        pattern = r"A: (.*?)\[(.*?)\] забанил игрока (.*?)\[(.*?)\] на (.*?) дней. Причина: (.*?)"
        matches = re.findall(pattern, data)
        try:
            for match in matches:
                admin, admin_id, player_nick, player_id, days, reason = match
                
                if player_nick.isdigit():
                    pass
                
                else:
                    if tag == '0':
                        if form_reason == '0':
                            input_file.write(f'/banoff 0 {player_nick} 2000 {reason}\n')
                            
                        else:
                            input_file.write(f'/banoff 0 {player_nick} 2000 Чит\n')
                            
                    else:
                        if form_reason == '0':
                            input_file.write(f'/banoff 0 {player_nick} 2000 Напишите_Сюда_Причину // {tag}\n')
                            
                        else:
                            input_file.write(f'/banoff 0 {player_nick} 2000 {form_reason} // {tag}\n')
                
            print(Fore.GREEN + f'\n> Сортировка данных была успешно закончена, спасибо за использование!')
            time.sleep(5)
            os.system('exit')
                
        except Exception as ex:
            print(Fore.RED + f'> Произошла ошибка в скрипте, отпишите разработчику!\n\n{ex}')
    
    elif choice == '2':
        form_reason = input(Fore.GREEN + '> Укажите причину (Напишите 0 если не нужно): ')
        pattern_mute = r"A: (.*?)\[(.*?)\] заглушил игрока (.*?)\[(.*?)\] на (.*?) минут. Причина: (.*?)"
        matches = re.findall(pattern_mute, data)
        try:
            for match in matches:
                admin, admin_id, player_nick, player_id, days, reason = match
                
                if player_nick.isdigit():
                    pass
                
                else:
                    if tag == '0':
                        if form_reason == '0':
                            input_file.write(f'/muteoff {player_nick} 30 Напишите_Сюда_Причину\n')
                            
                        else:
                            input_file.write(f'/muteoff {player_nick} 30 {form_reason}\n')
                        
                    else:
                        if form_reason == '0':
                            input_file.write(f'/muteoff {player_nick} 30 Напишите_Сюда_Причину // {tag}\n')
                            
                        else:
                            input_file.write(f'/muteoff {player_nick} 30 {form_reason} // {tag}\n')

            print(Fore.GREEN + f'\n> Сортировка данных была успешно закончена, спасибо за использование!')
            time.sleep(5)
            os.system('exit')
                
        except Exception as ex:
            print(Fore.RED + f'> Произошла ошибка в скрипте, отпишите разработчику!\n\n{ex}')
            
    elif choice == '3':
        form_reason = input(Fore.GREEN + '> Укажите причину (Напишите 0 если не нужно): ')
        pattern_jail = r"A: (.*?)\[(.*?)\] посадил игрока (.*?)\[(.*?)\] в деморган на (.*?) минут. Причина: (.*?)"
        matches = re.findall(pattern_jail, data)
        try:
            for match in matches:
                admin, admin_id, player_nick, player_id, days, reason = match
                
                if player_nick.isdigit():
                    pass
                
                else:
                    if tag == '0':
                        if form_reason == '0':
                            input_file.write(f'/jailoff {player_nick} 30 Напишите_Сюда_Причину\n')
                            
                        else:
                            input_file.write(f'/jailoff {player_nick} 30 {form_reason}\n')
                        
                    else:
                        if form_reason == '0':
                            input_file.write(f'/jailoff {player_nick} 30 Напишите_Сюда_Причину // {tag}\n')
                            
                        else:
                            input_file.write(f'/jailoff {player_nick} 30 {form_reason} // {tag}\n')

            print(Fore.GREEN + f'\n> Сортировка данных была успешно закончена, спасибо за использование!')
            time.sleep(5)
            os.system('exit')
                
        except Exception as ex:
            print(Fore.RED + f'> Произошла ошибка в скрипте, отпишите разработчику!\n\n{ex}')

main()