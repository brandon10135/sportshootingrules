import tkinter as tk
from tkinter import *
from tkinter import ttk
from shooter_calcs import *


def distance_to_target():
    #Calculate the distance to the target

    object_size_actual = object_inches.get()
    object_size_mils = object_mils.get()

    object_distance = distance_in_yards(object_size_actual,object_size_mils)

    output_label.config(text=f"Distance in yards: {object_distance}")

def correction_required():
    #Calculate the correction requird from when you shoot and are either short or long
    correction_inches_seen = correction_inches.get()
    known_distance = entered_distance.get()
    
    correction_factor = correction_moa(correction_inches_seen,known_distance)

    correction_final_label.config(text=f"MOA change required: {correction_factor}")

def windange_correction_calc():
    #Correction calcultion for when you are battling the wind
    range_to_target = windage_range.get()
    windspeed = windspeed_entry.get()

    correction_needed_windage = wind_correction(range_to_target,windspeed)

    windage_final_label.config(text=f"MOA change required: {correction_needed_windage}")

def headwind_tailwind_calc():
    #Headwind or tailwind calculation start. It will return a negative or positive value depending on the headwind or tailwind. 
    range_to_target_hw_tw = headwind_range.get()
    windspeed_hw_tw = headwind_tailwind_entry.get()
    hw_or_tw = combobox.get()

    correction_needed_hw_tw = hw_tw_correction(range_to_target_hw_tw,windspeed_hw_tw,hw_or_tw)

    if hw_or_tw == "Headwind":
        headwind_final_label.config(text=f"Yardage change required: {correction_needed_hw_tw}")
    else:
        headwind_final_label.config(text=f"Yardage change required: - {correction_needed_hw_tw}")

def sights_adjuster():
    sight_height = sight_height_entry.get()
    known_zero_range = combobox_known_range.get()
    desired_zero_range = combobox_desired_range.get()
    bullet_type = combobox_bullet_type.get()

    final_sight_answer = new_range_zero(sight_height,known_zero_range,desired_zero_range,bullet_type)

    sight_adujustment_final_label.config(text=f"Required change in inches: {final_sight_answer}")

def sights_adjuster_moa():
    sight_height_moa = sight_height_entry_moa.get()
    known_zero_range_moa = combobox_known_range_moa.get()
    desired_zero_range_moa = combobox_desired_range_moa.get()
    bullet_type_moa = combobox_bullet_type_moa.get()

    final_moa_adjustment = new_range_zero_moa(sight_height_moa,known_zero_range_moa,desired_zero_range_moa,bullet_type_moa)
    sight_adujustment_final_label_moa.config(text=f"Required change in MOA: {final_moa_adjustment}")


#Initialize and start the GUI.

gui = tk.Tk()
gui.title("I suck at shooting")

gui.geometry("750x750")

notebook = ttk.Notebook(gui)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text='Correction Factors')
notebook.add(tab2, text='Adjusting zero range')

notebook.pack(expand=1, fill='both')

#Start the collection and tkinter coding for yards calculation.

input_label = tk.Label(tab1, text="Calculate distance to your target in yards.")
input_label.place(x=0,y=20)

input_label = tk.Label(tab1, text="Input Object size (inches):")
input_label.place(x=0,y=50)

object_inches = tk.Entry(tab1)
object_inches.place(x=4,y=70)

input_label = tk.Label(tab1, text="Input Object size (mils):")
input_label.place(x=0,y=90)

object_mils = tk.Entry(tab1)
object_mils.place(x=4,y=110)

distance_button = tk.Button(tab1, text="Get distance to target", command=distance_to_target)
distance_button.place(x=4,y=130)

output_label = tk.Label(tab1, text="")
output_label.place(x=2,y=160)

#Start the collection and tkinter coding for inches of correction.

input_label = tk.Label(tab1, text="Calculate MOA correction based on how short or long the shot was.")
input_label.place(x=0,y=190)

correction_label = tk.Label(tab1, text= "Please input amount short of target (inches).")
correction_label.place(x=0,y=220)

correction_inches = tk.Entry(tab1)
correction_inches.place(x=4,y=240)

distance_for_calc_label = tk.Label(tab1, text= "Please input distance to target (yards).")
distance_for_calc_label.place(x=0,y=260)

