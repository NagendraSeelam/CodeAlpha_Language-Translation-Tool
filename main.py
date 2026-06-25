from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

translator = Translator()

def translate():
    text = input_text.get("1.0", END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text")
        return

    try:
        translated = translator.translate(
            text,
            src=source_lang.get(),
            dest=target_lang.get()
        )

        output_text.delete("1.0", END)
        output_text.insert(END, translated.text)

    except Exception as e:
        messagebox.showerror("Error", str(e))


root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")

languages = sorted(LANGUAGES.keys())

source_lang = StringVar(value="en")
target_lang = StringVar(value="hi")

Label(root, text="Source Language").pack()

ttk.Combobox(
    root,
    textvariable=source_lang,
    values=languages
).pack()

Label(root, text="Target Language").pack()

ttk.Combobox(
    root,
    textvariable=target_lang,
    values=languages
).pack()

Label(root, text="Input Text").pack()

input_text = Text(root, height=8)
input_text.pack(fill="x", padx=10)

Button(
    root,
    text="Translate",
    command=translate
).pack(pady=10)

Label(root, text="Translated Text").pack()

output_text = Text(root, height=8)
output_text.pack(fill="x", padx=10)

root.mainloop()
