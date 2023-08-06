#################################################################
#                                                               #
#          Compounds (Compounds handler)                        #
#                                                               #
# @author: Sergio Lins               sergio.lins@roma3.infn.it  #
#################################################################

import numpy as np
from . import EnergyLib
import logging
logger = logging.getLogger("logfile")
try:
    import xraylib as xlib
    #xlib.SetErrorMessages(0) #deprecated in xraylib
    logger.info("Xraylib sucessfully imported in Compounds")
except:
    logger.warning("FAILED TO LOAD XRAYLIB MODULE\nCompounds library will not work!")
    class mock():
        def __init__(__self__):
            __self__.value = 0
        def CS_Total(__self__,Z,energy):
            return __self__.value

    xlib = mock()
        

CompoundList = {
        'Air'           :{'O':2,'N':2,},
        'Azurite'       :{'Cu':3,'C':2,'O':8,'H':2},
        'AuSheet'       :{'Au':9,'Ag':1},
        'CoBlue'        :{'Co':1,'Al':2,'O':4},
        'Cuprite'       :{'Cu':2,'O':1},
        'Ethanol'       :{'C':2,'H':6,'O':1},
        'PbWhite'       :{'Pb':3,'O':4,'C':1,'H':2},
        'PbCarbonate'   :{'Pb':1,'C':1,'O':3},
        'PureAu'        :{'Au':1},
        'PureCu'        :{'Cu':1},
        'Tenorite'      :{'Cu':1,'O':1},
        'TiWhite'       :{'Ti':1,'O':2},
        'Vermilion'     :{'Hg':1,'S':1},
        'Water'         :{'H':2,'O':1},
        'ZnWhite'       :{'Zn':1,'O':1},
        }

WeightList = {
        'Au24'          :{'Au':0.999,'Ag':0.001},
        'AuAg23.5'      :{'Au':0.985,'Ag':0.015},
        'AuCu23.5'      :{'Au':0.985,'Cu':0.015},
        'FibulaGold'    :{'Au':0.88,'Hg':0.12},
        'Tumbaga'       :{'Au':0.12,'Ag':0.16,'Cu':0.72},
        'SardinianCu'   :{'Cu':0.90,'Sn':0.081,'Pb':0.019},
        'LinOil'        :{'C':0.78,'O':0.11,'H':0.11},
        'OceanBlue'     :{'H':0.0413,'C':0.2925,'O':0.2674,'Al':0.1907,'Co':0.2082},
        'PbWhitePrimer' :{'Pb':0.6612,'O':0.1722,'C':0.1328,'H':0.0163,'Ca':0.0174}, \
                # After Favaro, 2010 and Gonzalez, 2015
        }

def ListDatabase():
    """ Prints all compounds on database """

    Database = dict(CompoundList,**WeightList)
    return Database


def make_mixutre_of(proportion, compounds):
    """ Mixes any number of compounds according to the porpoorstions passed.
    
    -------------------------------------------------------------------------------

    INPUT:
        proportion; 1D float or integer list
        compounds; 1D compound class objects list 
    OUTPUT:
        mixture; compound class object """
    
    if len( proportion ) != len( compounds ):
        raise ValueError(f"Input lists must have same dimension! Got {len(proportion)} and {len(compounds)}")

    sum_of_ratios = sum(proportion)
    if sum_of_ratios > 1:
        for index in range (len(proportion)): 
            proportion[index] = proportion[index] / sum_of_ratios

    mixture = compound()
    for i in range( len( proportion ) ):
        for key in compounds[i].weight:
            if key not in mixture.weight:
                mixture.weight[key] = 0
        for key in compounds[i].weight:
            mixture.weight[key] += compounds[i].weight[key] * proportion[i]

    mixture.give_density()
    mixture.mass = None
    mixture.chem = None
    
    name_list = []
    for ingredient in compounds:
        name_list.append(ingredient.name)
    mixture.origin = {'Mode':'by_mixing','Proportion':proportion,'Origin':name_list}
    names = ""
    for name in name_list: names = names + "" + name
    mixture.name = names 
    return mixture


