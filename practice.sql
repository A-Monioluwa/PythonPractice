CREATE TABLE roles(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);


CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    firstname VARCHAR (100),
    lastname VARCHAR (100),
    email VARCHAR (50) UNIQUE,
    `password` VARCHAR (100),
    role_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE RESTRICT
);

CREATE TABLE user_profile(
   id INT PRIMARY KEY AUTO_INCREMENT,
    gender VARCHAR(50),
    passport VARCHAR(100),
    bio TEXT,
    user_id INT,
    FOREIGN KEY( user_id) REFERENCES users(id) ON DELETE CASCADE
)




CREATE TABLE product(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) UNIQUE,
    qty INT,
    price DECIMAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE category(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE   
);

 CREATE TABLE product_category(
     id INT AUTO_INCREMENT PRIMARY KEY,
     product_id INT, 
     category_id INT,
     FOREIGN KEY (product_id) REFERENCES product(id) ON DELETE CASCADE,
     FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE RESTRICT
);

INSERT INTO roles (name)
VALUES
('Admin'),
('Seller'),
('Customer');


INSERT INTO users (firstname, lastname, email, password, role_id)
VALUES
('John', 'Doe', 'john.admin@example.com', 'john123',
 (SELECT id FROM roles WHERE name = 'Admin')),

('Sarah', 'Manager', 'sarah.manager@example.com', 'sarah123',
 (SELECT id FROM roles WHERE name = 'Admin')),

('David', 'Electronics', 'david.seller@example.com', 'david123',
 (SELECT id FROM roles WHERE name = 'Seller')),

('Grace', 'Fashion', 'grace.seller@example.com', 'grace123',
 (SELECT id FROM roles WHERE name = 'Seller')),

('Michael', 'Store', 'michael.seller@example.com', 'michael123',
 (SELECT id FROM roles WHERE name = 'Seller')),

('Mary', 'Johnson', 'mary@example.com', 'mary123',
 (SELECT id FROM roles WHERE name = 'Customer')),

('Peter', 'Williams', 'peter@example.com', 'peter123',
 (SELECT id FROM roles WHERE name = 'Customer')),

('Esther', 'Adeyemi', 'esther@example.com', 'esther123',
 (SELECT id FROM roles WHERE name = 'Customer')),

('Daniel', 'Okafor', 'daniel@example.com', 'daniel123',
 (SELECT id FROM roles WHERE name = 'Customer')),

('Blessing', 'Ibrahim', 'blessing@example.com', 'blessing123',
 (SELECT id FROM roles WHERE name = 'Customer'));


INSERT INTO category (name)
VALUES
('Electronics'),
('Fashion'),
('Home & Kitchen'),
('Beauty & Personal Care'),
('Sports & Fitness');


INSERT INTO product (title, qty, price)
VALUES
-- Electronics (1-20)
('Samsung Galaxy A15', 25, 185000),
('iPhone 13', 12, 650000),
('HP Pavilion Laptop', 10, 450000),
('Dell Inspiron Laptop', 8, 520000),
('Lenovo ThinkPad', 15, 480000),
('Wireless Bluetooth Mouse', 50, 7500),
('USB Keyboard', 40, 9500),
('JBL Bluetooth Speaker', 30, 45000),
('Sony Headphones', 20, 85000),
('Oraimo Power Bank', 45, 18000),
('Samsung Smart TV 43 Inch', 7, 320000),
('LG Smart TV 55 Inch', 6, 480000),
('Canon Digital Camera', 10, 350000),
('USB Flash Drive 64GB', 80, 6500),
('External Hard Drive 1TB', 25, 55000),
('Apple AirPods Pro', 18, 195000),
('Smart Watch Series 8', 30, 75000),
('Phone Charging Cable', 100, 3500),
('Wireless Router', 20, 35000),
('Portable Mini Projector', 12, 125000),

-- Fashion (21-40)
('Men Cotton T-Shirt', 60, 8500),
('Women Casual Dress', 40, 18000),
('Men Denim Jeans', 35, 22000),
('Women Skinny Jeans', 30, 20000),
('Men Leather Belt', 50, 7500),
('Women Handbag', 25, 35000),
('Men Sneakers', 30, 28000),
('Women Sneakers', 35, 26000),
('Men Formal Shoes', 20, 45000),
('Women High Heels', 25, 32000),
('Unisex Hoodie', 45, 25000),
('Men Polo Shirt', 40, 15000),
('Women Blouse', 35, 12000),
('Men Wrist Watch', 30, 40000),
('Women Wrist Watch', 25, 38000),
('Baseball Cap', 60, 6500),
('School Backpack', 40, 18000),
('Travel Suitcase', 15, 85000),
('Women Scarf', 55, 5000),
('Men Traditional Outfit', 20, 55000),

-- Home & Kitchen (41-60)
('Electric Blender', 25, 45000),
('Microwave Oven', 15, 95000),
('Electric Kettle', 35, 22000),
('Rice Cooker', 25, 38000),
('Non Stick Frying Pan', 45, 18000),
('Cooking Pot Set', 20, 65000),
('Dinner Plate Set', 40, 25000),
('Stainless Steel Spoon Set', 60, 8500),
('Kitchen Knife Set', 30, 15000),
('Water Dispenser', 12, 125000),
('Standing Fan', 20, 55000),
('Table Fan', 35, 28000),
('Electric Iron', 40, 22000),
('Vacuum Cleaner', 15, 85000),
('Washing Machine', 8, 280000),
('Refrigerator', 10, 350000),
('Bed Sheet Set', 45, 18000),
('Pillow Set', 50, 12000),
('Curtain Set', 30, 35000),
('Plastic Storage Box', 70, 8500),

