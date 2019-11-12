create table farmer (
	aid		varchar(12) not null,
	first_name	varchar(20) not null,
	last_name	varchar(20) not null, 
	village		varchar(20) not null,
	education	varchar(20) not null,
	gender		varchar(20) not null,
	mobile_no	varchar(10) not null,
	primary key (aid)
);

create table field (
	fid 		int not null AUTO_INCREMENT,
	crop_name 	varchar(20) not null,
	irrogation 	varchar(20) not null,
	season 		varchar(20) not null,
	primary key(fid)
);

create table service (
	region			varchar(20) not null,
	service_mode 	varchar(20) not null,
	pincode			varchar(6) not null,
	primary key(service_mode, pincode)
);

create table scheme (
	sid 		varchar(4) not null,
	scheme_name	varchar(30) not null,
	loan 		varchar(8) not null,
	primary key (sid)
);

create table sector (
	aid 	varchar(12),
	fid		int,
	sector_no varchar(3) not null,
	primary key(aid, fid),
	foreign key(aid) references farmer(aid) on delete cascade,
	foreign key(fid) references field(fid)
);

create table takes (
	aid 	varchar(12),
	sid		varchar(4),
	primary key(aid),
	foreign key(aid) references farmer(aid) on delete cascade,
	foreign key(sid) references scheme(sid)
);
	
create table business (
	aid 	varchar(12),
	service_mode	varchar(20),
	pincode varchar(6),
	income 	varchar(8) not null,
	primary key(aid, pincode, service_mode),
	foreign key(aid) references farmer(aid) on delete cascade,
	foreign key(service_mode, pincode) references service(service_mode, pincode)
);

