# DOM XSS - DOM XSS in `document.write` sink using source `location.search`

**Platform:** PortSwigger Web Security Academy  
**Topic:** DOM-based Cross-Site Scripting (DOM XSS)  
**Difficulty:** Apprentice

## Lab Description

This lab contains a DOM-based Cross-Site Scripting vulnerability in the search query tracking functionality.

The application uses the JavaScript `document.write()` function to write data into the page. The data passed to `document.write()` comes from `location.search`, which can be controlled through the website URL.

The objective of the lab is to perform a Cross-Site Scripting attack that calls the `alert()` function.

---

## Reconnaissance

After reading the lab description, my first thought was to input a search value in the search bar of the application.

I then began exploring the application's code using Burp Suite to understand how the search input was being processed.

### Interesting Input

Upon exploring the application's code, I discovered the JavaScript function responsible for writing the search value into the page.

![Input](./input.png)

### Source

The relevant JavaScript code was:

```javascript
function trackSearch(query) {
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
}

var query = (new URLSearchParams(window.location.search)).get('search');

if(query) {
    trackSearch(query);
}
```

The search parameter is obtained from the URL using `URLSearchParams`:

```javascript
var query = (new URLSearchParams(window.location.search)).get('search');
```

This means that the value of the `search` parameter can be controlled through the URL.

---

## Identifying the Vulnerability

The data flows through the application as follows:

```text
URL search parameter-> URLSearchParams-> query-> trackSearch(query)-> document.write()
```

So, the user-controlled value eventually reaches `document.write()`:

```javascript
document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
```

`document.write()` writes the input right into HTML.

Because the value of `query` is inserted into the HTML without the input being sanitized in any way, it leaves the application vulnerable to DOM based XSS that attackers may exploit.

---

## Exploitation

I then attempted to change the `search` param to see if it injects HTML into the page and it did, so I moved onto working with the given task.

### Payload

```text
"><svg onload=alert(1)>
```

The payload was placed into the `search` parameter of the URL.

![payload](payload.png)

The injected input was interpreted as HTML by the browser, allowing JavaScript to be executed.

---

## Result

The payload successfully triggered the `alert()` function, confirming the vulnerability.

![Labsolved](solved.png)

---

## What I Learned

- How `location.search` can act as a source of user-controlled data.
- How to trace user input through JavaScript.
- How `document.write()` can become a dangerous sink when used with untrusted input.
- How to identify the source and sink of a DOM XSS vulnerability.
- How Burp Suite can be used to inspect application behavior and JavaScript.

## Key learnings from the lab
 
The main learning of the lab was the flow of data from the URL into `document.write()`:
