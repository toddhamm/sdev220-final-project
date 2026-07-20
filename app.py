# imports
import csv
import customtkinter as ctk
import os
from tkinter import filedialog, ttk

class AttendanceTrendsApp(ctk.CTk):
    def __init__(self):
        
        # inherit from CTK
        super().__init__()
        
        # app title
        self.title("Attendance Trends")
        
        # set initial width and height
        self.geometry("1000x600")

        # container for buttons
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=40, padx=20)

        # open csv file button
        self.open_btn = ctk.CTkButton(self.button_frame, text="New Report", command=self.open_csv)
        #self.btn.grid(row=0, column=0, padx=20, pady=20)
        self.open_btn.pack(side="left", padx=10)

        # list saved reports button
        self.list_btn = ctk.CTkButton(self.button_frame, text="Saved Reports", command=self.list_saved_reports)
        self.list_btn.pack(side="left", padx=10)

        # close the app button
        self.exit_btn = ctk.CTkButton(self.button_frame, text="Exit", command=self.destroy)
        self.exit_btn.pack(side="left", padx=10)

        # create a window / frame / "tree" view below the buttons
        self.tree = ttk.Treeview(self, show="headings")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    # open the csv
    def open_csv(self):
        # set initial directory as Desktop
        file_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # show only csv file types
        file_types = [
            ("CSV", "*.csv"),
        ]

        # dialog for selecting file
        selected_file = filedialog.askopenfilename(
            initialdir=file_path,
            title="Select CSV File",
            filetypes=file_types
        )

        # exit method if can't find Desktop
        if not file_path: 
            return
        
        # remove anything in the window / frame below
        self.tree.delete(*self.tree.get_children())

        # open the file and display data in the "tree" container
        with open(selected_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader)
            self.tree["columns"] = headers
            for h in headers: self.tree.heading(h, text=h)
            for row in reader: self.tree.insert("", "end", values=row)

    # get user input for grade level method
    def get_grade_level(self):
        user_text = self.entry.get() 
        print(f"User typed: {user_text}")
        
        # 2. Update the label to display it
        self.output_label.configure(text=f"Submitted: {user_text}")

    # save imported csv

    # clear imported data

    # process the csv

    # list stored reports
    def list_saved_reports(self):
        pass

    # quit the program
    def quit_app(self):
        pass

# 
if __name__ == "__main__":
    app = AttendanceTrendsApp()
    app.mainloop()