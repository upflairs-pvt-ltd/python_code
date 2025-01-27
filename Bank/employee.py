# import manager as mng 
# print(mng.employee_id) 
# mng.employee_data()


# manager.employee_data()  
# print(manager.manager_salary)


# ===> TO ACCESS SPECIFIC CONTENT FROM MODULE 
# from manager import employee_data 
# from manager import manager_data
# from manager import employee_data,manager_data  
# employee_data() 
# manager_data() 


# from manager import employee_data as emp_data
# emp_data()
 

# from manager import *     # import manager , manager. 
# employee_data()


# from subbranch.branch import subranch_name 
# print(subranch_name)
# print(subranch_city)


# from subbranch.branch import subranch_name , subranch_city
# print(subranch_name)
# print(subranch_city)


# from subbranch.branch import subranch_name as sub_brnch_nm 
# print(sub_brnch_nm)

# from subbranch.branch import * 
# print(subranch_name)


from manager import employee_data , manager_data
print(employee_data())
print()
print(manager_data())