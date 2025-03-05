import tkinter as tk
from tkinter import messagebox

def encrypt(text):
    encrypted = []
    for char in text:
        if char.isalpha():
            # 生成偏移量（1-9）
            offset = str((ord(char.lower()) - ord('a') + 1) % 9 + 1)
            # 计算加密后的字母位置
            position = ord(char.lower()) - ord('a')
            new_position = (position + int(offset)) % 26
            new_char = chr(new_position + ord('a'))
            # 保持大小写
            if char.isupper():
                new_char = new_char.upper()
            encrypted.append(offset + new_char)
        else:
            # 非字母字符保持不变
            encrypted.append(char)
    return ''.join(encrypted)

def decrypt(text):
    decrypted = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i].isdigit() and text[i+1].isalpha():
            offset = int(text[i])
            char = text[i+1]
            position = ord(char.lower()) - ord('a')
            original_position = (position - offset) % 26
            original_char = chr(original_position + ord('a'))
            # 保持大小写
            if char.isupper():
                original_char = original_char.upper()
            decrypted.append(original_char)
            i += 2
        else:
            # 非字母字符保持不变
            decrypted.append(text[i])
            i += 1
    return ''.join(decrypted)

def encrypt_text():
    input_text = text_input.get("1.0", tk.END).strip()
    encrypted_text = encrypt(input_text)
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", encrypted_text)

def decrypt_text():
    input_text = text_input.get("1.0", tk.END).strip()
    decrypted_text = decrypt(input_text)
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", decrypted_text)

def clear_text():
    text_input.delete("1.0", tk.END)
    text_output.delete("1.0", tk.END)

# 创建主窗口
root = tk.Tk()
root.title("加密解密工具")

# 输入文本框
tk.Label(root, text="输入文本：").pack()
text_input = tk.Text(root, height=5, width=50)
text_input.pack()

# 输出文本框
tk.Label(root, text="输出文本：").pack()
text_output = tk.Text(root, height=5, width=50)
text_output.pack()

# 按钮区域
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="加密", command=encrypt_text)
encrypt_button.pack(side=tk.LEFT, padx=10)

decrypt_button = tk.Button(button_frame, text="解密", command=decrypt_text)
decrypt_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="清空", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=10)

# 运行主循环
root.mainloop()
