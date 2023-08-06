__version__ = "0.1.0"
version = "0.1.0"
class RedWire:
  def __init__(self, token):
    if not token == "init":
      raise Exception("Use \"RedWire(\"init\")\" to start RedWire.")
  def test(): # This is only fired if you have started redwire
    print("RedWire is working!")
  class system:
    def __init__(self):
      pass
    def version():
      return "v" + version
    def close(status=0):
      exit(status)
  class main:
    def __init__(self):
      pass
    def post(out):
      print(out)
    def recieve(prompt):
      return input(prompt)
  class vars:
    def __init__(self):
      self.names = []
      self.vals = []
    def create(name, val=0):
      self.names.append(name)
      self.vals.append(val)
    def set(name, val=0):
      self.vals[self.names.index(name)] = val
    def get(name):
      return self.vals[self.names.index(name)]
    def delete(name):
      del self.vals[self.names.index(name)]
      del self.names[self.names.index(name)]
  class opers:
    def __init__(self):
      pass
    def add(a, b):
      return a + b
    def subtract(a, b):
      return a - b
    def multiply(a, b):
      return a * b
    def divide(a, b):
      return a / b
    def mod(a, b):
      return a % b
  class data:
    def __init__(self):
      pass
    def mean(*data): # *data is a list
      sum = 0
      length = len(data)
      for i in range(length):
        sum += data[i]
      return sum
    def range(*data):
      data = [int(x) for x in data]
      data = data.sort()
      return data[len(data)] - data[0]
    def median(*data):
      data = [int(x) for x in data]
      data = data.sort()
      if len(data) % 2 == 0:
        lower = data[(len(data) / 2) - 1]
        upper = data[(len(data) / 2)]
        median = (lower + upper) / 2
      else:
        median = data[((len(data) / 2) - 0.5) + 1]
      return median
    def mode(*data):
      from collections import Counter
      data = Counter(data)
      return [k for k, v in data.items() if v == data.most_common(1)[0][1]]
