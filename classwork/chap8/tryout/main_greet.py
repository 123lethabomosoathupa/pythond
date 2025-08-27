
# 1. Import the whole module
import greetings
greetings.greet("Alice")

# 2. Import the function directly
from greetings import greet
greet("Bob")

# 3. Import the function with an alias
from greetings import greet as gn
gn("Charlie")

# 4. Import the module with an alias
import greetings as gr
gr.greet("Diana")

# 5. Import everything from the module (not recommended for big programs)
from greetings import *
greet("Eve")
