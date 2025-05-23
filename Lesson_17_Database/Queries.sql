/* Show first name, last name, and gender of patients whose gender is 'M' */
SELECT first_name, last_name, gender 
FROM patients 
WHERE gender='M';

/* Show first name and last name of patients who does not have allergies. (null) */
SELECT first_name, last_name 
FROM patients 
WHERE allergies IS null;

/* Show first name of patients that start with the letter 'C' */
SELECT first_name 
FROM patients 
WHERE first_name LIKE "C%";

/* Show first name and last name of patients that weight within the range of 100 to 120 (inclusive) */
SELECT first_name, last_name 
FROM patients 
WHERE weight BETWEEN 100 and 120;

/* Update the patients table for the allergies column. If the patient's allergies is null then replace it with 'NKA' */
UPDATE patients 
SET allergies = 'NKA'
WHERE allergies IS NULL;

/* Show first name and last name concatinated into one column to show their full name. */
select concat(first_name, ' ', last_name) as full_name
FROM patients;

/* Show first name, last name, and the full province name of each patient. Example: 'Ontario' instead of 'ON' - JOINS */
select first_name, last_name, province_name
FROM patients
JOIN province_names
ON province_names.province_id = patients.province_id;
