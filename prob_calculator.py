import copy
import random
# Consider using the modules imported above.
class Hat:
  def __init__(self, **balls):
      self.contents=[]
      for key, value in balls.items():
          self.contents+=[key]*value
  
  def draw(self, draw_balls):
      remball=[]
      if draw_balls > len(self.contents)-1:
          return self.contents
      else:
          c=len(self.contents)-1
          temp=0
          while draw_balls>0:
              temp=random.randint(0,c)
              remball.append(self.contents.pop(temp))
              draw_balls=draw_balls-1
              c= c-1
          #print(remball)
          return remball
  
  def affiche(self):
      print(self.contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  ori_list=hat.contents.copy()
  #print("liste copié"+str(ori_list))
  succes=0
  total=num_experiments
  while num_experiments >0:
      a=hat.draw(num_balls_drawn) #int 5 retourn , [color, color]
      b=0
      for key, value in expected_balls.items(): #{"red":2,"green":1}
          if a.count(key)>=value:
              b+=1
      if b==len(expected_balls.keys()):
          succes+=1
      num_experiments=num_experiments-1
      hat.contents=ori_list.copy()
      #print("list actuel"+str(hat.balls))
      #print("liste copié"+str(ori_list))
  return succes/total
