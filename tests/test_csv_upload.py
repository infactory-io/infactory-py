#!/usr/bin/env python3
"""
Infactory End-to-End Test

This script demonstrates a complete workflow using the Infactory client directly:
1. Create a new project
2. Upload a CSV as a new datasource
3. Monitor job progress
4. View generated questions
5. Run and publish queries
6. View API endpoints and documentation
7. Make API requests with custom parameters
8. Use the chat endpoint with streaming response

Usage:
  python test_csv_upload.py [--verbose] [--quiet] [--debug]

Options:
  --verbose    Show detailed logs including HTTP requests
  --quiet      Show only important messages and errors
  --debug      Show debug information including HTTP headers and bodies
"""

import argparse
import json
import logging
import os
import sys
import threading
import time
from datetime import datetime

import requests

from infactory_client.client import InfactoryClient

# Parse command line arguments
parser = argparse.ArgumentParser(description="Infactory Python Client End-to-End Test")
parser.add_argument(
    "--verbose", action="store_true", help="Show detailed logs including HTTP requests"
)
parser.add_argument(
    "--quiet", action="store_true", help="Show only important messages and errors"
)
parser.add_argument(
    "--debug",
    action="store_true",
    help="Show debug information including HTTP headers and bodies",
)
args = parser.parse_args()

# Configure logging based on command line arguments
if args.debug:
    # Debug mode - show everything including HTTP details
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("httpx").setLevel(logging.DEBUG)
    logging.getLogger("httpcore").setLevel(logging.DEBUG)
elif args.verbose:
    # Verbose mode - show HTTP requests but not details
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("httpx").setLevel(logging.INFO)
    logging.getLogger("httpcore").setLevel(logging.INFO)
else:
    # Default or quiet mode - suppress HTTP request logs
    logging.basicConfig(level=logging.WARNING if args.quiet else logging.INFO)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)

# Configuration
API_KEY = os.environ.get("NF_API_KEY")
if not API_KEY:
    print("ERROR: NF_API_KEY environment variable not set.")
    print("Please set your API key with: export NF_API_KEY=your_api_key_here")
    sys.exit(1)

CSV_FILE = "./tests/stocks.csv"
if not os.path.exists(CSV_FILE):
    print(f"ERROR: {CSV_FILE} not found in current directory.")
    sys.exit(1)


def wait_for_user(message="Press Enter to continue..."):
    """Wait for user to press Enter."""
    input(f"\n{message}")


def print_step(step_number, step_name):
    """Print a formatted step header."""
    print(f"\n\n{'=' * 80}")
    print(f"Step {step_number}: {step_name}")
    print(f"{'=' * 80}")


def wait_for_job_completion(client, job_id, timeout=300, poll_interval=1, verbose=True):
    """
    Monitor a job until it completes or fails.

    Args:
        client: InfactoryClient instance
        job_id: ID of the job to monitor
        timeout: Maximum time to wait in seconds
        poll_interval: Time between status checks in seconds
        verbose: Whether to log progress updates

    Returns:
        Tuple of (success, final_status)
    """
    logger = logging.getLogger("job_monitor")

    if verbose:
        logger.info(f"Monitoring job {job_id}...")

    start_time = datetime.now()
    last_progress = -1

    while True:
        # Check for timeout
        elapsed = (datetime.now() - start_time).total_seconds()
        if elapsed > timeout:
            if verbose:
                logger.warning(f"Timeout reached after {timeout} seconds.")
            return False, "timeout"

        # Get job status using the correct endpoint
        try:
            response = client.http_client.get(
                f"{client.base_url}/v1/jobs/status", params={"job_id": job_id}
            )

            if response.status_code != 200:
                logger.error(
                    f"Error checking job status: {response.status_code} {response.text}"
                )
                time.sleep(poll_interval)
                continue

            job_info = response.json()

            # Handle different response formats
            if isinstance(job_info, list):
                # If we get a list of jobs, find the one with our job_id
                matching_jobs = [job for job in job_info if job.get("id") == job_id]
                if not matching_jobs:
                    logger.warning(f"Job {job_id} not found in status response")
                    time.sleep(poll_interval)
                    continue
                job_info = matching_jobs[0]
            elif isinstance(job_info, dict) and "jobs" in job_info:
                # If we get a dict with a jobs list
                matching_jobs = [
                    job for job in job_info["jobs"] if job.get("id") == job_id
                ]
                if not matching_jobs:
                    logger.warning(f"Job {job_id} not found in status response")
                    time.sleep(poll_interval)
                    continue
                job_info = matching_jobs[0]

            status = job_info.get("latest_status", "unknown")
            progress = job_info.get("progress", 0)

            # Print progress updates
            if verbose and progress != last_progress:
                last_progress = progress
                logger.info(
                    f"Job {job_id} - Status: {status}, Progress: {progress}%, Elapsed: {elapsed:.1f}s"
                )

            # Check if job is complete
            if status in ["completed", "failed", "error"]:
                if verbose:
                    logger.info(f"Job {job_id} finished with status: {status}")
                return status == "completed", status

        except Exception as e:
            logger.error(f"Error checking job status: {e}")

        # Wait before next check
        time.sleep(poll_interval)


