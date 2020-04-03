# -*- coding: utf-8 -*-
"""

@author: Djibo648
"""


eleves = {}

def personne_elue(name):
    return name == 'Zoureni'

from collections import deque

eleves["Boris"]=["Amir","Franck","Nathalie","Bertrand"]
eleves["Amir"]=[]
eleves["Franck"]=[]
eleves["Nathalie"]=[]
eleves["Bertrand"]=["Erna","Hassana","Abdelkrim"]
eleves["Erna"]=[]
eleves["Hassana"]=[]
eleves["Zoureni"]=["Sekou","Auriane","Corlings"]
eleves["Sekou"]=[]
eleves["Auriane"]=[]
eleves["Corlings"]=[]
eleves["Abdelkrim"]=["Souleyman","Zack","Zoureni"]
eleves["Souleyman"]=[]
eleves["Zack"]=[]

def search(name):
     visitees = []
     search_queue = deque()
     search_queue += eleves[name]
     print( len(eleves.values()) )
     while search_queue:
        personne = search_queue.popleft()
        if not personne in visitees:
           if personne_elue(personne):
              print(personne + " a le fameux Mac")
              return True
        search_queue += eleves[personne]
        visitees.append(personne)
     return False

      

if __name__== "__main__":
  search("Boris")


