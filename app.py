import csv
import customtkinter as ctk
import os
from tkinter import filedialog, ttk

class AttendanceTrendsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Attendance Trends")
        self.geometry("1000x600")

        # open csv file button
        self.btn = ctk.CTkButton(self, text="New Report", command=self.open_csv)
        #self.btn.grid(row=0, column=0, padx=20, pady=20)
        self.btn.pack(pady=10)

        # list saved reports
        self.btn = ctk.CTkButton(self, text="Saved Reports", command=self.list_saved_reports)
        #self.btn.grid(row=0, column=1, padx=20, pady=20)
        self.btn.pack(pady=10)

        # close the app
        self.btn = ctk.CTkButton(self, text="Exit", command=self.destroy)
        #self.btn.grid(row=0, column=2, padx=20, pady=20)
        self.btn.pack(pady=10)

        self.tree = ttk.Treeview(self, show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    # open the csv
    def open_csv(self):
        # to do: start at desktop directory
        file_path = os.path.join(os.path.expanduser("~"), "Desktop")

        file_types = [
            ("CSV", "*.csv"),
        ]

        selected_file = filedialog.askopenfilename(
            initialdir=file_path,
            title="Select CSV File",
            filetypes=file_types
        )

        # file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path: return
        
        self.tree.delete(*self.tree.get_children())
        with open(selected_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader)
            self.tree["columns"] = headers
            for h in headers: self.tree.heading(h, text=h)
            for row in reader: self.tree.insert("", "end", values=row)

    # process the csv

    # list stored reports
    def list_saved_reports(self):
        pass

    # quit the program
    def quit_app(self):
        pass

if __name__ == "__main__":
    app = AttendanceTrendsApp()
    app.mainloop()