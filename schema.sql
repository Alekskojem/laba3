drop table if exists users;
create table users (
  id serial primary key not null,
  username varchar(80) not null,
  surname varchar(80) not null,
  lastname varchar(80) not null,
  user_group varchar(80) not null,
  group_id varchar(80) not null
);