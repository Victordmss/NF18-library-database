# NF18-library-database (UTC Project)
## NF18 group project consisting of the modeling and implementation of a library database.

### Système de gestion d'une bibliothèque

You are in charge of designing a management system for a municipal **library** that wishes to computerize its activities: cataloguing, consultations, user management, loans, etc.

The library offers access to a wide range of resources of different types (books :books: , films :movie_camera:, and music recordings :sound:). 
A **resource**, whatever its type, has a unique code, a title, a list of contributors, a date of appearance, a publisher, a genre and a classification code that allows it to be located in the library. 
<br> 
A **contributor** :bust_in_silhouette: is characterized by last name, first name, date of birth and nationality. In the case of a book, the contributors are the authors of the document. In the case of a musical work, we distinguish between composers and performers. In the same way, we will distinguish directors and actors for films. We also want to keep specific information depending on the type of document, for example: the ISBN of a book and its summary, the language of written documents and films, the length of a film or a musical work, the synopsis of a film, etc. Finally, the resources in the library may be available in multiple copies, each in a different condition: new, good, damaged or lost.

Each **member** of the library staff has a user account (login and password) that allows him/her to access the system administration functions. Each member is characterized by his or her last name, first name, address and e-mail address.

Members :busts_in_silhouette: of the library also have a **user account** (login and password) as well as a member card that allows them to borrow documents. A **member** is characterized by his name, first name, date of birth, address, e-mail address and telephone number. The library wishes to keep track of all memberships, current and past.

In order to borrow a **document**, a member needs to be authenticated. Each loan is characterized by a loan date and a loan duration. A document can only be borrowed if it is available and in good condition. A member can only borrow a limited number of works at the same time, each for a limited period of time. A member will be penalized for late return of a work, as well as if he/she damages the condition of the work. Any delay in the return of borrowed documents will result in the suspension of lending rights for a period equal to the number of days of delay. In the event of loss or serious deterioration of a document, the suspension of lending rights is maintained until the member pays for the document. Finally, the library may choose to blacklist a member in case of repeated sanctions.

### Besoins :clipboard:
  -> To make it easier for members to find documents and manage their loans. <br>
  -> Facilitate the management of document resources: add documents, modify their description, add copies of a document, etc.<br>
  -> Make it easier for staff to manage loans, delays and reservations.<br>
  -> Facilitate the management of users and their data.<br>
  -> Establish statistics on the documents borrowed by the members, this will allow for example to establish the list of popular documents, but also to study the profile of the members to be able to suggest documents to them.<br>
