SELECT p.product_name, pl.year, pl.price
from Product p
RIGHT JOIN Sales pl ON p.product_id = pl. product_id;