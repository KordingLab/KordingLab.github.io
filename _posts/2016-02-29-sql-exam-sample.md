---
title: Microsoft SQL example
categories: students
header-img: images/post/dino3.jpg
---

I have to take EDW exam (Northwestern Data Warehouse exam) this coming week which is an SQL exam. I think people/ lab members who will work with EDW in order to access medical data that they provide have to take that too. The database that they have is Microsoft SQL 2008 (MSSQL). There is an easy way to query MSSQL on my Mac by installing
native app called [SQLPro for MSSQL](http://www.macsqlclient.com/). For SQLPro, you have to add following field that EDW gave to an application before connecting to the database: server name (`<serve_name>.database.windows.net`),
Login (`user_name`), Password (`password`), Database `database_name`.
Also there is a way to connect using Python with  Pandas library and [`pymssql`](http://www.pymssql.org/en/latest/) to connect to the database as follows:


```python
import pandas as pd
import pymssql
conn = pymssql.connect(server='<serve_name>.database.windows.net',
                       user='<user_name>@<server_name>.database.windows.net',
                       password='<password>',
                       database='<database_name>',
                       port='1433',
                       login_timeout=15) # create connection
pd.read_sql("select * from information_schema.tables", conn) # put any query in first argument
```

The following is my answer to the example questions:

List tables available

```sql
select * from information_schema.tables;
```

List all gender codes available in the system sorted alphabetically by title.

```sql
select distinct gender_title from edw_emr_ods.gender_codes as g order by g.gender_title
```

List the two youngest patients showing a patient's name and date of birth.

```sql
select top 2 patient_nm, dob from edw_emr_ods.patients as p order by p.dob desc
```

List all diagnosis codes that contain the word "pain" in their title showing the diagnosis code and its title.

```sql
select code,title from edw_emr_ods.diagnoses where title like '%pain%'
```

List the current date and time (the example below was generated on March 12, 2013 at 8:05 AM for example):

```sql
select getdate() as current_dt
```

List all patients showing each patient's name and their NMH MRN (if they have one).

```sql
select patient_nm, mrn as nmh_mrn
from edw_emr_ods.patients  p
left join edw_emr_ods.patient_mrns pm
on (p.patient_id = pm.patient_id and pm.mrn_type = 'NMH')
```

Dr. Nick Riviera wants a list of all his encounters showing the encounter ID, department name,and encounter date. He's also requested that the earliest encounter display first.

```sql
select d.department_id, d.department_nm, e.start_dts
from edw_emr_ods.encounters e, edw_emr_ods.departments d
where (e.provider_id = 1 and e.department_id = d.department_id)
order by e.start_dts asc;
```

List all patients showing each person’s month of birth and whether that falls within the first or second half of the calendar year.

```sql
select patient_nm, MONTH(dob) as dob_month,
case when MONTH(dob) <= 6
	then '1st Half'
	else '2nd Half'
end as part_of_year
from edw_emr_ods.patients;
```

List each diagnosis in the system and show the first time it was documented on any encounter.

```sql
select code, title, MIN(start_dts) as earliest_case
from edw_emr_ods.diagnoses as d, edw_emr_ods.encounters as e, edw_emr_ods.encounter_diagnoses as ed
where d.diagnosis_id = ed.diagnosis_id and ed.encounter_id = e.encounter_id
group by d.code, d.title
```

The clinical application has some basic built-in reporting functionality and it reports that only 17 valid encounters exist. The “encounters” table has 18 rows. Why might the system only believe 17 of those rows are valid?

**ans.** there is a column name `deleted_ind` that indicates whether that row is still existed or not

```sql
select COUNT(*) from edw_emr_ods.encounters -- give 18
select COUNT(*) from edw_emr_ods.encounters as e where e.deleted_ind = 0 -- give 17
```

List all encounter types that have been charted on valid encounters and how many times each was charted. If the encounter type is missing, use the title “Unknown.”

```sql
select coalesce(et.encounter_title, 'unknown') as encounter_title, COUNT(encounter_type_cd) as encounter_ct
from edw_emr_ods.encounter_type_codes et
right join edw_emr_ods.encounters e
on (et.encounter_type_code_id = e.encounter_type_cd and e.deleted_ind = 0)
group by et.encounter_title
```

The Division Administrator of the “Inpatient Floor 8” department needs a list of all providers and the number of valid encounters they had in the department. Even providers with no visits in that department should appear.

```sql
select p.provider_nm, count(e.provider_id) as encounter_ct
from edw_emr_ods.providers as p
left join edw_emr_ods.encounters as e
on (p.provider_id = e.provider_id and e.department_id = 4 and e.deleted_ind = 0)
group by p.provider_nm
```

Each department would like to contact the first patient who was treated by their staff. Generate a list of each department, the name of the first patient and the date on which that first visit occurred.

```sql
select d.department_nm, p.patient_nm, de.start_dts
from
edw_emr_ods.departments as d,
edw_emr_ods.encounters as e,
edw_emr_ods.patients as p,
(select d.department_id, min(e.start_dts) as start_dts
from edw_emr_ods.departments as d, edw_emr_ods.encounters as e, edw_emr_ods.patients as p
where (d.department_id = e.department_id and e.patient_id = p.patient_id)
group by d.department_id) as de
where (d.department_id = e.department_id and e.patient_id = p.patient_id and de.department_id = e.department_id and de.start_dts = e.start_dts)
```

In querying SQL, “sargable” search terms are important. What does this mean and why is it important?

**Ans.** sargable means that a query is capable of having the query engine optimize the execution plan that the query use
