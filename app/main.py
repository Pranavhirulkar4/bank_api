from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.gql_schema import schema
from app.database import init_db

init_db()

app = FastAPI()
graphql_app = GraphQLRouter(schema)

@app.get('/')
def root():
    return {'message': 'GraphQL server running at /gql'}

app.include_router(graphql_app, prefix='/gql')