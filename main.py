from multiprocessing import Process
import runpy

with open("TOKEN.txt", 'r') as file:
    TOKEN = file.read()
def run_reg_bot():
    runpy.run_module("regular_bot.py")

def run_slash_bot():
    runpy.run_module("slash_bot.py")

def run_cli_for_bot():
    running = 1
    while running:
        user_input = input("> ")
        if user_input == "quit":
            running = 0
    slash_bot_run.close()
    regular_bot_run.close()

if __name__ == '__main__':
    processes = []
    processes.append(Process(target=run_reg_bot))
    processes.append(Process(target=run_slash_bot))
    for p in processes:
        p.start()

    for p in processes:
        p.join()
    print('ks')
