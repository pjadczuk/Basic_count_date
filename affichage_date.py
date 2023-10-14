import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from extraire_date import liste
class GymAgendaApp:
    def __init__(self, root, dates):
        self.root = root
        self.root.title("Gym Agenda")

        self.selected_dates = set()

        self.cal = Calendar(self.root, firstweekday='monday', showothermonthdays=False)
        self.cal.pack()

        self.fill_agenda(dates)

    def fill_agenda(self, dates):
        for date in dates:
            year, month, day = map(int, date)
            date_instance = datetime(year, month, day).date()
            self.selected_dates.add(date_instance)
            self.cal.calevent_create(date_instance, "Gym", "present")

if __name__ == "__main__":
    root = tk.Tk()
    ma_liste= liste    #liste= liste de extraire_date
    app = GymAgendaApp(root, ma_liste)
    root.mainloop()
