-- 코드를 작성해주세요
SELECT COUNT(*) as count
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0  -- 2번 형질이 없는 경우
  AND ((GENOTYPE & 1) = 1 OR (GENOTYPE & 4) = 4);  -- 1번 또는 3번 형질을 보유한 경우