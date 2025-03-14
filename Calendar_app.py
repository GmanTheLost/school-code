import calendar
from datetime import datetime, timedelta


class CalendarApp:
    def __init__(self):
        self.events = {}

    def add_event(self):
        """Prompt user to add an event with a date, description, and priority"""
        while True:
            date_str = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter event description: ")

            try:
                # Ensure month and day have leading zeros if needed
                date_parts = date_str.split("-")
                if len(date_parts) != 3:
                    raise ValueError("Date must be in the format YYYY-MM-DD.")

                year, month, day = date_parts
                if len(month) == 1:
                    month = "0" + month
                if len(day) == 1:
                    day = "0" + day

                # Reassemble the date string
                date_str = f"{year}-{month}-{day}"

                # Check if the date is valid
                datetime.strptime(date_str, "%Y-%m-%d")

                # Process priority input
                priority = int(input("Enter priority (1 = High, 2 = Medium, 3 = Low):"))
                if priority not in [1, 2, 3]:
                    raise ValueError("Priority must be 1, 2, or 3.")

                if date_str not in self.events:
                    self.events[date_str] = []

                self.events[date_str].append((description, priority))
                print("Event added successfully.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}")



    def edit_event(self):
        while True:
            """Allow user to edit an existing event."""
            date_str = input("Enter date (YYYY-MM-DD) to edit an event: ")

            if date_str in self.events:
                print("\nExisting events for this date:")
                for i, (event, priority) in enumerate(self.events[date_str], 1):
                    print(f"{i}. {event} (priority:{priority})")
                try:
                    choice = int(input("Enter the event number to edit: ")) - 1
                    if choice < 0 or choice >= len(self.events[date_str]):
                        raise IndexError("Invalid selection.")
                    
                    new_description = input("Enter a new event description: ")
                    new_priority = int(input("Enter new priority (1 = High, 2 = Medium, 3 = Low):"))

                    if new_priority not in [1,2,3]:
                        raise ValueError("Priority must be 1, 2, or 3.")
                    
                    self.events[date_str][choice] = (new_description, new_priority)
                    print("Event updated successfully!\n")
                    break

                except (ValueError, IndexError) as e:
                    print(f"error: {e}")

            else:
                print("No events found for this date.")
                break


    def delete_event(self):
        """Allow user to delete an event."""
        while True:
            date_str = input("Enter date (YYYY-MM-DD) to delete an event: ")

            if date_str in self.events:
                print("\nExisting events for this date:")
                for i, (event, priority) in enumerate(self.events[date_str], 1):
                    print(f"{i}. {event} (Priority: {priority})")

                try:
                    choice = int(input("Enter the event number to delete: ")) - 1
                    if choice < 0 or choice >= len(self.events[date_str]):
                        raise IndexError("Invalid selection.")

                    del self.events[date_str][choice]
                    if not self.events[date_str]:  # Remove the date key if no events remain
                        del self.events[date_str]

                    print("Event deleted successfully!\n")
                    break

                except (ValueError, IndexError) as e:
                    print(f"Error: {e}")
                    

            else:
                print("No events found for this date.")
                break
            
    def view_events_by_date(self):
        """Display events for a specific date."""
        date_str = input("Enter date (YYYY-MM-DD) to view events: ")

        if date_str in self.events:
            print(f"\nEvents on {date_str}:")
            for event, priority in sorted(self.events[date_str], key=lambda x: x[1]):  # Sort by priority
                print(f"- {event} (Priority: {priority})")
        else:
            print("No events found.")
    def view_events_by_month(self):
        """Display all events for a specific month."""
        year = input("Enter year (YYYY): ")
        month = input("Enter month (MM): ")

        try:
            year, month = int(year), int(month)
            print(f"\nEvents in {calendar.month_name[month]} {year}:")

            found = False
            for date, event_list in self.events.items():
                if date.startswith(f"{year}-{month:02d}"):
                    found = True
                    print(f"{date}:")
                    for event, priority in sorted(event_list, key=lambda x: x[1]):
                        print(f"  - {event} (Priority: {priority})")

            if not found:
                print("No events found for this month.")

        except ValueError:
            print("Invalid input.")

    def view_events_by_year(self):
        """Display all events for a specific year."""
        year = input("Enter year (YYYY): ")

        try:
            year = int(year)
            print(f"\nEvents in {year}:")

            found = False
            for date, event_list in self.events.items():
                if date.startswith(f"{year}-"):
                    found = True
                    print(f"{date}:")
                    for event, priority in sorted(event_list, key=lambda x: x[1]):
                        print(f"  - {event} (Priority: {priority})")

            if not found:
                print("No events found for this year.")

        except ValueError:
            print("Invalid input.")

    def search_events(self):
        """Search for events by keyword."""
        keyword = input("Enter a keyword to search: ").lower()
        print("\nSearch Results:")

        found = False
        for date, event_list in self.events.items():
            for event, priority in event_list:
                if keyword in event.lower():
                    found = True
                    print(f"{date}: {event} (Priority: {priority})")

        if not found:
            print("No matching events found.")


    def display_monthly_calendar(self):
        """Display the calendar for a specific month with events marked with asterisks."""
        year = input("Enter year (YYYY): ")
        month = input("Enter month (MM): ")

        try:
            year, month = int(year), int(month)

            # Print the header with the month and year
            print(f"\n{calendar.month_name[month]} {year}".center(28))
            print("Mo Tu We Th Fr Sa Su")

            # Get the month's calendar
            weeks = calendar.monthcalendar(year, month)
            
            # Display each week in the calendar
            for week in weeks:
                line = ""
                for day in week:
                    if day == 0:
                        line += "   "  # Add space for days outside the month
                    else:
                        # Format the date string
                        date_str = f"{year}-{month:02d}-{day:02d}"
                        
                        # If there's an event on this date, add an asterisk
                        if date_str in self.events:
                            line += f"{day:2}* "
                        else:
                            line += f"{day:2}  "
                print(line)
        except ValueError:
            print("Invalid input. Please enter a valid year and month.")
    
   
    def menu(self):
        """Main menu system."""
        while True:
            print("\nSimple Calendar App")
            print("1. Add Event")
            print("2. Edit Event")
            print("3. Delete Event")
            print("4. View Events by Date")
            print("5. View Events by Month")
            print("6. View Events by Year")
            print("7. Search Events")
            print("8. Display Monthly Calendar")
            print("9. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_event()
            elif choice == "2":
                self.edit_event()
            elif choice == "3":
                self.delete_event()
            elif choice == "4":
                self.view_events_by_date()
            elif choice == "5":
                self.view_events_by_month()
            elif choice == "6":
                self.view_events_by_year()
            elif choice == "7":
                self.search_events()
            elif choice == "8":
                self.display_monthly_calendar()
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    app = CalendarApp()
    app.menu()