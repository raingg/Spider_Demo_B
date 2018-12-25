drop database if exists db_b;
create database db_b;

-- user table
drop table if exists db_b.user;
create table db_b.user (
  id       int auto_increment primary key
  comment 'id PK',
  email    varchar(255) not null unique
  comment 'email NN UN',
  password varchar(64)  not null
  comment 'password NN'
)
  comment 'user table';

-- user_info table
drop table if exists db_b.user_info;
create table db_b.user_info (
  id         int          auto_increment primary key
  comment 'id PK',
  username   varchar(255) comment 'username',
  avatar     varchar(255) default 'default.png'
  comment 'avatar',
  mobile     varchar(255) comment 'mobile',
  createTime datetime comment 'sign up time',
  updateTime datetime comment 'last sign in time',
  updateIp   varchar(255) comment 'last sign in IP address',
  token      varchar(255) comment 'reset password token',
  tokenTime  bigint comment 'token time',
  userId     int comment 'user id FK'
)
  comment 'user info table';

-- product table
drop table if exists db_b.product;
create table db_b.product (
  id             int                     auto_increment primary key
  comment 'id PK',
  title          varchar(255)   not null
  comment '名称 NN',
  `desc`         text comment '描述',
  price          decimal(10, 2) not null
  comment '价格 NN',
  originalPrice  decimal(10, 2) comment '原价',
  coverPicture   varchar(255)   not null
  comment '封面图片 NN',
  slidePictures  text           not null
  comment '幻灯图片组 NN',
  detailPictures text           not null
  comment '详情图片组 NN',
  spec           varchar(255)   not null
  comment '规格 NN',
  stock          int            not null
  comment '库存数量 NN',
  status         int            not null default 0
  comment '状态：0- 1- 2-',
  createTime     datetime       not null
  comment '创建时间 NN',
  updateTime     datetime comment '更新时间',
  categoryId     int comment 'category id FK'
)
  comment 'product table';

# id,title,group,desc,icon,categoryId

set foreign_key_checks = 0;
-- category table
drop table if exists db_b.category;
create table db_b.category (
  id         int                   auto_increment primary key
  comment 'id PK',
  title      varchar(255) not null
  comment 'title NN',
  `group`    varchar(255)          default null
  comment '分组',
  `desc`     varchar(255)          default null
  comment 'describe NN',
  icon       varchar(255)          default null
  comment 'icon',
  categoryId int comment 'parent category id NULL-',
  status     int                   default 0
  comment 'status 0-; 1-',
  createTime datetime     not null default now()
  comment 'create time NN',
  updateTime datetime              default null
  comment '更新时间'
)
  comment 'category table';

-- address table
drop table if exists db_b.address;
create table db_b.address (
  id       int                   auto_increment primary key
  comment 'id PK',
  province varchar(255) not null
  comment 'province NN',
  city     varchar(255)
  comment 'city',
  area     varchar(255) not null
  comment 'area NN',
  town     varchar(255) not null
  comment 'town NN',
  detail   varchar(255) not null
  comment 'detail NN',
  name     varchar(255) not null
  comment 'name NN',
  mobile   varchar(255) not null
  comment 'mobile NN',
  status   int          not null default 0
  comment 'status 1: default address',
  userId   int comment 'user id FK'
)
  comment 'address table';

-- cart table
drop table if exists db_b.cart;
create table db_b.cart (
  id         int auto_increment primary key
  comment 'id PK',
  productId  int      not null
  comment 'product id NN FK',
  number     int      not null
  comment 'product number NN',
  createTime datetime not null
  comment 'create time NN',
  updateTime datetime comment 'update time',
  userId     int comment 'user id FK'
)
  comment 'cart table';

alter table db_b.user_info
  add constraint
  user_info_fk_userId
foreign key (userId)
references db_b.user (id);

alter table db_b.product
  add constraint
  product_fk_categoryId
foreign key (categoryId)
references db_b.category (id);

alter table db_b.address
  add constraint
  address_fk_userId
foreign key (userId)
references db_b.user (id);

alter table db_b.cart
  add constraint
  cart_fk_productId
foreign key (productId)
references db_b.product (id);

alter table db_b.cart
  add constraint
  cart_fk_userId
foreign key (userId)
references db_b.user (id);

select *
from db_b.user;

select *
from db_b.user_info;

select *
from db_b.product;

select *
from db_b.category;

select now();

select *
from db_b.category c1
       inner join db_b.category c2 on c1.id = c2.parentId;

-- String title, String desc, double price, String coverPicture, String slidePictures, String detailPictures, String spec, int stock, int status, String createTime, String updateTime

select *
from db_b.product;

-- MySQL

select *
from db_b.product
limit 3 offset 9;

select *
from db_b.address;

set foreign_key_checks = 1;

truncate table db_b.user;

truncate table db_b.user_info;

select *
from db_b.cart;

truncate db_b.cart;

select sum(number)
from db_b.cart
where userId = 1
group by userId;

select *
from db_b.cart
where id in (3, 4);

select *
from db_b.category;

truncate table db_b.category;

load data local infile 'D:\\PycharmProjects\\Spider_Demo_B\\data\\csv\\category.csv'
into table db_b.category
fields terminated by ','
ignore 1 lines
(id, title, @v_group, @v_desc, @v_icon, @v_categoryId)
set
`group` = ifnull(@v_group, ''),
`desc` = ifnull(@v_desc, ''),
icon = ifnull(@v_icon, ''),
categoryId = ifnull(@v_categoryId, '');
