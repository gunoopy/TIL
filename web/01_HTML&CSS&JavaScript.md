# HTML

> **H**yper **T**ext **M**arkup **L**anguage

<br/>

<br/>

## HTML Basic Form

> <tagname attributename = "value">Contents...</tagname>

```html
<h1>My First Heading</h1>
<p>My First paragraph.</p>
<a href = "http://google.com">Link to Google.</a>
```

<br/>

<br/>

## Skeleton

```html
<!DOCTYPE html>
<html>
    <head>
        <title>...</title>
        <meta charset = "utf-8">
        ... head ...
    </head>
    
    <body>
        ... body ...
    </body>
</html>
```

- **`<!DOCTYPE html>`** : declaration defines that **this document is an HTML5 document**, and helps **browsers to display web pages correctly**
- **`<html>`** : element is **the root element of an HTML page**
- **`<head>`** : element **contains meta information** about the HTML page
- **`<title>`** : element specifies a title for the HTML page (which is shown in **the browser's title bar or in the page's tab**)
- **`<body>`** : element defines the document's body, and is **a container for all the visible contents**, such as headings, paragraphs, images, hyperlinks, tables, lists, etc.

<br/>

<br/>

## Heading tags : `<h1>` ~ `<h6>` 

> HTML headings are defined with the `<h1>` to `<h6>` tags.

```html
<h1>This is heading 1</h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>
<h4>This is heading 4</h4>
<h5>This is heading 5</h5>
<h6>This is heading 6</h6>
```

<br/>

<br/>

## Paragraph tag : `<p>`

> HTML paragraphs are defined with the `<p>` tag.

```html
<h1>Title</h1>
<p>Html is...</p>
<p>CSS is...</p>
<p>Javascript is...</p>
```

<br/>

<br/>

## Link tag : `<a>`(anchor)

> The link's destination is specified in the `href` attribute.

```html
<a href = "http://w3schools.com/html">Click to Learn HTML!</a>
```

<br/>

<br/>

## Images tag : `<img>`

> The source file (`src`), alternative text (`alt`), `width`, and `height` are provided as attributes

```html
<img src = "google.jpg" alt = "No Image!" width = "104" height = "142">

<img src = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" width = "10%">
```

<br/>

<br/>

## Line Break tag : `<br>`

```html
<p>HTML is <br>...</p>
```

<br/>

<br/>

## Formatting tags

| Tag        | Description      |
| ---------- | ---------------- |
| `<b>`      | Bold text        |
| `<strong>` | Important text   |
| `<u>`      | Underlined text  |
| `<i>`      | Italic text      |
| `<em>`     | Emphasized text  |
| `<mark>`   | Marked text      |
| `<small>`  | Smaller text     |
| `<del>`    | Deleted text     |
| `<ins>`    | Inserted text    |
| `<sub>`    | Subscript text   |
| `<sup>`    | Superscript text |

```html
<p>
    This text is
    <b>bold</b>
    <strong>strong</strong>
    <u>underline</u>
    <i>italic</i>
    <em>emphasized</em>
    <small>small</small>
    <mark>mark</mark>
    <del>delete</del>
    <ins>insert</ins>
    <sub>subscripted</sub>
    <sup>superscripted</sup>
</p>
```

<br/>

<br/>

## `Style` attribute

> Used to **add styles** to an element, such as color, font, size, and more

```html
<body style = "background-color : powderblue;">
    <h1 style = "color : red;">Heading</h1>
    <p style = "font-size : 20px; background-color : pink; color : green;">contents1...</p>
    <p style = "text-align : center; background-color : yellow;">contents2...</p>
</body>
```

<br/>

<br/>

## List tags : `<ul>`, `<ol>`

> Used with `<li>` (list) tags.

- `<ul>` : Unordered List

```html
<ul>
    <li>item1</li>
    <li>item2</li>
    <li>item3</li>
</ul>
```

<br/>

- `<ol>` : Ordered List

```html
<ol>
    <li>item1</li>
    <li>item2</li>
    <li>item3</li>
</ol>
```

<br/>

- Sublist

```html
<ul>
    <li>item1
        <ol>
            <li>item1-1</li>
            <li>item1-2</li>
            <li>item1-3</li>
        </ol>
    </li>
    <li>item2</li>
    <li>item3</li>
</ul>
```

<br/>

<br/>

## Table tags : `<table>`

> Used with `<tr>` (table row) & `<th>` (table head) & `<td>` (table data)

```html
<table style = "width : 100%;">
    <tr>
        <th>Name</th>
        <th>Score1</th>
        <th>Score2</th>
    </tr>
    <tr>
        <td>John</td>
        <td>100</td>
        <td>90</td>
    </tr>
    <tr>
        <td>Jane</td>
        <td>10</td>
        <td>20</td>
    </tr>
</table>
```

<br/>

- Add style (CSS)

```css
<style>
    table, th, td{
        border : 1px solid black;
        border-collapse : collapse;
    }
        th, td{
        padding : 10px;
    }
</style>
```

<br/>

<br/>

## Block-level tag : `<div>`

> always starts on a **new line**
>
> always takes up the **full width** available

<br/>

