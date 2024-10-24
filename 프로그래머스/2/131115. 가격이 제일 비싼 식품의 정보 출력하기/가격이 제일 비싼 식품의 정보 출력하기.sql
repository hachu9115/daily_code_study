-- 코드를 입력하세요
SELECT * from food_product
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT)