-- 코드를 입력하세요
SELECT F.flavor from first_half F 
left outer join icecream_info I ON F.flavor = I.flavor
where total_order >= 3000 and ingredient_type = 'fruit_based'
order by total_order desc