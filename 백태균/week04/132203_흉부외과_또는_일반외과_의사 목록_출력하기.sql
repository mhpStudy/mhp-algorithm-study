select dr_name, dr_id, mcdp_cd, hire_ymd
from doctor
where mcdp_cd = "GS" or mcdp_cd = "CS"
order by hire_ymd desc, dr_name;