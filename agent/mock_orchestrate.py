# mock_orchestrate.py
# This file simulates IBM watsonx Orchestrate behavior for the hackathon
# So that our agent can "run workflows" without needing IBM access.

class MockOrchestrate:
    """
    A lightweight mock engine that simulates:
    - workflow runs
    - skill calling
    - task chaining
    - async triggers
    """

    def __init__(self):
        self.logs = []

    def log(self, message):
        print(f"[MOCK-ORCHESTRATE] {message}")
        self.logs.append(message)

    def run_workflow(self, name, **kwargs):
        """
        Simulate starting a workflow.
        """
        self.log(f"Workflow '{name}' triggered with parameters: {kwargs}")
        return {
            "workflow": name,
            "status": "completed",
            "result": kwargs
        }

    def run_skill(self, skill_name, func, *args, **kwargs):
        """
        Simulate calling a digital skill.
        """
        self.log(f"Skill '{skill_name}' executed.")
        result = func(*args, **kwargs)
        return {
            "skill": skill_name,
            "output": result
        }

    def chain(self, steps):
        """
        Simulate a workflow chain.
        Example:
        orchestrate.chain([
            ("load_data", func),
            ("clean_data", func),
            ("generate_report", func)
        ])
        """
        results = {}
        for step_name, func, params in steps:
            self.log(f"Running workflow step: {step_name}")
            results[step_name] = func(**params)
        return results


# Global orchestrate engine instance
orchestrate = MockOrchestrate()

