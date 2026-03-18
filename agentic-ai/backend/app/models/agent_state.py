class AgentState:
    def __init__(self, current_state: str, previous_state: str = None):
        self.current_state = current_state
        self.previous_state = previous_state

    def update_state(self, new_state: str):
        self.previous_state = self.current_state
        self.current_state = new_state

    def reset_state(self):
        self.previous_state = self.current_state
        self.current_state = "initial"  # or any default state you want to define

    def __repr__(self):
        return f"AgentState(current_state='{self.current_state}', previous_state='{self.previous_state}')"
