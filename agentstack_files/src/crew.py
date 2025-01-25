from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import agentstack

@CrewBase
class AgentstackfilesCrew():
    """agentstack_files crew"""

    @task
    def hello_world(self) -> Task:
        return Task(
            config=self.tasks_config['hello_world'],
        )

    @task
    def notify_user(self) -> Task:
        return Task(
            config=self.tasks_config['notify_user'],
        )

    @agent
    def alex(self) -> Agent:
        return Agent(
            config=self.agents_config['alex'],
            tools=[*agentstack.tools['file_read']], # add tools here or use `agentstack tools add <tool_name>
            verbose=True,
        )

    @agent
    def acc_partner(self) -> Agent:
        return Agent(
            config=self.agents_config['acc_partner'],
            tools=[], # add tools here or use `agentstack tools add <tool_name>
            verbose=True,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Test crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            
            verbose=True,
        )