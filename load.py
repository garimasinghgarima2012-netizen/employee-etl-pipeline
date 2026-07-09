from connect_db import get_connection
# import transform

def load(employee):
    con = get_connection()
    cursor= con.cursor()

    query='''
    insert into employees( id,name ,email,department, salary ,old_salary ,increment ,new_salary ,rating ,valid_email ) 
    values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    email = VALUES(email),
    department = VALUES(department),
    salary = VALUES(salary),
    old_salary = VALUES(old_salary),
    increment = VALUES(increment),
    new_salary = VALUES(new_salary),
    rating = VALUES(rating),
    valid_email = VALUES(valid_email)
    '''
    for i in employee:
        cursor.execute(query,(
            i["id"],
            i["name"],
            i["email"],
            i["department"],
            i["salary"],
            i["old_salary"],
            i["increment"],
            i["new_salary"],
            i["rating"],
            i["valid_email"],
            ))
    con.commit()