import os
print ("代碼1:整點響鈴")
print ("代碼2:設定時間響鈴")

x = input("請輸入代碼:")


if x=="1":
 os.system('final_1.py')
elif x=="2":
 os.system('final_2.py')
else:
 print ("輸入錯誤!!")