'''
A base class representing an abstract Environment.
'Real' Environment classes must inherit from this one.
The environment keeps a list of .agents.
Each agent has a .performance slot, initialized to 0.
'''

from src.agentClass import Agent

class Environment:
  def __init__(self):
    self.agents = []

  def percept(self, agent):
    #Return the percept that the agent sees at this point. (Implement this in derived classes)
    print("I don't know how to percept.")

  def execute_action(self, agent, action):
    #Change the world to reflect this action. (Implement this in derived classes)
    print("I don't know how to execute_action.")

  def default_location(self, thing):
    #Default location to place a new thing with unspecified location.
    return None

  def is_done(self):
    #By default, we're done when we can't find a live agent.
    
    return not any(agent.is_alive() for agent in self.agents)

  def step(self):
        #Run the environment for one time step.
        if not self.is_done():
            actions = []
            for agent in self.agents:
                if agent.alive:
                    #print(self.percept(agent))
                    action=agent.program(self.percept(agent))
                    print("Agent percepted {}.".format(self.percept(agent)))
                    print("Agent decided to do {}.".format(action))
                    actions.append(action)
                else:
                    print("Agent {} is dead.".format(agent))
                    actions.append("")
            for (agent, action) in zip(self.agents, actions):
                self.execute_action(agent, action)
        else:
          print("There is no one here who could work...")
        return actions

  def run(self, steps=10):
        #Run the Environment for given number of time steps.
        for step in range(steps):
            if self.is_done():
                print("We can't find a live agent")
                return
            print("step {0}:".format(step+1))
            self.step()

  def add_thing(self, thing, location=None):
    #from agentClass import Agent
    if thing in self.agents:
      print("Can't add the same agent twice")
    else:
      if isinstance(thing, Agent):
        thing.performance = 0
        thing.location = location if location is not None else self.default_location(thing)
        self.agents.append(thing)

  def delete_thing(self, thing):
    if thing in self.agents:
      self.agents.remove(thing)
