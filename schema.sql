create table users (
    id integer primary key,
    email varchar(64) not null,
    password varchar(64) not null
);

insert into users (email, password) values ("c@hackbrightacademy.com", "fish_are_awesome");

Users
=====
id:int
email:string
password:string

Posts
=====
id:int
title:string
body:text
user_id:int
created_at:date

Votes
=====
id:int
user_id:int
post_id:int
value:int
