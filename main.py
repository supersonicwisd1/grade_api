from fastapi import FastAPI, Query
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/get_info")
async def get_info(
    slack_name: str = Query(..., description="Slack name"),
    track: str = Query(..., description="Track"),
):
    # Get the current day of the week
    current_day = datetime.utcnow().strftime('%A')

    # Calculate UTC time with validation of +/-2 hours
    utc_time = datetime.utcnow() + timedelta(hours=2)
    utc_time_str = utc_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Define the GitHub URLs
    github_file_url = f"https://github.com/supersonicwisd1/grade_api/blob/main/main.py"
    github_repo_url = f"https://github.com/supersonicwisd1/grade_api"

    # Create the response JSON
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return response
