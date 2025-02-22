from linked_list import LinkedList

first_list = LinkedList()
first_list.insert_at_beginning(5)
first_list.insert_at_beginning(10)
first_list.insert_at_beginning(15)
first_list.insert_at_end(20)
first_list.insert_at_end(25)


print("Зв'язний список 1:")
first_list.print_list()

first_list.reverse()
print("Зв'язний список 1 після реверсування:")
first_list.print_list()

first_list.sort()
print("Зв'язний список 1 після сортування:")
first_list.print_list()


second_list = LinkedList()
second_list.insert_at_beginning(7)
second_list.insert_at_beginning(11)
second_list.insert_at_beginning(22)
second_list.insert_at_end(2)
second_list.insert_at_end(14)

second_list.sort()

first_list.merge_sorted(second_list)
print("Об'єднаний відсортований зв'язаний список:")
first_list.print_list()
