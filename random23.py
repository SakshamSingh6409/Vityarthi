'''import tkinter as tk

class AnimatedButton:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Disappearing Button")
        self.root.geometry("400x300")
        self.root.configure(bg="#e8e6f0")
        
        # Container frame
        container = tk.Frame(root, bg="#e8e6f0")
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Expanded button (with social icons) - positioned first so it's behind
        self.expanded_btn = tk.Canvas(container, width=250, height=60, 
                                     bg="#e8e6f0", highlightthickness=0)
        self.expanded_btn.pack()
        
        # Draw rounded rectangle for expanded button
        self.draw_rounded_rect(self.expanded_btn, 10, 10, 240, 50, 25, 
                              outline="#5855d6", width=2, fill="#5855d6")
        
        # Add glow effect (light circle on left)
        self.expanded_btn.create_oval(15, 15, 65, 65, 
                                     fill="#7b79e8", outline="")
        
        # Social media icons
        icons = ["f", "📷", "🐦", "in"]
        x_positions = [50, 95, 140, 185]
        
        for icon, x in zip(icons, x_positions):
            self.expanded_btn.create_text(x, 30, text=icon, 
                                         font=("Arial", 16, "bold"), 
                                         fill="white")
        
        # Initial button (SAHRE text) - positioned on top
        self.initial_btn = tk.Canvas(container, width=250, height=60, 
                                    bg="#e8e6f0", highlightthickness=0)
        self.initial_btn.place(x=0, y=0)
        
        # Draw rounded rectangle for initial button
        self.draw_rounded_rect(self.initial_btn, 10, 10, 240, 50, 25, 
                              outline="#5855d6", width=3, fill="white")
        
        # Add text
        self.initial_btn.create_text(125, 30, text="SAHRE", 
                                    font=("Arial", 18, "bold"), 
                                    fill="#5855d6")
        
        # Animation variables
        self.alpha = 1.0
        self.is_animating = False
        
        # Bind hover events
        self.initial_btn.bind("<Enter>", self.start_fade_out)
        self.initial_btn.bind("<Leave>", self.start_fade_in)
        
        # Cursor effects
        self.expanded_btn.bind("<Enter>", lambda e: self.root.config(cursor="hand2"))
        self.expanded_btn.bind("<Leave>", lambda e: self.root.config(cursor=""))
    
    def draw_rounded_rect(self, canvas, x1, y1, x2, y2, radius, **kwargs):
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2,
            x1, y2-radius,
            x1, y1+radius,
            x1, y1
        ]
        return canvas.create_polygon(points, smooth=True, **kwargs)
    
    def start_fade_out(self, event):
        if not self.is_animating and self.alpha > 0:
            self.root.config(cursor="hand2")
            self.is_animating = True
            self.fade_out()
    
    def start_fade_in(self, event):
        if self.alpha < 1.0:
            self.root.config(cursor="")
            self.fade_in()
    
    def fade_out(self):
        if self.alpha > 0:
            self.alpha -= 0.05
            # Fade effect by moving up and scaling
            self.initial_btn.place(x=0, y=-int((1-self.alpha)*30))
            
            # Create fade effect by adjusting colors
            gray_level = int(255 * (1 - self.alpha))
            fill_color = f"#{gray_level:02x}{gray_level:02x}{gray_level:02x}"
            
            self.root.after(20, self.fade_out)
        else:
            self.initial_btn.place_forget()
            self.is_animating = False
    
    def fade_in(self):
        if self.alpha < 1.0:
            self.alpha += 0.05
            if self.alpha > 1.0:
                self.alpha = 1.0
            
            # Fade in effect
            self.initial_btn.place(x=0, y=-int((1-self.alpha)*30))
            self.root.after(20, self.fade_in)
        else:
            self.initial_btn.place(x=0, y=0)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedButton(root)
    root.mainloop()'''
