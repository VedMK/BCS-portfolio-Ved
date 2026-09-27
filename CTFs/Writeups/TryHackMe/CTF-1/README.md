# Missing Person

**Platform:** TryHackMe  
**Category:** OSINT   
**Difficulty:** Easy  
**Date Solved:** 27-09-2026  
**Tools used:** Exiftool, Google, Google Maps

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

<p align="center">
  <img src="MP-1.jpeg" width="600" height="700">
</p>


<p align="center">
  <img src="MP-2.jpeg" width="600" height="700">
</p>


---

## Initial Analysis-1

I first opened the MotoGP image file, because it corresponded with the first flags.

---

## Investigation

### Flags 1 and 2


The file name "MotoGP" was a takeaway on what I would be looking for, MotoGP stands for "Motorcycle Grand Prix". Using Google, I searched for "PERTAMINA MotoGP", "PERTAMINA" comes from the text in the given image. The search had a vast range of results that I would have to filter through.

My next thought was to use Exiftool to see if the image metadata contained the image creation date, which would give me the timeline I would be looking for, and it did.

<p align="center">
  <img src="MOTOGP-1.jpeg" width="600" height="700">
</p>

```text
2025:10:05
```
The timeline I should be looking for was revealed.

Next I searched for "MotoGP circuit 2025". This gave me a site that tracked the schedules for the 2025 races.

<p align="center">
  <img src="MOTOGP-2.jpeg" width="600" height="700">
</p>

I opened the site and knew what timeline I was looking for, so I scrolled down to October. The races took place in Indonesia in October, so I clicked on the dropdown which gave me the event type, date and time of the events that took place.

<p align="center">
  <img src="MOTOGP-3.jpeg" width="600" height="700">
</p>

From the schedule there were two events, the warm up and the race itself, giving two possibilities to identify the circuit that was in the image. But the assumptions were easily cleared by looking at the time. The image was taken at around `12:33:12` *(see Exiftool metadata above)*, and the scheduled time for the race event was at 10. This meant the image was most likely taken during the main race itself.

Now that I identified the location, date and event: it would be easy to make a simple google search "INDONESIAN GP 2025 OCTOBER 5 RACE" and get the required flag.

<p align="center">
  <img src="MOTOGP-4.jpeg" width="600" height="700">
</p>

In the site description of the event wiki, the details of the circuit at which the event took place was mentioned. I opened the website to confirm the find.

<p align="center">
  <img src="MOTOGP-5.jpeg" width="600" height="700">
</p>

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
