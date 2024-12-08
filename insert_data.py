import utils as userdb
from log import logger

def employee_insertion() -> str :
    logger.info(f'in employee_insertion function, creating query for fetch data in employee table')
    table = '''
        INSERT INTO employee (id, email, name, joining_date) VALUES
        (1, 'john.doe@example.com', 'John Doe', '2023-01-15'),
        (2, 'jane.smith@example.com', 'Jane Smith', '2023-02-10'),
        (3, 'mike.brown@example.com', 'Mike Brown', '2023-03-08'),
        (4, 'emma.wilson@example.com', 'Emma Wilson', '2023-04-25'),
        (5, 'liam.johnson@example.com', 'Liam Johnson', '2023-05-30'),
        (6, 'olivia.taylor@example.com', 'Olivia Taylor', '2023-06-15'),
        (7, 'noah.anderson@example.com', 'Noah Anderson', '2023-07-20'),
        (8, 'ava.martin@example.com', 'Ava Martin', '2023-08-10'),
        (9, 'lucas.moore@example.com', 'Lucas Moore', '2023-09-15'),
        (10, 'mia.clark@example.com', 'Mia Clark', '2023-10-05'),
        (11, 'elijah.thomas@example.com', 'Elijah Thomas', '2023-11-12'),
        (12, 'sophia.harris@example.com', 'Sophia Harris', '2023-12-01'),
        (13, 'william.lee@example.com', 'William Lee', '2024-01-19'),
        (14, 'amelia.walker@example.com', 'Amelia Walker', '2024-02-14'),
        (15, 'james.hall@example.com', 'James Hall', '2024-03-18'),
        (16, 'isabella.adams@example.com', 'Isabella Adams', '2024-04-22'),
        (17, 'benjamin.king@example.com', 'Benjamin King', '2024-05-11'),
        (18, 'charlotte.wright@example.com', 'Charlotte Wright', '2024-06-07'),
        (19, 'jackson.scott@example.com', 'Jackson Scott', '2024-07-21'),
        (20, 'harper.green@example.com', 'Harper Green', '2024-08-15');
        '''
    logger.info('query has been created')
    return table
def department_data_insertion() -> str:
    logger.info(f'in employee_insertion function, creating query for fetch data in department table')
    table = '''
        INSERT INTO department (id, department_name, manager)
        VALUES
        (6, 'Human Resources', 1),
        (7, 'Finance', 2),
        (8, 'Engineering', 3),
        (9, 'Marketing', 4),
        (10, 'Sales', 5),
        (11, 'Marketing', 4),
        (12, 'Sales', 5),
        (13, 'Finance', 2),
        (14, 'Human Resources', 1),
        (15, 'Engineering', 3),
        (16, 'Marketing', 4),
        (17, 'Sales', 5),
        (18, 'Marketing', 4),
        (19, 'Human Resources', 1),
        (20, 'Finance', 2);
    '''
    logger.info('query has been created')
    return table
def projects_data_insertion() -> str :
    logger.info(f'in employee_insertion function, creating query for fetch data in project table')
    table = '''
        INSERT INTO project (id,project_name, start_date, end_date, budget) 
        VALUES
        (1,'Project Alpha', '2024-01-01', '2024-12-31', 100000.00),
        (2,'Project Beta', '2024-03-15', '2024-09-15', 50000.00),
        (1,'Project Gamma', '2024-05-01', '2024-11-30', 200000.00),
        (5,'Project Delta', '2024-06-01', '2024-12-31', 150000.00),
        (4,'Project Epsilon', '2024-07-01', '2025-06-30', 75000.00),
        (1,'Project Zeta', '2024-08-01', '2025-01-31', 120000.00),
        (3,'Project Eta', '2024-09-01', '2024-12-31', 95000.00),
        (2,'Project Theta', '2024-10-01', '2025-03-31', 110000.00),
        (4,'Project Iota', '2024-11-01', '2025-06-30', 80000.00),
        (3,'Project Kappa', '2024-12-01', '2025-09-30', 130000.00),
        (6,'Project Alpha', '2024-01-01', '2024-12-31', 100000.00),
        (7,'Project Beta', '2024-03-15', '2024-09-15', 50000.00),
        (8,'Project Gamma', '2024-05-01', '2024-11-30', 200000.00),
        (9,'Project Delta', '2024-06-01', '2024-12-31', 150000.00),
        (10,'Project Epsilon', '2024-07-01', '2025-06-30', 75000.00),
        (11,'Project Zeta', '2024-08-01', '2025-01-31', 120000.00),
        (12,'Project Eta', '2024-09-01', '2024-12-31', 95000.00),
        (13,'Project Theta', '2024-10-01', '2025-03-31', 110000.00),
        (14,'Project Iota', '2024-11-01', '2025-06-30', 80000.00),
        (15,'Project Kappa', '2024-12-01', '2025-09-30', 130000.00),
        (16,'Project Beta', '2024-03-15', '2024-09-15', 50000.00),
        (17,'Project Gamma', '2024-05-01', '2024-11-30', 200000.00),
        (18,'Project Delta', '2024-06-01', '2024-12-31', 150000.00),
        (19,'Project Epsilon', '2024-07-01', '2025-06-30', 75000.00),
        (20,'Project Zeta', '2024-08-01', '2025-01-31', 120000.00),
        (6,'Project Eta', '2024-09-01', '2024-12-31', 95000.00),
        (8,'Project Theta', '2024-10-01', '2025-03-31', 110000.00),
        (9,'Project Iota', '2024-11-01', '2025-06-30', 80000.00),
        (14,'Project Kappa', '2024-12-01', '2025-09-30', 130000.00);
    '''
    logger.info('query has been created')
    return table
