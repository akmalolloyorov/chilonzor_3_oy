from json_manager import JsonManager, int_input


class User(JsonManager):
    def show_menu_user(self, phone_number: str):
        text = """
        1. Search flights | from_airport, to_airport -> all the available flights:
        2. Buy ticket | Passport_number, gmail
        3. Back
        4. My booked flight
        5. Log out
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            pass
        else:
            self._is_active = False
            self.exit = False
            self._active_phone = None
            return
