# Missing Person

**Platform:** TryHackMe  
**Category:** OSINT   
**Difficulty:** Easy  
**Date Solved:** 27-09-2026  
**Tools used:** Exiftool,

---

## Challenge Objective

What is the commercial name of this circuit?
Format: English, full commercial name.

When did the event take place?
Format: DD-DD/MM/YYYY.

He told me he ate delicious Mexican food. What is the name of the restaurant?

At what time was this photo taken?
Format: HH:MM:SS.

```text
He sent me a message, this is the last I heard from him: ”Went to this cool MotoGP after party, and became friends with one of the local DJs who played that night. We’re going to visit a cave tomorrow.”
```
What is the full address of the bar’s location?

What is the DJ's stage name?

After digging into the DJ's other online accounts, what cave does he take tourists to?

What number did the DJ list for his tour business?
Format: Full number, no country code.

---

## Information Provided

"My friend went on holiday in 2025 and shared some photos, but I haven’t heard from him since. Can you help me track him down for the police report?"

Download the zip file attached to this task and start your investigation!

```text
Contents of zip file were 2 images
```



---

## Initial Analysis

I looked for unique identifiers such as visible text, shop or restaurant names, street signs, architectural features, and other distinctive structures that could help narrow down the location.

---

## Investigation

### Finding Clues


Upon searching for clues, I came across a piece of text on a building that was just barely visible.

<p align="center">
  <img src="MM-find.png" width="700" height="700">
</p>

```text
JULIEN
```

The challenge also explicitly mentioned the location was in Paris.

---

### Searching for the location

After identifying the clues, I searched for the text I saw on the building along with "Paris" to narrow the search in Google Maps.

<p align="center">
  <img src="MM-loc3.jpeg" width="600" height="700">
</p>

Then I zoomed into each search location to find an intersection point of an Avenue and a Rue, as specified by the challenge. 

One location 
```text
Maison julien
```
stood out, with an intersection of an Avenue and a Rue.

<p align="center">
  <img src="MM-loc2.jpeg" width="500" height="700">
</p>

Next I switched to satellite view to find any visible comparison of the top view and the given image. The tree and zebra-crossing in Google Maps seemed to match the tree and zebra-crossing I could see in the image. I was convinced that I must've found the location due to clues matching the information.

---

### Verification

After I suspected the location, I investigated it using Google Street View. The building on street view was evidently the same, and I spotted the same piece of text I saw as an initial clue. I also noticed the same structural identifiers I had noted from the image provided by the challenge.

<p align="center">
  <img src="MM-1.png" width="700" height="700">
</p>

---

### Capturing the flag

Once I verified and confirmed the location in the challenge image, I zoomed out near the location on Google Maps and spotted a metro station right across the street.

<p align="center">
  <img src="MM-2.png" width="700" height="700">
</p>

The challenge was solved and using the format given by the CTF platform, the final flag I captured was

```text
OSINT{SAINT_PHILIPPE_DU_ROULE}
```
