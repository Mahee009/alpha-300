
-- Reviews + Ratings + Helpfulness Votes - Schema


-- 1. Users table - people who write reviews and vote
CREATE TABLE users (
    user_id     SERIAL PRIMARY KEY,
    username    VARCHAR(50)  NOT NULL UNIQUE,
    email       VARCHAR(100) NOT NULL UNIQUE,
    created_at  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 2. Products table - items that can be reviewed
CREATE TABLE products (
    product_id  SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    price       DECIMAL(10,2) NOT NULL,
    created_at  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 3. Reviews table - a user's rating + review for a product
CREATE TABLE reviews (
    review_id   SERIAL PRIMARY KEY,
    product_id  INTEGER  NOT NULL,
    user_id     INTEGER  NOT NULL,
    rating      INTEGER  NOT NULL CHECK (rating BETWEEN 1 AND 5),
    title       VARCHAR(100),
    comment     TEXT,
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (product_id, user_id),
    CONSTRAINT fk_reviews_product
        FOREIGN KEY (product_id) REFERENCES products(product_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_reviews_user
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE
);

-- 4. Review_Votes table - helpful / not helpful votes on a review
CREATE TABLE review_votes (
    review_id   INTEGER NOT NULL,
    user_id     INTEGER NOT NULL,
    is_helpful  BOOLEAN NOT NULL,
    voted_at    TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (review_id, user_id),
    CONSTRAINT fk_votes_review
        FOREIGN KEY (review_id) REFERENCES reviews(review_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_votes_user
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE
);


-- Indexes


-- reviews are mostly fetched by product (product page)
CREATE INDEX idx_reviews_product ON reviews(product_id);

-- to get all reviews written by a user
CREATE INDEX idx_reviews_user ON reviews(user_id);

-- filtering reviews by star rating
CREATE INDEX idx_reviews_rating ON reviews(rating);

-- counting votes for a review
CREATE INDEX idx_votes_review ON review_votes(review_id);

-- votes given by a user
CREATE INDEX idx_votes_user ON review_votes(user_id);