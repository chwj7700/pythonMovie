class Singleton(object):
  __instance = None
  
  def __new__(cls):
    if not isinstance(cls.__instance, cls):
      cls.__instance = super(Singleton, cls).__new__(cls)
    return cls.__instance