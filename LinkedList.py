import random


class List:
    def __init__(self, head):
        self.head = head

    def get_last_elem(self):
        current_obj = self.head
        while current_obj.has_next():
            current_obj = current_obj.next
        return current_obj

    def get_elem_and_previous(self, filter_value):
        current_obj = self.head
        while current_obj.next.value != filter_value or current_obj.has_next():
            current_obj = current_obj.next
        return current_obj, current_obj.next


    def add(self, node_obj):
        last_elem = self.get_last_elem()
        last_elem.next = node_obj


    def delete(self, filter_value):
        prev_obj, obj_for_delete = self.get_elem_and_previous(filter_value)
        prev_obj.next = obj_for_delete.next #присваиваем ссылку на тот объект который мы хотим удалить ссылку на следующей от удаляемого

    def __repr__(self):
        result = f'List ['
        current_obj = self.head
        while current_obj.has_next():
            result += f'{current_obj.value} '
            current_obj = current_obj.next
        return result + f']'


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def has_next(self):
        return self.next is not None

    def get_next(self):
        return self.next


listik = List(Node(5, None))

for i in range(6):
    listik.add(Node(random.randint(10, 500), None))
print(listik)