entered_distance = tk.Entry(tab1)
entered_distance.place(x=4,y=280)

correction_final_label = tk.Label(tab1, text="")
correction_final_label.place(x=2,y=330)

inches_of_correction_button = tk.Button(tab1, text="Get correction required", command=correction_required)
inches_of_correction_button.place(x=4,y=300)

# Start the collection of data for windage rule and correction. 

input_label = tk.Label(tab1, text="Calculate MOA correction based on full crosswind (90 degrees to bullet path).")
input_label.place(x=0,y=360)

windage_range_label = tk.Label(tab1, text= "Please input distance to target (yards).")
windage_range_label.place(x=0,y=390)

windage_range = tk.Entry(tab1)
windage_range.place(x=4,y=410)

windspeed_label = tk.Label(tab1, text= "Please input windspeed.")
windspeed_label.place(x=0,y=430)

windspeed_entry = tk.Entry(tab1)
windspeed_entry.place(x=4,y=450)

windage_final_label = tk.Label(tab1, text="")
windage_final_label.place(x=2,y=500)

inches_of_correction_button = tk.Button(tab1, text="Get correction required", command=windange_correction_calc)
inches_of_correction_button.place(x=4,y=470)

#Headwind and Tailwind calculations gathering

headwind_label = tk.Label(tab1, text="Calculate yardage correction based on headwind or tailwind.")
headwind_label.place(x=0,y=530)

headwind_range_label = tk.Label(tab1, text= "Please input distance to target (yards).")
headwind_range_label.place(x=0,y=550)

headwind_range = tk.Entry(tab1)
headwind_range.place(x=4,y=570)

headwind_tailwind_label = tk.Label(tab1, text= "Please input windspeed.")
headwind_tailwind_label.place(x=0,y=590)

headwind_tailwind_entry = tk.Entry(tab1)
headwind_tailwind_entry.place(x=4,y=610)

headwind_final_label = tk.Label(tab1, text="")
headwind_final_label.place(x=2,y=660)

headwind_tailwind_button = tk.Button(tab1, text="Get correction required", command=headwind_tailwind_calc)
headwind_tailwind_button.place(x=4,y=630)

options = ['Headwind', 'Tailwind']

# Creating combobox
combobox = ttk.Combobox(tab1, values=options, state="readonly")
combobox.current(0)
combobox.place(x = 215, y = 550)

#Creates 

sight_adjustment = tk.Label(tab2, text="Calculate sight ajustment from known zero to another range.")
sight_adjustment.place(x=0,y=10)

sight_adjustment_label= tk.Label(tab2, text= "Please input sight height from barrel in inches. (Ex. 1.5)")
sight_adjustment_label.place(x=0,y=40)

sight_height_entry = tk.Entry(tab2)
sight_height_entry.place(x=4,y=60)

# Creating comboboxes which pull information from Hornady ballistics excel sheet

