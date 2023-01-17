# !/usr/bin/python3
# so proud of myself
def element_at(my_list, idx):
    for num in range(len(my_list)):
        if idx < 0:
            return None
        elif idx > len(my_list)-1:
            return None
        else:
             num = idx
             return (my_list[num])



