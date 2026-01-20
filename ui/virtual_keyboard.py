import tkinter as tk

def launch_virtual_keyboard():
    keyboard = tk.Tk()
    keyboard.title("Virtual Keyboard")

    keys = [
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
        'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
        'Z', 'X', 'C', 'V', 'B', 'N', 'M'
    ]

    def on_key_press(key):
        print(f"Pressed: {key}")

    for idx, key in enumerate(keys):
        button = tk.Button(keyboard, text=key, command=lambda k=key: on_key_press(k))
        button.grid(row=idx // 10, column=idx % 10)

    keyboard.mainloop()