options_bullets = ["25 gr. HP","24 gr. NTX (26” Bbl)","32 gr. V-MAX (26” Bbl)","40 gr. V-MAX (26” Bbl)","45 gr. SP (26” Bbl)","60 gr. V-MAX (Steel Case)(16” Bbl)","60 gr. V-MAX (Steel Case)(16 Bbl)","35 gr.V-MAX","45 gr. SP","45 gr. HP","35 gr. NTX","50 gr. V-MAX","35 gr. NTX","40 gr. V-MAX","50 gr. GMX","53 gr. V-MAX","55 gr. HP","55 gr. GMX","55 gr. V-MAX","55 gr. HP (Steel Case)","62 gr. FMJ","68 gr. BTHP","73 gr. ELD Match","75 gr. BTHP","75 gr. BTHP","75 gr. BTHP","75 gr. BTHP (Steel Case)","55 gr. GMX (20” Bbl)","62 gr. FMJ (20” Bbl)","75 gr. BTHP (20” Bbl)","75 gr. InterLock HD SBR^{™}(20” Bbl)","35 gr. NTX","40 gr. V-MAX","50 gr. V-MAX","50 gr. V-MAX","55 gr. V-MAX","55 gr. V-MAX","58 gr. V-MAX","75 gr. V-MAX","80 gr. GMX","80 gr. GMX","87 gr. SST","95 gr. SST","100 gr. InterLock BTSP","95 gr. SST","108 gr. ELD Match","110 gr. FTX","100 gr. InterLock SP","117 gr. SST","90 gr. GMX","90 gr. GMX","117 gr. SST","117 gr. InterLock BTSP","90 gr. GMX","123 gr. ELD Match","123 gr. SST","140 gr. BTHP","140 gr. SST","129 gr. SST","130 gr. ELD Match","120 gr. GMX","120 gr. GMX","120 gr. ELD Match","129 gr. SST","129 gr. InterBond","129 gr. InterLock","140 gr. ELD Match","140 gr. BTHP","143 gr. ELD-X","147 gr. ELD Match","140 gr. InterLock SP","100 gr. GMX","110 gr. V-MAX (16” Bbl)","110 gr. BTHP W/C","120 gr. SST (16” Bbl)","120 gr. SST","130 gr. GMX","130 gr. InterBond","130 gr. GMX","130 gr. SST","130 gr. InterLock SP","140 gr. SST","140 gr. InterLock SP","140 gr. InterLock BTSP","145 gr. ELD-X","150 gr. InterLock SP","139 gr. SST","140 gr. InterLock SP","120 gr. SST","139 gr. GMX","139 gr. GMX","139 gr. SST","139 gr. InterLock SP","150 gr. ELD-X","139 gr. GMX","139 gr. SST","150 gr. ELD-X","139 gr. GMX","139 gr. InterLock SP","139 gr. SST","139 gr. GMX","139 gr. SST","154 gr. InterLock SP","154 gr. InterBond","154 gr. SST","154 gr. InterLock SP","162 gr. SST","162 gr. ELD-X","162 gr. InterLock BTSP","139 gr. GMX","140 gr. MonoFlex","160 gr. FTX","150 gr. SST","125 gr. SST","150 gr. SST","150 gr. GMX","150 gr. InterBond","150 gr. InterLock SP","150 gr. SST","155 gr. BTHP (Steel Case)","155 gr. A-MAX","155 gr. ELD Match","155 gr. BTHP","165 gr. InterLock SP","165 gr. GMX","165 gr. SST","165 gr. InterBond","165 gr. GMX","165 gr. InterLock BTSP","168 gr. BTHP","168 gr. ELD Match","168 gr. ELD Match","168 gr. A-MAX","178 gr. BTHP","178 gr. BTHP","178 gr. ELD-X","125 gr. SST","150 gr. SST","150 gr. GMX","150 gr. InterLock SP","165 gr. GMX","165 gr. InterBond","165 gr. SST","165 gr. GMX","165 gr. InterLock BTSP","168 gr. ELD Match","178 gr. ELD-X","180 gr. InterLock SP","180 gr. GMX","180 gr. InterBond","180 gr. SST","180 gr. InterLock SP","200 gr. ELD-X","150 gr. SST","150 gr. GMX","165 gr. SST","165 gr. GMX","178 gr. ELD-X","180 gr. SST","180 gr. InterBond","150 gr. SST","150 gr. GMX","150 gr. InterLock SP","165 gr. GMX","165 gr. GMX","165 gr. InterLock BTSP","178 gr. ELD Match","180 gr. InterLock SP","180 gr. GMX","180 gr. InterBond","180 gr. InterLock SP","180 gr. SST","195 gr. BTHP","200 gr. ELD-X","165 gr. GMX","180 gr. InterLock SP","180 gr. GMX","200 gr. ELD-X","180 gr. GMX","220 gr. ELD-X","180 gr. GMX","220 gr. ELD-X","123 gr. SST (Steel Case)(20” Bbl)","123 gr. SST (Steel Case)(20” Bbl)","150 gr. InterLock SP","174 gr. BTHP","195 gr. SP","196 gr. BTHP","200 gr. FTX","200 gr. SST","225 gr. SST","185 gr. GMX","200 gr. SST","225 gr. SST","250 gr. BTHP","250 gr. InterLock SP-RP","285 gr. ELD Match","285 gr. BTHP","200 gr. InterLock SP","200 gr. InterLock SP","286 gr. InterLock SP-RP","286 gr. InterLock SP-RP","225 gr. InterLock SP-RP","270 gr. InterLock SP-RP","250 gr. GMX","270 gr. InterLock SP-RP SF","270 gr. InterLock SP-RP","300 gr. DGS","300 gr. DGX","250 gr. GMX","270 gr. InterLock SP-RP SF","300 gr. DGX SF","300 gr. DGS SF","400 gr. DGX","400 gr. DGS","300 gr. InterLock SP","400 gr. DGX","400 gr. DGS","400 gr. DGX","400 gr. DGS","400 gr. DGX","400 gr. DGS","400 gr. DGX","400 gr. DGS","400 gr. DGX","400 gr. DGS","265 gr. InterLock FP","265 gr. FTX","250 gr. FTX (20” Bbl)","250 gr. MonoFlex","325 gr. FTX","325 gr. FTX","480 gr. DGX","480 gr. DGS","480 gr. DGX","480 gr. DGS","500 gr. DGX SF","500 gr. DGS SF","500 gr. DGX","500 gr. DGS","500 gr. DGX","500 gr. DGS","570 gr. DGX","570 gr. DGS","750 gr. A-MAX (36” Bbl)"]
options_range = ["100","200","300","400","500"]

