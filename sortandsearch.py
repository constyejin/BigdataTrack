import pandas as pd
import time

def check_time(function, *args):
  start_time = time.time()
  if len(args)==0:
   result = function()
  elif len(args)==1:
    result = function(args[0])
  else:
   result = function(args[0], args[1])

  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"{function.__name__}을 실행한 시간은 : \t{elapsed_time:0.5f}초입니다.\n")
  return result


def load_list():
  data_list = []
  file = open('./data/trade_apt_api.csv', 'r', encoding='utf-8')
  lines = file.readlines()
  for line in lines[1:]:
    columns = line.split(',')
    data_list.append(columns)

  file.close()
  # print(data_list[11:21])
  return data_list

# load_list()


def load_df():
  data_df = pd.read_csv('./data/trade_apt_api.csv')
  # print(data_df.head())
  return data_df


def price_sort_list_select(lst):
  for i in range(len(lst)):
   min_idx = i
  for j in range(i+1, len(lst)):
    if lst[min_idx] > lst[j]:
     min_idx = j
  lst[i], lst[min_idx] = lst[min_idx], lst[i]
  print(lst[:5])
  return

check_time(load_df)
check_time(load_list)