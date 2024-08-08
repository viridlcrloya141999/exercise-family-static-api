from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                'id': self._generateId(),
                'first_name': 'Jhon',
                'last_name': self.last_name,
                'age': 33,
                'lucky_numbers': [7, 13, 22]
            },
            {
                'id': self._generateId(),
                'first_name': 'Jane',
                'last_name': self.last_name,
                'age': 33,
                'lucky_numbers': [10, 14, 3]
            },
            {
                'id': self._generateId(),
                'first_name': 'Jimmy',
                'last_name': self.last_name,
                'age': 5,
                'lucky_numbers': [1]
            }
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member.update({
            'id': member.get('id', self._generateId()),
            'last_name': self.last_name
        })
        self._members.append(member)
        return member

    def delete_member(self, id):
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)
                return True
        return False

    def update_member(self, id, new_info):
        for i, member in enumerate(self._members):
            if member['id'] == id:
                self._members[i] = {**member, **new_info, 'id': id, 'last_name': self.last_name}
                return self._members[i]
        return False

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        return False

    def get_all_members(self):
        return self._members
