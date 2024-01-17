import tkinter as tk
from tkinter import messagebox

def generate_seat_letters(number):
    current_letter = ord('A')
    for _ in range(number):
        yield chr(current_letter)
        current_letter = (current_letter - ord('A') + 1) % 4 + ord('A')

def generate_seats(number):
    row = 0
    for seat_letter in generate_seat_letters(number):
        if seat_letter == 'A':
            row += 1
        if row == 13:
            row += 1
        yield f"{row}{seat_letter}"

def assign_seats(passengers):
    seat_generator = generate_seats(len(passengers))
    return {passenger: next(seat_generator) for passenger in passengers}

def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        base_string = f'{seat}{flight_id}'
        yield base_string + '0' * (12 - len(base_string))

def on_submit():
    passenger_names = entry_passengers.get().split(',')
    passenger_names = [name.strip() for name in passenger_names if name.strip()]

    if not passenger_names:
        messagebox.showinfo("Error", "Please enter passenger names.")
        return

    seats_assigned = assign_seats(passenger_names)
    ticket_codes = list(generate_codes(seats_assigned.values(), "FL123"))

    result_text = "Assigned Seats:\n"
    for passenger, seat in seats_assigned.items():
        result_text += f"{passenger}: {seat}\n"

    result_text += "\nTicket Codes:\n"
    result_text += "\n".join(ticket_codes)

    messagebox.showinfo("Results", result_text)

# GUI setup
root = tk.Tk()
root.title("Airline Ticketing System")

label_instruction = tk.Label(root, text="Enter passenger names (comma-separated):")
label_instruction.pack(pady=10)

entry_passengers = tk.Entry(root, width=50)
entry_passengers.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=20)

root.mainloop()
