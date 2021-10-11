import numpy as np
import math
class seawaterProps:
    def __init__(self, props):
        # Initialize a spiral-wound crossflow module with properties from the dict "props"
        self.properties = props

    def rho(self,props):
        T = props["Temperature"]
        P = props["Pressure"]
        P0 = 1
        S = 1.0
        s = S/1000

        # Psat = SW_Psat(props)/1E6
        # P0 = Psat

        P0 = 0.101325

        a = [9.9992293295E+02, 2.0341179217E-02,-6.1624591598E-03, 2.2614664708E-05,-4.6570659168E-08]
        b = [8.0200240891E+02,-2.0005183488E+00, 1.6771024982E-02,-3.0600536746E-05,-1.6132224742E-05]

        rho_w = a[0] + a[1]*T + a[2]*T**2 + a[3]*T**3 + a[4]*T**4
        D_rho = b[0]*s + b[1]*s*T + b[2]*s*T**2 + b[3]*s*T**3 + b[4]*s**2.*T**2;
        rho_sw_sharq   = rho_w + D_rho

        c = [ 5.0792E-04,-3.4168E-06, 5.6931E-08,-3.7263E-10, 1.4465E-12,-1.7058E-15,-1.3389E-06, 4.8603E-09,-6.8039E-13]
        d=[-1.1077e-06,5.5584e-09,-4.2539e-11,8.3702e-09]

        F_P = np.exp( (P-P0)*(c[0] + c[1]*T + c[2]*T**2 + c[3]*T**3 + c[4]*T**4 + c[5]*T**5 + S*(d[0] + d[1]*T + d[2]*T**2)) + 0.5*(P**2-P0**2)*(c[6] + c[7]*T + c[8]*T**3   + d[3]*S))

        return rho_sw_sharq*F_P

    def visc(self,props):
        return 1

    def diffusivity(self,props):
        return 1
        
    def rho(self,props):
        return 1

    def osmP(self,props):
        return 1

class dimLessNumbers:

    def __init__(self, props):
        # Initialize a spiral-wound crossflow module with properties from the dict "props"
        self.properties = props

    def reynolds(self,props):
        return 1
        
    def schmitt(self,props):
        return 1
    def sherwood(self,props):
        return 1
