create table Users (
    id integer primary key autoincrement,
    name varchar(64) not null,
    email varchar(64) not null,
    password varchar(64) not null
);

create table Posts (
    id integer primary key autoincrement,
    title varchar(64) not null,
    body text not null,
    category varchar(100) not null,
    user_id integer default ('0000'),
    created_at timestamp default (datetime('now', 'localtime'))
);

create table Rates (
    id integer primary key autoincrement,
    user_id integer default ('0000'),
    post_id integer default ('0000'),
    value integer
);

insert into users (email, password) values ("c@hackbrightacademy.com", "fish_are_awesome");
