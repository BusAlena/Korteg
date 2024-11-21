immutable_var='A', 'B', 'C', 1, 2, 3, True
print(immutable_var)
# В соотвествии с особенностями кортежа, элементы которые в нем содержатся являются неизменяемыми.
# При этом, тип элемента не влияет на функцию кортежа.
#immutable_var[0]='E'
# Результат: Traceback (most recent call last):
#  File "C:\MAMI\M1L1\.venv\module_1_5.py", line 4, in <module>
#   immutable_var[0]='E'
#    ~~~~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment
mutable_list=['a', 'b', 'c', 1, 2, 3, False]
print(mutable_list)
mutable_list[0]='f'
print(mutable_list)