from tkinter import *
from tkinter import filedialog
from stegano import lsb

def hide_message():
    try:
        cover_image = cover_entry.get()
        secret_message = secret_entry.get()
        output_image = output_entry.get()

        # Hide the message in the cover image
        secret = lsb.hide(cover_image, secret_message)
        secret.save(output_image)

        status_label.config(text="Message hidden successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")

def reveal_message():
    try:
        input_image = input_entry.get()

        # Reveal the message from the image
        secret_message = lsb.reveal(input_image)

        revealed_message.config(state=NORMAL)

        revealed_message.delete(1.0, END)
        revealed_message.insert(END, secret_message)

        revealed_message.config(state=DISABLED)

        status_label.config(text="Message revealed successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")

def select_cover_image():
    filename = filedialog.askopenfilename()
    cover_entry.delete(0, END)
    cover_entry.insert(END, filename)

def select_output_image():
    filename = filedialog.asksaveasfilename(defaultextension=".png")
    output_entry.delete(0, END)
    output_entry.insert(END, filename)

def select_input_image():
    filename = filedialog.askopenfilename()
    input_entry.delete(0, END)
    input_entry.insert(END, filename)

root = Tk()
root.title("Steganography")

# Hide message section
hide_frame = LabelFrame(root, text="Hide Message")

hide_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

cover_label = Label(hide_frame, text="Cover Image:")
cover_label.grid(row=0, column=0, sticky="e")

cover_entry = Entry(hide_frame, width=50)
cover_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
cover_button = Button(hide_frame, text="Browse", command=select_cover_image)
cover_button.grid(row=0, column=2)

secret_label = Label(hide_frame, text="Secret Message:")
secret_label.grid(row=1, column=0, sticky="e")
secret_entry = Entry(hide_frame, width=50)
secret_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

output_label = Label(hide_frame, text="Output Image:")
output_label.grid(row=2, column=0, sticky="e")
output_entry = Entry(hide_frame, width=50)

output_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
output_button = Button(hide_frame, text="Save As", command=select_output_image)
output_button.grid(row=2, column=2)

hide_button = Button(hide_frame, text="Hide Message", command=hide_message)

hide_button.grid(row=3, column=0, columnspan=3, pady=5)

# Reveal message section
reveal_frame = LabelFrame(root, text="Reveal Message")
reveal_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

input_label = Label(reveal_frame, text="Input Image:")

input_label.grid(row=0, column=0, sticky="e")
input_entry = Entry(reveal_frame, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
input_button = Button(reveal_frame, text="Browse", command=select_input_image)
input_button.grid(row=0, column=2)

reveal_button = Button(reveal_frame, text="Reveal Message", command=reveal_message)
reveal_button.grid(row=1, column=0, columnspan=3, pady=5)

revealed_message = Text(reveal_frame, width=60, height=5, wrap=WORD)
revealed_message.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
revealed_message.config(state=DISABLED)

# Status label
status_label = Label(root, text="", fg="green")
status_label.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
root.mainloop()
