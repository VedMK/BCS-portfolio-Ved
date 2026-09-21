<p align="center">
<img src="https://typingsvg.vercel.app/api/svg?lines=%5B%7B%22text%22%3A%22Directory%20Fuzzer%22%2C%22color%22%3A%22%23FFD700%22%2C%22typingSpeed%22%3A0.055%2C%22deleteSpeed%22%3A0.08%7D%5D&font=JetBrains%20Mono&backgroundColor=%23000000&width=900&height=200&pause=3500&repeat=true&center=true&vCenter=true&border=false&cursorStyle=straight&fontWeight=600&backgroundOpacity=1">
</p>

A Python based web directory and file fuzzer that I built to learn about web content discovery, HTTP requests and pen testing.

# Purpose

I made this project to allow users who discover this repository to understand how a directory fuzzer works, and to use it as a means for learning.

The personal goal for this project was to understand how directory and file discovery works by creating a simple implementation myself rather than relying on existing tools.

# What I'm Learning

Through this project, I'm exploring:

- HTTP requests and responses
- HTTP status codes
- Wordlists
- Automated content discovery
- Python scripting
- Basic penetration testing methodology

# How It Works

The fuzzer asks the user for a domain name/ip address.

A wordlist containing potentially discoverable directories and files.

It then constructs URLs from the wordlist and sends HTTP requests to the target.

Responses are displayed based on their HTTP status code.

Example->
Target: http://127.0.0.1:8000

Output:
- URL: http://127.0.0.1:8000/login, Status Code: 200, Body Length: 565
- URL: http://127.0.0.1:8000/admin, Status Code: 403, Body Length: 234


# Computer tech used

- Python
- HTTP/HTTPS
- Web Security
- Git & GitHub

Current Status->

Early development

The current version is intentionally simple.

# Ethical Use

This tool is intended for authorized security testing only.

I will use it against systems I own, intentionally vulnerable applications, CTFs, and other environments where I have permission to perform security testing.
