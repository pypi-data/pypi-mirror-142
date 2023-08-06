def test_mypackage():
    print('Inside mypackage')
def say_hello(name=None):
  if name is None:
    return "HelloVVV, World!"
  else:
    return f"Hello, {name}!"