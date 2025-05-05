class TuringMachine:
    def __init__(self, tape):
        """
        Initializes the Turing Machine with a given input tape.

        Parameters:
        tape (str): The input string containing 'a', 'b', and 'a' in the required format.

        Attributes:
        self.tape (list): A list representation of the tape with an added blank symbol ('$') at the end.
        self.head (int): Position of the tape head.
        self.state (str): Current state of the Turing Machine.
        self.transitions (dict): Dictionary containing transition rules.
        """
        self.tape = list(tape) + ["$"]  # Add blank symbol at the end
        self.head = 0  # Tape head starts at position 0
        self.state = "Q0"  # Initial state

        # TODO 1: Define all the transitions for the Turing Machine.
        # The transition table follows this format:
        # (Current State, Current Tape Symbol) → (Next State, New Tape Symbol, Move Direction)
        # State Q0 is done for you as an example.
        self.transitions = {
            # State Q0
            ("Q0", "a"): ("Q1", "X", "R"),
            ("Q0", "b"): ("Q4", "b", "R"),
            ("Q1", "a"): ("Q1", "a", "R"),
            ("Q1", "b"): ("Q2", "b", "R"),
            ("Q2", "b"): ("Q2", "b", "R"),
            ("Q2", "Z"): ("Q2", "Z", "R"),
            ("Q2", "a"): ("Q3", "Z", "L"),
            ("Q3", "b"): ("Q3", "b", "L"),
            ("Q3", "a"): ("Q3", "a", "L"),
            ("Q3", "Z"): ("Q3", "Z", "L"),
            ("Q3", "X"): ("Q0", "X", "R"),
            ("Q4", "b"): ("Q5", "b", "L"),
            ("Q4", "Z"): ("Q5", "Z", "L"),
            ("Q5", "b"): ("Q6", "Y", "R"),
            ("Q5", "Z"): ("Q8", "Z", "R"),
            ("Q6", "b"): ("Q6", "b", "R"),
            ("Q6", "Z"): ("Q6", "Z", "R"),
            ("Q6", "a"): ("Q7", "Z", "L"),
            ("Q7", "b"): ("Q7", "b", "L"),
            ("Q7", "Z"): ("Q7", "Z", "L"),
            ("Q7", "Y"): ("Q5", "Y", "R"),
            ("Q8", "Z"): ("Q8", "Z", "R"),
            ("Q8", "$"): ("ha", "$", "L")
        }

    def move(self):
        """
        Simulates the Turing Machine execution.

        The machine moves according to its transition rules until it reaches an accepting ("ha")
        or rejecting state.

        Returns:
        str: "Accepted" if the input belongs to the language, "Rejected" otherwise.
        """
        while self.state != "ha":  # ha is the accepting state
            # TODO 2: Read the current symbol at the tape head
            symbol = self.tape[self.head]

            if (self.state, symbol) in self.transitions:
                # TODO 3: Fetch the next state, replacement symbol, and movement direction
                next_state, new_symbol, direction = self.transitions[(
                    self.state, symbol)]
                # TODO 4: Update the tape by replacing the current symbol with the new symbol
                self.tape[self.head] = new_symbol
                # TODO 5: Move the tape head in the correct direction
                if direction == 'R':
                    self.head += 1
                elif direction == 'L':
                    self.head -= 1
                    if self.head < 0:
                        return "Rejected"

                # TODO 6: Update the turing machine state
                self.state = next_state
            else:
                # TODO 7: If there is no valid transition

                return "Rejected"

        # TODO 7: If the machine reaches the accepting state
        return "Accepted"


Input = input()

tm = TuringMachine("abaa")
result = tm.move()
print(result)
