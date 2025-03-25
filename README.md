# Infactory SDK

The Infactory SDK provides simple and powerful interfaces to work with your data and AI services. It allows you to connect your data sources, create query programs, and publish them as APIs, all from your terminal or Python code.

## Installation

```bash
pip install infactory
```

## Development and Deployment

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/infactory-io/infactory-py.git
cd infactory-py
```

2. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:
```bash
poetry install
```

4. Run tests:
```bash
poetry run pytest
```

### Publishing to PyPI

The package is automatically published to PyPI when a new version tag is pushed to the repository. To release a new version:

1. Update the version in `pyproject.toml`
2. Create and push a new version tag:
```bash
git add pyproject.toml
git commit -m "Bump version to X.Y.Z"
git tag vX.Y.Z
git push origin main --tags
```

The GitHub Actions workflow will automatically:
- Build the package
- Run tests
- Publish to PyPI using trusted publisher configuration

## Getting Started

### Setting your API Key

Before using the SDK, you need to set your API key. You can either set it as an environment variable or use the CLI login command:

```bash
# Set the API key as an environment variable
export NF_API_KEY=your_api_key_here

# Or use the CLI login command
nf login
```

## CLI Examples

The Infactory CLI (`nf`) provides a set of commands to interact with the Infactory platform.

### 1. Login to Infactory

```bash
$ nf login
Enter your API key: ********************
API key saved successfully!
```

### 2. Connect a Postgres datasource

```bash
$ nf datasource create --name "Product Database" --type postgres --project-id my-project-id
Datasource created successfully!
ID: ds-abc123
Name: Product Database
Type: postgres

$ nf datasource configure ds-abc123 --uri "postgresql://username:password@host:port/database"
Datasource configured successfully!
```

### 3. Subscribe to jobs for the data source

```bash
$ nf jobs subscribe --datasource-id ds-abc123
Subscribing to jobs for datasource ds-abc123...
[2025-03-25 14:30:21] Job j-123456 started: Connecting to PostgreSQL database
[2025-03-25 14:30:22] Job j-123456 progress: Successfully connected to database
[2025-03-25 14:30:25] Job j-123456 progress: Analyzing table structure
[2025-03-25 14:30:30] Job j-123456 progress: Found 12 tables with 450,000 rows total
[2025-03-25 14:30:45] Job j-123456 completed: Database connection established and schema analyzed
```

### 4. Generate a query program

```bash
$ nf query generate --dataline-id dl-456def --name "Monthly Sales by Region"
Query program generation started...
Analyzing data structure...
Generating query program...
Query program created successfully!
ID: qp-789ghi
Name: Monthly Sales by Region
```

### 5. Run the new code

```bash
$ nf query run qp-789ghi
Running query program qp-789ghi...
Results:
+----------+--------+-------------+
| Month    | Region | Total Sales |
+----------+--------+-------------+
| Jan 2025 | North  | $245,678.90 |
| Jan 2025 | South  | $198,432.45 |
| Jan 2025 | East   | $312,567.80 |
| Jan 2025 | West   | $276,543.21 |
| Feb 2025 | North  | $267,890.12 |
| Feb 2025 | South  | $210,987.65 |
...
```

### 6. Publish the query program

```bash
$ nf query publish qp-789ghi
Publishing query program qp-789ghi...
Query program published successfully!
Endpoint URL: https://api.infactory.ai/v1/live/monthly-sales/v1/data
```

### 7. Display the available endpoints

```bash
$ nf endpoints list --project-id my-project-id
+-------------+-----------------+----------------------------------+--------+
| Endpoint ID | Name            | URL                              | Method |
+-------------+-----------------+----------------------------------+--------+
| ep-123abc   | Monthly Sales   | /v1/live/monthly-sales/v1/data   | GET    |
| ep-456def   | Product Details | /v1/live/product-details/v1/data | GET    |
| ep-789ghi   | Customer Stats  | /v1/live/customer-stats/v1/data  | GET    |
+-------------+-----------------+----------------------------------+--------+
```

### 8. Generate a CURL request for an endpoint

```bash
$ nf endpoints curl-example ep-123abc
CURL example for endpoint ep-123abc:

curl -X GET "https://api.infactory.ai/v1/live/monthly-sales/v1/data" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json"
```

## Python SDK Examples

The Infactory Python SDK provides a simple interface to interact with the Infactory platform.

### 1. Import and setup

```python
import infactory as nf

# Initialize the client with your API key (or it will use NF_API_KEY environment variable)
client = nf.Client(api_key="your_api_key_here")
client.connect()
```

### 2. Create and configure a datasource

```python
# Get the current project or set a specific one
project = client.projects.get("my-project-id")

# Create a new datasource
datasource = client.datasources.create(
    name="Product Database",
    project_id=project.id,
    type="postgres"
)

# Configure the datasource connection
datasource = client.datasources.update(
    datasource.id,
    uri="postgresql://username:password@host:port/database"
)

print(f"Datasource created: {datasource.name} (ID: {datasource.id})")
```

### 3. List datalines in the project

```python
# Get all datalines for the project
datalines = client.datalines.list(project_id=project.id)

for dl in datalines:
    print(f"Dataline: {dl.name} (ID: {dl.id})")
```

### 4. Create a query program

```python
# Choose a dataline from the list
dataline = datalines[0]

# Create a new query program
query_program = client.query_programs.create(
    name="Monthly Sales by Region",
    question="What are the monthly sales by region?",
    code="""
    import pandas as pd

    def execute(df):
        # Group by month and region, sum sales
        result = df.groupby(['month', 'region'])['sales'].sum().reset_index()
        return result
    """,
    dataline_id=dataline.id,
    project_id=project.id
)

print(f"Query program created: {query_program.name} (ID: {query_program.id})")
```

### 5. Run the query program

```python
# Evaluate the query program
result = client.query_programs.evaluate(query_program.id)

print("Query results:")
print(result)
```

### 6. Publish the query program

```python
# Publish the query program to make it available as an API
published_program = client.query_programs.publish(query_program.id)

print(f"Query program published: {published_program.id}")
```

### 7. Create an API endpoint

```python
# Get API endpoints from the project
apis = client.projects.get_apis(project.id)

if apis:
    api = apis[0]
    print(f"Using existing API: {api.name}")
else:
    # Create a new API
    api = client.apis.create(
        name="Sales Analytics API",
        description="API for sales data analytics",
        project_id=project.id
    )
    print(f"Created new API: {api.name}")

# Create an endpoint for the query program
endpoint = client.apis.create_endpoint(
    api_id=api.id,
    name="Monthly Sales",
    http_method="GET",
    description="Get monthly sales data by region",
    queryprogram_id=query_program.id
)

print(f"Endpoint created: {endpoint.path}")
```

### 8. Get endpoint URL and details

```python
# Get details for all endpoints in the API
endpoints = client.apis.get_endpoints(api.id)

for ep in endpoints:
    print(f"Endpoint: {ep.name}")
    print(f"URL: https://api.infactory.ai/v1/live/{api.slug}/{api.version}/{ep.path}")
    print(f"Method: {ep.http_method}")
    print(f"Description: {ep.description}")
    print("-" * 50)
```

## Advanced Features

Check out our [documentation](https://docs.infactory.ai) for more information on advanced features such as:

- Custom transformations and data processing
- Automated data quality checks
- Integration with ML models
- Real-time data streaming
- Team collaboration features

## Support

If you need help or have any questions, please contact us at support@infactory.ai or visit our [support portal](https://support.infactory.ai).
