import os
from crewai import Agent, Task, Crew, Process, LLM

# Use CrewAI's native LLM wrapper to avoid OpenAI fallback.
llm = LLM(
     model="ollama/gemma3:4b",
     base_url="http://localhost:11434",
     temperature=0.1,
)



add_agent = Agent(role='Addition Agent', 
                  goal='Create merge ready addition script',
                  description='Write add() function + test the functionalities with edge cases',
                  backstory='Expert programmer who outputs only code, no explanations.',
                  llm=llm,
                  verbose=True,
                  allow_delegation=False)

sub_agent = Agent(role='Subtraction Agent', 
                  goal='Create merge ready subtraction script',
                  description='Write subtract() function + test the functionalities with edge cases',
                  backstory='Expert programmer who outputs only code, no explanations.',
                  llm=llm,
                  verbose=True,
                  allow_delegation=False)

mul_agent = Agent(role='Multiplication Agent', 
                  goal='Create merge ready multiplication script',
                  description='Write multiply() function + test the functionalities with edge cases',
                  backstory='Expert programmer who outputs only code, no explanations.',
                  llm=llm,
                  verbose=True,
                  allow_delegation=False)

div_agent = Agent(role='Division Agent', 
                  goal='Create merge ready division script',
                  description='Write divide() function + test the functionalities with edge cases',
                  backstory='Expert programmer who outputs only code, no explanations.',
                  llm=llm,
                  verbose=True,
                    allow_delegation=False)

orchestrator = Agent(role='File Writer Agent',
                     goal='Gather outputs and produce the final Python file content',
                     description='''Collect outputs from the specialist agents and return the full
                     final_calculator.py contents as plain Python (no markdown).''',
                     backstory='Expert in consolidating agent outputs into a clean Python file.',
                     llm=llm,
                     verbose=True,
                     allow_delegation=False)


add_task = Task(description='''Create addition script which takes 2 number and returns the sum. 
              Test cases should include positive, negative and zero values. 
              handle edge cases wisely, user may not be educated to provide only integers.''', 
              expected_output='Python add() function with complete test cases', 
              agent=add_agent)
sub_task = Task(description='''Create subtraction script which takes 2 number and returns the difference. 
              Test cases should include positive, negative and zero values. 
              handle edge cases wisely, user may not be educated to provide only integers.''', 
              expected_output='Python subtract() function with complete test cases', 
              agent=sub_agent)
mul_task = Task(description='''Create multiplication script which takes 2 number and returns the product. 
              Test cases should include positive, negative and zero values. 
              handle edge cases wisely, user may not be educated to provide only integers.''', 
              expected_output='Python multiply() function with complete test cases', 
              agent=mul_agent)
div_task = Task(description='''Create division script which takes 2 number and returns the quotient. 
              Test cases should include positive, negative and zero values. 
              handle edge cases wisely, user may not be educated to provide only integers.''', 
              expected_output='Python divide() function with complete test cases', 
              agent=div_agent)
write_task = Task(description='''Combine the outputs from prior tasks into a single Python file.
       The file must include all 4 functions and an interactive menu. and complete below todo list
       1. Respond ONLY with valid Python source code (no markdown fences).
       2. If in case there is no menu, create a simple one that allows users to select the operation and input numbers.
       3. Make sure the python file is getting executed without any errors if not fix it until it has no errors.
       Do not write python fences or other backticks. only a raw python content''', 
            expected_output='Complete Python source for final_calculator.py',
            agent=orchestrator,
            output_file=r"final_calculator.py",
            context=[add_task, sub_task, mul_task, div_task])

tasks = [add_task, sub_task, mul_task, div_task, write_task]

crew = Crew(name='Calculator Crew', agents=[add_agent, sub_agent, mul_agent, div_agent, orchestrator],
            tasks=tasks,
            process=Process.sequential,
            verbose=True,
            tracing=True
            )

if __name__ == "__main__":
    print("Starting the Calculator Crew...")
    print("Crew members:", [agent.role for agent in crew.agents])
    print("Process type:", crew.process)
    result = crew.kickoff()