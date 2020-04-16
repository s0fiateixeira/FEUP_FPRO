#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:38:48 2018

@author: exame
"""

def genealogy(l):
    result = tuple([])
    first = tuple([])
    second = tuple([])
    third = tuple([])
    fourth = tuple([])
    for i in range(len(l)):
        if l[i][1] == "sibling":
            first = first.__add__(l[i])
        elif l[i][1] == "parent":
            second = second.__add__(l[i])
        elif l[i][1] == "cousin":
            third = third.__add__(l[i])
        elif l[i][1] == "grandparent":
            fourth = fourth.__add__(l[i])
    result = result.__add__(first)
    result = result.__add__(second)
    result = result.__add__(third)
    result = result.__add__(fourth)
    return(result)
    
    
#lista = ("maria", "parent"), ("matilde", "grandparent"),("geraldes", "grandparent"), ("carlos", "sibling"),("paulo", "sibling"), ("artur", "grandparent"),("pedro", "parent"), ("alfredo", "cousin"), ("carla", "cousin")
    
#lista = [("sofia", "sibling"), ("sara", "parent"), ("bernardo","parent")]

#print(genealogy(lista))



#Susana needs to build a genealogy tree of her family for her school homework. She has asked
#her family and written everything as a list of tuples, where each tuple is (name,
#relationship). The relationship is given as "sibling”, “parent”, “cousin” or “grandparent".
#For example:
#l=[("maria", "parent"), ("matilde", "grandparent"),
#("geraldes", "grandparent"), ("carlos", "sibling"),
#("paulo", "sibling"), ("artur", "grandparent"),
#("pedro", "parent"), ("alfredo", "cousin"), ("carla", "cousin")]
#Write a Python function genealogy(l) to help her order the family. The order is given by
#relationship using the following rule: sibling < parent < cousin < grandparent. When there is a
#draw, use the relative's name by ascending order.
#Save your program in the file genealogy.py inside the folder PE2.
#For example:
#● genealogy(l) (where l is the previous list) returns the list:
#[('carlos', 'sibling'), ('paulo', 'sibling'), ('maria',
#'parent'), ('pedro', 'parent'), ('alfredo', 'cousin'), ('carla',
#'cousin'), ('artur', 'grandparent'), ('geraldes', 'grandparent'),
#('matilde', 'grandparent')]
#● genealogy([("sofia", "sibling"), ("sara", "parent"), ("bernardo",
#"parent")]) returns the list:
#[('sofia', 'sibling'), ('bernardo', 'parent'), ('sara',
#'parent')]