global_list = []
tasks_dict = {}

c = 1
while c <=3:
  tasks_list = []
  d = input('Введите дату: ')
  tasks_list.append(d)
  z = input('Введите задачу: ')
  tasks_list.append(z)
  global_list.append(tasks_list)
  c+=1

tasks_dict = dict(global_list) #переводим список в словарь

for k,v in tasks_dict.items():
  print(k, v)
