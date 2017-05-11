slidenumbers: true

# Introduction to HTTP

---

What is the difference between Internet and World Wide Web?

---

Internet is the network of computers.

World Wide Web is an application on top of internet, like many others including email, ftp, telnet, ssh etc.

World Wide Web is the killer app of the internet. It revolutioned the internet.

---

# World Wide Web - Key Concepts

* Uniform Resource Locator (URL)
* Hyper Text Markup Language (HTML)
* Hyper Text Transfer Protocol (HTTP)

---

# Uniform Resource Locatior

Locate any resource with a single string. 

Examples:

	https://rootconf.in/2017/building-restful-apis
	https://www.cleartrip.com/account/trips/17041292873

Revolutionary idea!

---

# Hyper Text

Document with references to other documents, which can be accessed immediately.

	The term hypertext is coined by 
	<a href="https://en.wikipedia.org/wiki/Ted_Nelson">Ted Nelson</a> 
	in 1963.


Very simple idea. Nothing comes closer even after half a century.

Think: how do you manage related word documents? 

---

# Hyper Text Transfer Protocol (HTTP)

HTTP is the protocol to transfer hypertext.

Simple text-based protocol.

---

# HTTP - Sample Request

	GET /hello?name=web HTTP/1.1
	Host: example.com
	User-Agent: Mozilla/5.0
	Accept: */*

---

# HTTP - Sample Response

	HTTP/1.1 200 OK
	Server: gunicorn/19.7.1
	Date: Thu, 11 May 2017 10:46:00 GMT
	Content-Type: text/html; charset=utf-8
	Content-Length: 11

	Hello, web!

---

# HTTP - Important Parts

* HTTP Methods 
	- GET, POST, PUT, DELETE
* Headers
	- Content-Type, Content-length, ...
* Status Codes
	- 200 OK, 404 Not Found

---

# Demo

Demo using `curl` and `netcat`.

---

# Safe and Idempotent Methods

* Safe - no side effects
	* GET and HEAD
* idempotence - the side-effects of more than one identical requests is the same as for a single request. 
	* GET, HEAD, PUT and DELETE

---

