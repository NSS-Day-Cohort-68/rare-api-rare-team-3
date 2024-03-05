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

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');


-- Add posts to test get functionailty
INSERT INTO Posts ("user_id", "category_id", "title", "publication_date", "image_url", "content", "approved")
VALUES (2, 2, 'First Post', '2024-03-05', NULL, 'Lorem ipsum content for the first post.', 1);

INSERT INTO Posts ("user_id", "category_id", "title", "publication_date", "image_url", "content", "approved")
VALUES (3, 1, 'Second Post', '2024-03-06', NULL, 'Lorem ipsum content for the second post.', 1);

INSERT INTO Posts ("user_id", "category_id", "title", "publication_date", "image_url", "content", "approved")
VALUES (1, 3, 'Third Post', '2024-03-07', NULL, 'Lorem ipsum content for the third post.', 0);

INSERT INTO Posts ("user_id", "category_id", "title", "publication_date", "image_url", "content", "approved")
VALUES (1, 2, 'Third Post', '2024-03-07', NULL, 'Lorem ipsum content for the fourth post.', 1);

-- Add users to join in get Posts fetch
INSERT INTO "Users" ("first_name", "last_name", "email", "bio", "username", "password", "profile_image_url", "created_on", "active")
VALUES ('John', 'Doe', 'john@example.com', 'Web developer', 'john_doe', 'hashed_password_1', NULL, '2024-03-05', 1);

INSERT INTO "Users" ("first_name", "last_name", "email", "bio", "username", "password", "profile_image_url", "created_on", "active")
VALUES ('Jane', 'Smith', 'jane@example.com', 'Software engineer', 'jane_smith', 'hashed_password_2', NULL, '2024-03-06', 1);

INSERT INTO "Users" ("first_name", "last_name", "email", "bio", "username", "password", "profile_image_url", "created_on", "active")
VALUES ('Bob', 'Johnson', 'bob@example.com', 'UX designer', 'bob_johnson', 'hashed_password_3', NULL, '2024-03-07', 0);

-- Add categories to join in get Posts fetch
INSERT INTO "Categories" ("label")
VALUES ('Sports');

INSERT INTO "Categories" ("label")
VALUES ('Science');