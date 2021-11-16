DROP DATABASE vizphiz;
CREATE DATABASE vizphiz;
USE vizphiz;

CREATE TABLE lamdamax
(
id int unsigned primary key,
genus  varchar(50),
species varchar(50),
celltype varchar(50),
lamdamax decimal(4,5),
method varchar(50),
stage varchar(50),
refid int,
notes varchar(1000)
);

CREATE TABLE references
(
refid int unsigned primary key,
doi varchar(100),
searchid int
);

CREATE TABLE search
(
searchid int unsigned primary key,
researcher varchar(50),
month int,
year int,
engine varchar(500),
keywords varchar(500)
);


CREATE TABLE opsins
(
opsinid int unsigned not null primary key,
species genefamily(50),
genus varchar(50),
species varchar(50),
database varchar(50),
accession  varchar(50),
dna varchar(10000),
aa varchar(3333),
refid int
);
