def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D
    """
    current_letter = ord('A')
    for _ in range(number):
        yield chr(current_letter)
        current_letter = (current_letter - ord('A') + 1) % 4 + ord('A')


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B
    """
    row = 0
    for seat_letter in generate_seat_letters(number):
        if seat_letter == 'A':
            row += 1
        if row == 13:
            row += 1
        yield f"{row}{seat_letter}"


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}
    """
    seat_generator = generate_seats(len(passengers))
    return {passenger: next(seat_generator) for passenger in passengers}


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.
    """
    for seat in seat_numbers:
        base_string = f'{seat}{flight_id}'
        yield base_string + '0' * (12 - len(base_string))



passenger_list = ["Adele", "Björk", "Charlie", "David"]
seats_assigned = assign_seats(passenger_list)
print("Assigned Seats:", seats_assigned)

ticket_codes = list(generate_codes(seats_assigned.values(), "FL123"))
print("Ticket Codes:", ticket_codes)