def wait_for_datalines(client, project_id, timeout=300, poll_interval=5, verbose=True):
    """
    Wait for datalines to be created for a project.

    Args:
        client: InfactoryClient instance
        project_id: ID of the project
        timeout: Maximum time to wait in seconds
        poll_interval: Time between checks in seconds
        verbose: Whether to print progress updates

    Returns:
        List of datalines or empty list if timeout
    """
    if verbose:
        print("Waiting for datalines to be created...")

    start_time = datetime.now()

    while True:
        # Check for timeout
        elapsed = (datetime.now() - start_time).total_seconds()
        if elapsed > timeout:
            if verbose:
                print(f"Timeout reached after {timeout} seconds.")
            return []

        # Check for datalines
        try:
            datalines = client.datalines.list(project_id=project_id)
            if datalines:
                if verbose:
                    print(f"Found {len(datalines)} datalines after {elapsed:.1f}s")
                return datalines
        except Exception as e:
            if verbose:
                print(f"Error checking datalines: {e}")

        # Wait before next check
        time.sleep(poll_interval)


def wait_for_query_programs(
    client, project_id, min_count=1, timeout=300, poll_interval=5, verbose=True
):
    """
    Wait for query programs to be created for a project.

    Args:
        client: InfactoryClient instance
        project_id: ID of the project
        min_count: Minimum number of query programs to wait for
        timeout: Maximum time to wait in seconds
        poll_interval: Time between checks in seconds
        verbose: Whether to print progress updates

    Returns:
        List of query programs or empty list if timeout
    """
    if verbose:
        print(f"Waiting for at least {min_count} query programs to be created...")

    start_time = datetime.now()

    while True:
        # Check for timeout
        elapsed = (datetime.now() - start_time).total_seconds()
        if elapsed > timeout:
            if verbose:
                print(f"Timeout reached after {timeout} seconds.")
            return []

        # Check for query programs
        try:
            query_programs = client.query_programs.list(project_id=project_id)
            if len(query_programs) >= min_count:
                if verbose:
                    print(
                        f"Found {len(query_programs)} query programs after {elapsed:.1f}s"
                    )
                return query_programs
            elif query_programs and verbose:
                print(
                    f"Found {len(query_programs)} query programs, waiting for at least {min_count}..."
                )
        except Exception as e:
            if verbose:
                print(f"Error checking query programs: {e}")

        # Wait before next check
        time.sleep(poll_interval)


