-- -- CREATE TABLE departments(
-- --     department_id SERIAL PRIMARY KEY,
-- --     department_name VARCHAR(50) NOT NULL
-- -- )

-- -- INSERT INTO departments(department_name)
-- -- VALUES
-- -- ('sales'),
-- -- ('marketing'),
-- -- ('it');

-- -- SELECT * FROM departments



-- CREATE TABLE employees(
--     employee_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL,
--     email VARCHAR(50) NOT NULL UNIQUE,
--     phone VARCHAR(50),
--     bio TEXT,
--     job_title VARCHAR(50) NOT NULL,
--     salary NUMERIC NOT NULL CHECK(salary > 0),
--     is_active BOOLEAN NOT NULL DEFAULT TRUE,
--     hire_date DATE,
--     last_login TIMESTAMP,
--     employee_status VARCHAR(20) NOT NULL DEFAULT 'active'
--                     CHECK(
--                         employee_status IN ('active','leave','terminated')
--                     ),
--     created_at TIMESTAMP NOT NULL DEFAULT now(),
--     department_id INT REFERENCES departments(department_id),
--     manager_id INT  REFERENCES employees(employee_id)

-- );


-- INSERT INTO employees
--   (first_name, last_name, email, phone, job_title, salary, hire_date, department_id, manager_id)
-- VALUES
--   ('Asha', 'Sharma', 'asha1@company.com', '9000000001', 'Sales Head', 120000.00, '2020-01-15',
--      (SELECT department_id FROM departments WHERE department_name = 'sales'), NULL)
-- RETURNING employee_id , email;


-- -- INSERT INTO employees
-- --   (first_name, last_name, email, phone, job_title, salary, hire_date, department_id, manager_id)
-- -- VALUES
-- --   ('Kiran', 'Deshmukh', 'kiran@company.com', '9000000004', 'Sales Executive', 45000.00, '2022-02-10',
-- --      (SELECT department_id FROM departments WHERE department_name = 'sales'),
-- --      (SELECT employee_id FROM employees WHERE email = 'asha@company.com'));




-- -- INSERT INTO employees
-- -- ( first_name, last_name, email, job_title,salary, department_id, manager_id )
-- -- VALUES
-- -- ('Om', 'Gawande', 'om@gmail.com', 'Software Specialist Trainee' , 400000, 
-- -- (SELECT department_id FROM departments WHERE department_name = 'it'),
-- -- (SELECT employee_id FROM employees WHERE email = 'om@gmail.com' )
-- -- )
-- -- ON CONFLICT (email) DO UPDATE
-- -- SET job_title = EXCLUDED.job_title, salary = EXCLUDED.salary


-- -- SELECT e.first_name, job_title, salary 
-- -- FROM employees e
-- -- WHERE email = 'om@gmail.com'

-- SELECT * FROM employees


-- SELECT first_name AS name, salary * 12 AS yearly FROM employees;

SELECT 
employees.first_name,
departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;







SELECT d.department_name , sum (e.department_id)
FROM departments d
FULL OUTER JOIN employees e
ON d.department_id = e.department_id
GROUP BY 
        d.department_id,
        d.department_name

SELECT * FROM employees