import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

# Function to translate text
def translate_text():
    try:
        # Get the input text
        input_text = input_text_box.get("1.0", tk.END).strip()
        
        if not input_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return
        
        # Get selected language
        target_language = language_combo.get()
        
        # Translate using Googletrans
        translator = Translator()
        translated_text = translator.translate(input_text, dest=language_dict[target_language]).text
        
        # Display translated text
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translated_text)
        
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")

# Set up the main application window
root = tk.Tk()
root.title("Simple Translator")

# Set window size and background color
root.geometry("600x500")
root.config(bg="#e5e5e5")

# Header Label (Centered)
header_label = tk.Label(root, text="Simple Translator", font=("Helvetica", 26, "bold"), bg="#e5e5e5", fg="#2C3E50")
header_label.pack(pady=20)

# Input text box
input_label = tk.Label(root, text="Enter text:", font=("Helvetica", 12), bg="#e5e5e5", fg="#2C3E50")
input_label.pack(pady=5)

input_text_box = tk.Text(root, height=5, width=50, font=("Helvetica", 12), wrap="word", bd=2, relief="solid")
input_text_box.pack(pady=10)

# Language selection combo box with full language names
language_label = tk.Label(root, text="Select target language:", font=("Helvetica", 12), bg="#e5e5e5", fg="#2C3E50")
language_label.pack(pady=5)

# Language full names and their corresponding language codes
language_dict = {
    "English": 'en',
    "Spanish": 'es',
    "French": 'fr',
    "German": 'de',
    "Italian": 'it',
    "Portuguese": 'pt',
    "Chinese": 'zh-cn',
    "Japanese": 'ja',
    "Arabic": 'ar',
    "Hindi": 'hi'
}

# Creating a combo box with the full language names
language_combo = ttk.Combobox(root, values=list(language_dict.keys()), state="readonly", font=("Helvetica", 12))
language_combo.set('English')  # default language
language_combo.pack(pady=10)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text, font=("Helvetica", 14, "bold"), bg="#3498DB", fg="white", relief="flat", width=20)
translate_button.pack(pady=15)

# Output text box
output_label = tk.Label(root, text="Translated text:", font=("Helvetica", 12), bg="#e5e5e5", fg="#2C3E50")
output_label.pack(pady=5)

output_text_box = tk.Text(root, height=5, width=50, font=("Helvetica", 12), wrap="word", bd=2, relief="solid")
output_text_box.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="Developed by Hassan Ahmed", font=("Helvetica", 10), bg="#e5e5e5", fg="#7F8C8D")
footer_label.pack(pady=20)


# Start the application
root.mainloop()
