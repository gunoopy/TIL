# NOSQL - MONGODB

> 분산 System, 병렬 System

<br/>

<br/>

## 기본 명령어

- `mkdir c:\mongodb\test`
- `mongod -dbpath c:\mongodb\test` : db instance 생성
- `mongo localhost:27017` : db 접속

- `use admin` : admin으로 사용
- `db.version()`
- `db.shutdownServer()`

- `db.logout()`

- `db.stats()` : 상태 확인

```shell
>db.stats()
 {
        "db" : "show",          <-DB명
        "collections" : 0,      <-컬렉션 수
        "views" : 0,            <-뷰어의 수
        "objects" : 0,          <-오브젝트 수
        "avgObjSize" : 0,       <-오브젝트의 평균 크기
        "dataSize" : 0,         <-데이터 크기
        "storageSize" : 0,      <-저장공간의 크기
        "numExtents" : 0,       <- 총 익스턴트 수
        "indexes" : 0,          <- 인덱스 수
        "indexSize" : 0,        <- 인덱스 크기
        "fsUsedSize" : 0,       <- 사용된 파일 크기
        "fsTotalSize" : 0,      <- 총 파일 크기
        "ok" : 1                <- 문장의 실행 상태(정상:1,  실패:0) 
}
```

- `db.hostInfo()` : host 정보 출력

```shell
> db.hostInfo()
{
        "system" : {
                "currentTime" : ISODate("2021-01-22T04:21:19.132Z"),
                "hostname" : "PGW",
                "cpuAddrSize" : 64,
                "memSizeMB" : NumberLong(8087),
                "memLimitMB" : NumberLong(8087),
                "numCores" : 4,
                "cpuArch" : "x86_64",
                "numaEnabled" : false
        },
        "os" : {
                "type" : "Windows",
                "name" : "Microsoft Windows 10",
                "version" : "10.0 (build 19041)"
        },
        "extra" : {
                "pageSize" : NumberLong(4096),
                "physicalCores" : 2
        },
        "ok" : 1
}
```

<br/>

<br/>

## 컬렉션 생성

>  `db.createCollection(컬렉션명)`

- `capped` : 저장 공간의 재사용이 가능한 타입
- `size` : collection의 최초 인스텐트 크기

```sql
use SALES

db.createCollection("employees",{
	capped : true,
	size : 100000
})

show collections
db.employees.stats()

db.emplyees.renameCollection("emp")
db.emp.drop()
```

<br/>

<br/>

## 데이터 삽입

> `db.<컬렉션명>.save({key : value})`

```sql
use test

m = {ename : "smith"}
n = {empno : 1101}

db.things.save(m)
db.things.save(n)
db.things.find()

show collections
```

<br/>

> `db.<컬렉션명>.insert({key : value})`

```sql
db.things.insert({empno : 1102, ename : "king"})

db.thing.insert({empno : 1101, job : "student"})

db.things.find()
```

<br/>

<br/>

## 반복문

```sql
for (var n = 1103 ; n <= 1120 ; n++) db.things.save({n : n, m : "test"})

db.things.find()
```

<br/>

<br/>

## 데이터 수정

> `update({PK : value}, {$set : {key : value}})`

```sql
db.things.update({n:1103}, { $set : {ename : "standford", dept : "research"}})
db.things.update({n:1104}, { $set: {ename : "John", dept : "inventory"}})
db.things.update({n:1105}, { $set: {ename : "Jeo", dept : "accounting"}})
db.things.update({n:1106}, { $set: {ename : "king", dept : "research"}})
db.things.update({n:1107}, { $set: {ename : "adams", dept : "personel"}})
db.things.update({n:1108}, { $set: {ename : "blake", dept : "inventory"}})
db.things.update({n:1109}, { $set: {ename : "smith", dept : "accounting"}})
db.things.update({n:1110}, { $set: {ename : "allen", dept : "research"}})
db.things.update({n:1119}, { $set: {ename : "clief", dept : "human resource"}})
db.things.update({n:1120}, { $set: {ename : "miller", dept : "personel"}})

db.things.save({empno : 1101, ename : "Blake", dept : "account"})
```





## 데이터 제거

> `remove({key : value})`

```sql
db.things.remove({m : "test"})
db.things.find()

db.things.remove({})
db.things.find()

db.things.drop()
```

