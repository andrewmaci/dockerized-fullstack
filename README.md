# Full-Stack Docker app 

This is a training project made while following [Francesco Ciulla](https://www.youtube.com/@francescociulla)'s video. Main objective of this project is an introduction to the dockerization of apps and connecting them between each other.

## Implementation

*'compose.yaml'* allows for creation of 3 main containers:
1. db - serving a PostgreSQL database
2. flaskapp - serving as backend API allowing for data transfer with the database
3. nextapp - contenerized next.js app implementing UI for interaction with the flask backend

## Usage

In order to run the application you need to build the *compose.yaml* file
```bash
docker compose up -d --build 
```
When the build finishes, all containers should be working and main page should be visible at *localhost:3000*. 

Keep in mind that this project doesn't implement a lot of data security features at flask API endpoints.

## Key takeaways

- I understod the concepts of 'compose' files.
- Practiced communication between multiple containers.
- Got accustomed with container creation and command line docker operations.
- Used Next.js for the first time.