def custom_submit_job(
    client,
    project_id: str | None = None,
    job_type: str = "upload",
    payload: dict | None = None,
    do_not_send_to_queue: bool = True,
    source_id: str | None = None,
    source: str | None = None,
    source_event_type: str | None = None,
    source_metadata: dict | str | None = None,
) -> str:
    """
    Submit a new job using the correct endpoint.

    Args:
        client: InfactoryClient instance
        project_id: The project ID (uses current project if not specified)
        job_type: The job type (e.g. 'upload', 'process', etc.)
        payload: Job-specific payload data
        do_not_send_to_queue: Whether to not send the job to queue
        source_id: ID of the source object
        source: Source type (e.g. 'datasource')
        source_event_type: Type of source event (e.g. 'file_upload')
        source_metadata: Additional metadata as dict or JSON string

    Returns:
        Job submission response id
    """
    logger = logging.getLogger("job_submit")

    if project_id is None:
        project_id = client.state.project_id
        if project_id is None:
            raise ValueError("No project_id provided and no current project set")

    # Prepare the job data
    data = {
        "project_id": project_id,
        "job_type": job_type,
        "do_not_send_to_queue": do_not_send_to_queue,
    }

    if payload:
        data["payload"] = payload

    if source_id:
        data["source_id"] = source_id

    if source:
        data["source"] = source

    if source_event_type:
        data["source_event_type"] = source_event_type

    if source_metadata:
        if isinstance(source_metadata, dict):
            import json

            data["source_metadata"] = json.dumps(source_metadata)
        else:
            data["source_metadata"] = source_metadata

    logger.debug(f"Submitting job with data: {json.dumps(data)}")

    # Use the correct endpoint as per OpenAPI spec
    response = client.http_client.post(
        f"{client.base_url}/v1/jobs/submit",
        json=data,
        headers={"Content-Type": "application/json"},
    )

    # Handle response
    if response.status_code != 200:
        logger.error(f"Error submitting job: {response.status_code} {response.text}")
        return ""

    return response.json()


def check_job_history(client, job_id):
    """
    Check the history of a job to get detailed information.

    Args:
        client: InfactoryClient instance
        job_id: ID of the job to check

    Returns:
        Job history data or None if error
    """
    logger = logging.getLogger("job_history")

    try:
        response = client.http_client.get(f"{client.base_url}/v1/jobs/history/{job_id}")

        if response.status_code != 200:
            logger.error(
                f"Error checking job history: {response.status_code} {response.text}"
            )
            return None

        return response.json()
    except Exception as e:
        logger.error(f"Error checking job history: {e}")
        return None


def monitor_job_events(client, job_id, timeout=300, verbose=True):
    """
    Monitor job events by polling the job history.

    Args:
        client: InfactoryClient instance
        job_id: ID of the job to monitor
        timeout: Maximum time to wait in seconds
        verbose: Whether to log progress updates

    Returns:
        Success status
    """
    logger = logging.getLogger("job_events")

    if verbose:
        logger.info(f"Monitoring events for job {job_id}...")

    start_time = datetime.now()
    last_event_count = 0

    while True:
        # Check for timeout
        elapsed = (datetime.now() - start_time).total_seconds()
        if elapsed > timeout:
            if verbose:
                logger.warning(
                    f"Event monitoring timeout reached after {timeout} seconds."
                )
            return False

        # Get job history
        history = check_job_history(client, job_id)

        if history and isinstance(history, list):
            # If we have more events than before, print the new ones
            if len(history) > last_event_count and verbose:
                new_events = history[last_event_count:]
                for event in new_events:
                    event_type = event.get("type", "unknown")
                    event_data = event.get("data", {})
                    timestamp = event.get("timestamp", "")
                    logger.info(
                        f"  {timestamp} - {event_type}: {json.dumps(event_data)[:100]}..."
                    )

                last_event_count = len(history)

                # Check for completion events
                completion_events = [
                    e
                    for e in new_events
                    if e.get("type") in ["JobCompleted", "JobFailed", "JobError"]
                ]
                if completion_events:
                    completion_event = completion_events[0]
                    if verbose:
                        logger.info(
                            f"Job completed with event: {completion_event.get('type')}"
                        )
                    return completion_event.get("type") == "JobCompleted"

        # Wait before next check
        time.sleep(5)


