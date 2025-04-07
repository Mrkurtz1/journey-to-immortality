import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib.pyplot as plt

time_per_stam = 15 * 60  # Seconds for a stam

title_levels_fon = {
    "C3": 0, "C2": 1, "C1": 2,
    "S3": 3, "S2": 4, "S1": 5,
    "B3": 6, "B2": 7, "B1": 8,
    "E6": 9, "E5": 10, "E4": 11,
    "E3": 12, "E2": 13, "E1": 14
}

title_levels_j = {
    "Q1": 0, "Q2": 1, "Q3": 2,
    "B1": 3, "B2": 4, "B3": 5,
    "C1": 6, "C2": 7, "C3": 8,
    "N1": 9, "N2": 10, "N3": 11,
    "N4": 12, "N5": 13, "N6": 14
}

know_gain = [
    100, 200, 300, 400, 500, 600, 700, 800,
    900, 1000, 1100, 1200, 1300, 1400, 1500
]

exp_req = [
    41000, 288000, 497000, 747000, 1050000,
    1410000, 1870000, 2360000, 2980000, 3660000,
    4460000, 5340000, 6340000, 7490000, 8730000
]

def calc_time_with_stam(exp, exp_rate, knowledge_gain):
    initial_time = exp / exp_rate
    max_stam = math.floor(initial_time / time_per_stam)

    final_time = 0
    for curr_stam in range(int(max_stam), -1, -1):
        curr_time = (exp - (knowledge_gain * 40 * curr_stam)) / exp_rate
        if curr_time > (curr_stam * time_per_stam):
            final_time = curr_time
            break
    return final_time

def exp_per_sec(knowledge_gain):
    return (knowledge_gain * 1.3) / 8

def secs_to_hours(secs):
    return secs / 3600

def compute():
    event_type = type_var.get()
    title = title_entry.get().strip()
    try:
        current_exp = int(exp_entry.get().strip())
    except ValueError:
        messagebox.showerror("Invalid Input", "Experience must be a number.")
        return

    if event_type == "Journey":
        index_map = title_levels_j
        level_keys = list(title_levels_j.keys())
    elif event_type == "Feast of Nature":
        index_map = title_levels_fon
        level_keys = list(title_levels_fon.keys())
    else:
        messagebox.showerror("Invalid Event", "Select a valid event type.")
        return

    if title not in index_map:
        messagebox.showerror("Invalid Title", f"Title {title} not recognized for {event_type}.")
        return

    start_index = index_map[title]
    cumulative_hours = []
    tier_labels = []

    curr_lvl_exp = exp_req[start_index] - current_exp
    total_time = calc_time_with_stam(
        curr_lvl_exp,
        exp_per_sec(know_gain[start_index]),
        know_gain[start_index]
    )
    cumulative_hours.append(secs_to_hours(total_time))
    tier_labels.append(level_keys[start_index + 1] if start_index + 1 < len(level_keys) else "Max")

    for i in range(start_index + 1, len(exp_req)):
        time_for_lvl = calc_time_with_stam(
            exp_req[i],
            exp_per_sec(know_gain[i]),
            know_gain[i]
        )
        total_time += time_for_lvl
        cumulative_hours.append(secs_to_hours(total_time))
        tier_labels.append(level_keys[i + 1] if i + 1 < len(level_keys) else "Max")

    result_var.set(f"Total Hours Remaining: {round(total_time/3600, 2)}")

    # Line chart: x = cumulative hours, y = tiers
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_hours, tier_labels, marker='o', linestyle='-')
    plt.xlabel('Cumulative Hours')
    plt.ylabel('Tiers')
    plt.title('Tier Progression Over Time')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("Experience Time Tracker")

ttk.Label(root, text="Event Type:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
type_var = tk.StringVar()
ttk.Combobox(root, textvariable=type_var, values=["Journey", "Feast of Nature"]).grid(row=0, column=1)

ttk.Label(root, text="Current Title (e.g. C3, Q2):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
title_entry = ttk.Entry(root)
title_entry.grid(row=1, column=1)

ttk.Label(root, text="Current EXP:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
exp_entry = ttk.Entry(root)
exp_entry.grid(row=2, column=1)

ttk.Button(root, text="Compute Time", command=compute).grid(row=3, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
ttk.Label(root, textvariable=result_var).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
