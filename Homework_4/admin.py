import random

from user import User, int_input


class Admin(User):
    def show_menu_admin(self):
        text = """
        1. Add plane (CRUD): ID, name, capacity
        2. Add airport (CRUD): name, country
        3. Add flight (CRUD): plane, form_airport, to_airport, flight_time, landing_time, status, tickets = 0,price
        4. Show all flight
        5. Logout
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.add_plane()
        elif num == 2:
            self.add_airport()
        elif num == 3:
            self.add_flight()
        elif num == 4:
            pass
        elif num == 5:
            self.exit = True
            return

    def add_flight(self):
        text = """
        1. Create flight
        2. Read flight
        3. Delete flight
        4. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.create_flight()
        elif num == 2:
            self.read_flight()
        elif num == 3:
            self.delete_flight()
        else:
            self.show_menu_admin()

    def create_flight(self):
        flights: dict = self.read_to_file(self._flight_file)
        id_list = []
        name_list = []
        for i, j in flights.items():
            if j["status"]:
                pass
            else:
                name_list.append(f"campaign: {j['campaign']}, name: {j['name']}, capacity: {j['capacity']}")
                id_list.append(i)
        if len(name_list) > 0:
            airports: dict = self.read_to_file(self._airport_file)
            if len(airports) > 2:
                name = self.list_choice(name_list)
                name_index = name_list.index(name)
                from_air = []
                country_air = []
                for i, j in airports.items():
                    country_air.append(j)
                    from_air.append(i)
                country = self.list_choice(country_air)
                c_index = country_air.index(country)
                from_airport = from_air[c_index]
                country_air.pop(c_index)
                from_air.pop(c_index)
                to_air = self.list_choice(country_air)
                c_index = country_air.index(to_air)
                to_airport = from_air[c_index]
                flight_time = input("flight time exp(2024-08-01 10:00): ")
                landing_time = input("landing time exp(2024-08-01 20:00): ")
                tickets = input("tickets: ")
                price = int_input("price: ")
                flights[name_index]['from_airport'] = from_airport
                flights[name_index]["to_airport"] = to_airport
                flights[name_index]["flight_time"] = flight_time
                flights[name_index]["landing_time"] = landing_time
                flights[name_index]['status'] = True
                flights[name_index]['tickets'] = tickets
                flights[name_index]['price'] = f"{price} USD"
                self.write_to_file(self._flight_file, flights)
            else:
                print("No choice airplane")
        else:
            print("No find flight")
            self.show_menu_admin()

    def read_flight(self):
        flights: dict = self.read_to_file(self._flight_file)
        for i, j in flights.items():
            text = f"""
        plane name: {j["name"]}
        campaign: {j["campaign"]}
        capacity: {j["capacity"]}
        from airport: {j["from_airport"]}
        to airport: {j["to_airport"]}
        flight time: {j["flight_time"]}
        landing time: {j["landing_time"]}
        tickets: {j["tickets"]}
        price: {j["price"]}
            """
            print(text)

    def delete_flight(self):
        flights: dict = self.read_to_file(self._flight_file)
        id_list = []
        name_list = []
        for i, j in flights.items():
            id_list.append(i)
            name_list.append(j)
        name = self.list_choice(name_list)
        c_index = name_list.index(name)
        ide = id_list[c_index]
        del flights[ide]
        self.write_to_file(self._flight_file, flights)

    def create_airport(self):
        name = input("Enter airport name: ")
        country = input("Enter airport country: ")
        x = {
            name: {
                "country": country
            }
        }
        self.add_to_file(self._airport_file, x)

    def read_airport(self):
        airports: dict = self.read_to_file(self._airport_file)
        for airport, airport_value in airports.items():
            print(f"Airport: {airport}, Country: {airport_value['country']}")

    def update_airport(self):
        airports: dict = self.read_to_file(self._airport_file)
        airport_name_list = []
        for airport in airports.keys():
            airport_name_list.append(airport)
        airport_name = self.list_choice(airport_name_list)
        new_airport = input("New Airport name: ")
        country = input("New country name")
        airports[new_airport] = {
            "country": country
        }
        del airports[airport_name]
        self.write_to_file(self._airport_file, airports)

    def delete_airport(self):
        airports: dict = self.read_to_file(self._airport_file)
        airport_name_list = []
        for airport in airports.keys():
            airport_name_list.append(airport)
        airport_name = self.list_choice(airport_name_list)
        del airports[airport_name]
        self.write_to_file(self._airport_file, airports)

    def add_airport(self):
        text = """
        1. Create an airport
        2. Read an airport
        3. Update an airport
        4. Delete an airport
        5. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.create_airport()
        elif num == 2:
            self.read_airport()
        elif num == 3:
            self.update_airport()
        elif num == 4:
            self.delete_airport()
        else:
            self.show_menu_admin()

    def add_plane(self):
        text = """
        1. Create a plane
        2. Read a plane
        3. Update a plane
        4. Delete a plane
        5. Exit
        """
        print(text)
        num = int_input("number: ")
        if num == 1:
            self.create_plane()
        elif num == 2:
            self.read_plane()
        elif num == 3:
            self.update_plane()
        elif num == 4:
            self.delete_plane()
        else:
            self.show_menu_admin()

    def create_plane(self):
        planes = self.read_to_file(self._flight_file)
        plane_id = random.randint(100000000000, 999999999999)
        while plane_id in planes.keys():
            plane_id = random.randint(100000000000, 999999999999)
        campaign = input("Campaign: ")
        plane_name = input("Enter plane name: ")
        capacity = int_input("Enter plane capacity: ")
        plane = {
            plane_id: {
                "name": plane_name,
                "campaign": campaign,
                "capacity": capacity,
                "from_airport": None,
                "to_airport": None,
                "flight_time": None,
                "landing_time": None,
                "status": None,
                "tickets": 0,
                "price": None
            }
        }
        self.add_to_file(self._flight_file, plane)

    def read_plane(self):
        planes: dict = self.read_to_file(self._flight_file)
        plane_id_list: list = []
        plane_name_list: list = []
        for ide, value in planes.items():
            plane_id_list.append(ide)
            plane_name_list.append(value['name'])
        plane_name = self.list_choice(plane_name_list)
        plane_index = plane_name_list.index(plane_name)
        plane_id = plane_id_list[plane_index]
        print(f"name: {planes[plane_id]['name']}")
        print(f"capacity: {planes[plane_id]['capacity']}")

    def update_plane(self):
        planes: dict = self.read_to_file(self._flight_file)
        plane_id_list: list = []
        plane_name_list: list = []
        for ide, value in planes.items():
            plane_id_list.append(ide)
            plane_name_list.append(value['name'])
        plane_name = self.list_choice(plane_name_list)
        plane_index = plane_name_list.index(plane_name)
        plane_id = plane_id_list[plane_index]
        name = input("Plane name: ")
        campaign = input("Campaign: ")
        capacity = int_input("Plane capacity: ")
        planes[plane_id]["name"] = name
        planes[plane_id]["campaign"] = campaign
        planes[plane_id]["capacity"] = capacity
        self.write_to_file(self._flight_file, planes)

    def delete_plane(self):
        planes: dict = self.read_to_file(self._flight_file)
        plane_id_list: list = []
        plane_name_list: list = []
        for ide, value in planes.items():
            plane_id_list.append(ide)
            plane_name_list.append(value['name'])
        plane_name = self.list_choice(plane_name_list)
        plane_index = plane_name_list.index(plane_name)
        plane_id = plane_id_list[plane_index]
        del planes[plane_id]
        print("successfully deleted plane")
        self.write_to_file(self._flight_file, planes)
