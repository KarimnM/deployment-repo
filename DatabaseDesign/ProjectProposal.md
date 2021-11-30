Database Project Proposals

Database Theory 508

Dhruv Sapra, Karim Mahmoud, Muhlisa Ortikova, Tony Rozzi

STUDY GROUP

A new startup is looking to develop a service that finds groups for students for studying and networking. This service needs to store information on users, user&#39;s purpose, courses, course sections, and types of meetings. This service will allow users to network with other users and find and set up groups so that they can study a common topic. The application will store locations that users can meet and coordinate schedules of the users. The application will also be able to allow users to select a meeting location that must necessarily contain specific studying tools (like whiteboards, projectors, printers, etc).

Developers will need to store information about its users such as names, D.O.B.s, usernames, and passwords. Passwords will be stored as a salted hash.

The entity set for the database comprises:

- Student
- Study Group
- Meeting
- Online Meeting
- In-person Meeting
- Location (includes attributes like &quot;study\_amenities&quot; such as whiteboards, printers, and projectors)
- Course
- Section
- Assignment

Some queries that could be asked of the database include:

1. What is the intersection of the negation of the class schedules of the students in a study group (so that it will report all possible times people could all meet together)?
2. What location would minimize the mean squared walking distance for the members in a study group from their most recent class&#39;s location?
3. What are all meeting locations that have a specified amenity (ex: list all meeting locations that have a projector)?
4. Who are the N users with the largest number of the same courses to a specific person?
5. Who are the N users with the largest number of the same sections to a specific person?
6. Who is the closest person to me who is working on the same assignment as me and is also looking for a partner (distance-wise)?
7. What is the contact information for the members of a study group?
8. What method of communication does a study group prefer (Discord, email, Slack)?
9. Does a study group tend to meet more in-person or online?
10. When will my next meeting be 10 minutes away (to send a reminder)?
11. Create a study group from a given set of students.
12. Who are all the students that want to work on a particular assignment?
13. Searching study-groups for a specific subject or class.
14. What is the largest study group size in the database?
15. What are the usernames of the members of a specific group?
16. What is the due date of an assignment that a specific group is working on?
17. Does a given person have a time-conflict between any of their study groups meetings?
18. What is the most common course to collaborate on?
19. How many study groups is a given student a part of?
20. What is the date of birth for a specific user to make sure he/she is eligible to use the service?
