INSERT INTO store_category (name)
VALUES
  ('Food'),
  ('Household Supplies'),
  ('Electronics'),
  ('Books'),
  ('Toys');

INSERT INTO store_item (id, name, slug, price, image, description, quantity, created, updated, category_id)
VALUES
  (1, 'Tin of Cookies', 'tin-of-cookies', 2.99, 'cookie-tin.jpg', 'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.', 500, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 1),
  (2, 'Canned Coffee', 'canned-coffee', 1.99, 'canned-coffee.jpg', 'Praesent sed lacinia mauris. Nulla congue nibh magna, at feugiat nunc scelerisque quis. Donec iaculis rutrum vulputate. Suspendisse lectus sem, vulputate ac lectus sed, placerat consequat dui.', 500, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 1),
  (3, 'Toilet Paper', 'toilet-paper', 7.99, 'toilet-paper.jpg', 'Donec volutpat erat erat, sit amet gravida justo sodales in. Phasellus tempus euismod urna. Proin ultrices nisi ut ipsum congue, vitae porttitor libero suscipit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam lacinia a nisi non congue.', 20, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 2),
  (4, 'Handmade Soap', 'handmade-soap', 3.99, 'soap.jpg', 'Praesent placerat, odio vel euismod venenatis, lectus arcu laoreet felis, et fringilla sapien turpis vestibulum nisl.', 50, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 2),
  (5, 'Set of Wooden Spoons', 'set-of-wooden-spoons', 14.99, 'wooden-spoons.jpg', 'Vivamus ut turpis in purus pretium mollis. Donec turpis odio, semper vel interdum ut, vulputate at ex. Duis dignissim nisi vel tortor imperdiet finibus. Aenean aliquam sagittis rutrum.', 100, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 2),
  (6, 'Camera', 'camera', 399.99, 'camera.jpg', 'In sodales, ipsum quis ultricies porttitor, tellus urna aliquam arcu, eget venenatis purus ligula ut nisi. Fusce ut felis dolor. Mauris justo ante, aliquet non tempus in, tempus ac lorem. Aliquam lacinia dolor eu sem eleifend ultrices. Etiam mattis metus metus. Sed ligula dui, placerat non turpis vitae, suscipit volutpat elit.', 30, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 3),
  (7, 'Tablet', 'tablet', 199.99, 'tablet.jpg', 'Praesent placerat, odio vel euismod venenatis, lectus arcu laoreet felis, et fringilla sapien turpis vestibulum nisl.', 50, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 3),
  (8, 'Tales at Bedtime', 'tales-at-badtime', 1.99, 'bedtime-book.jpg', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ornare diam quis eleifend rutrum. Aliquam nulla est, volutpat non enim nec, pharetra gravida augue. Donec vitae dictum neque. Pellentesque arcu lorem, fringilla non ligula ac, tristique bibendum erat. Ut a semper nibh. Quisque a mi et mi tempor ultricies.', 100, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 4),
  (9, 'Spinning Top', 'spinning-top', 3.99, 'spinning-top.jpg', 'Ut vulputate hendrerit nibh, a placerat elit cursus interdum.', 1000, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 5),
  (10, 'Set of Plastic Horses', 'set-of-plastic-horses', 2.99, 'plastic-horses.jpg', 'Sed a mauris condimentum, elementum enim in, rhoncus dui. Phasellus lobortis leo odio, sit amet pharetra turpis porta quis.', 1000, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 5),
  (11, 'Teddy Bear', 'teddy-bear', 7.99, 'teddy-bear.jpg', 'Vestibulum et erat finibus erat suscipit vulputate sed vitae dui. Ut laoreet tellus sit amet justo bibendum ultrices. Donec vitae felis vestibulum, congue augue eu, finibus turpis.', 100, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 5),
  (12, 'Alphabet Blocks', 'alphabet-blocks', 9.99, 'alphabet-blocks.jpg', 'Morbi consectetur viverra urna, eu fringilla turpis faucibus sit amet. Suspendisse potenti. Donec at dui ac sapien eleifend hendrerit vel sit amet lectus.', 600, '2003-04-12 04:05:06 EST', '2003-04-12 04:05:06 EST', 5);

