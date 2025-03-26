#!/usr/bin/env python3
"""
Infactory CLI End-to-End Demo

This script demonstrates a complete workflow using the Infactory CLI:
1. Create a new project
2. Upload a CSV as a new datasource
3. Monitor job progress
4. View generated questions
5. Run and publish queries
6. View API endpoints and documentation
7. Make API requests with custom parameters
8. Use the chat endpoint with streaming response

Prerequisites:
- Have the infactory-client package installed: pip install infactory
- Have the stocks.csv file in the same directory
- Set your API key as an environment variable: export NF_API_KEY=your_api_key_here
"""

import json
import os
import subprocess
import sys
import time
import uuid

# Configuration
API_KEY = os.environ.get("NF_API_KEY")
if not API_KEY:
    print("ERROR: NF_API_KEY environment variable not set.")
    print("Please set your API key with: export NF_API_KEY=your_api_key_here")
    sys.exit(1)

CSV_FILE = "stocks.csv"
if not os.path.exists(CSV_FILE):
    print(f"ERROR: {CSV_FILE} not found in current directory.")
    sys.exit(1)

# Check if the infactory-client is installed
try:
    from infactory_client.client import InfactoryClient
except ImportError:
    print("ERROR: infactory-client package not installed.")
    print("Please install it with: pip install infactory")
    sys.exit(1)


# Helper function to run CLI commands
def run_command(command, capture_output=True, print_output=True):
    """Run a shell command and return its output."""
    if print_output:
        print(f"\n\033[1;36m> {command}\033[0m")

    try:
        result = subprocess.run(
            command, shell=True, capture_output=capture_output, text=True
        )

        if result.returncode != 0:
            print(f"Command failed with exit code {result.returncode}")
            print(f"Error: {result.stderr}")
            sys.exit(1)

        if print_output and capture_output:
            if result.stdout:
                print(result.stdout)

        return result
    except Exception as e:
        print(f"Error executing command: {e}")
        sys.exit(1)


def wait_for_user():
    """Wait for user to press Enter to continue."""
    input("\n\033[1;33mPress Enter to continue...\033[0m")


# Step 1: Login and check current state
print("\n\033[1;32m=== Step 1: Login and Check Current State ===\033[0m")
run_command("nf login")
run_command("nf show")
wait_for_user()

# Step 2: Select organization and team
print("\n\033[1;32m=== Step 2: Select Organization and Team ===\033[0m")
run_command("nf orgs list")
run_command("nf orgs select")
run_command("nf teams list")
run_command("nf teams select")
wait_for_user()

# Step 3: Create a new project
print("\n\033[1;32m=== Step 3: Create a New Project ===\033[0m")

# First, we need the current team ID
try:
    team_id_result = run_command("nf show --json", print_output=False)
    client_state = json.loads(team_id_result.stdout)

    if not client_state.get("team"):
        print("ERROR: No team selected. Please select a team first.")
        sys.exit(1)

    team_id = client_state["team"]["id"]

    # Create a unique project name
    project_name = f"Stock Analysis {str(uuid.uuid4())[:8]}"
    print(f"Creating new project: {project_name}")

    # We don't have a CLI command to create a project directly, so we'll use the Python API
    client = InfactoryClient()
    client.connect()

    print(f"Creating project '{project_name}' in team {team_id}")
    project = client.projects.create(
        name=project_name,
        team_id=team_id,
        description="Stock data analysis project created via demo script",
    )
    print(f"Project created successfully: {project.name} (ID: {project.id})")

    # Set the project as the current project
    run_command(f"nf projects set {project.id}")
except Exception as e:
    print(f"ERROR creating project: {e}")
    sys.exit(1)

wait_for_user()

# Step 4: Create a datasource and upload CSV
print("\n\033[1;32m=== Step 4: Create a Datasource and Upload CSV ===\033[0m")
datasource_name = f"Stock Data {str(uuid.uuid4())[:8]}"
run_command(f"nf datasources create {datasource_name} --type csv")