def skills_data_insertion() -> str :
    logger.info(f'in employee_insertion function, creating query for fetch data in skill table')
    table = '''

        INSERT INTO skill (id, skill_name)
        VALUES
        (1, 'Development'), (1, 'Sales'), (1, 'Marketing'), (1, 'Data'), (1, 'Data Analytics'),
        (2, 'Development'), (2, 'Sales'), (19, 'Marketing'), (2, 'Data'), (2, 'Communication'),
        (3, 'Development'), (3, 'Sales'), (3, 'Marketing'), (3, 'Data Analytics'), (3, 'Communication'),
        (4, 'Development'), (4, 'Sales'), (4, 'Marketing'), (17, 'Data'), (16, 'Data Analytics'),
        (5, 'Development'), (13, 'Sales'), (5, 'Marketing'), (5, 'Communication'), (5, 'Data Analytics'),
        (6, 'Development'), (6, 'Sales'), (18, 'Marketing'), (6, 'Data'), (6, 'Data Analytics'),
        (7, 'Development'), (7, 'Sales'), (14, 'Marketing'), (7, 'Data Analytics'), (7, 'Communication'),
        (8, 'Development'), (8, 'Sales'), (8, 'Marketing'), (8, 'Data'), (8, 'Data Analytics'),
        (9, 'Development'), (20, 'Sales'), (15, 'Marketing'), (9, 'Data Analytics'), (9, 'Communication'),
        (10, 'Development'), (10, 'Sales'), (10, 'Marketing'), (10, 'Data'), (10, 'Data Analytics'),
        (11, 'Development'), (11, 'Sales'), (11, 'Marketing'), (11, 'Communication'), (11, 'Data Analytics'),
        (12, 'Development'), (12, 'Sales'), (12, 'Marketing'), (12, 'Data'), (12, 'Data Analytics');
        '''
    logger.info('query has been created')
    return table
def tasks_data_insertion() -> str :
    logger.info(f'in employee_insertion function, creating query for fetch data in task table')
    table = '''
        INSERT INTO task (id,task_name, task_description, deadline)
        VALUES
        (1,'Backend Development', 'Develop and implement the backend API for the application', '2024-12-31'),
        (8,'Frontend Development', 'Design and implement the user interface of the application', '2024-12-15'),
        (10,'Database Design', 'Design the relational database schema and structure', '2024-12-10'),
        (6,'Testing', 'Write test cases and perform unit testing on modules', '2024-12-20'),
        (1,'Deployment', 'Deploy the application to the production environment', '2024-12-25'),
        (20,'Documentation', 'Prepare user and technical documentation for the project', '2024-12-05'),
        (12,'Code Review', 'Review the codebase and ensure adherence to coding standards', '2024-12-12'),
        (3,'Security Audit', 'Perform a security audit of the application', '2024-12-18'),
        (11,'Project Management', 'Coordinate with teams and ensure project milestones are met', '2024-12-01'),
        (11,'Client Communication', 'Communicate with the client regarding project progress and issues', '2024-12-08');

    '''
    logger.info('query has been created')
    return table
def clients_data_insertion() -> str :
    logger.info(f'in employee_insertion function, creating query for fetch data in client table')
    table = '''
        INSERT INTO client (id, client_name, contact_email)
        VALUES
        (1, 'Acme Corp', 'contact@acmecorp.com'),
        (2, 'Tech Innovations', 'support@techinnovations.com'),
        (3, 'Global Enterprises', 'info@globalenterprises.com'),
        (4, 'Alpha Solutions', 'contact@alphasolutions.com'),
        (5, 'Beta Industries', 'support@betaindustries.com');
        '''
    
    return table

def insert_data_into_db() :
    logger.info('In insert_data_into_db function processing is being started for inserting data')
    try :
        logger.info('processing is being started for insert data in employee table')
        userdb.cursor.execute(employee_insertion())
        userdb.db_connection.commit()
        logger.info('employee data has been inserted')

        logger.info('processing is being started for insert data in department table')
        userdb.cursor.execute(department_data_insertion())
        userdb.db_connection.commit()
        logger.info('department data has been inserted')


        logger.info('processing is being started for insert data in project table')
        userdb.cursor.execute(projects_data_insertion())
        userdb.db_connection.commit()
        logger.info('project data has been inserted')

        logger.info('processing is being started for insert data in skill table')
        userdb.cursor.execute(skills_data_insertion())
        userdb.db_connection.commit()
        logger.info('skill data has been inserted')

        logger.info('processing is being started for insert data in task table')
        userdb.cursor.execute(tasks_data_insertion())
        userdb.db_connection.commit()
        logger.info('task data has been inserted')


        logger.info('processing is being started for insert data in client table')
        userdb.cursor.execute(clients_data_insertion())
        userdb.db_connection.commit()
        logger.info('client data has been inserted')
    except Exception as err :
        logger.info(f'unable to create table, we found err -> {err}')
        exit()