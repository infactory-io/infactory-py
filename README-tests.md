# Testing Best Practices for the Infactory SDK

Testing a client SDK like Infactory requires a multi-layered testing approach to ensure both the Python library and CLI work correctly. Here's a comprehensive testing strategy:

## 1. Unit Tests

### Python SDK Unit Tests

Unit tests should validate the individual components of your SDK without requiring actual API calls:

- **Test models**: Ensure model serialization/deserialization works correctly
- **Test service classes**: Verify that API calls are constructed properly
- **Test client initialization**: Check that configuration loading works as expected
- **Test error handling**: Validate that API errors are caught and transformed properly

Use mock responses with a library like `unittest.mock` or `pytest-mock`:

```python
def test_projects_list(mocker):
    # Mock the HTTP response
    mock_response = [{"id": "proj-123", "name": "Test Project", "team_id": "team-456"}]
    mock_get = mocker.patch("infactory_client.client.Client._get", return_value=mock_response)

    # Create client and call the method
    client = Client(api_key="test_key")
    projects = client.projects.list(team_id="team-456")

    # Assertions
    mock_get.assert_called_once_with("v1/projects", {"team_id": "team-456"})
    assert len(projects) == 1
    assert projects[0].id == "proj-123"
    assert projects[0].name == "Test Project"
```

### CLI Unit Tests

For the CLI, test that commands properly parse arguments and call the appropriate SDK methods:

```python
def test_projects_list_command(mocker):
    # Mock the projects.list method
    mock_projects = [MagicMock(id="proj-123", name="Test Project")]
    mock_client = MagicMock()
    mock_client.projects.list.return_value = mock_projects
    mocker.patch("infactory_cli.get_client", return_value=mock_client)

    # Call the CLI command handler
    args = MagicMock(team_id="team-456")
    handle_projects_list(args)

    # Assertions
    mock_client.projects.list.assert_called_once_with(team_id="team-456")
```

## 2. Integration Tests

Integration tests validate that your SDK can properly interact with the API:

### Approach 1: Mock Server

Set up a mock server that mimics the Infactory API responses:

- Use tools like `responses`, `requests-mock`, or `httpx-mock` to intercept HTTP requests
- Create a fixture with realistic API responses
- Test complete workflows through multiple API calls

```python
def test_create_and_publish_query_program(requests_mock):
    # Mock API responses
    requests_mock.post("https://api.infactory.ai/v1/queryprograms", json={"id": "qp-123", "name": "Test Query"})
    requests_mock.patch("https://api.infactory.ai/v1/queryprograms/qp-123/publish", json={"id": "qp-123", "published": True})

    # Execute the workflow
    client = Client(api_key="test_key")
    query = client.query_programs.create(name="Test Query", dataline_id="dl-456", code="test code")
    published = client.query_programs.publish(query.id)

    # Assertions
    assert published.id == "qp-123"
    assert published.published is True
```

### Approach 2: VCR-style Tests

Record actual API responses and replay them in tests:

- Use `vcr.py` or `betamax` to record and replay HTTP interactions
- Run tests against the actual API once, then replay for subsequent test runs
- Provides realistic responses without hitting the API repeatedly

```python
@vcr.use_cassette('fixtures/vcr_cassettes/project_list.yaml')
def test_list_projects():
    client = Client(api_key="test_key")
    projects = client.projects.list(team_id="team-456")

    assert len(projects) > 0
    assert projects[0].id is not None
```

## 3. End-to-End (E2E) Tests

E2E tests validate complete user workflows against the actual API:

### Approach 1: Test Account

- Create a dedicated test account in the Infactory platform
- Run automated tests against this account with real API calls
- Test full workflows from start to finish

```python
def test_e2e_datasource_workflow():
    # Use a test API key from environment variable
    client = Client(api_key=os.environ.get("NF_TEST_API_KEY"))

    # Create a project
    project = client.projects.create(name="Test Project", team_id=os.environ.get("NF_TEST_TEAM_ID"))

    # Create a datasource
    datasource = client.datasources.create(name="Test DB", project_id=project.id, type="postgres")

    # List datasources
    datasources = client.datasources.list(project_id=project.id)

    # Assertions
    assert any(ds.id == datasource.id for ds in datasources)

    # Clean up
    client.datasources.delete(datasource.id)
    client.projects.delete(project.id)
```

### Approach 2: CLI E2E Tests

Test the CLI commands against the actual API:

```python
def test_cli_e2e():
    # Run CLI commands using subprocess
    result = subprocess.run(
        ["nf", "login", "--key", os.environ.get("NF_TEST_API_KEY")],
        capture_output=True, text=True
    )
    assert "API key saved successfully" in result.stdout

    result = subprocess.run(
        ["nf", "projects", "list", "--team-id", os.environ.get("NF_TEST_TEAM_ID")],
        capture_output=True, text=True
    )
    assert "ID" in result.stdout
```

## 4. Test Environment Setup

For comprehensive testing, set up:

1. **CI/CD Pipeline Integration**:
   - Run unit tests on every commit
   - Run integration tests on PRs
   - Run E2E tests on release branches

2. **Test Fixtures**:
   - Create reusable test data
   - Set up environment for realistic workflows
   - Implement automatic cleanup after tests

3. **Testing Matrix**:
   - Test across different Python versions (3.8, 3.9, 3.10, 3.11, 3.12)
   - Test on different operating systems (Windows, macOS, Linux)

## 5. Testing Recommendations

### When to Mock vs. Use Live Endpoints

- **Unit Tests**: Always use mocks
- **Integration Tests**: Use recorded responses or a mock server
- **E2E Tests**: Use a dedicated test account with live endpoints

### Best Practices

1. **Use a dedicated test account**: Don't use production credentials
2. **Clean up test resources**: Delete any created resources after tests
3. **Use fixture data**: Prepare test data for reproducible results
4. **Make tests independent**: Each test should be able to run on its own
5. **Use realistic data**: Test with data that resembles real-world usage
6. **Test edge cases**: Error handling, rate limiting, authentication failures
7. **Test CLI workflows**: Validate common command patterns
8. **Focus on main workflows**: Prioritize testing the most common user flows

By implementing this testing strategy, you'll build confidence in your Infactory SDK and ensure a quality experience for your users across both the Python library and CLI interfaces.
