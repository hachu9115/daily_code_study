-- 코드를 작성해주세요
select concat(quarter(differentiation_date), 'Q') AS 'QUARTER',
count(*) as ECOLI_COUNT from ECOLI_DATA
group by concat(quarter(differentiation_date), 'Q')
ORDER BY concat(quarter(differentiation_date), 'Q');