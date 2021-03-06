import config

def main():
    database = r"C:\SQLite\db\pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    # create a database connection
    conn = config.create_connection(database)
    
    # create tables
    if conn is not None:
        # create projects table
        config.create_table(conn, sql_create_projects_table)
        print("Projects table created")

        # create tasks table
        config.create_table(conn, sql_create_tasks_table)
        print("Task table created")
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()