
#  Bank Branch GraphQL API – Internship Assignment

This project solves the problem of querying bank branch data efficiently using a modern backend stack.


##  Problem Statement

Build a backend service that allows querying bank branches and their details (like IFSC, city, state, address, bank name) with multiple filters using GraphQL.


##  Solution Approach

I built a lightweight, fast API using:

- **FastAPI** – for the web server
- **Strawberry GraphQL** – to expose GraphQL queries
- **SQLite** – to store structured bank data
- **CSV file** – as the original data source
- **SQLAlchemy** – for ORM to handle DB operations
- **Pandas** – to load and clean the CSV

###  Why GraphQL?

GraphQL lets clients request **only the data they need** — making it ideal for frontend devs or mobile apps needing flexibility.


## 🛠️ Steps I Followed

1. Loaded the `bank_branches.csv` using `pandas`
2. Cleaned the data (e.g., removed nulls)
3. Stored it into a SQLite database using SQLAlchemy models (`Bank`, `Branch`)
4. Built a GraphQL API using Strawberry and FastAPI
5. Added filters like:
   - `city`, `state`, `district`
   - `bankName`, `ifscStartsWith`, `branch`, `addressContains`
   - `limit`, `offset` for pagination


## Sample Query

```graphql
query {
  branches(city: "MUMBAI", bankName: "HDFC", limit: 5) {
    edges {
      node {
        branch
        ifsc
        bank {
          name
        }
      }
    }
  }
}
```

##  How to Run Locally

```bash
git clone <your-repo>
cd bank_api
python -m venv venv
venv\Scripts\activate       
pip install -r requirements.txt
python -m app.seed          
uvicorn app.main:app --reload

CTRL+C  #(to stop the server)#
```

Then visit: [http://localhost:8000/gql]


## Why I Didn’t Deploy

I focused on delivering a clean local solution with:
- Fully tested GraphQL schema
- All filters implemented
- Heroku-compatible files included

I can deploy quickly if needed (Heroku, Render, etc.), but local execution was enough to demonstrate the API.

##  Final Note

This project is fully functional and testable via the GraphQL playground.  
