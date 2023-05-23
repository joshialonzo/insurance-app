from tkinter import Tk, ttk
from tkinter import filedialog


def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    file_path_label.config(text=file_path)


# Create the Tkinter application window
window = Tk()
window.title("CSV File Uploader")

# Create a button to upload the file
upload_button = ttk.Button(window, text="Upload CSV File", command=upload_file)
upload_button.pack(pady=10)

# Create a label to display the file path
file_path_label = ttk.Label(window, text="No file selected")
file_path_label.pack()

# Run the Tkinter event loop
window.mainloop()
