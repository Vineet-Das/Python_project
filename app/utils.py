# business layer

def get_data(employee_data):
    data = []
    for i in employee_data:
        data.append({"id": i.id, "name": i.name, "age": i.age , "dept":i.dept})
    return data