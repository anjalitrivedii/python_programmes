import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My Portfolio")
root.geometry("600x600")
root.configure(bg="#f0f0f0")

header = tk.Frame(root, bg="#4a4e69", height=100)
header.pack(fill="x")
tk.Label(header, text="Anjali Trivedi", font=("Lucida Handwriting", 18, "bold"), bg="#4a4e69", fg="white").pack(pady=10)
tk.Label(header, text="BCA Student | Python Developer", font=("Helvetica", 12), bg="#4a4e69", fg="white").pack()

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

about_tab = tk.Frame(notebook, bg="white")
tk.Label(about_tab, text="About Me", font=("Ariel", 16, "bold"), bg="white").pack(pady=10)
about_text = """Hello!I'm Anjali Trivedi, a BCA student passionate about Python, web development,and building practical apps with good UI/UX."""
tk.Label(about_tab, text=about_text, wraplength=500, justify="left", bg="white").pack(padx=20)

skills_tab = tk.Frame(notebook, bg="white")
tk.Label(skills_tab, text="Skills", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
skills = ["Python", "Tkinter", "Django", "MySQL", "HTML & CSS", "Git & Github"]
for skill in skills:
    tk.Label(skills_tab, text=f"• {skill}", anchor="w", bg="white").pack(fill="x", padx=30)

projects_tab = tk.Frame(notebook, bg="white")
tk.Label(projects_tab, text="Projects", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
projects = [
    "To-Do list app (python & Tkinter)",
    "Student Management System (Python + MySQL)",
    " Recipe Generator (Tkinter + API)",
]
for proj in projects:
    tk.Label(projects_tab, text=f"- {proj}", anchor="w", bg="white").pack(fill="x", padx=30)

# Contact Tab
contact_tab = tk.Frame(notebook, bg="white")
tk.Label(contact_tab, text="Contact Me", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
tk.Label(contact_tab, text="📧 Email: anjalitri1122@gmail.com", bg="white").pack(pady=5)
tk.Label(contact_tab, text="📱 Phone: +91 9874653772", bg="white").pack(pady=5)
tk.Label(contact_tab, text="🌐 GitHub: https://github.com/anjalitrivedii", bg="white").pack(pady=5)
tk.Label(contact_tab, text=" linkedin: https://linkedin.com/in/anjali-trivedi", bg="white").pack(pady=5)
notebook.add(about_tab, text="About")
notebook.add(skills_tab, text="Skills")
notebook.add(projects_tab, text="Projects")
notebook.add(contact_tab, text="Contact")

root.mainloop()
