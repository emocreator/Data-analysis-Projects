import tkinter as tk
import random
import pyautogui

win = tk.Tk()  # create new window instance
win.geometry("800x800")
win.title("Random Password Generator")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-/\\'?|"

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        pyautogui.alert(text="Please enter a whole number")
        return
    pwd = ""
    for char in range(length):
        pwd += chars[random.randint(0, len(chars) - 1)]
    gen_pw_text_field.delete("1.0", "end")
    gen_pw_text_field.insert("1.0", pwd)



# ------- Labels -------
len_label = tk.Label(text="Enter the number of characters you want your password to contain", font=("Roboto Light", 16))
len_label.place(x=0, y=0)
gen_pwd_label = tk.Label(text="Generated password", font=("Roboto Light", 16))
gen_pwd_label.place(x=2, y=44)
# ---------- Entry --------
length_entry = tk.Entry(width=28)
length_entry.place(x=4, y=28)

# ---------- Text field -------
gen_pw_text_field = tk.Text(width=40, height=18, font=("Roboto Light", 14))
gen_pw_text_field.place(x=2, y=74)
# ---------- Button -------
gen_pwd_b = tk.Button(text="Generate Password", font=("Roboto Light", 12), width=16, height=4, command=generate_password)
gen_pwd_b.place(x=560, y=100)

win.mainloop()