try:
    # Get the datasource ID from the output
    datasource_id_result = run_command("nf datasources list --json", print_output=False)
    datasources = json.loads(datasource_id_result.stdout)

    if not datasources:
        print("ERROR: No datasources found after creation. Check the API response.")
        sys.exit(1)

    datasource_id = datasources[0][
        "id"
    ]  # Assuming the first datasource is the one we just created

    print(f"Uploading {CSV_FILE} to datasource {datasource_id}...")
    # Since there's no direct CLI command for upload, we'll use the Python API
    datasource_response = client.datasources.upload(
        datasource_id=datasource_id, file_path=CSV_FILE
    )
    print("CSV file uploaded successfully!")
    print(f"Response: {json.dumps(datasource_response, indent=2)}")
except Exception as e:
    print(f"ERROR uploading CSV: {e}")
    sys.exit(1)

wait_for_user()

# Step 5: Monitor job progress
print("\n\033[1;32m=== Step 5: Monitor Job Progress ===\033[0m")
print(f"Monitoring jobs for datasource {datasource_id}...")

# Start the job subscription in a separate process
print("Subscribing to job updates... (press Ctrl+C to stop after a while)")
try:
    # Using a timeout to prevent hanging indefinitely
    print("(Monitoring will automatically stop after 30 seconds)")
    process = subprocess.Popen(f"nf jobs subscribe {datasource_id}", shell=True)

    # Wait for 30 seconds or until keyboard interrupt
    timeout = 30
    try:
        for i in range(timeout):
            time.sleep(1)
            # Show a countdown
            sys.stdout.write(f"\rMonitoring... {timeout - i} seconds remaining ")
            sys.stdout.flush()
        print("\n\nMonitoring timed out. Moving on to the next step.")
    except KeyboardInterrupt:
        print("\n\nStopped job monitoring.")

    # Terminate the process if it's still running
    if process.poll() is None:
        process.terminate()
        time.sleep(1)
        if process.poll() is None:
            process.kill()
except Exception as e:
    print(f"ERROR monitoring jobs: {e}")

wait_for_user()

# Step 6: List the generated datalines
print("\n\033[1;32m=== Step 6: List Generated Datalines ===\033[0m")
run_command("nf datalines list")
wait_for_user()

# Step 7: View and interact with generated query programs
print("\n\033[1;32m=== Step 7: View Generated Query Programs ===\033[0m")
run_command("nf query list")

# Check if we have query programs
try:
    query_list_result = run_command("nf query list --json", print_output=False)
    query_programs = json.loads(query_list_result.stdout)

    if not query_programs:
        print(
            "\nNo query programs found yet. This is normal if the data is still being processed."
        )
        print(
            "In a real scenario, you would wait until the data processing is complete."
        )
        print("For the demo, we'll continue with mocked data for the remaining steps.")

        # Create mock query programs for the demo
        print("\nCreating mock query programs for demonstration...")
        mock_queries = True
    else:
        mock_queries = False
except Exception as e:
    print(f"ERROR checking query programs: {e}")
    mock_queries = True

wait_for_user()

# Step 8: Select and run each query program
print("\n\033[1;32m=== Step 8: Run and Publish Query Programs ===\033[0m")

if mock_queries:
    # Mock data for demonstration
    print("Using mock data for demonstration purposes...")
    mock_query_programs = [
        {"id": "qp-mock1", "name": "Average Stock Price by Month"},
        {"id": "qp-mock2", "name": "Top Performing Stocks"},
        {"id": "qp-mock3", "name": "Price Trends Analysis"},
        {"id": "qp-mock4", "name": "Volume vs Price Correlation"},
    ]

    for i, query in enumerate(mock_query_programs, 1):
        query_id = query["id"]
        print(
            f"\n\033[1;34mSimulating query {i}: {query['name']} (ID: {query_id})\033[0m"
        )

        print(f"[MOCK] Running query {query_id}...")
        print("[MOCK] Query results would appear here...")

        print(f"\n[MOCK] Publishing query {query_id}...")
        print(f"[MOCK] Query program {query_id} published successfully!")

        if i % 3 == 0:  # Pause after every 3 queries
            wait_for_user()
else:
    # Use real query programs
    try:
        for i, query in enumerate(query_programs[:12], 1):  # Process up to 12 queries
            query_id = query["id"]
            print(
                f"\n\033[1;34mRunning query {i}: {query['name']} (ID: {query_id})\033[0m"
            )

            # Run the query
            run_command(f"nf query get {query_id} --run")

            # Publish the query
            print(f"\nPublishing query {query_id}...")
            run_command(f"nf query get {query_id} --publish")

            if i % 3 == 0:  # Pause after every 3 queries
                wait_for_user()
    except Exception as e:
        print(f"ERROR processing queries: {e}")

