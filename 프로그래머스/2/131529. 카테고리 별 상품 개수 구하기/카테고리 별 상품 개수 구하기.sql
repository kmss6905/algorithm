SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY_CODE, COUNT(*) AS PRODUCT_COUNT
FROM PRODUCT
GROUP BY LEFT(PRODUCT_CODE, 2)
ORDER BY CATEGORY_CODE ASC;