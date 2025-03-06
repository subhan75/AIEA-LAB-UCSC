class BackwardChaining:
    def __init__(self):
        # Define rules and facts as instance variables
        self.rules = {
            "diabetes": [["high_blood_sugar", "frequent_urination"], 
                         ["high_blood_sugar", "blurred_vision"], 
                         ["fatigue", "weight_loss"], 
                         ["hyperglycemia", "frequent_urination"]],
            "hyperglycemia": [["high_blood_sugar"]]
        }
        self.facts = {"high_blood_sugar", "frequent_urination", "blurred_vision"}

    def back_chain(self, goal, visited=None):
        # Reinitialize visited only if it's None, not at every recursive call
        if visited is None:
            visited = set()

        # If the goal is already a fact, return True
        if goal in self.facts:
            return True

        # If the goal has already been visited, return False to avoid loops
        if goal in visited:
            return False

        # Mark the goal as visited
        visited.add(goal)

        # If the goal is not in the rules, it cannot be derived
        if goal not in self.rules:
            return False

        # Get the premises for the goal
        premises_list = self.rules[goal]

        # Check each set of premises
        for premises in premises_list:
            # Assume all premises in this set are true
            all_premises_true = True

            # Check each premise in the set
            for premise in premises:
                if not self.back_chain(premise, visited):
                    all_premises_true = False
                    break

            # If all premises in this set are true, the goal is true
            if all_premises_true:
                return True

        # If no set of premises is satisfied, the goal is false
        return False

# Create an instance of the BackwardChaining class
instance = BackwardChaining()

# Define the goal
goal = "diabetes"

# Call the back_chain method
result = instance.back_chain(goal)

# Print the result
print(f"Does the patient have {goal}? {result}")