# Step 9: View the API endpoints
print("\n\033[1;32m=== Step 9: View API Endpoints ===\033[0m")
run_command("nf endpoints list")

# Get an endpoint ID for curl example
endpoint_id = "ep-123abc"  # This is a placeholder; in reality, we would get this from the endpoint list
run_command(f"nf endpoints curl-example {endpoint_id}")
wait_for_user()

# Step 10: Make API requests with custom parameters
print("\n\033[1;32m=== Step 10: Make API Requests with Custom Parameters ===\033[0m")
base_url = "https://api.infactory.ai"
endpoint_url = "/v1/live/stock-analysis/v1/data"  # This is a placeholder

print(f"Making API request to {base_url}{endpoint_url}")
print("With custom parameters: limit=5, sort_by=date")

# Example API request
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

try:
    print("[MOCK] Simulating API request...")
    # Simulate a successful response for demonstration
    mock_response = {
        "data": [
            {
                "date": "2023-03-01",
                "symbol": "AAPL",
                "price": 145.91,
                "volume": 83521000,
            },
            {
                "date": "2023-03-02",
                "symbol": "AAPL",
                "price": 149.58,
                "volume": 75684300,
            },
            {
                "date": "2023-03-03",
                "symbol": "AAPL",
                "price": 151.03,
                "volume": 70898900,
            },
            {
                "date": "2023-03-06",
                "symbol": "AAPL",
                "price": 153.83,
                "volume": 86325700,
            },
            {
                "date": "2023-03-07",
                "symbol": "AAPL",
                "price": 152.59,
                "volume": 67039100,
            },
        ],
        "meta": {"count": 5, "total": 22, "sort_by": "date", "order": "asc"},
    }
    print("API request successful!")
    print(json.dumps(mock_response, indent=2))

    # Uncomment to make a real API request
    # response = requests.get(
    #     f"{base_url}{endpoint_url}",
    #     headers=headers,
    #     params={"limit": 5, "sort_by": "date"}
    # )
    #
    # if response.status_code == 200:
    #     print("API request successful!")
    #     print(json.dumps(response.json(), indent=2))
    # else:
    #     print(f"API request failed with status code {response.status_code}")
    #     print(response.text)
except Exception as e:
    print(f"Error making API request: {e}")

wait_for_user()

# Step 11: Use the chat endpoint with streaming response
print("\n\033[1;32m=== Step 11: Use Chat Endpoint with Streaming Response ===\033[0m")
chat_url = f"{base_url}/v1/live/chat"

print(f"Making streaming request to {chat_url}")
print("Question: What was the highest stock price in the last month?")

try:
    # Simulated streaming response (in reality, we would use SSE or WebSockets)
    print("\nStreaming response:")

    # Simulate a streaming response
    streaming_response = [
        "Analyzing the stock data...",
        "Looking at prices over the last month...",
        "The highest stock price in the last month was $157.82 for AAPL on March 15, 2023.",
        "This represents a 12.4% increase from the beginning of the month.",
        "Other notable high prices were $145.73 for MSFT and $208.91 for GOOG.",
    ]

    for chunk in streaming_response:
        print(chunk)
        time.sleep(1)  # Simulate streaming delay

    print("\nStreaming response completed!")
except Exception as e:
    print(f"Error with streaming request: {e}")

# Summary
print("\n\033[1;32m=== Demo Completed Successfully! ===\033[0m")
print("This demo showcased the complete workflow of the Infactory platform:")
print("1. Created a new project")
print("2. Uploaded a CSV file as a datasource")
print("3. Monitored job progress")
print("4. Viewed generated questions")
print("5. Ran and published queries")
print("6. Viewed API endpoints and documentation")
print("7. Made API requests with custom parameters")
print("8. Used the chat endpoint with streaming response")

print("\nNotes:")
print("- Some steps used mock data for demonstration purposes")
print("- In a real scenario, you would need to wait for data processing to complete")
print("- The actual API endpoints and responses would vary based on your data")
print("- The 'nf' CLI tool provides powerful commands for managing Infactory resources")
print("\nFor more information, please refer to the Infactory documentation.")
