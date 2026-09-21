
# SSRF - SSRF with blacklist-based input filter

**Platform:** PortSwigger Web Security Academy  
**Topic:** Server-Side Request Forgery 
**Difficulty:** Practitioner

## Lab Description

This lab has a stock check feature which fetches data from an internal system.

To solve the lab, change the stock check URL to access the admin interface at `http://localhost/admin` and delete the user carlos.

The developer has deployed two weak anti-SSRF defenses that you will need to bypass.

---

## Reconnaissance

The lab description mentioned the vulnerability is in the stock check functionality. So I began exploring the site to find the given feature, which was present for all products when you click "View details" under the product.

![Input field](Lab2-0.png)

Next, I used Burp suite to examine the HTTP requests when I click "check stock".

### Discoveries

Upon examining the HTTP requests for the "check stock" button, it was evident that the request method was POST. Interestingly I also found that the application communicates to the back-end with the API, with it being input via a variable called "stockApi" to fetch the stock units when the post request is sent.

![HTTP](Lab2-1.png)

### Source

The relevant part of the request was:

```HTTP

stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1

```

The stock units are then fetched by a back-end request the server makes after the HTTP request is sent.

This means that the value of the `stockApi` variable can be changed using Burp, or a custom payload can be sent via curl.

---

## Identifying the Vulnerability

The data flows through the application as follows:

```text
Check stock-> stockApi-> server-> Backend-> server-> Browser
```

So, the user-controlled value eventually reaches the backend with:

```HTTP
stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1
```

The backend returns the response to the server and then the server displays it to the user.

Because the value of stockApi is essentially user-controlled input, an attacker can modify the 'stockApi' variable to make the server send requests to internal resources that the attacker wouldn't normally be able to access from his/her browser.

---

## Exploitation

I then attempted to change the 'stockApi' by copy-pasting the request into Burp repeater. First I attempted the most basic payload:

```text
https://localhost/admin
```

which returned

![return](Lab2-2.png)

This confirms that the payload did reach the server, but the anti-SSRF defense detected malicious input and blocked it.

The same response occurred when I changed the path to

```text
users
alice
robots.txt
```

This suggests that the anti-SSRF defense was working based upon the hostname. To bypass this, I entered 127.0.0.1 instead, but the same response was returned.

So, I once again changed the hostname to 127.1, which also represents the loopback address, but may avoid the anti-SSRF defense. This time,

```text
https://127.1/robots.txt
```
gave me a status code 200 response with lab content, but

```text
https://127.1/admin
```

gave me the same response as before.

It was now evident that the path was also being checked before performing the request. So, I encoded the "a" of the admin in URL encoding, i.e "%2561". This time, it returned the admin panel.

![admin](Lab2-3.png)

Clicking the "delete" button didn't work, so I examined the response content where I found the required path to delete the user "carlos".

```text
/admin/delete?username=carlos
```

This time, I pasted the path right into the request in Burp repeater, and encoded the "a" of "admin" again.

### Payload

```text
stockApi=http://127.1/%2561dmin/delete?username=carlos
```

The payload was placed into the `stockApi` variable.

![payload](Lab2-payload.png)

The request was interpreted by the server as a valid request and the because the server was able to access the internal admin interface, it deleted carlos's account.

---

## Result

The payload successfully deleted carlos's account, confirming the vulnerability.

![Labsolved](Lab2-solved.png)

---

## What I Learned

- How SSRF can occur when a server makes requests using user controlled input.
- How to track user input through the application to identify an SSRF vulnerability.
- How Burp suite repeater can be used to inspect and modify HTTP requests.
- How blacklist based SSRF defenses can sometimes be bypassed using alternative representations.
- How double URL encoding can be used to bypass filters that block specific paths.

## Key learnings from the lab

The main learning of the lab was understanding how user controlled input can cause the server to make requests to internal resources.

The `stockApi` parameter was controlled by the user, but the server trusted this value and used it to make the stock check request. This allowed the request to be redirected to the internal admin interface.

I also learned how blacklist based SSRF defenses can be weak. The filter blocked values such as `localhost` and `127.0.0.1`, but `127.1` was another representation of the loopback address but was not in the blacklist.

The second filter blocked the `/admin` path. By double URL encoding the "a" in `admin` as `%2561`, I bypassed the anti-SSRF filter.

Overall, this lab helped me understand the basic SSRF request flow and how weak input filtering can sometimes be bypassed.
