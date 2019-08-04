-- Create a table of departments
CREATE TABLE departments (
	dept_no VARCHAR,
	dept_name VARCHAR NOT NULL,
	PRIMARY KEY (dept_no)
);

SELECT * FROM departments;

-- Create a table of dept_emp
CREATE TABLE dept_emp (
	emp_no INTEGER,
	dept_no VARCHAR NOT NULL,
	from_date DATE,
	to_date DATE
);

SELECT * FROM dept_emp;

-- Create a table of dept_manager
CREATE TABLE dept_manager (
	dept_no VARCHAR NOT NULL,
	emp_no INTEGER,
	from_date DATE,
	to_date DATE
);

SELECT * FROM dept_manager;

-- Create a table of employees
CREATE TABLE employees (
	emp_no INTEGER,
	birth_date DATE,
	first_name VARCHAR NOT NULL,
	last_name VARCHAR NOT NULL,
	gender VARCHAR NOT NULL,
	hire_date DATE
);

SELECT * FROM employees;


-- Create a table of salaries
CREATE TABLE salaries (
	emp_no INTEGER,
	salary INTEGER,
	from_date DATE,
	to_date DATE
  
);

SELECT * FROM salaries;

-- Create a table of titles
CREATE TABLE titles (
	emp_no INTEGER,
	title VARCHAR,
	from_date DATE,
	to_date DATE
  
);

SELECT * FROM titles;

-- Adding constraints

ALTER TABLE employees ADD CONSTRAINT pk_emp_no PRIMARY KEY(emp_no);

ALTER TABLE dept_emp ADD CONSTRAINT fk_dept_emp_emp_no FOREIGN KEY(emp_no)
REFERENCES employees (emp_no);

ALTER TABLE dept_emp ADD CONSTRAINT fk_dept_emp_dept_no FOREIGN KEY(dept_no)
REFERENCES departments (dept_no);

ALTER TABLE dept_manager ADD CONSTRAINT fk_dept_manager_dept_no FOREIGN KEY(dept_no)
REFERENCES departments (dept_no);

ALTER TABLE dept_manager ADD CONSTRAINT fk_dept_manager_emp_no FOREIGN KEY(emp_no)
REFERENCES employees (emp_no);

ALTER TABLE salaries ADD CONSTRAINT fk_emp_no FOREIGN KEY(emp_no)
REFERENCES employees (emp_no);

ALTER TABLE titles ADD CONSTRAINT fk_emp_no FOREIGN KEY(emp_no)
REFERENCES employees (emp_no);

-- List the following details of each employee: employee number, last name, first name, gender, and salary.

SELECT e.emp_no, e.first_name, e.last_name, e.gender, s.salary 
FROM employees e
INNER JOIN salaries s ON e.emp_no = s.emp_no;

-- List employees who were hired in 1986.

SELECT * FROM employees
WHERE TO_CHAR(hire_date, 'YYYY/MM/DD') LIKE '1986%';

-- List the manager of each department with the following information: department number, department name, the manager's 
-- employee number, last name, first name, and start and end employment dates.

SELECT dm.dept_no, d.dept_name, e.emp_no, e.last_name, e.first_name, dm.from_date, dm.to_date
FROM dept_manager dm
INNER JOIN employees e ON dm.emp_no = e.emp_no
INNER JOIN departments d ON dm.dept_no = d.dept_no;

-- List the department of each employee with the following information: employee number, 
-- last name, first name, and department name.

-- Displaying only active employees (to_date LIKE '9999%')

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees e
INNER JOIN dept_emp de ON e.emp_no = de.emp_no
INNER JOIN departments d ON de.dept_no = d.dept_no
WHERE TO_CHAR(de.to_date, 'YYYY/MM/DD') LIKE '9999%'
ORDER BY emp_no;

-- List all employees whose first name is "Hercules" and last names begin with "B."

SELECT * FROM employees
WHERE first_name = 'Hercules' and last_name like 'B%'
ORDER BY emp_no;

-- List all employees in the Sales department, including their employee number, last name, first name, and department name.

-- Displaying only active employees (to_date LIKE '9999%')

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees e
INNER JOIN dept_emp de ON e.emp_no = de.emp_no
INNER JOIN departments d ON de.dept_no = d.dept_no
WHERE TO_CHAR(de.to_date, 'YYYY/MM/DD') LIKE '9999%'
AND de.dept_no IN
(
	SELECT dept_no FROM departments
	WHERE dept_name = 'Sales'
)
ORDER BY emp_no;

-- List all employees in the Sales and Development departments,
-- including their employee number, last name, first name, and department name.

-- Displaying only active employees (to_date LIKE '9999%')

SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees e
INNER JOIN dept_emp de ON e.emp_no = de.emp_no
INNER JOIN departments d ON de.dept_no = d.dept_no
WHERE TO_CHAR(de.to_date, 'YYYY/MM/DD') LIKE '9999%'
AND de.dept_no IN
(
	SELECT dept_no FROM departments
	WHERE dept_name = 'Sales' OR dept_name ='Development'
)
ORDER BY emp_no;

-- In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

SELECT employees.last_name, COUNT(last_name) AS "Count Last Name"
FROM employees
GROUP BY last_name
ORDER BY "Count Last Name" DESC;


SELECT * FROM employees WHERE emp_no = 499942;