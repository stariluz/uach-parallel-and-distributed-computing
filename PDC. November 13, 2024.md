Create or replace trigger replicar_jh
after insert or delete or update on job_history
for each row
begin 
if inserting then
    insert into rjob_history values(:new.employee_id, :new.start_date ...);
elsif deleting then
    delete from rjob_history
    where employee_id =:old.employee_id and start_date = :old.start_date;
else
    update rjob_history
    set end_date
endif
end replicar_jg;


Crear vistas materializadas.

Las vistas materializadas no tienen datos propios.

grant create any materialized view to user1;

create materialized view resulen_sal;
build immediate
refresh complete on demand -- on commit, 
as
    select deptno Nodepto, sum(sal) Nomina
    from emp
    group by deptno;

execute dbms_mview.refresh('resumen_sal');

create materialized view resumen_sal
build deferred
refresh complete next sysdate * .24/24
as
    ...
    