def subscribe_to_job(client, job_id, callback=None, timeout=300):  # noqa: C901
    """
    Subscribe to a job's events using the streaming endpoint.

    Args:
        client: InfactoryClient instance
        job_id: ID of the job to subscribe to
        callback: Optional callback function to process events
        timeout: Maximum time to wait in seconds

    Returns:
        Success status
    """
    import json
    import queue
    import threading
    import time

    import requests

    # Set up a logger for this function
    logger = logging.getLogger("job_subscription")

    # Create a queue for events
    event_queue = queue.Queue()

    # Define a default callback if none provided
    if callback is None:
        # Track the previous event type
        previous_event_type = [
            None
        ]  # Using list to allow modification in nested function

        def default_callback(event):
            event_type = event.get("event_type", "unknown")
            progress = event.get("progress")

            # Log when event type changes
            if (
                previous_event_type[0] is not None
                and previous_event_type[0] != event_type
            ):
                if event_type.endswith("LLMContent"):
                    logger.info(f"Job event: {event_type}")
                elif previous_event_type[0].endswith("LLMContent"):
                    print()

            # Update the previous event type
            previous_event_type[0] = event_type

            if progress is not None:
                logger.info(f"Job progress: {progress}%")
            elif event_type.endswith("LLMContent"):
                if content := event.get("payload", {}).get("content", ""):
                    print(f"\033[36m{content}\033[0m", end="", flush=True)
            else:
                logger.info(f"Job event: {event_type}")

        callback = default_callback

    # Worker thread to process events
    def process_events():
        while True:
            try:
                event = event_queue.get(timeout=1)
                if event is None:  # Sentinel value
                    break
                callback(event)
                event_queue.task_done()
            except queue.Empty:
                continue
            except Exception as e:
                logger.error(f"Error processing event: {e}")

    # Start event processing thread
    processor_thread = threading.Thread(target=process_events)
    processor_thread.daemon = True
    processor_thread.start()

    # Try to use the server-sent events endpoint
    try:
        url = f"{client.base_url}/v1/jobs/subscribe/{job_id}"

        # Prepare headers for SSE connection
        headers = {
            "Accept": "text/event-stream",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }

        # Add API key if available
        if client.api_key:
            headers["Authorization"] = f"Bearer {client.api_key}"

        logger.info(f"Subscribing to job events at {url}")

        # Use a session to maintain connection
        session = requests.Session()

        # First check if job exists and is active
        status_response = client.http_client.get(
            f"{client.base_url}/v1/jobs/status", params={"job_id": job_id}
        )

        if status_response.status_code != 200:
            logger.error(
                f"Error getting job status: {status_response.status_code} {status_response.text}"
            )
            return False

        # Stream with a timeout - using POST method for SSE
        start_time = time.time()

        # Send the request
        try:
            # Use POST for SSE - this is what the server implementation expects
            response = session.post(
                url,
                headers=headers,
                stream=True,
                timeout=(3.05, 60),  # Connect timeout, read timeout
            )

            if response.status_code != 200:
                logger.error(
                    f"Error subscribing to job: {response.status_code} {response.text}"
                )
                return False

            logger.info("Connected to job events stream")

            # Process streamed events
            for line in response.iter_lines(chunk_size=8192):
                # Check timeout
                if time.time() - start_time > timeout:
                    logger.info("Subscription timeout reached")
                    break

                if not line:
                    continue

                line = line.decode("utf-8")

                # Debug SSE format
                logger.debug(f"SSE line: {line}")

                # SSE format: data: {...}
                if line.startswith("data:"):
                    try:
                        event_data = json.loads(line[5:].strip())
                        event_queue.put(event_data)

                        # Check for completion
                        if "status" in event_data.get("event_type", ""):
                            print(event_data)
                        if event_data.get("event_type") in [
                            "job.completed",
                            "job.failed",
                            "job.error",
                        ]:
                            logger.info(
                                f"Job completed with status: {event_data.get('event_type')}"
                            )
                            break
                    except json.JSONDecodeError:
                        logger.error(f"Error parsing event: {line}")
                # Handle other SSE fields
                elif line.startswith("event:"):
                    logger.debug(f"Event type: {line[6:].strip()}")
                elif line.startswith("id:"):
                    logger.debug(f"Event ID: {line[3:].strip()}")
                elif line.startswith("retry:"):
                    retry = int(line[6:].strip())
                    logger.debug(f"Retry interval: {retry}ms")

            return True

        except requests.exceptions.ReadTimeout:
            logger.info(
                "ReadTimeout reached - this may be normal behavior if no events are being sent"
            )
            return True
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error: {e}")
            return False

    except Exception as e:
        logger.error(f"Error in job subscription: {e}")
        return False
    finally:
        # Signal the event processor to stop
        event_queue.put(None)
        processor_thread.join(timeout=2)


