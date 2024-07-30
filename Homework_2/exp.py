u = {
    "TM346545": {
        "name": "Sanjar Ibn Ravshan",
        "phone_number": 999999999,
        "password": "ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d",
        "group": {
            "n50": {
                "python": {
                    "lesson_1": {
                        "lesson_time": "16:00 24.07.2024",
                        "lesson_name": "OOP",
                        "students": {
                            "SP346546": 3,
                            "SP654985": 4
                        }
                    },
                    "lesson_2": {
                        "lesson_time": "24.07.2024",
                        "lesson_name": "decorators",
                        "students": {
                            "SP346546": 4,
                            "SP654985": 5
                        }
                    }
                },
                "Java": {
                    "lesson_1": {
                        "lesson_time": "24.07.2024",
                        "lesson_name": "if, else, for",
                        "students": {
                            "SP346546": "none",
                            "SP654985": "none"
                        }
                    }
                }
            }
        }
    }
}
print(len(u["TM346545"]['group']['n50']['python']))
