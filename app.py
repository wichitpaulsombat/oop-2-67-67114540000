class Student(object):
  student_count = 0

  def __new__(self):
    print('Student.__new__')

  def __init__(self):
    print('Student.__init__')
    self.gpa = 4.0

  def study_hard(self):
    print('Sir, yes sir.')
  