```html
<h1>Heading...</h1>
<div style = "border : 1px solid red;">This is div1 element...</div>
<div style = "border : 1px solid red;">This is div2 element...</div>
<p style = "border : 1px solid black;">Contents1...</p>
<p style = "border : 1px solid black;">Contents2...</p>
```

<br/>

<br/>

## Inline tag : `<span>`

> does **not start on a new line**

```html
<p>The span element is an <span style = "border : 1px solid red;">inline element</span>. and will not start on a new line.</p>
```

<br/>

<br/>

## Divide Tag : `<div>`

```html
<style>
    #grid{
      display : grid;
      grid-template-columns : 150px 1fr;
    }
    ul{
      border-right: 1px solid gray;
      margin:0;
      padding :30px;
    }
</style>
    
<div id = "grid">
    <ul>
        <li><a href="python.html" class = "saw">Python</a></li>
        <li><a href="database.html" class = "saw">Database</a></li>
        <li><a href="html.html">HTML</a></li>
    </ul>
    <div id = "article">
        <h1>Home Page</h1>
        <p>About Python, Database and HTML...</p>
    </div>
</div>
```

<br/>

<br/>

## Layout tag

> semantic elements that define the **different parts** of  a web page

<img src = "https://www.w3schools.com/html/img_sem_elements.gif" align = "left">

| Tag         | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `<header>`  | a header for a document or a section                         |
| `<nav>`     | a set of navigation links                                    |
| `<section>` | a section in a document                                      |
| `<article>` | an independent, self-contained content                       |
| `<aside>`   | content aside from the content (like a sidebar)              |
| `<footer>`  | a footer for a document or a section                         |
| `<details>` | additional details that the user can open and close on demand |
| `<summary>` | a heading for the `<details>` element                        |



<br/>

<br/>

---

---

<br/>

<br/>

# CSS

> **C**ascading **S**tyle **S**heets

<br/>

## 3 Ways Using CSS

| Way      | Usage                                                       |
| -------- | ----------------------------------------------------------- |
| Inline   | by using the `style` attribute inside HTML elements         |
| Internal | by using a `<style>` element in the `<head>` section        |
| External | by using a `<link>` element to link to an external CSS file |

<br/>

<br/>

## Inline CSS

> **`style` attribute** of an HTML element

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Inline CSS</title>
  </head>
  <body style = "background-color : powderblue;">
    <h1 style = "color : red;">Heading...</h1>
    <p style = "background-color : pink; text-align : center;">Contents1...</p>
    <p style = "background-color : pink; text-align : center;">Contents2...</p>
  </body>
</html>
```

<br/>

<br/>

## Internal CSS

> **`<style>` element** in the `<head>` section

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Internal CSS</title>
    <style>
      body{
        background-color : powderblue;
      }
      h1{
        color : red;
      }
      p{
        background-color : pink;
        text-align : center;
      }
    </style>
  </head>
  <body>
    <h1>Heading...</h1>
    <p>Contents1...</p>
    <p>Contents2...</p>
  </body>
</html>
```

<br/>

<br/>

## External CSS

> **`<link>` element** to link to an external **CSS file**

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>External CSS</title>
    <link rel="stylesheet" href="style.css">
    <!--link rel="stylesheet" href="https://www.w3schools.com/html/styles.css"-->
  </head>
  <body>
    <h1>Heading...</h1>
    <p>Contents1...</p>
    <p>Contents2...</p>
  </body>
</html>
```

- `style.css`

```css
body{
  background-color : powderblue;
}
h1{
  color : red;
}
p{
  background-color : pink;
  text-align : center;
}
```

<br/>

<br/>

## CSS Colors, Fonts, and Sizes

| Property      | Description    |
| ------------- | -------------- |
| `color`       | the text color |
| `font-family` | the font       |
| `font-size`   | the text size  |

- `style.css`

```css
body{
  background-color : powderblue;
}
h1{
  color : red;
  font-family : consolas;
  font-size : 300%;
}
p{
  color : purple;
  font-size : 20px;
  background-color : pink;
  text-align : center;
}
```

<br/>

<br/>

## CSS Border, Padding and Margin

| Property  | Description                                     |
| --------- | ----------------------------------------------- |
| `border`  | border around an HTML element                   |
| `padding` | padding (space) between the text and the border |
| `margin`  | margin (space) outside the border               |

- `style.css`

```css
p{
    border : 3px solid yellow;
    padding : 15px;
    margin : 50px;
}
```

<br/>

<br/>

## Example Homepage Using CSS

- `index.html`

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>with CSS</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Heading...</h1>
    <p>Contents1...</p>
    <p>Contents2...</p>
  </body>
</html>
```

- `style.css`

```css
body{
  background-color : powderblue;
  font-family : consolas;
  text-align : center;
}
h1{
  border : 3px solid green;
  padding : 10px;
  color : red;
  font-size : 300%;
}
p{
  border : 3px solid yellow;
  padding : 15px;
  margin : 50px;
  color : purple;
  font-size : 20px;
  background-color : pink;
}
```

<br/>

<br/>

---

---

<br/>

<br/>

# Javascript

<br/>

<br/>

<br/>

<br/>

<br/>