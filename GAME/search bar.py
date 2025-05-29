import tkinter as tk
import webbrowser
def search():
    query =entry.get()
    if query.strip():
        webbrowser.open(f"https://www.google.com/search?q={query}")
#create the main window
root = tk.Tk()
root.title("Google Search")
root.geometry("500x150")
root.configure(bg="white")

#center the window
root.eval('tk::PlaceWindow . center')
#entry widget for search
entry = tk.Entry(root, font=("Arial",16), width=35, bd=2, relief=tk.GROOVE)
entry.pack(pady=30)
entry.focus()
#search button
search_btn = tk.Button(root, text="Google search",font=("Arial",12),command=search)
search_btn.pack()
#Bind Enter key to trigger search
root.bind('<Return>',lambda event: search())
#Run the app
root.mainloop()