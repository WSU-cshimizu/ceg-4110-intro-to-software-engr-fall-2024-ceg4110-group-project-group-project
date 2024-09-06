﻿**Project Overview Proposal: Online Voting** 

**System for Student Elections**

**Name of the Proposed Project:**

**Vote Online** – A Secure Online Voting System for Student Elections 

**Elevator Pitch:**

**Why are you building your thing?**

We are building **Vote Online** to address the inefficiencies of traditional student elections, such as low voter turnout, long administrative processes, and security issues in manual voting. By moving the process online, we aim to increase student participation, improve transparency and security, and make the election process more accessible for both voters and election administrators. 

**N "Things of Complexity" (Components):**

As we are a group of 5 students, there will be **5 main components**: 

1. **Voter Authentication & Security (2FA)** 
   1. **Complexity:** Implementing secure authentication (e.g., SSO with the university’s credentials and Two-Factor Authentication) to ensure only eligible students can access the system. 
   1. **Description:** This module will handle the login process, user authentication, and checking if a student is eligible to vote. 
   1. **Assigned to:** Sachin Patel (Full Stack Developer) 
1. **Candidate and Election Management (Admin Dashboard)** 
- **Complexity:**  Creating  a  dashboard  for  the  election  administrators  to  set  up elections, manage voter lists, candidates, and configure voting periods. 
- **Description:** Admins can create elections, upload candidates, and monitor voting. This involves backend integration with a database for managing elections and candidate profiles. 
- **Assigned to:** Divyesh Ambaliya (Back-End Developer) 
3. **Ballot Design and Voting Process (Client-Side Voting Interface)** 
   1. **Complexity:**  Designing  a  user-friendly  interface  where  students  can  view candidate details, select their choices, and confirm their vote. 
   1. **Description:** The voting page will allow users to select candidates, confirm their votes, and cast them securely while maintaining anonymity. 
   1. **Assigned to:** Dhruv Patel & Michael Donahue (Front-End Developer) 
3. **API Handling (Backend Integration)** 
- **Complexity**: Implementing effective and safe APIs to support internal program functionality as well as external system integration, guaranteeing seamless data transfer and communication between client and server. 
- **Description:** This component entails creating and implementing API endpoints for the project that handles a variety of tasks, including obtaining election-related data, casting ballots, and verifying voter eligibility. It also entails safely communicating with other systems, like databases that hold student information and suppliers of authentication.  It  is  crucial  to  make  sure  the  APIs  are  safe,  streamlined,  and preserve data integrity. 
- **Assigned to:** Prashant Rai (Django Developer) 
5. **Database Management** 
- **Complexity:**  Designing  and  managing  the  database  to  securely  store  user information, election details, candidate profiles, and votes. 
- **Description:**  Ensuring that  the database can handle large volumes of data,  is optimized for performance, and guarantees data integrity and security. 
- **Assigned to:** Divyesh Ambaliya (Database Manager) 

**How the Components Fit Together (Predicted Architecture):**

- **Front-End (Client Side)** 
  - Voter authentication, candidate viewing, ballot design, and voting submission. 
  - Framework: React.js for building an interactive, responsive interface. 
- **Back-End (Admin Side & Vote Management)** 
  - Admin dashboard for creating elections, managing candidates, and monitoring votes. 
  - Secure vote counting, real-time results, and voter eligibility verification. 
  - Framework: Django or Node.js for managing user data, security, and interactions with the database. 
- **Database Layer** 
  - Store voter information, election data, candidates, and votes. 
  - Database: PostgreSQL or MySQL for relational data management. 

**Predicted Architecture:** 

6. **Voter Login (SSO/2FA)**: Authenticates users and retrieves eligibility information. 
6. **Client Voting Interface**: Displays candidates, collects and submits votes. 
6. **Backend Voting Logic**: Validates votes, encrypts them, and records in the database. 
6. **Admin Dashboard**: Manages elections and tracks results.** 
6. **API Handling**: Develops and manages API endpoints within the project for validating voter eligibility, submitting votes, and retrieving data. It also integrates with external systems to ensure secure and efficient data transfer.** 

We think we will implement: 

- **Authentication via OAuth2** or the university’s Single Sign-On system to ensure secure login. 
- **Data encryption** on both the database and during data transfer using SSL/TLS protocols. 
- **Scalable cloud hosting**, potentially using services like AWS or Heroku, to ensure the platform can handle high traffic during peak voting hours. 

**Technology Stack/Frameworks:**

- **Frontend:** 
  - **React.js**: For building a responsive, modern voting interface with fast rendering. 
- **Backend:** 
  - **Django** (Python) or **Node.js** (JavaScript): Both are secure, scalable frameworks suitable for handling database interactions and backend logic. 
- **Database:** 
  - **PostgreSQL** or **MySQL**: Relational database systems that can handle structured election data (voter information, votes, candidate profiles). 
- **Authentication & Security:** 
  - **OAuth2.0**  or  **JWT**  (JSON  Web  Tokens)  for  managing  user  sessions  and authentication. 
  - **SSL/TLS** for secure data transfer. 

**Why are we picking this tech stack?**

- **React.js** is chosen for its flexibility in creating fast, dynamic front-end applications, and its vast ecosystem of libraries and tools. 
- **Django** or **Node.js** provides robust backend capabilities, with Django offering strong security features out of the box, and Node.js being lightweight and asynchronous. 
- **PostgreSQL/MySQL**  are  industry-standard  databases  for  handling  relational  data, offering powerful querying capabilities and compatibility with most backends. 

We chose this stack for its balance of security, performance, scalability, and ease of integration with modern cloud services like AWS or Heroku. 

**Predicted Life Cycle/Methodology:**

We plan to follow the **Agile Methodology**, breaking down our project into **weekly sprints** to deliver incremental progress. Key phases include: 

11. **Requirements Gathering & Planning** (Week 1-2) 
    1. Define user stories, system requirements, and scope. 
11. **Design Phase** (Week 3-4) 
    1. Design the system architecture, database schema, and wireframes for UI. 
11. **Development Phase** (Week 5-10) 
    1. Start frontend and backend development in parallel. 
    1. Implement authentication, admin dashboard, voting process, and database. 
11. **Testing & Refinement** (Week 11-12) 
- Perform unit testing, security audits, and usability testing. 
- Collect feedback from mock users. 
15. **Deployment & Maintenance** (Week 13-14) 
- Deploy the system on cloud servers and perform final checks. 
- Continuous monitoring and bug fixes as required. 
