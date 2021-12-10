from systems import *

treatment_train = System()

treatment_train.add(
    UF(
    module='hollow_fiber', 
    models=['surrogate']), 
    loc='main')

treatment_train.add(FO(module='cross_flow', models=['physics']), loc='main')
treatment_train.add(RO(module='cross_flow', models=['ROSA']), loc='main')
treatment_train.add(MD(module='counter_current', models=['physics']), loc='waste')
treatment_train.add(UV(module='reactor', models='surrogate'), loc='main')

treatment_train.simulate()
treatment_train.report()
