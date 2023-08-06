__version__ = '1.1.0'
version = "1.1.0"
class Cut:
  def __init__(self, keyword) -> None:
    if keyword == "init": # Cut has to be initialized to work
      pass
    else: # It wasn't
      raise Exception("Cut must be initialized with \"cut = Cut(\"init\")\"")
  def test():
    print("Cut is working!")
  class system: # System "module" (e.x. cut.system.version())
    def __init__(self) -> None:
      pass
    def version():
      return "v" + version
  class main: # Main "module" (e.x. cut.main.spit())
    def __init__(self) -> None:
      pass
    def spit(out):
      print(out)
    def steal(prompt):
      return input(prompt)
  class vars: # Vars "module" (e.x. cut.vars.create())
    def __init__(self) -> None:
      self.names = []
      self.vals = []
    def create(name, val=0):
      self.names.append(name)
      self.vals.append(val)
    def get(name):
      return self.vals[self.names.index(name)]
    def set(name, val):
      if not name in self.names:
        raise SyntaxError(f"{name} variable does not exist.")
      else:
        self.vals[self.names.index(name)] = val
    def delete(name):
      del self.vals[self.names.index(name)]
      del self.names[self.names.index(name)]
  class opers: # Opers "module" (e.x. cut.opers.add())
    def __init__(self) -> None:
      pass
    def add(a, b):
      return a + b
    def subtract(a, b):
      return a - b
    def multiply(a, b):
      return a * b
    def divide(a, b, mode):
      if mode == "float":
        return a / b
      elif mode == "int":
        return a // b
  class data: # Data "module" (e.x. cut.data.mean())
    def mode(*data):
      from numpy import mode as m
      return m(data)
    def median(*data):
      from numpy import median as m
      return m(data)
    def mean(*data):
      from numpy import mean as m
      return m(data)