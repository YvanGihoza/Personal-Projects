A PL/SQL procedure that performs the following tasks in order to add a record to the Assignments table.

1.  The procedure accepts from user the values for the following attributes: Bldg, Apt, T_ID, Duration, and Rent.

2.  Then it performs the following checks:
    (a) The unit, i.e., the (bldg, apt) pair, must exist in Units table.
    (b) The t_id must exist in Tenants table.
    (c) The unit must be available for rent.  [See task five of last assignment.]

    If any of these conditions fail, the procedure prints an appropriate message and quits.

3.  If all of the above conditions are satisfied, the procedure determines the start_date as the date when 
the procedure being run.

4.  The procedure then inserts a record into the Assignments table having the attributes’ values as supplied by 
the user in step 1, and the start_date value as determined in step 3.  It then prints a message indicating successful 
addition of the record and quits.
