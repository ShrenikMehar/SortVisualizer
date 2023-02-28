import time
import random
import sys

from tkinter import Tk, Canvas
import tkinter as tk

import colorsys


def draw_bars(canvas, bars):
    canvas.delete("all")
    canvas_width = int(canvas.cget("width"))
    canvas_height = int(canvas.cget("height"))

    bar_width = min(10, canvas_width // len(bars))
    bar_gap = 2

    for i, bar_height in enumerate(bars):
        x0 = i * (bar_width + bar_gap)
        y0 = canvas_height - bar_height
        x1 = x0 + bar_width
        y1 = canvas_height

        # Generate a rainbow color based on the bar's value
        hue = (bar_height / canvas_height) * 0.7  # Map bar height to a hue value in [0, 0.7]
        saturation = 1.0
        value = 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
        fill_color = f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

        canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color, outline="black")

    canvas.update()

def bubble_sort(canvas, bars):
    for i in range(len(bars)):
        swapped = False

        for j in range(len(bars) - i - 1):
            if bars[j] > bars[j+1]:
                bars[j], bars[j+1] = bars[j+1], bars[j]
                swapped = True
                draw_bars(canvas, bars)
                time.sleep(0.0001)

        if not swapped:
            break


def selection_sort(canvas, bars):
    for i in range(len(bars)):
        min_idx = i
        for j in range(i+1, len(bars)):
            if bars[j] < bars[min_idx]:
                min_idx = j

        bars[i], bars[min_idx] = bars[min_idx], bars[i]
        draw_bars(canvas, bars)
        time.sleep(0.05)


def insertion_sort(canvas, bars):
    for i in range(1, len(bars)):
        key = bars[i]
        j = i - 1
        while j >= 0 and key < bars[j]:
            bars[j + 1] = bars[j]
            j -= 1
            draw_bars(canvas, bars)
            time.sleep(0.001)
        bars[j + 1] = key
        draw_bars(canvas, bars)
        time.sleep(0.001)


def quick_sort(canvas, bars, low, high):
    if low < high:
        pi = partition(canvas, bars, low, high)

        quick_sort(canvas, bars, low, pi-1)
        quick_sort(canvas, bars, pi+1, high)

def partition(canvas, bars, low, high):
    pivot = bars[high]
    i = low - 1

    for j in range(low, high):
        if bars[j] < pivot:
            i += 1
            bars[i], bars[j] = bars[j], bars[i]
            draw_bars(canvas, bars)
            time.sleep(0.01)

    bars[i+1], bars[high] = bars[high], bars[i+1]
    draw_bars(canvas, bars)
    time.sleep(0.01)

    return i+1

def radix_sort(canvas, bars):
    max_val = max(bars)
    num_digits = len(str(max_val))

    for d in range(num_digits):
        buckets = [[] for _ in range(10)]

        for bar in bars:
            digit = (bar // 10 ** d) % 10
            buckets[digit].append(bar)

        bars = [bar for bucket in buckets for bar in bucket]

        draw_bars(canvas, bars)
        time.sleep(0.5)


class SortingAlgorithmSelector:
    def __init__(self, master):
        self.master = master
        master.title("Select Sorting Algorithm")
        master.geometry("1200x400")
        master.config(bg="#d4d4d4")

        self.title_label = tk.Label(master, text="Select Sorting Algorithm", font=("Arial", 24), bg="#d4d4d4")
        self.title_label.pack(pady=(20, 10))

        self.flag = 0

        self.bubble_sort_button = tk.Button(master, text="Bubble Sort", font=("Arial", 14), bg="#f2f2f2", bd=0, padx=20, pady=10, command=self.bubble_sort)
        self.bubble_sort_button.pack(fill="x", padx=20, pady=(10, 5))

        self.selection_sort_button = tk.Button(master, text="Selection Sort", font=("Arial", 14), bg="#e6e6e6", bd=0, padx=20, pady=10, command=self.selection_sort)
        self.selection_sort_button.pack(fill="x", padx=20, pady=5)

        self.insertion_sort_button = tk.Button(master, text="Insertion Sort", font=("Arial", 14), bg="#d9d9d9", bd=0, padx=20, pady=10, command=self.insertion_sort)
        self.insertion_sort_button.pack(fill="x", padx=20, pady=5)

        self.quick_sort_button = tk.Button(master, text="Radix Sort", font=("Arial", 14), bg="#cccccc", bd=0, padx=20, pady=10, command=self.quick_sort)
        self.quick_sort_button.pack(fill="x", padx=20, pady=5)

        self.merge_sort_button = tk.Button(master, text="Quick Sort", font=("Arial", 14), bg="#bfbfbf", bd=0, padx=20, pady=10, command=self.merge_sort)
        self.merge_sort_button.pack(fill="x", padx=20, pady=5)

        self.exit_button = tk.Button(master, text="Exit", font=("Arial", 14), bg="#b3b3b3", bd=0, padx=20, pady=10, command=self.exit_program)
        self.exit_button.pack(fill="x", padx=20, pady=(5, 20))

    def bubble_sort(self):
        self.flag = 1
        self.master.destroy()

    def selection_sort(self):
        self.flag = 2
        self.master.destroy()

    def insertion_sort(self):
        self.flag = 3
        self.master.destroy()

    def quick_sort(self):
        self.flag = 4
        self.master.destroy()

    def merge_sort(self):
        self.flag = 5
        self.master.destroy()

    def exit_program(self):
        self.master.destroy()

    

if __name__ == '__main__':
    rootx = tk.Tk()
    app = SortingAlgorithmSelector(rootx)
    rootx.mainloop()

    root = Tk()
    canvas = Canvas(root, width=1200, height=400)
    canvas.pack()

    bars = [random.randint(1, 300) for i in range(100)]
    draw_bars(canvas, bars)

    if(app.flag==1):
        bubble_sort(canvas, bars)
    
    elif(app.flag==2):
        selection_sort(canvas, bars)

    elif(app.flag==3):
        insertion_sort(canvas, bars)
    
    elif(app.flag==4):
        radix_sort(canvas, bars)

    elif(app.flag==5):
        quick_sort(canvas,bars, 0, len(bars)-1)

    root.mainloop()