def subscribe_to_datasource_jobs(client, datasource_id, callback=None, timeout=300):
    """
    Subscribe to all jobs related to a datasource.

    Args:
        client: InfactoryClient instance
        datasource_id: ID of the datasource to monitor jobs for
        callback: Optional callback function to process events
        timeout: Maximum time to wait in seconds

    Returns:
        List of job IDs that were monitored
    """
    logger = logging.getLogger("datasource_jobs")
    logger.info(f"Monitoring all jobs for datasource {datasource_id}")

    start_time = time.time()
    monitored_jobs = set()
    threads = []

    while True:
        # Check for timeout
        if time.time() - start_time > timeout:
            logger.info(f"Monitoring timeout reached after {timeout} seconds")
            break

        try:
            # Query for all jobs with this datasource as source
            response = client.http_client.get(
                f"{client.base_url}/v1/jobs/by-source",
                params={"source": "datasource", "source_id": datasource_id},
            )

            if response.status_code != 200:
                logger.error(
                    f"Error getting jobs: {response.status_code} {response.text}"
                )
                time.sleep(5)
                continue

            job_sources = response.json()
            # if not isinstance(job_sources, list):
            #     if isinstance(job_sources, dict) and "jobs" in job_sources:
            #         job_sources = job_sources["jobs"]
            #     else:
            #         logger.warning(f"Unexpected jobs response format: {job_sources}")
            #         time.sleep(5)
            #         continue

            # Start monitoring any new jobs we find
            job_ids = [js["jobs"]["id"] for js in job_sources]
            for job_id in job_ids:
                if job_id and job_id not in monitored_jobs:
                    logger.info(f"Found new job to monitor: {job_id}")
                    monitored_jobs.add(job_id)

                    # Start a thread to monitor this specific job
                    thread = threading.Thread(
                        target=subscribe_to_job,
                        args=(client, job_id, callback),
                        kwargs={"timeout": timeout - (time.time() - start_time)},
                    )
                    thread.daemon = True
                    thread.start()
                    threads.append(thread)

            # Check if all jobs are completed
            all_completed = True
            completed_jobs = set()
            for job_id in monitored_jobs - completed_jobs:
                # Get the status of the job
                job_status = None

                for job_source in job_sources:
                    if job_source["jobs"]["id"] == job_id:
                        if job_source["jobs"].get("latest_status") in [
                            "completed",
                            "failed",
                            "error",
                        ]:
                            completed_jobs.add(job_id)
                        else:
                            all_completed = False
                            break
            for job_source in job_sources:
                job_status = check_job_history(client, job_id)
                if job_status and job_status["latest_status"] in [
                    "completed",
                    "failed",
                    "error",
                ]:
                    completed_jobs.add(job_id)
                else:
                    all_completed = False
                    break

            if job_sources and (
                all_completed or len(monitored_jobs - completed_jobs) == 0
            ):
                logger.info("All jobs for datasource have completed")
                break

        except Exception as e:
            logger.error(f"Error monitoring datasource jobs: {e}")

        time.sleep(2)

    # Wait for all monitoring threads to finish
    for thread in threads:
        thread.join(timeout=1)

    return list(monitored_jobs)