sight_adjustment_label= tk.Label(tab2, text= "Please select type of bullet from dropdown list.")
sight_adjustment_label.place(x=0,y=80)

combobox_bullet_type = ttk.Combobox(tab2, values=options_bullets, state="readonly")
combobox_bullet_type.current(0)
combobox_bullet_type.place(x = 2, y = 100)

known_zero_label= tk.Label(tab2, text= "Please select known zero range of rifle.")
known_zero_label.place(x=0,y=120)

combobox_known_range = ttk.Combobox(tab2, values=options_range, state="readonly")
combobox_known_range.current(0)
combobox_known_range.place(x = 2, y = 140)

desired_zero_label= tk.Label(tab2, text= "Please select desired zero range of rifle.")
desired_zero_label.place(x=0,y=160)

combobox_desired_range = ttk.Combobox(tab2, values=options_range, state="readonly")
combobox_desired_range.current(0)
combobox_desired_range.place(x = 2, y = 180)

#Creating the final label and button which will provide the answer

sight_adjustment_button = tk.Button(tab2, text="Get correction required", command=sights_adjuster)
sight_adjustment_button.place(x=4,y=210)

sight_adujustment_final_label = tk.Label(tab2, text="")
sight_adujustment_final_label.place(x=2,y=240)

#Creating the data retrieval for MOA click on a range change 

sight_adjustment_moa = tk.Label(tab2, text="Calculate MOA ajustment from known zero to another range.")
sight_adjustment_moa.place(x=0,y=270)

sight_adjustment_moa_label= tk.Label(tab2, text= "Please input sight height from barrel in inches. (Ex. 1.5)")
sight_adjustment_moa_label.place(x=0,y=300)

sight_height_entry_moa = tk.Entry(tab2)
sight_height_entry_moa.place(x=4,y=320)

sight_adjustment_label= tk.Label(tab2, text= "Please select type of bullet from dropdown list.")
sight_adjustment_label.place(x=0,y=340)

combobox_bullet_type_moa = ttk.Combobox(tab2, values=options_bullets, state="readonly")
combobox_bullet_type_moa.current(0)
combobox_bullet_type_moa.place(x = 2, y = 360)

known_zero_label_moa= tk.Label(tab2, text= "Please select known zero range of rifle.")
known_zero_label_moa.place(x=0,y=380)

combobox_known_range_moa = ttk.Combobox(tab2, values=options_range, state="readonly")
combobox_known_range_moa.current(0)
combobox_known_range_moa.place(x = 2, y = 400)

desired_zero_label_moa= tk.Label(tab2, text= "Please select desired zero range of rifle.")
desired_zero_label_moa.place(x=0,y=420)

combobox_desired_range_moa = ttk.Combobox(tab2, values=options_range, state="readonly")
combobox_desired_range_moa.current(0)
combobox_desired_range_moa.place(x = 2, y = 440)

sight_adjustment_button_moa = tk.Button(tab2, text="Get correction required", command=sights_adjuster_moa)
sight_adjustment_button_moa.place(x=4,y=460)

sight_adujustment_final_label_moa = tk.Label(tab2, text="")
sight_adujustment_final_label_moa.place(x=2,y=490)

gui.mainloop()
