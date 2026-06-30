
import os
import sys
import platform

def main():
    # Очистка экрана в зависимости от ОС
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

    print("====================================")
    print("      ANON MARKET v1.0 (P2P)        ")
    print("====================================")
    print(f"Система: {platform.system()} {platform.release()}")
    print("Статус: Ожидание команд...")
    print("====================================")
    
    # Здесь в будущем будет твой основной функционал
    try:
        while True:
            cmd = input("AnonMarket > ")
            if cmd == "exit":
                break
            print(f"Команда '{cmd}' принята системой.")
    except KeyboardInterrupt:
        print("\nВыход...")

if __name__ == "__main__":
    main()
