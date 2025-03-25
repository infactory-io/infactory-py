"""
Here are some examples of the ways to use the Infactory API.
"""

from infactory_client.client import InfactoryClient


def create_api_for_user():
    nf = InfactoryClient()
    nf.login()  # This should open a browser window to login via Clerk and return with the JWT token
    # optionally
    nf.connect()  # This should connect to the Infactory API using the API Key to generate the JWT token

    # The account creation should also run to create a default organization, team, user and project and set it to the state of the client
    state = nf.state
    print(state)

    # The state serve as the default parameters for all requests

    nf.upload(
        "data/test.csv"
    )  # This should upload the file to the default project and create a dataline
    nf.explore(
        n=10
    )  # This should generate 10 random questions and answers about the data - stored as query programs
    nf.query_programs.publish(
        all=True, public=True
    )  # This should publish all query programs publicly
    print(nf.query_programs())  # This should list all query programs
    print(nf.project.docs.endpoint())  # This should return the project docs endpoint
    print(
        nf.project.docs.as_tools()
    )  # Format the docs as tools to be used in a LLM chain


def ask_questions_of_a_dataset():
    nf = InfactoryClient()
    nf.login()
    # nf.connect()
    # Assuming a default project and datasource and query programs have been created
    # Select a query program from a list of query programs
    query_program = nf.query_programs()[0]
    print(query_program)

    # Ask a question of the query program
    answer = nf.ask(query_program)
    print(answer)
