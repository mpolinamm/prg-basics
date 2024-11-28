cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total = sum(len(row) for row in seats)
   return total

def seats_available(seats):
   available = sum(row.count('A') for row in seats)
   return available

def seats_booked(seats):
   booked = sum(row.count('B') for row in seats)
   return booked

def seat_status(seats, row, place):
   if 1 <= row <= len(seats) and 1 <= place <= len(seats[row - 1]):
      return "Available" if seats[row - 1][place - 1] == 'A' else "Booked"
   else:
      return "Invalid seat"
   return 

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))