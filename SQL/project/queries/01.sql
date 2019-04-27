select first_name,middle_name,last_name,street_address,city,state,zipcode
                	from person
            	where 
Mail_To='Y'
            	order by state,city,last_name,first_name,middle_name;