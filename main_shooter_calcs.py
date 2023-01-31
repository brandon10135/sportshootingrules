import tkinter as tk
from tkinter import ttk
from shooter_calcs import *

def distance_to_target():
    object_size_actual = object_inches.get()
    object_size_mils = object_mils.get()

    object_distance = distance_in_yards(object_size_actual,object_size_mils)

    output_label.config(text=f"Distance in yards: {object_distance}")

def correction_required():
    correction_inches_seen = correction_inches.get()
    known_distance = entered_distance.get()
    
    correction_factor = correction_moa(correction_inches_seen,known_distance)

    correction_final_label.config(text=f"MOA change required: {correction_factor}")

def windange_correction_calc():
    range_to_target = windage_range.get()
    windspeed = windspeed_entry.get()

    correction_needed_windage = wind_correction(range_to_target,windspeed)

    windage_final_label.config(text=f"MOA change required: {correction_needed_windage}")

def headwind_tailwind_calc():
    range_to_target_hw_tw = headwind_range.get()
    windspeed_hw_tw = headwind_tailwind_entry.get()
    hw_or_tw = combobox.get()

    correction_needed_hw_tw = hw_tw_correction(range_to_target_hw_tw,windspeed_hw_tw,hw_or_tw)

    if hw_or_tw == "Headwind":
        headwind_final_label.config(text=f"MOA change required: {correction_needed_hw_tw}")
    else:
        headwind_final_label.config(text=f"MOA change required: - {correction_needed_hw_tw}")

#Initialize and start the GUI.

gui = tk.Tk()
gui.title("I suck at shooting")

gui.geometry("750x750")

#Start the collection and tkinter coding for yards calculation.

input_label = tk.Label(gui, text="Calculate distance to your target in yards.")
input_label.place(x=0,y=10)

input_label = tk.Label(gui, text="Input Object size (inches):")
input_label.place(x=0,y=40)

object_inches = tk.Entry(gui)
object_inches.place(x=4,y=60)

input_label = tk.Label(gui, text="Input Object size (mils):")
input_label.place(x=0,y=80)

object_mils = tk.Entry(gui)
object_mils.place(x=4,y=100)

distance_button = tk.Button(gui, text="Get distance to target", command=distance_to_target)
distance_button.place(x=4,y=120)

output_label = tk.Label(gui, text="")
output_label.place(x=2,y=150)

#Start the collection and tkinter coding for inches of correction.

input_label = tk.Label(gui, text="Calculate MOA correction based on how short or long the shot was.")
input_label.place(x=0,y=180)

correction_label = tk.Label(gui, text= "Please input amount short of target (inches).")
correction_label.place(x=0,y=210)

correction_inches = tk.Entry(gui)
correction_inches.place(x=4,y=230)

distance_for_calc_label = tk.Label(gui, text= "Please input distance to target (yards).")
distance_for_calc_label.place(x=0,y=250)

entered_distance = tk.Entry(gui)
entered_distance.place(x=4,y=270)

correction_final_label = tk.Label(gui, text="")
correction_final_label.place(x=2,y=320)

inches_of_correction_button = tk.Button(gui, text="Get correction required", command=correction_required)
inches_of_correction_button.place(x=4,y=290)

# Start the collection of data for windage rule and correction. 

input_label = tk.Label(gui, text="Calculate MOA correction based on full crosswind (90 degrees to bullet path).")
input_label.place(x=0,y=350)

windage_range_label = tk.Label(gui, text= "Please input distance to target (yards).")
windage_range_label.place(x=0,y=380)

windage_range = tk.Entry(gui)
windage_range.place(x=4,y=400)

windspeed_label = tk.Label(gui, text= "Please input windspeed.")
windspeed_label.place(x=0,y=420)

windspeed_entry = tk.Entry(gui)
windspeed_entry.place(x=4,y=440)

windage_final_label = tk.Label(gui, text="")
windage_final_label.place(x=2,y=490)

inches_of_correction_button = tk.Button(gui, text="Get correction required", command=windange_correction_calc)
inches_of_correction_button.place(x=4,y=460)

#Headwind and Tailwind calculations gathering

headwind_label = tk.Label(gui, text="Calculate MOA correction based on headwind or tailwind.")
headwind_label.place(x=0,y=520)

headwind_range_label = tk.Label(gui, text= "Please input distance to target (yards).")
headwind_range_label.place(x=0,y=540)

headwind_range = tk.Entry(gui)
headwind_range.place(x=4,y=560)

headwind_tailwind_label = tk.Label(gui, text= "Please input windspeed.")
headwind_tailwind_label.place(x=0,y=580)

headwind_tailwind_entry = tk.Entry(gui)
headwind_tailwind_entry.place(x=4,y=600)

headwind_final_label = tk.Label(gui, text="")
headwind_final_label.place(x=2,y=650)

headwind_tailwind_button = tk.Button(gui, text="Get correction required", command=headwind_tailwind_calc)
headwind_tailwind_button.place(x=4,y=620)

options = ['Headwind', 'Tailwind']

# Creating combobox
combobox = ttk.Combobox(gui, values=options, state="readonly")
combobox.current(0)
combobox.place(x = 215, y = 540)

gui.mainloop()
