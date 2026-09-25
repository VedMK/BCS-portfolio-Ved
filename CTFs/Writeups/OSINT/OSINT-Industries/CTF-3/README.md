# HOLEHE & THE SECRET EMAIL

**Platform:** OSINT Industries  
**Category:** OSINT
**Difficulty:** Easy-Medium  
**Date Solved:** 25-09-2026
**Tools used:** Google, CURL(CLi), GPG(CLi)

---

## Challenge Objective

Using open-source intelligence only, find:

- The creator of Holehe
- The public email address used for Holehe
- The exact creation date of this email address

The final flag must be based only on this date.

---

## Information Provided

You are investigating the origins of a popular OSINT tool used to pivot from email addresses to online accounts: Holehe.

Behind every tool, there is a creator — and behind that creator, there is an email address.

---

## Initial Analysis

The first thing I did was search up "Holehe" on google. This gave me the top sites for the search results.

---

## Investigation

### Finding the creator

The topmost search results were a Holehe website for OSINT, and a github repository for Holehe. 





---

### Searching for the location

My best shot was to perform a reverse image search using google lens.

<p align="center">
  <img src="Uni1.jpeg" width="600" height="700">
</p>

The results gave me 
```text
Bond University
```
and
```text
Gold Coast
```

---

### Verification

After the search results, I went to google maps in satellite mode to verify the structures and pattern.

The pattern can be compared from the image and the google map result. They seem similar.

<p align="center">
  <img src="Uni3.png" width="600" height="700">
</p>  

Next I went to street view to have a better view at the infrastructure.

<p align="center">
  <img src="Uni2.png" width="600" height="700">
</p>  

The same straight path, tents to the left, pattern on the floor and the library on the left can be easily compared. This verified the location.

---

### Capturing the flag

Once I verified and confirmed the location in the challenge image, I zoomed out in Google Maps and found the city in which the university was located:

```text
Robina
```

The challenged was solved and using the format given by the CTF platform, the final flag I captured was

```text
OSINT{"bond_university_robina"}
```


Is this format ok for the OSINT challenge in OSINT Industries? Or it needs to be diff from GEOSINT? IFyes then make a new format
