import datetime
from google.adk.agents import Agent
from google.adk.planners import PlanReActPlanner


def get_current_time() -> dict:
    """Returns the current date and time.

    Returns:
        dict: status and result or error msg.
    """
    try:
        now = datetime.datetime.now()
        report = f"The current time is {now.strftime('%Y-%m-%d %H:%M:%S')}"
        return {"status": "success", "report": report}
    except Exception:
        return {
            "status": "error",
            "error_message": ("Sorry, I couldn't get the current time."),
        }


root_agent = Agent(
    name="date_time_agent",
    model="gemini-2.0-flash",
    description=("Helpful assistant"),
    instruction=(
        "Do not ask the user any follow up questions. Use the tools at your disposal."),
    tools=[get_current_time],
    planner=PlanReActPlanner(),
)