'''
import tkinter as tk
import math
import random

class LiquidGlass:
    def __init__(self, root):
        self.root = root
        self.root.title("Liquid Glass Effect")
        self.root.configure(bg='#1a1a2e')
        
        # Canvas setup
        self.width = 800
        self.height = 600
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, 
                                bg='#0f0f1e', highlightthickness=0)
        self.canvas.pack()
        
        # Create background gradient
        self.create_background()
        
        # Blob properties
        self.blobs = []
        self.num_blobs = 5
        self.init_blobs()
        
        # Animation
        self.animate()
    
    def create_background(self):
        """Create a gradient background"""
        for i in range(self.height):
            ratio = i / self.height
            r = int(15 + (30 - 15) * ratio)
            g = int(15 + (30 - 15) * ratio)
            b = int(30 + (60 - 30) * ratio)
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.canvas.create_line(0, i, self.width, i, fill=color, width=1)
    
    def init_blobs(self):
        """Initialize blob objects"""
        colors = ['#4a90e2', '#e24a90', '#90e24a', '#e2904a', '#904ae2']
        
        for i in range(self.num_blobs):
            blob = {
                'x': random.randint(100, self.width - 100),
                'y': random.randint(100, self.height - 100),
                'radius': random.randint(60, 120),
                'dx': random.uniform(-1.5, 1.5),
                'dy': random.uniform(-1.5, 1.5),
                'color': colors[i % len(colors)],
                'phase': random.uniform(0, 2 * math.pi),
                'oval': None,
                'inner_ovals': []
            }
            self.blobs.append(blob)
    
    def draw_blob(self, blob):
        """Draw a single blob with glass effect"""
        x, y = blob['x'], blob['y']
        r = blob['radius']
        
        # Delete old shapes
        if blob['oval']:
            self.canvas.delete(blob['oval'])
        for oval in blob['inner_ovals']:
            self.canvas.delete(oval)
        blob['inner_ovals'] = []
        
        # Add organic movement to radius
        wobble = math.sin(blob['phase']) * 10
        current_r = r + wobble
        
        # Main blob with semi-transparency effect (using stipple)
        blob['oval'] = self.canvas.create_oval(
            x - current_r, y - current_r,
            x + current_r, y + current_r,
            fill=blob['color'], outline='',
            stipple='gray50'
        )
        
        # Inner highlight for glass effect
        highlight = self.canvas.create_oval(
            x - current_r * 0.6, y - current_r * 0.6,
            x + current_r * 0.3, y + current_r * 0.3,
            fill='white', outline='',
            stipple='gray25'
        )
        blob['inner_ovals'].append(highlight)
        
        # Outer glow
        for i in range(3):
            scale = 1 + (i + 1) * 0.08
            glow = self.canvas.create_oval(
                x - current_r * scale, y - current_r * scale,
                x + current_r * scale, y + current_r * scale,
                fill='', outline=blob['color'],
                width=2, stipple='gray12'
            )
            blob['inner_ovals'].append(glow)
    
    def update_blob(self, blob):
        """Update blob position and properties"""
        # Update position
        blob['x'] += blob['dx']
        blob['y'] += blob['dy']
        
        # Bounce off edges
        if blob['x'] - blob['radius'] < 0 or blob['x'] + blob['radius'] > self.width:
            blob['dx'] *= -1
            blob['x'] = max(blob['radius'], min(self.width - blob['radius'], blob['x']))
        
        if blob['y'] - blob['radius'] < 0 or blob['y'] + blob['radius'] > self.height:
            blob['dy'] *= -1
            blob['y'] = max(blob['radius'], min(self.height - blob['radius'], blob['y']))
        
        # Update phase for wobble effect
        blob['phase'] += 0.05
    
    def animate(self):
        """Main animation loop"""
        for blob in self.blobs:
            self.update_blob(blob)
            self.draw_blob(blob)
        
        # Schedule next frame
        self.root.after(30, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = LiquidGlass(root)
    root.mainloop()

'''

from tkinter import *
from tkinter import ttk
win = Tk()
win.title("Sarah")

def clickMe():
    #button1.configure(text="Hello " + name.get())
    ttk.Label(win, text="Welcome to Tkinter!"+name.get()).grid(column=0, row=3)

#text
ttk.Label(win, text="Enter your name:").grid(column=0, row=0)

name = StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

button1 = ttk.Button(win, text="Click Me", command=clickMe)
button1.grid(column=1, row=1)

win.mainloop()