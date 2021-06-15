# Nodejs

> JavaScript 실행하기 위한 플랫폼

<br/>

## 실행

- `cmd` 실행
- 경로 이동
- `main.js` 실행

```shell
node main.js
```

<br/>

<br/>

<br/>

## Read File

> **fs.readFile**( **파일명** , **encoding** , **콜백함수(err, data)** {
>
> &nbsp;&nbsp;&nbsp;&nbsp;...
>
> });

```javascript
var fs = require("fs");

fs.readFile("sample.txt", "utf8", function(err, data){
	console.log(data);
});
```

<br/>

<br/>

## Read Directory

> **fs.reaaddir**( **경로** , **콜백함수(err, filelist)** {
>
> &nbsp;&nbsp;&nbsp;&nbsp;...
>
> });

```javascript
var testFolder = "./data";
var fs = require("fs");

fs.readdir(testFolder, function(err, filelist){
	console.log(filelist);
});
```

<br/>

<br/>

## Write File

>**fs.writeFile**( **경로** , **내용** , **encoding** , **콜백함수(err)**{
>
>&nbsp;&nbsp;&nbsp;&nbsp;...
>
>});

```javascript
fs.writeFile('data/nodejs', 'nodejs is ...', 'utf8', function(err){
	console.log('nodejs file Written.');
});
```

<br/>

<br/>

## File Rename

> **fs.rename**( **이전 파일명** , **새로운 파일명** , **콜백함수(err)**{
>
> &nbsp;&nbsp;&nbsp;&nbsp;...
>
> });

```javascript
var id = post.id;
var title = post.title;

fs.rename(`data/${id}`, `data/${title}`, function(err){
    // update description
});
```

<br/>

<br/>

## 보안 이슈1. 오염된 정보 유입 - path.parse

> 상위 디렉토리의 접근을 막을 때 주로 사용

- `path.parse`

```javascript
var path = require('path');
console.log(path.parse('/../password.js'));

/* 결과
{
  root: '/',
  dir: '/..',
  base: 'password.js',
  ext: '.js',
  name: 'password'
} */
```

- `query`문으로 입력받은 `path`를 `parse`

```javascript
var url = require('url');
var path = require('path');

var queryData = url.parse(_url, true).query; // '?id=../password.js' 입력 시
var filteredId = path.parse(queryData.id).base;

// queryData.id == '../password.js'
// filterdId == 'password.js'
```

<br/>

<br/>

## 보안 이슈2. 오염된 정보 유출 - sanitize-html

- 사용자가 다음 내용의 파일을 저장하였을 때, 파일을 내보내면 `<script>`가 실행이 됨.
  - `some title...`

```html
content...
<script>
    location.href = 'http://google.com/';
</script>
content...
```

- 태그 비활성화
  - `html entities` - https://www.w3schools.com/html/html_entities.asp

```html
content...
&lt;script&gt;
    location.href = 'http://google.com/';
&lt;/script&gt;
content...
```

<br/>

### `sanitize html`

- https://www.npmjs.com/package/sanitize-html
- 설치
  - `-S` : 현재 프로젝트에서만 부품으로서 사용

```shell
npm init
npm install -S sanitize-html
```

- 사용

```javascript
var sanitizeHTML = require('sanitize-html');

var title = queryData.id;
var sanitizedTitle = sanitizeHtml(title);
var sanitizedDescription = sanitizeHtml(description, {
  allowedTags:['h1']
});
```

<br/>

<br/>

---

---

<br/>

<br/>

## Syncronous & Asynchronous

- syncronous(동기)
  - 프로그램이 순차적으로 실행
  - 출력 순서 : A -> B -> C

```javascript
console.log('A');
var result = fs.readFileSync('syntax/sample.txt', 'utf8');
console.log(result);
console.log('C');
```

<br/>

- asyncronous(비동기)
  - 프로그램이 병렬적으로 실행
  - 출력 순서 : A -> C -> B
  - `callback` 함수로 동기화

```javascript
console.log('A');
fs.readFile('syntax/sample.txt', 'utf8', function(err, result){
    console.log(result);
});
console.log('C');
```

<br/>

<br/>

## Call Back

- 함수를 파라미터로 사용하여 호출
  - 실행 결과 : A
- `slowfunc()` 함수 종료 후 `callback()` 함수 호출 (동기화)

```javascript
var a = function(){
    console.log('A');
}

function slowfunc(callback){
    callback();
}

slowfunc(a);
```

<br/>

<br/>

---

---

<br/>

<br/>

## Form

- 서버에 데이터를 보낼 때 사용
- `method = "post"` : 데이터를 url로 보내지 않고 숨겨서 보냄

