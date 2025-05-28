import unittest
import sys
import os

# Adjust path to import DeciderAgent from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.decider_agent import DeciderAgent

class TestDeciderAgent(unittest.TestCase):
    def setUp(self):
        self.agent = DeciderAgent()

    def test_decide_maths(self):
        self.assertEqual(self.agent.decide_subject("Tell me about algebra"), "maths")
        self.assertEqual(self.agent.decide_subject("What is a prime NUMBER?"), "maths")
        self.assertEqual(self.agent.decide_subject("Explain calculus concepts."), "maths")

    def test_decide_physics(self):
        self.assertEqual(self.agent.decide_subject("What is newton's law of motion?"), "physics")
        self.assertEqual(self.agent.decide_subject("Explain ENERGY and work."), "physics")
        self.assertEqual(self.agent.decide_subject("Tell me about GRAVITY"), "physics")

    def test_decide_chemistry(self):
        self.assertEqual(self.agent.decide_subject("What is a MOLECULE?"), "chemistry")
        self.assertEqual(self.agent.decide_subject("Explain chemical reactions."), "chemistry")
        self.assertEqual(self.agent.decide_subject("Tell me about the periodic table of ELEMENTs."), "chemistry")

    def test_decide_biology(self):
        self.assertEqual(self.agent.decide_subject("Describe the structure of a CELL."), "biology")
        self.assertEqual(self.agent.decide_subject("What is DNA?"), "biology")
        self.assertEqual(self.agent.decide_subject("Explain the theory of EVOLUTION."), "biology")
        self.assertEqual(self.agent.decide_subject("Tell me about plant life cycle."), "biology")


    def test_decide_history(self):
        self.assertEqual(self.agent.decide_subject("Tell me about World War II events."), "history")
        self.assertEqual(self.agent.decide_subject("What happened in ancient Rome?"), "history")
        self.assertEqual(self.agent.decide_subject("Discuss the major PAST events."), "history")

    def test_decide_geography(self):
        self.assertEqual(self.agent.decide_subject("What is the capital of France? It's about a country."), "geography")
        self.assertEqual(self.agent.decide_subject("Explain how maps are made."), "geography")
        self.assertEqual(self.agent.decide_subject("Tell me about the Earth's tectonic plates."), "geography")
        self.assertEqual(self.agent.decide_subject("Which region is known for coffee production?"), "geography")

    def test_decide_economics(self):
        self.assertEqual(self.agent.decide_subject("What is market demand and supply?"), "economics")
        self.assertEqual(self.agent.decide_subject("Explain the concept of trade."), "economics")
        self.assertEqual(self.agent.decide_subject("Tell me about finance and money management."), "economics")

    def test_decide_unknown(self):
        self.assertEqual(self.agent.decide_subject("Tell me a fun fact."), "unknown")
        self.assertEqual(self.agent.decide_subject("What's the weather like?"), "unknown")
        self.assertEqual(self.agent.decide_subject("This prompt has no specific keywords."), "unknown")
        self.assertEqual(self.agent.decide_subject(""), "unknown") # Empty prompt

if __name__ == '__main__':
    unittest.main()
