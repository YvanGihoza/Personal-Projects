set serveroutput on

accept BldgNum prompt "Building Number: ";
accept AptNum prompt "Apt Number: ";
accept T_idNum prompt "Tenants ID: " ;
accept DurationNum prompt "Duration: " ;
accept RentNum prompt "Rent: ";
Declare
   var_Bldg number;
   var_Apt number;
   var_T_id number;
   var_Duration number;
   var_Rent decimal(6,2);
   var_Bldg_temp number;
   var_Apt_temp number;
   rowsFnd number;
Begin
   var_Bldg := '&BldgNum';
   var_Apt := '&AptNum';
   var_T_id := '&T_idNum';
   var_Duration := '&DurationNum';
   var_Rent := '&RentNum';

   select count(Building), count(Apartment) into var_Bldg_temp, var_Apt_temp from units where
   Building = var_Bldg and Apartment = var_apt;
   if var_Bldg_temp = 0 or var_Apt_temp = 0 then
      dbms_output.put_line('INVALID UNIT!');
      return;
   end if;

   select count(ID) into rowsFnd from Tenants where ID = var_T_id;
   if rowsFnd = 0 then 
      dbms_output.put_line('INVALID ID!');
      return;
   end if; 

   select count(Building), count(Apartment) into var_Bldg_temp, var_Apt_temp from units where
   Building = var_Bldg and Apartment = var_Apt and (var_Bldg,var_Apt) not in 
   (select Bldg, Apt from Assignments where (Start_Date < sysdate) and ((add_months (Start_Date, Duration)) > sysdate));
   if var_Bldg_temp = 0 or var_Apt_temp = 0 then
      dbms_output.put_line('TAKEN!');
      return;
   end if;
   
   insert into Assignments(Bldg, Apt, T_ID, Start_Date, Duration, Rent) 
   values(var_Bldg, var_Apt, var_T_id, sysdate, var_Duration, var_Rent);

   dbms_output.put_line('The records were inserted');
end;
/
