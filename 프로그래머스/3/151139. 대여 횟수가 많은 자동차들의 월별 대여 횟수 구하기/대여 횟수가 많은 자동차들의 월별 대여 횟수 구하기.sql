# -- 코드를 입력하세요

# # SELECT CAR_ID, COUNT(CAR_ID)
# # FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# # WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
# # GROUP BY CAR_ID
# # HAVING COUNT(*) > 5
# SELECT
#     MONTH(START_DATE) as MONTH,
#     CAR_ID,
#     COUNT(*) as RECORDS
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE month(start_date) between 8 and 10  and CAR_ID IN (SELECT CAR_ID
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
# GROUP BY CAR_ID
# HAVING COUNT(*) >= 5)
# GROUP BY MONTH(START_DATE)
# ORDER BY MONTH(START_DATE) ASC, CAR_ID DESC;


select month(start_date)as MONTH,car_id as CAR_ID,count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where month(start_date) between 8 and 10  and
car_id in 
(
select car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where month(start_date) between 8 and 10  
group by car_id
having count(*) >4
)
group by car_id,month
order by month asc ,car_id desc