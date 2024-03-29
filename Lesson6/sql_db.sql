create table if not exists mainmenu (
id integer primary key autoincrement,
title text not null,
url text not null
);

create table if not exists posts(
id integer primary key autoincrement,
title text not null,
text text not null,
url text not null,
time integer not null
);

create table if not exists users(
id integer primary key autoincrement,
name text not null,
email text not null,
psw text not null,
avatar BLOB default NULL,
time integer NOT NULL
);