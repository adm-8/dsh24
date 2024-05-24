CREATE TABLE IF NOT EXISTS app.users (
    id  integer NOT NULL PRIMARY KEY,
    username varchar(100) NOT NULL,
    first_name varchar(100) NOT NULL DEFAULT '',
    last_name varchar(100) NOT NULL DEFAULT '',
    current_state jsonb NOT NULL DEFAULT '{}'::jsonb,
    last_action_dttm timestamp NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS app.messages (
    id  integer NOT NULL,
    user_id integer NOT NULL,
    body jsonb NOT NULL DEFAULT '{}'::jsonb,
    msg_dttm timestamp NOT NULL DEFAULT NOW()
);

