CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);
CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);
CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`category_id`) REFERENCES `Categories`(`id`)
);
CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
 "creation_datetime" date,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);
CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);
CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);
CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);


INSERT INTO Reactions ('label', 'image_url')
VALUES ('happy', 'https://pngtree.com/so/happy');


-- Add posts to database
INSERT INTO Posts (
    "user_id",
    "category_id",
    "title",
    "publication_date",
    "image_url",
    "content",
    "approved"
  )
VALUES (
    2,
    2,
    'The Impact of Artificial Intelligence on Healthcare',
    '2024-03-11 17:15:27.051853',
    NULL,
    'Artificial intelligence (AI) is revolutionizing the healthcare industry...',
    1
  );

INSERT INTO Posts (
    "user_id",
    "category_id",
    "title",
    "publication_date",
    "image_url",
    "content",
    "approved"
  )
VALUES (
    3,
    1,
    'Climate Change: The Urgency for Global Action',
    '2024-03-11 17:15:27.051853',
    NULL,
    'Climate change is one of the most pressing challenges facing humanity...',
    1
  );

INSERT INTO Posts (
    "user_id",
    "category_id",
    "title",
    "publication_date",
    "image_url",
    "content",
    "approved"
  )
VALUES (
    1,
    3,
    'The Future of Renewable Energy Sources',
    '2024-03-11 17:15:27.051853',
    NULL,
    'Renewable energy sources such as solar, wind, and hydroelectric power...',
    0
  );

INSERT INTO Posts (
    "user_id",
    "category_id",
    "title",
    "publication_date",
    "image_url",
    "content",
    "approved"
  )
VALUES (
    6,
    2,
    'Exploring the Potential of Space Tourism',
    '2024-03-11 17:15:27.051853',
    NULL,
    'Space tourism, once a distant dream, is now becoming a tangible reality...',
    1
  );

INSERT INTO Posts (
    "user_id",
    "category_id",
    "title",
    "publication_date",
    "image_url",
    "content",
    "approved"
)
VALUES (
    2,
    1,
    'The Importance of Regular Exercise',
    '2024-03-11 17:15:27.051853',
    NULL,
    'Regular exercise has numerous benefits for both physical and mental health...',
    1
);

INSERT INTO Posts (
    "user_id",
    "category_id",
    "title",
    "publication_date",
    "image_url",
    "content",
    "approved"
)
VALUES (
    3,
    3,
    'Advancements in Artificial Neural Networks',
    '2024-03-11 17:15:27.051853',
    NULL,
    'Artificial neural networks have seen significant advancements...',
    1
);

INSERT INTO Posts (
    "user_id",
    "category_id",
    "title",
    "publication_date",
    "image_url",
    "content",
    "approved"
)
VALUES (
    4,
    2,
    'The Rise of E-Sports',
    '2024-03-11 17:15:27.051853',
    NULL,
    'E-Sports, or electronic sports, have become increasingly popular...',
    1
);

INSERT INTO Posts (
    "user_id",
    "category_id",
    "title",
    "publication_date",
    "image_url",
    "content",
    "approved"
)
VALUES (
    3,
    1,
    'The Future of Electric Vehicles',
    '2024-03-11 17:15:27.051853',
    NULL,
    'Electric vehicles are poised to revolutionize the automotive industry...',
    1
);

INSERT INTO Posts (
    "user_id",
    "category_id",
    "title",
    "publication_date",
    "image_url",
    "content",
    "approved"
)
VALUES (
    2,
    3,
    'The Impact of Climate Change on Biodiversity',
    '2024-03-11 17:15:27.051853',
    NULL,
    'Climate change poses a significant threat to global biodiversity...',
    1
);

-- Add users to database
INSERT INTO Users (
    "first_name",
    "last_name",
    "email",
    "bio",
    "username",
    "password",
    "profile_image_url",
    "created_on",
    "active"
  )
VALUES (
    'John',
    'Doe',
    'john@example.com',
    'Web developer',
    'john_doe',
    'hashed_password_1',
    NULL,
    '2024-03-11 17:15:27.051853',
    1
  );

INSERT INTO Users (
    "first_name",
    "last_name",
    "email",
    "bio",
    "username",
    "password",
    "profile_image_url",
    "created_on",
    "active"
  )
VALUES (
    'Jane',
    'Smith',
    'jane@example.com',
    'Software engineer',
    'jane_smith',
    'hashed_password_2',
    NULL,
    '2024-03-11 17:15:27.051853',
    1
  );

INSERT INTO Users (
    "first_name",
    "last_name",
    "email",
    "bio",
    "username",
    "password",
    "profile_image_url",
    "created_on",
    "active"
  )
VALUES (
    'Bob',
    'Johnson',
    'bob@example.com',
    'UX designer',
    'bob_johnson',
    'hashed_password_3',
    NULL,
    '2024-03-11 17:15:27.051853',
    0
  );

INSERT INTO Users (
    "first_name",
    "last_name",
    "email",
    "bio",
    "username",
    "password",
    "profile_image_url",
    "created_on",
    "active"
)
VALUES (
    'Emily',
    'Jones',
    'emily@example.com',
    'Graphic Designer',
    'emily_jones',
    'hashed_password_4',
    NULL,
    '2024-03-11 17:15:27.051853',
    1
);

INSERT INTO Users (
    "first_name",
    "last_name",
    "email",
    "bio",
    "username",
    "password",
    "profile_image_url",
    "created_on",
    "active"
)
VALUES (
    'Michael',
    'Brown',
    'michael@example.com',
    'Marketing Manager',
    'michael_brown',
    'hashed_password_5',
    NULL,
    '2024-03-11 17:15:27.051853',
    1
);

INSERT INTO Users (
    "first_name",
    "last_name",
    "email",
    "bio",
    "username",
    "password",
    "profile_image_url",
    "created_on",
    "active"
)
VALUES (
    'Sarah',
    'Clark',
    'sarah@example.com',
    'UX/UI Designer',
    'sarah_clark',
    'hashed_password_6',
    NULL,
    '2024-03-11 17:15:27.051853',
    0
);

-- Add starter categories to database
INSERT INTO Categories ('label')
VALUES ('News');

INSERT INTO Categories ("label")
VALUES ('Sports');

INSERT INTO Categories ("label")
VALUES ('Science');

  
-- Add starter comments to database
INSERT INTO Comments ("post_id", "author_id", "content", "creation_datetime")
VALUES (1, 1, "This is such a funny comment!", '2024-03-11 17:15:27.051853');

INSERT INTO Comments ("post_id", "author_id", "content", "creation_datetime")
VALUES (2, 2, "BLAH BLAH BLAH", '2024-03-11 17:15:27.051853');

INSERT INTO Comments ("post_id", "author_id", "content", "creation_datetime")
VALUES (1, 1, "test test test", '2024-03-11 17:15:27.051853');

-- Add starter tags to database
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Tags ('label') VALUES ('Python');
INSERT INTO Tags ('label') VALUES ('Machine Learning');
INSERT INTO Tags ('label') VALUES ('Data Science');
INSERT INTO Tags ('label') VALUES ('Artificial Intelligence');
