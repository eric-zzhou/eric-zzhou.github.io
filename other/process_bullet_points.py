s = """
Explored evolutionary reinforcement learning, an advanced fusion of genetic algorithms and machine learning (ML). Genetic algorithms, inspired by biological evolution, were employed to generate randomized populations, selectively refining individuals based on heuristic evaluation for subsequent generations. ML models, particularly neural networks, allowed for complex decision-making processes.
 • Leveraged the NEAT library to orchestrate the training of AI bots for complex games, including Flappy Bird, Pong, and 2048
 • Delved into academic research papers pertaining to genetic programming and reinforcement learning, acquiring an in-depth understanding of fundamental principles
 • Applied the min-max algorithm and conducted comprehensive heuristic explorations across various gaming scenarios
"""

lines = s.split("\n")
for line in lines:
    line = line.replace("•", "").strip()
    if line:
        print("<li>" + line + "</li>")