class compound:
    """ Methods:
    set_compound(*args, ctype=None, mode="by_atom", name="new_compound")
    set_attenuation(energy)
    mix(proportion, compounds)
    Attributes: name, mass, chem, density, weight, origin, tot_att, lin_att """

    def __init__(__self__):
        __self__.chem = {}
        __self__.mass = 0
        __self__.density = 0
        __self__.weight = {}
        __self__.name = "new_compound"
        __self__.identity = " "
    
    def set_compound(__self__,*args,ctype=None,mode='by_atom',name='new_compound'):
        """ Creates the compound according to input. The compound can be created
        manually or from the database; from a weights fraction list or atom count list.
        
        -------------------------------------------------------------------------------

        INPUT:
            *args; compound setup, string or 2 same-sized lists
            ctype; string (optional)
            mode; string (optional)
            name; string (optional) """

        if ctype == 'custom' and mode == 'by_atom':
            for atom in range(len(args[0])):
                if args[0][atom] < 1: raise ValueError("Can't compute fraction of atom!")
            __self__.create_compound(args[0],args[1])
            __self__.origin = 'by_atom'
        elif ctype == 'custom' and mode == 'by_weight':
            if sum(args[0]) > 1: raise ValueError("Sum of weights exceeds 1!")
            __self__.create_compound_by_weight(args[0],args[1])
        else:
            try: __self__.set_from_database(args[0])
            except: 
                try: __self__.set_from_w_database(args[0])
                except: raise ValueError("{} not found in database".format(args[0]))
        pass
        if ctype == None: name = args[0]
        __self__.give_name(name)

    def reset(__self__):
        __self__.chem = {}
        __self__.mass = 0
        __self__.density = 0
        __self__.weight = {}
        __self__.name = "new_compound"
        __self__.identity = " "
        __self__.tot_att = (0, 0) 
        __self__.lin_att = (0, 0)

    def create_compound(__self__,atoms,elements):
        """ Sets the compound attributes with a 2 list input, mode='by_atom'.
        
        ---------------------------------------------------------------------

        INPUT:
            atoms; 1D int list
            elements; 1D string list """

        __self__.chem = {\
                "{0}".format(elements[i]):(EnergyLib.AtomWeight[elements[i]]*atoms[i])\
                for i in range(len(atoms))}
        mass = __self__.total_mass()
        __self__.weightpercent()
        __self__.give_density()
    
    def create_compound_by_weight(__self__, ratios, elements):
        """ Sets the compound attributes with a 2 list input, mode='by_weight'.

        -----------------------------------------------------------------------

        INPUT:
            atoms; 1D float list
            elements; 1D string list """

        if len(ratios) == len(elements):
            __self__.weight = {"{0}".format(elements[i]):ratios[i] for i in range(len(ratios))}
            for key in __self__.weight:
                if __self__.weight[key] > 1:
                    raise ValueError("Sum of weights larger than 100%! {}".format(ratios))
                    break
            __self__.give_density()
            __self__.mass = None
            __self__.chem = None
            __self__.origin = 'by_weight'
        else: raise ValueError('{0} and {1} have different lenghts'.format(ratios,elements))

    def set_from_database(__self__,name_of_compound):
        """ Sets the compound attributes from database """

        elements = [element for element in CompoundList[name_of_compound]]
        atoms = [CompoundList[name_of_compound][atom] for atom in elements]
        __self__.chem = {"{0}".format(\
                elements[i]):(EnergyLib.AtomWeight[elements[i]]*atoms[i])\
                for i in range(len(atoms))}
        mass = __self__.total_mass()
        __self__.weightpercent()
        __self__.give_density()
        __self__.origin = 'from_database'
        __self__.name = name_of_compound
    
    def set_from_w_database(__self__,name_of_compound):
        """ Sets the compound attributes from database """
        
        elements = [element for element in WeightList[name_of_compound]]
        ratios = []
        for element in WeightList[name_of_compound]:
            ratios.append(WeightList[name_of_compound][element])
        __self__.weight = {"{0}".format(elements[i]):ratios[i] for i in range(len(ratios))}
        __self__.chem = None
        __self__.mass = None
        __self__.give_density()
        __self__.origin = 'from_weight_database'
        __self__.name = name_of_compound
    
    def weightpercent(__self__):
        """ Sets the weight fraction attribute. This is needed in order to calculate
        the compound density. A compound will always have a weight attribute. """

        for element in __self__.chem:
            __self__.weight[element] = __self__.chem[element]/__self__.mass 
         
    def total_mass(__self__):
        """ Calculates the compound total mass """

        total_mass = 0
        for element in __self__.chem:
            total_mass += __self__.chem[element]
        __self__.mass = total_mass
        return total_mass
    
    def give_density(__self__):
        """ Calculates the compound density according to weight fraction """

        identityWeight = 0
        identityElement = " "
        try:
            for element in __self__.weight:
                if __self__.weight[element] > identityWeight:
                    identityWeight = __self__.weight[element]
                    identityElement = element
                __self__.density += __self__.weight[element]*EnergyLib.DensityDict[element]
            __self__.identity = identityElement
        except:
            raise ValueError("{} has no property weight!".format(__self__))
        return

    def mix(__self__, proportion, compounds):
        """ Mixes two compound class objects proportionally. This resets the attributes
        according to the mixing outcomes.
        
        -------------------------------------------------------------------------------

        INPUT:
            proportion; 1D float list
            compounds; 1D compound class objects list 
        OUTPUT:
            mixture; compound class object """
        
        sum_of_ratios = sum(proportion)
        if sum_of_ratios > 1:
            for index in range (len(proportion)): 
                proportion[index] = proportion[index] / sum_of_ratios

        mixture = compound()
        for i in range( len( proportion ) ):
            for key in compounds[i].weight:
                if key not in mixture.weight:
                    mixture.weight[key] = 0
            for key in compounds[i].weight:
                mixture.weight[key] += compounds[i].weight[key] * proportion[i]

        mixture.give_density()
        mixture.mass = None
        mixture.chem = None
        
        name_list = []
        for ingredient in compounds:
            name_list.append(ingredient.name)
        mixture.origin = \
                {'Mode':'by_mixing','Proportion':proportion,'Origin':name_list}
        names = ""
        for name in name_list: names = names + "" + name
        mixture.name = names 
         
        return mixture

    def set_attenuation(__self__,energy):
        """ Sets the linear and total attenuation coefficients according to input.
        Values are taken from xraylib (Brunetti et al., 2004), which is constantly
        updated.

        --------------------------------------------------------------------------

        INPUT:
            energy; int or string """

        mu1_w ,mu2_w = 0,0
        if type(energy) == int:
            for element in __self__.weight:
                ele_no = EnergyLib.Element_No[element]
                #print(ele_no, element)
                mu1 = xlib.CS_Total(ele_no,energy)
                mu2 = 0
                mu1_w += mu1*__self__.weight[element]
                mu2_w += mu2*__self__.weight[element]
        else:
            for element in __self__.weight:
                attenuated_no = EnergyLib.Element_No[energy]
                ele_no = EnergyLib.Element_No[element]
                attenergy_a = EnergyLib.Energies[attenuated_no]
                attenergy_b = EnergyLib.kbEnergies[attenuated_no]
                mu1,mu2 = xlib.CS_Total(ele_no,attenergy_a),xlib.CS_Total(ele_no,attenergy_b)
                mu1_w += mu1*__self__.weight[element]
                mu2_w += mu2*__self__.weight[element]
        __self__.tot_att = (mu1_w,mu2_w) 
        __self__.lin_att = (__self__.density * mu1_w , __self__.density * mu2_w)
    
    def give_name(__self__,a_string):
        """ Attributes a string to compound class object name attribute """

        __self__.name = a_string


if __name__.endswith('__main__'):         
    ListDatabase()