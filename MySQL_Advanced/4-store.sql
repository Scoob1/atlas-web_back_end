-- Create a trigger to decrease the quantity of an item when a new order is added
DELIMITER //

CREATE TRIGGER decrease_quantity_after_insert
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity in the items table based on the order number
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //

DELIMITER ;

