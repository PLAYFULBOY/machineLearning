# -*- coding: utf-8 -*-


#����һ���б�

number_list = (1, 3, 5, 7, 9)

string_list = ["abc", "bbc", "python"]

mixed_list = ['python', 'java', 3, 12]

#�����б��е�ֵ


second_num = number_list[1]

third_string = string_list[2]

fourth_mix = mixed_list[3]

print("second_num: {1} third_string: {1} fourth_mix: {2}".format(second_num, third_string, fourth_mix))

number_list[1] = 5

print("number_list" + str(number_list))