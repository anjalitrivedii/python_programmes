import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageEnhance
import datetime
import os


# Apply optional filter to image
def apply_filter(img, filter_type):
    if filter_type == "Grayscale":
        return img.convert("L").convert("RGB")
    elif filter_type == "Sepia":
        sepia = img.convert("RGB")
        width, height = sepia.size
        pixels = sepia.load()
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                pixels[x, y] = (min(tr, 255), min(tg, 255), min(tb, 255))
        return sepia
    else:
        return img


# Build polaroid frame with optional caption and date
def add_polaroid_frame(image_path, caption, include_date, filter_type):
    img = Image.open(image_path).convert("RGB")
    img = apply_filter(img, filter_type)
    img_width, img_height = img.size

    border_top = int(img_height * 0.1)
    border_side = int(img_width * 0.1)
    border_bottom = int(img_height * 0.3)

    frame_width = img_width + 2 * border_side
    frame_height = img_height + border_top + border_bottom

    frame = Image.new("RGB", (frame_width, frame_height), "white")
    frame.paste(img, (border_side, border_top))

    draw = ImageDraw.Draw(frame)

    # Border and line
    draw.rectangle([border_side, border_top, border_side + img_width, border_top + img_height],
                   outline="black", width=4)
    draw.line([(border_side, border_top + img_height + 5),
               (frame_width - border_side, border_top + img_height + 5)],
              fill="gray", width=2)

    # Font
    try:
        font = ImageFont.truetype("arial.ttf", int(img_height * 0.05))
    except:
        font = ImageFont.load_default()

    # Caption
    bbox = draw.textbbox((0, 0), caption, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (frame_width - text_width) // 2
    text_y = img_height + border_top + 10
    draw.text((text_x, text_y), caption, fill="black", font=font)

    # Date stamp (optional)
    if include_date:
        date_str = datetime.datetime.now().strftime("%d %b %Y")
        date_font = ImageFont.truetype("arial.ttf",
                                       int(img_height * 0.035)) if font != ImageFont.load_default() else font
        date_bbox = draw.textbbox((0, 0), date_str, font=date_font)
        date_width = date_bbox[2] - date_bbox[0]
        date_x = (frame_width - date_width) // 2
        date_y = text_y + bbox[3] - bbox[1] + 10
        draw.text((date_x, date_y), date_str, fill="gray", font=date_font)

    return frame


# Handle image selection
def select_image():
    global current_polaroid
    file_path = filedialog.askopenfilename()
    if file_path:
        caption = caption_entry.get()
        include_date = date_var.get()
        filter_type = filter_var.get()
        polaroid = add_polaroid_frame(file_path, caption, include_date, filter_type)
        polaroid.thumbnail((400, 500))
        polaroid_tk = ImageTk.PhotoImage(polaroid)

        image_label.config(image=polaroid_tk)
        image_label.image = polaroid_tk
        current_polaroid = polaroid  # Save for exporting


# Save final image
def save_image():
    if current_polaroid:
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                 filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
        if save_path:
            current_polaroid.save(save_path)
            messagebox.showinfo("Saved", f"Image saved to:\n{save_path}")
    else:
        messagebox.showwarning("No Image", "Please generate a polaroid image first.")


# GUI setup
root = tk.Tk()
root.title("Polaroid Camera Aesthetic")
root.geometry("520x700")
root.configure(bg="white")

caption_label = tk.Label(root, text="Enter Caption:", bg="white", font=("Arial", 12))
caption_label.pack(pady=5)

caption_entry = tk.Entry(root, width=40, font=("Arial", 12))
caption_entry.pack(pady=5)

filter_var = tk.StringVar(value="Normal")
filter_label = tk.Label(root, text="Select Filter:", bg="white", font=("Arial", 12))
filter_label.pack(pady=5)
filter_menu = tk.OptionMenu(root, filter_var, "Normal", "Grayscale", "Sepia")
filter_menu.pack(pady=5)

date_var = tk.BooleanVar()
date_check = tk.Checkbutton(root, text="Add Date", variable=date_var, bg="white", font=("Arial", 12))
date_check.pack(pady=5)

upload_btn = tk.Button(root, text="Upload Image", command=select_image, bg="#f0f0f0", font=("Arial", 12))
upload_btn.pack(pady=10)

save_btn = tk.Button(root, text="Save Polaroid", command=save_image, bg="#dff0d8", font=("Arial", 12))
save_btn.pack(pady=5)

image_label = tk.Label(root, bg="white")
image_label.pack(pady=10)

current_polaroid = None  # To store the generated image

root.mainloop()
