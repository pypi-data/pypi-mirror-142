# Installation

`pip install compwizard`

# Compounds.py documentation

This module creates virtual compounds either from a database or from user input.
The virtual compound object will contain its chemical and physical attributes.
A compound can be initialized either by entering the name of a compound exisitng in the current database or by manually passing the parameters.
Compounds created via the weights fractions of elements will have .mass and .chem attributes empty.
Database can be checked with the `Compounds.ListDatabase()` command.
<br>
To import the package in the project, use `import Elements`
The Compounds library is found within it. You can also use the following: `from Elements import Compounds`

---

#### compound.set_compound(_\*args,ctype=None,mode='by_atom',name='new_compound'_)
  Parameters:
  * **\*args: _compound setup, string or 2 lists_**
  <br>The name of compound from database or two lists containing: first, the ratios or weights of elements, second, the elements.
  * **ctype: _string, optional_**
  <br>The initialization mode 'custom' or None, None is default and stands for a compound from the database. 
  * **mode: _string, optional_**
  <br>The initialization type 'by_atom' or 'by_weight', 'by_atom' is default. This parameter should be defined if creating a 'custom' compound.
   * **name: _string, optional_**
  <br>Name of the new compound. Default is 'new_compound'. The name can be changed if desired by using the Compounds.give_name method.
  
  Example:
  ```python
  from Elements import Compounds
  new_compound = Compounds.compound()
  new_compound.set_compound([2,1],['H','O'],ctype='custom')
  nem_compound.set_compound([0.12,0.88],['H','O'],ctype='custom',mode='by_weight')
  new_compound.set_compound('water')
  ```
All compounds in the example will have the same properties.

---

#### make_mixture_of(_proportion, compounds_)
  Parameters:
  * **proportion: _list_**
  <br>The ratio which the compounds will be mixed, either in weight fraction or in parts.
  * **compounds: _list_**
  <br>List of compound objects.
  <br> **proportion** and **compounds** must have the same dimension.
  
  Example:
  ```python
  from Elements import Compounds
  compound1 = Compounds.compound()
  compound2 = Compounds.compound()
  compound1.set_compound('linoil')
  compound2.set_compound('TiWhite')
  new_compound = Compounds.max_mixture_of( [25, 75], [compound1, compound2] )
  ```
The compound created by the mixture function will be a mixture with 25% compound1 and 75% compound2.

---

#### compound.set_attenuation(_energy_)
  Parameters:
  * **energy: _string_ or _integer_**
  <br>The element the compound will be attenuating. _E.g._ if energy is set as 'Pb', it means the coeficients will be calculated for the attenuation of lead lines. If an integer is entered, the coefficients will be calculated for that one specific energy. It will still return a tuple, but with the second element equal to 0.
  
  Example:
  ```python
  mycompound = Compounds.compound()
  mycompound.set_compound('AuSheet')
  mycompound.set_attenuation('Pb')
  print(mycompound.lin_att,mycompound.tot_att)
  ```
  > (1912.6349060000002, 2833.4862456446012) (103.1, 152.73821000000004)
  
  (by now the method returns a tuple, it will be changed in the future to return a dictionary with the line names as keys and the coefficients)
  
---

#### compound.mix(_proportion,compounds_)
  Parameters:
  * **proportion: _list_**
  <br>The ratio which the compounds will be mixed, either in weight fraction or in parts. The first value always refers to the compound starting the mixture, i.e. the object where the method is being applied to.
  * **compounds: _list_**
  <br>List containing the compound(s) objects to be mixed together.
  
  Example:
  ```python
  water = Compounds.compound()
  water.set_compound('water')
  mycompound = Compounds.compound()
  mycompound.set_compound('Linoil')
  mixture = mycompound.mix([2,10],[water])
  print(mixture.weight)
  print(mixture.density)
  ```
  > {'H': 0.09166666666666667, 'O': 0.09166666666666667, 'C': 0.65}
  <br> 1.4756558333333334

---  

#### Attributes
```python
  water = Compounds.compound()
  water.set_compound('water')
```

* **.name**
  returns a string containing the name of the compound.
  ```python
  print(water.name)
  ```
  > 'water'
* **.mass**
  returns a float value with the atomic mass of the compound.
    ```python
  print(water.mass)
  ```
  > 18.02
* **.chem**
  returns a dictionary with the total atomic mass of each constituent chemical element.
  ```python
  print(water.chem)
  ```
  > {'H': 2.02, 'O': 16.0}
* **.density**
  return a float value with the total density of the compound
  ```python
  print(water.density)
  ```
  > 0.0009663706992230855
* **.weight**
  returns a dictionary with the weight fraction of each constituent chemical element in a similar way of .chem
  ```python
  print(water.weight)
  ```
  > {'H': 0.1120976692563818, 'O': 0.8879023307436182}
* **.origin**
  returns a string with the origin of the compound. Values are: 'by_weight', 'by_atom', 'by_mixing' or 'from_database'
  ```python
  print(water.origin)
  ```
  > from_database
* **.tot_att** and **.lin_att**
  each will return a tuple with the attenuation coefficients of a given element. .tot_att will return the total attenuation while .lin_att will returns the linear attenuation (the same as .tot_att multiplied by the compound's density).
  ```python
  water.set_attenuation('Cu')
  print(water.lin_att)
  print(water.tot_att)
  ```
  > (0.009849807036256424, 0.007272790368341503)
  <br>(10.192576248612653, 7.525880466148724)

  If an `int` is passed as the set_attenuation argument, the tuple's second index will be 0.
