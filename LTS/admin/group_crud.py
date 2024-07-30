from LTS.admin.for_admin import ForAdmin, int_input
import json


class GroupCrud(ForAdmin):
    def group_crud(self, teacher_file: dict, student_file: dict) -> str:
        text = """
        1. Add New Group
        2. View All Groups
        3. Update Group Information
        4. Delete Group
        5. Exit
        """
        print(text)
        num = int_input("Number: ")
        if num == 1:
            self.add_group(teacher_file=teacher_file, student_file=student_file)
        elif num == 2:
            self.view_all_groups(teacher_file=teacher_file)
        elif num == 3:
            self.update_group(teacher_file=teacher_file, student_file=student_file)
        elif num == 4:
            self.delete_group(teacher_file=teacher_file, student_file=student_file)
        else:
            return "num"
        self.group_crud(teacher_file=teacher_file, student_file=student_file)

    def add_group(self, teacher_file: dict, student_file: dict) -> None:
        my_list: list = ['teacher']
        m_list: list = self.for_admin_teacher_direction_lesson(teacher_file, student_file, my_list)
        teacher: str = m_list[0]
        group_name: str = input("Group Name: ")
        groups: list = []
        for i in teacher_file.values():
            for j in i['group'].keys():
                groups.append(j)
        while group_name in groups:
            group_name = input("Group Name Exists, Please Try Again: ")
        gr: dict = {group_name: {
            "direction": [],
            "students": []
        }}
        teacher_file[teacher]['group'].update(gr)
        self.write_to_file(self._teacher_file, teacher_file)
        print("Added")

    def view_all_groups(self, teacher_file: dict) -> None:
        self.__str__()
        groups: list = []
        for u, i in teacher_file.items():
            for j in i['group'].keys():
                groups.append(f"teacher: {teacher_file[u]['name']}, group: {j}")
        print(json.dumps(groups, indent=4))

    def update_group(self, teacher_file: dict, student_file: dict) -> None:
        groups: list = []
        groups_list: list = []
        teacher_list: list = []
        for u, i in teacher_file.items():
            for j in i['group'].keys():
                groups_list.append(j)
                groups.append(f"teacher: {teacher_file[u]['name']}, group: {j}")
                teacher_list.append(u)
        group: str = self.list_choice(groups)
        g_index: int = groups.index(group)
        teacher: str = teacher_list[g_index]
        gr: str = groups_list[g_index]
        new_gr: str = input("Change the group name: ")
        n_gr: dict = {new_gr: teacher_file[teacher]["group"][gr]}

        student_list: list = []
        for user, value in student_file.items():
            if value['group'] == gr:
                student_list.append(user)
        if len(student_list) > 0:
            for user in student_list:
                student_file[user]['group'] = new_gr
        else:
            pass
        teacher_file[teacher]['group'].update(n_gr)
        del teacher_file[teacher]['group'][gr]
        self.write_to_file(self._teacher_file, teacher_file)
        self.write_to_file(self._student_file, student_file)

    def delete_group(self, teacher_file: dict, student_file: dict) -> None:
        groups: list = []
        groups_list: list = []
        teacher_list: list = []
        for u, i in teacher_file.items():
            for j in i['group'].keys():
                groups_list.append(j)
                groups.append(f"teacher: {teacher_file[u]['name']}, group: {j}")
                teacher_list.append(u)

        group: str = self.list_choice(groups)
        g_index: int = groups.index(group)
        teacher: str = teacher_list[g_index]
        gr: str = groups_list[g_index]

        if len(teacher_file[teacher]['group'][gr]['direction']) > 0:
            student_list = teacher_file[teacher]['group'][gr]["students"]
            direction_list = teacher_file[teacher]['group'][gr]["direction"]

            for direction in direction_list:
                del teacher_file[teacher]['direction'][direction]
            for student in student_list:
                for direction in direction_list:
                    del student_file[student]['direction'][direction]

        del teacher_file[teacher]['group'][gr]
        self.write_to_file(self._teacher_file, teacher_file)
        self.write_to_file(self._student_file, student_file)
