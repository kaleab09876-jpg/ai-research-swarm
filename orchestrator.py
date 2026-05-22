from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import track
from rich.align import Align
import time

from agents.researcher import research_topic
from agents.summarizer import summarize_research
from agents.fact_checker import verify_information

console = Console()

console.print(
    Align.center(
        "[bold magenta]AI RESEARCH SWARM[/bold magenta]\n"
        "[cyan]Multi-Agent Research Framework[/cyan]"
    )
)

console.print("\n[bold]Initializing autonomous research workflow...[/bold]\n")

workflow_steps = [
    "Loading research topic",
    "Routing task to Research Agent",
    "Collecting information",
    "Routing task to Summarizer Agent",
    "Generating condensed brief",
    "Routing task to Fact Checker Agent",
    "Verifying consistency",
    "Generating final research report"
]

for step in track(workflow_steps, description="Processing Agents..."):
    time.sleep(0.7)

with open("reports/ai_safety_report.txt", "r") as file:
    report = file.read()

research = research_topic(report)

summary = summarize_research(research)

verification = verify_information(summary)

console.print("\n")

console.print(
    Panel(
        research,
        title="[bold blue]Research Agent[/bold blue]",
        border_style="blue"
    )
)

console.print(
    Panel(
        summary,
        title="[bold yellow]Summarizer Agent[/bold yellow]",
        border_style="yellow"
    )
)

console.print(
    Panel(
        verification,
        title="[bold green]Fact Checker Agent[/bold green]",
        border_style="green"
    )
)

table = Table(title="Research Workflow Summary")

table.add_column("Agent", style="cyan", justify="center")
table.add_column("Status", style="green", justify="center")
table.add_column("Task")

table.add_row(
    "Research Agent",
    "Complete",
    "Knowledge Collection"
)

table.add_row(
    "Summarizer Agent",
    "Complete",
    "Research Compression"
)

table.add_row(
    "Fact Checker Agent",
    "Complete",
    "Information Verification"
)

console.print("\n")
console.print(table)

console.print(
    "\n[bold green]Autonomous research workflow completed successfully.[/bold green]"
)