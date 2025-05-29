import tkinter as tk
import math
import time

class AnalogStopwatch:
    def __init__(self, root):  # fixed __init__
        self.root = root
        self.root.title("Analog Stopwatch")

        self.canvas_size = 300
        self.center = self.canvas_size // 2
        self.radius = 100

        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white')
        self.canvas.pack()

        self.start_time = None
        self.running = False
        self.hand = None
        self.elapsed = 0  # added initialization

        self.draw_watch_face()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="start", command=self.start).pack(side='left', padx=5)
        tk.Button(btn_frame, text="stop", command=self.stop).pack(side='left', padx=5)
        tk.Button(btn_frame, text="reset", command=self.reset).pack(side='left', padx=5)

    def draw_watch_face(self):
        self.canvas.create_oval(
            self.center - self.radius, self.center - self.radius,
            self.center + self.radius, self.center + self.radius,
            outline="black", width=2
        )
        for i in range(12):
            angle = math.radians(i * 30)
            x_inner = self.center + (self.radius - 10) * math.sin(angle)
            y_inner = self.center - (self.radius - 10) * math.cos(angle)
            x_outer = self.center + self.radius * math.sin(angle)
            y_outer = self.center - self.radius * math.cos(angle)
            self.canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=2)

    def update_hand(self):
        if not self.running:
            return
        elapsed = time.time() - self.start_time
        seconds = int(elapsed % 60)
        angle = math.radians(seconds * 6)

        x = self.center + (self.radius - 20) * math.sin(angle)
        y = self.center - (self.radius - 20) * math.cos(angle)
        if self.hand:
            self.canvas.delete(self.hand)
        self.hand = self.canvas.create_line(
            self.center, self.center, x, y,
            fill="red", width=3
        )
        self.root.after(1000, self.update_hand)

    def start(self):
        if not self.running:
            self.running = True
            if self.start_time is None:
                self.start_time = time.time()
            else:
                self.start_time = time.time() - self.elapsed
            self.update_hand()

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed = time.time() - self.start_time

    def reset(self):
        if self.running:
            self.running = False
        self.start_time = None
        self.elapsed = 0
        if self.hand:
            self.canvas.delete(self.hand)
            self.hand = None

# Run the stopwatch
root = tk.Tk()
app = AnalogStopwatch(root)  # pass root
root.mainloop()