```html
<form action = "http://localhost:3000/create_process" method = 'post'>
    <p>
        <input type="text" name = 'title'>
    </p>
    <p>
        <textarea name="description"></textarea>
    </p>
    <p>
        <input type="submit">
    </p>
</form>
```

<br/>

<br/>

## POST 방식으로 전송된 데이터 받기

- `querystring` 라이브러리 불러오기
  - `require("querystring")`

```javascript
var qs = require('querystring');

// formaction = "http://localhost:3000/create_process" 인 경우
if (pathname === '/create_process'){
    var body = '';
    
    // 요청한 데이터를 받는 함수
    request.on('data', function(data){
        body += data;
    });
    
    // 요청이 끝난 후 실행되는 함수 (주로 query문 parse)
    request.on('end', function(){
        var post = qs.parse(body);
        var title = post.title;
        var description = post.description;
        
        console.log(post, title, description);
        
        response.writeHead(200);
        response.end('success');
    });
}
```

<br/>

<br/>

- 전송된 데이터를 `write` & `rediect`

```javascript
var title = post.title;
var description = post.description;

// request 받은 title과 description으로 파일 저장
fs.writeFile(`data/${title}`, description, 'utf8', function(err){
    // 302 : redirection & 경로 설정
    response.writeHead(302, {Location : `/?id=${title}`});
    response.end();
})
```

<br/>

<br/>

<br/>

<br/>

---

---

<br/>

<br/>

## 객체(Object)

- 객체 안의 함수
  - `this.<key>` : 현재 속해있는 객체의 key값에 접근

```javascript
var p = {
    v1 : 'v1',
    v2 : 'v2',
    f1 : function(){
        console.log(this.v1); // this.v1 == 'v1'
    } ,
    f2 : function(){
        console.log(this.v2); // this.v2 == 'v2'
    }
}

p.f1();
p.f2();
```

<br/>

<br/>

## Module화

> template을 파일로 저장하여 module로서 이용할 수 있다.

- `lib/template.js`

```javascript
module.exports = {
    HTML : function(title, list, body, control){
        return `// HTML`;
    },
    
    list : function(filelist){
        return `// list`;
    }
}
// module.exports = template;
```

<br/>

- `main.js`

```javascript
var template = require('./lib/template.js');

var list = template.list(filelist);
var html = template.HTML(title, list, body, control);
```

<br/>

<br/>

---

---

<br/>

<br/>

## NPM & PM2

> `NPM`(패키지 매니저) : 패키지 설치 및 업데이트 등을 관리해 주는 프로그램
>
> `PM2`(프로세스 매니저) : 실행중인 Node.js 애플리케이션을 관리해 주는 프로그램

<br/>

- `pm2`
  - `Node.js` 파일을 수정해도 재실행시키지 않고 자동으로 반영을 함.
  - `Node.js` 파일을 강제로 종료해도 자동으로 재실행을 함.
  - https://pm2.keymetrics.io/

<br/>

<br/>

- `pm2` 설치
  - `-g` : 독립된 소프트웨어로서 설치된 컴퓨터 어디서든 사용 가능

```shell
npm install pm2 -g
또는
sudo npm install pm2 -g
```

<br/>

<br/>

- `main.js` 프로그램 실행
  - `--watch` : 파일 수정시 자동으로 재실행
  - `--no-daemon` : daemon(백그라운드)에서 실행 방지(`log`가 실행됨)
  - `--ignore-watch="data/* sessions/*"` : 데이터 변경 시 `main.js`가 재실행되는 것을 방지
    - `data/*` `sessions/*` 두 폴더에 적용

```shell
pm2 start main.js
```

```shell
pm2 start main.js --watch
```

```shell
pm2 start main.js --watch --no-daemon
```

```shell
pm2 start main.js --ignore-watch="data/* sessions/*" --no-daemon
```

<br/>

<br/>

- `pm2`에 의해 실행되고 있는 프로그램 조회

```shell
pm2 list
```

```shell
pm2 monit
q
```

<br/>

<br/>

- `main.js` 프로그램 종료
  - `stop` : 프로그램 하나만 종료
  - `kill` : 생성한 프로세스 전체 종료

```shell
pm2 stop main.js
```

```shell
pm2 kill
```

<br/>

<br/>

- `log` 실행
  - 에러나 파일 수정 시 화면에 보여줌.

```shell
pm2 log
```

<br/>

<br/>

---

---

<br/>

<br/>

## MySQL

- 설치
  - https://www.npmjs.com/package/mysql
  - `--save` : `package.json` 파일에 `dependencies` 에 `mysql` 추가

```shell
npm install --save mysql
```

<br/>

- 연결

```javascript
var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'me',
  password : 'secret',
  database : 'my_db'
});
 
connection.connect();
 
connection.query('SELECT * FROM topic', function (error, results, fields) {
  if (error) throw error;
  console.log(results);
});
 
connection.end();
```