-- Beauty & Personal Care (61-80)
('Nivea Body Lotion', 60, 8500),
('Dove Body Wash', 55, 7500),
('CeraVe Facial Cleanser', 30, 18500),
('Neutrogena Sunscreen', 35, 15000),
('Shea Butter Cream', 50, 6500),
('Hair Shampoo', 60, 8500),
('Hair Conditioner', 55, 9000),
('Hair Growth Oil', 40, 7500),
('Electric Hair Dryer', 25, 28000),
('Hair Straightener', 20, 35000),
('Makeup Brush Set', 35, 15000),
('Foundation Makeup', 40, 12000),
('Lipstick Set', 50, 9500),
('Face Powder', 45, 8500),
('Perfume Spray', 30, 25000),
('Deodorant Roll On', 70, 5500),
('Toothbrush Pack', 80, 3500),
('Toothpaste Pack', 75, 4500),
('Facial Moisturizer', 45, 12000),
('Body Scrub', 40, 9500),

-- Sports & Fitness (81-100)
('Yoga Mat', 40, 18000),
('Skipping Rope', 60, 5500),
('Dumbbell Set 5KG', 25, 35000),
('Dumbbell Set 10KG', 20, 55000),
('Resistance Band Set', 45, 12000),
('Football', 50, 15000),
('Basketball', 35, 18000),
('Tennis Racket', 20, 45000),
('Badminton Racket Set', 25, 28000),
('Running Shoes', 40, 35000),
('Sports Water Bottle', 70, 6500),
('Gym Gloves', 50, 8500),
('Exercise Ball', 30, 15000),
('Push Up Bar', 35, 12000),
('Fitness Tracker', 25, 45000),
('Cycling Helmet', 20, 28000),
('Sports Jersey', 45, 18000),
('Swimming Goggles', 40, 9500),
('Camping Tent', 15, 85000),
('Hiking Backpack', 25, 45000);


INSERT INTO product_category
    (product_id, category_id)
SELECT
    p.id,
    c.id
FROM product p
CROSS JOIN category c
WHERE
    (p.title IN (
        'Samsung Galaxy A15',
        'iPhone 13',
        'HP Pavilion Laptop',
        'Dell Inspiron Laptop',
        'Lenovo ThinkPad',
        'Wireless Bluetooth Mouse',
        'USB Keyboard',
        'JBL Bluetooth Speaker',
        'Sony Headphones',
        'Oraimo Power Bank',
        'Samsung Smart TV 43 Inch',
        'LG Smart TV 55 Inch',
        'Canon Digital Camera',
        'USB Flash Drive 64GB',
        'External Hard Drive 1TB',
        'Apple AirPods Pro',
        'Smart Watch Series 8',
        'Phone Charging Cable',
        'Wireless Router',
        'Portable Mini Projector'
    ) AND c.name = 'Electronics')

    OR (p.title IN (
        'Men Cotton T-Shirt',
        'Women Casual Dress',
        'Men Denim Jeans',
        'Women Skinny Jeans',
        'Men Leather Belt',
        'Women Handbag',
        'Men Sneakers',
        'Women Sneakers',
        'Men Formal Shoes',
        'Women High Heels',
        'Unisex Hoodie',
        'Men Polo Shirt',
        'Women Blouse',
        'Men Wrist Watch',
        'Women Wrist Watch',
        'Baseball Cap',
        'School Backpack',
        'Travel Suitcase',
        'Women Scarf',
        'Men Traditional Outfit'
    ) AND c.name = 'Fashion')

    OR (p.title IN (
        'Electric Blender',
        'Microwave Oven',
        'Electric Kettle',
        'Rice Cooker',
        'Non Stick Frying Pan',
        'Cooking Pot Set',
        'Dinner Plate Set',
        'Stainless Steel Spoon Set',
        'Kitchen Knife Set',
        'Water Dispenser',
        'Standing Fan',
        'Table Fan',
        'Electric Iron',
        'Vacuum Cleaner',
        'Washing Machine',
        'Refrigerator',
        'Bed Sheet Set',
        'Pillow Set',
        'Curtain Set',
        'Plastic Storage Box'
    ) AND c.name = 'Home & Kitchen')

    OR (p.title IN (
        'Nivea Body Lotion',
        'Dove Body Wash',
        'CeraVe Facial Cleanser',
        'Neutrogena Sunscreen',
        'Shea Butter Cream',
        'Hair Shampoo',
        'Hair Conditioner',
        'Hair Growth Oil',
        'Electric Hair Dryer',
        'Hair Straightener',
        'Makeup Brush Set',
        'Foundation Makeup',
        'Lipstick Set',
        'Face Powder',
        'Perfume Spray',
        'Deodorant Roll On',
        'Toothbrush Pack',
        'Toothpaste Pack',
        'Facial Moisturizer',
        'Body Scrub'
    ) AND c.name = 'Beauty & Personal Care')

    OR (p.title IN (
        'Yoga Mat',
        'Skipping Rope',
        'Dumbbell Set 5KG',
        'Dumbbell Set 10KG',
        'Resistance Band Set',
        'Football',
        'Basketball',
        'Tennis Racket',
        'Badminton Racket Set',
        'Running Shoes',
        'Sports Water Bottle',
        'Gym Gloves',
        'Exercise Ball',
        'Push Up Bar',
        'Fitness Tracker',
        'Cycling Helmet',
        'Sports Jersey',
        'Swimming Goggles',
        'Camping Tent',
        'Hiking Backpack'
    ) AND c.name = 'Sports & Fitness');


SELECT 'Products' AS table_name,
       COUNT(*) AS total
FROM product

UNION ALL

SELECT 'Categories', COUNT(*)
FROM category

UNION ALL

SELECT 'Product Categories', COUNT(*)
FROM product_category

UNION ALL

SELECT 'Roles', COUNT(*)
FROM roles;