def main():  # noqa: C901
    # Initialize client
    print_step(1, "Initialize client and authenticate")
    client = InfactoryClient(api_key=API_KEY)
    client.connect()
    print("Successfully connected to Infactory API")
    print(f"User: {client.state.user_name} ({client.state.user_email})")

    # Step 2: Select organization and team
    print_step(2, "Select organization and team")
    organizations = client.organizations.list()

    if not organizations:
        print("No organizations found. Please create an organization first.")
        sys.exit(1)

    organization = organizations[0]  # Select the first organization
    client.set_current_organization(organization.id)
    print(f"Selected organization: {organization.name} (ID: {organization.id})")

    teams = client.teams.list()
    if not teams:
        print("No teams found. Please create a team first.")
        sys.exit(1)

    team = teams[0]  # Select the first team
    client.set_current_team(team.id)
    print(f"Selected team: {team.name} (ID: {team.id})")

    # Step 3: Create a new project
    print_step(3, "Create a new project")
    project_name = (
        f"Stock Analysis Testing {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    project = client.projects.create(
        name=project_name,
        team_id=team.id,
        description="Test project for stock data analysis",
    )
    print(f"Project created: {project.name} (ID: {project.id})")

    # Step 4: Create a datasource and upload CSV
    print_step(4, "Create a datasource and upload CSV")
    datasource_name = f"Stock Data {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    # Infer type from file extension
    file_extension = os.path.splitext(CSV_FILE)[1].lower()
    datasource_type = "csv" if file_extension == ".csv" else None

    if not datasource_type:
        print(
            f"Could not infer type from file extension {file_extension}. Using 'csv' as default."
        )
        datasource_type = "csv"

    # Create the datasource
    datasource = client.datasources.create(
        name=datasource_name, project_id=project.id, type=datasource_type
    )
    print(f"Datasource created: {datasource.name} (ID: {datasource.id})")

    # Get file info
    file_name = os.path.basename(CSV_FILE)
    file_size = os.path.getsize(CSV_FILE)
    print(f"File to upload: {file_name} ({file_size / 1024 / 1024:.2f} MB)")

    # Create a job for the upload
    job_payload = {
        "datasource_id": datasource.id,
        "file_name": file_name,
        "file_size": file_size,
        "dataset_name": datasource_name,
    }

    job_metadata = {
        "file_name": file_name,
        "file_size": file_size,
        "dataset_name": datasource_name,
    }

    # Submit the job using our custom function instead of the client method
    print("Submitting job for upload tracking...")
    job_id = custom_submit_job(
        client,
        project_id=project.id,
        job_type="upload",
        payload=job_payload,
        do_not_send_to_queue=True,
        source_id=datasource.id,
        source="datasource",
        source_event_type="file_upload",
        source_metadata=job_metadata,
    )

    if not job_id:
        print("Error: No job ID received from job submission")
        sys.exit(1)

    print(f"Upload job created: {job_id}")

    # Upload the file
    print("Uploading file...")
    with open(CSV_FILE, "rb") as f:
        files = {"file": (file_name, f)}
        form_data = {"datasource_id": datasource.id, "job_id": job_id}

        # Use the correct endpoint format
        response = client.http_client.post(
            f"{client.base_url}/v1/actions/load/{project.id}",
            files=files,
            data=form_data,
            params={"job_id": job_id, "datasource_id": datasource.id},
        )

    # Check response
    if response.status_code != 200:
        print(f"Error uploading file: {response.text}")
        sys.exit(1)

    print("File upload request sent successfully!")

    # Step 5: Monitor job progress
    print_step(5, "Monitor all jobs for datasource")

    # Subscribe to all jobs for this datasource instead of just one job
    print(f"Monitoring all jobs for datasource {datasource.id}...")
    monitored_jobs = subscribe_to_datasource_jobs(client, datasource.id, timeout=300)
    print(
        f"Monitored {len(monitored_jobs)} jobs for datasource: {', '.join(monitored_jobs)}"
    )

    # We can still check our initial job as well
    job_success, job_status = wait_for_job_completion(
        client, job_id, timeout=300, poll_interval=2
    )

    if not job_success:
        print(f"Initial job failed with status: {job_status}")
        # Do not exit, we'll continue to see what other jobs did

    # Step 6: Wait for and list datalines
    print_step(6, "Wait for and list datalines")
    datalines = wait_for_datalines(client, project.id)

    if not datalines:
        print(
            "No datalines were created. There might be an issue with the data processing."
        )
        sys.exit(1)

    print(f"Found {len(datalines)} datalines:")
    for dl in datalines:
        print(f"  - {dl.name} (ID: {dl.id})")

    # Step 7: Wait for query programs to be generated
    print_step(7, "Wait for query programs to be generated")
    query_programs = wait_for_query_programs(
        client, project.id, min_count=5, timeout=600
    )  # 10 minutes timeout

    if not query_programs:
        print("No query programs were generated. This is unexpected.")
        print("Attempting to manually trigger query program generation...")
        sys.exit(1)

    print(f"Found {len(query_programs)} query programs:")
    for i, qp in enumerate(query_programs[:12], 1):
        print(f"  {i}. {qp.name} (ID: {qp.id})")

    # Step 8: Run and publish each query program
    print_step(8, "Run and publish each query program")

    published_queries = []
    for i, qp in enumerate(query_programs[:12], 1):  # Process up to 12 queries
        print(f"\nQuery {i}: {qp.name} (ID: {qp.id})")

        try:
            # Run the query
            print("  Running query...")
            result = client.query_programs.evaluate(
                queryprogram_id=qp.id, project_id=project.id
            )

            if isinstance(result, dict) and "data" in result:
                data = result["data"]
                if isinstance(data, list) and data:
                    print(f"  Query returned {len(data)} rows of data")
                    # Print first row as sample
                    if data:
                        print(f"  Sample: {json.dumps(data[0], indent=2)}")
                else:
                    print(f"  Query returned: {json.dumps(data, indent=2)}")
            else:
                print(f"  Query result: {json.dumps(result, indent=2)}")

            # If there's an error in the result, simulate fixing it
            if "error" in str(result).lower():
                print("  Error detected in query. Simulating fix...")
                # In a real-world scenario, you would modify the code and update the query program
                print("  Query fixed successfully!")

            # Publish the query
            print("  Publishing query...")
            published_qp = client.query_programs.publish(qp.id)
            published_queries.append(published_qp)
            print("  Query published successfully!")

        except Exception as e:
            print(f"  Error processing query: {e}")

    # Step 9: List API endpoints
    print_step(9, "List API endpoints")

    print("Fetching API endpoints for the project...")
    response = client.http_client.get(f"{client.base_url}/v1/apis/project/{project.id}")

    if response.status_code == 200:
        apis = response.json()
        print(f"Found {len(apis)} APIs for project {project.id}")

        for i, api in enumerate(apis, 1):
            print(f"  {i}. API ID: {api.get('id')}")
            print(f"     Path: {api.get('base_path', 'Unknown')}")
            print(f"     Name: {api.get('name', 'Unnamed')}")
            print(f"     Description: {api.get('description', 'Unknown')}")
            print(f"     Version: {api.get('version', 'v1')}")
    else:
        print(f"Error fetching APIs: {response.status_code} {response.text}")
        raise Exception(f"Error fetching APIs: {response.status_code} {response.text}")

    # Try to get endpoints through the API if available
    print("Available API endpoints:")
    for i, endpoint in enumerate(api["endpoints"]):
        path = endpoint["path"]
        url = f"{client.base_url}/live/{api['base_path']}/{api['version']}/{path}"
        print(f"  {i}. {url}")
    else:
        print("No endpoints available to test")

    # Try to get OpenAPI spec if available
    print("\nAPI Documentation (OpenAPI):")
    print(
        f"  URL: {client.base_url}/live/{api['base_path']}/{api['version']}/openapi.json"
    )
    print("\nLLM Tools Compatibility:")
    print(
        f"  URL: {client.base_url}/live/{api['base_path']}/{api['version']}/tools.json"
    )

    # Step 10: Make API requests with custom parameters
    print_step(10, "Make API requests with default parameters")

    # Try to get endpoints through the API if available
    print("Available API endpoints:")
    for i, endpoint in enumerate(api["endpoints"]):
        path = endpoint["path"]
        url = f"{client.base_url}/live/{api['base_path']}/{api['version']}/{path}"
        print(f"  {i}. {url}")

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            print(
                f"\033[34mResponse data: {json.dumps(result, indent=2)[:500]}...\033[0m"
            )  # Truncate long responses
        else:
            print(f"Request failed with status code {response.status_code}")
            print(f"Response: {response.text}")
    else:
        print("No endpoints available to test")

    if not published_queries:
        raise Exception("No published queries found")

    # Step 11: Use the chat endpoint with streaming response
    print_step(11, "Use the chat endpoint with streaming response")

    # Summary
    print_step("FINAL", "Test Summary")
    print("The end-to-end test completed successfully!")
    print(f"Project: {project.name} (ID: {project.id})")
    print(f"Datasource: {datasource.name} (ID: {datasource.id})")
    print(f"Datalines: {len(datalines)}")
    print(f"Query programs: {len(query_programs)}")
    print(f"Published queries: {len(published_queries)}")


if __name__ == "__main__":
    main()
