from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
import os

class AppUI:
    def __init__(self, master):
        self.master = master
        master.title("CV and Job Matcher")

        self.label = Label(master, text="Upload your CV:")
        self.label.pack()

        self.cv_entry = Entry(master, width=50)
        self.cv_entry.pack()

        self.browse_button = Button(master, text="Browse", command=self.browse_cv)
        self.browse_button.pack()

        self.job_label = Label(master, text="Enter Job Description or URL:")
        self.job_label.pack()

        self.job_entry = Entry(master, width=50)
        self.job_entry.pack()

        self.submit_button = Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()

    def browse_cv(self):
        filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Text files", "*.txt")])
        if filename:
            self.cv_entry.delete(0, 'end')
            self.cv_entry.insert(0, filename)

    def submit(self):
        cv_path = self.cv_entry.get()
        job_description = self.job_entry.get()

        if not os.path.isfile(cv_path):
            messagebox.showerror("Error", "Please upload a valid CV file.")
            return

        if not job_description:
            messagebox.showerror("Error", "Please enter a job description or URL.")
            return

        # Here you would call the functions to handle the CV and job description
        # For example: handle_cv(cv_path) and scrape_job_description(job_description)

        messagebox.showinfo("Success", "CV and Job Description submitted successfully!")

if __name__ == "__main__":
    root = Tk()
    app = AppUI(root)
    root.mainloop()