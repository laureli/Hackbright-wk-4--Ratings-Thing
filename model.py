class Student(object):
    def __init__(self, first_name, last_name, github):
        self.first_name = first_name
        self.last_name = last_name
        self.github = github
    
    def get_projects(self):
        sql = "select * from projects where github=?"
        projects = db_execute(sql, (self.github,))

        p_list = []
        for p in projects:
            p = Project(p[0], p[1])
            p_list.append(p)

        return p_list



class Project(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

def get_student_by_github(github):
    sql = "select first_name, last_name, github from students where github=?"
    row = db_execute(sql, (github,))
    s = Student(row[0], row[1], row[2])
    return s



def make_tables():
    pass

def connect():
    pass

def db_execute(sql, params):
    return ("Christian", "Fernandez", "chriszf")
