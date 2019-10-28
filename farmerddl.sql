create table farmer (
	aid		varchar(12) not null, 
	first_name	varchar(20) not null,
	last_name	varchar(20) not null, 
	village		varchar(20) not null,
	education	varchar(20) not null,
	gender		varchar(20) not null,
	mobile_no	numeric(10,0) not null,
	primary key (aid)
);

create table field (
	fid 		varchar(4) not null,
	crop_name 	varchar(20) not null,
	irrogation 	varchar(20) not null,
	season 		varchar(20) not null,
	primary key(fid, season)
);

create table service (
	region			varchar(20) not null,
	service_mode 	varchar(20) not null,
	pincode			numeric(6,0) not null,
	primary key(service_mode, pincode)
);

create table scheme (
	sid 		varchar(4) not null,
	scheme_name	varchar(30) not null,
	loan 		numeric(8,2) not null,
	primary key (sid)
);

create table sector (
	aid 	varchar(12),
	fid		varchar(4),
	sector_no numeric(3,0) not null,
	season 	varchar(20),
	primary key(aid, fid, season),
	foreign key(aid) references farmer(aid) on delete cascade,
	foreign key(fid, season) references field(fid, season)
);
	
create table takes (
	aid 	varchar(12),
	sid		varchar(4),
	primary key(aid),
	foreign key(aid) references farmer(aid) on delete cascade,
	foreign key(sid) references loan(sid)
);
	
create table business (
	aid 	varchar(12),
	pincode varchar,
	service_mode	varchar(20),
	income 	varchar(8) not null,
	primary key(aid, pincode, service_mode),
	foreign key(aid) references farmer(aid) on delete cascade,
	foreign key(pincode, service_mode) references service(pincode, service_mode)
);
