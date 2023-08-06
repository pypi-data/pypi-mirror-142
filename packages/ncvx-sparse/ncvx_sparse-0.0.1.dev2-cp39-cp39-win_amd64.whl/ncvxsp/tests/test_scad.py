# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:58:19 2021

@author: Clément Lejeune (clement.lejeune@irit.fr; clementlej@gmail.com)
"""

from sklearn.utils.estimator_checks import check_estimator
from ncvxsp.linear_model import SCADnet, MultiTaskSCADnet

## test of SCADnet
scad_ratios = [0.01, 0.25, 0.5, 0.75, 1.] # scad_ratio=0. => User Warning
gam_vals = [2.0001, 3.7, 100.]

for ratio in scad_ratios:
    for gam in gam_vals:
        scad = SCADnet(scad_ratio=ratio, 
                                gam=gam)
        try:
            check_estimator(scad)
            print('\n Test passed with : ')
            print('scad_ratio={}'.format(ratio))
            print('gam={}'.format(gam))

        except:
            print('\n Issue with : ')
            print('scad_ratio={}'.format(ratio))
            print('gam={}'.format(gam))
# passes

## test of MultiTaskSCADnet
### SCAD(||w_i||_1, gam): l1-sparsity across tasks
scad_ratios = [0.01, 0.25, 0.5, 0.75, 1.] # scad_ratio=0. => User Warning
gam_vals = [2.0001, 3.7, 100.]

for ratio in scad_ratios:
    for gam in gam_vals:
        scad_mt_gl1 = MultiTaskSCADnet(scad_ratio=ratio, 
                                        gam=gam, 
                                        task_sparsity='group-l1')
        try:
            check_estimator(scad_mt_gl1)
            print('\n Test passed with : ')
            print('scad_ratio={}'.format(ratio))
            print('gam={}'.format(gam))

        except:
            print('\n Issue with : ')
            print('scad_ratio={}'.format(ratio))
            print('gam={}'.format(gam))
# passes

### SCAD(||w_i||_2, gam): l2-sparsity across tasks
scad_ratios = [0.01, 0.25, 0.5, 0.75, 1.] # scad_ratio=0. => User Warning
gam_vals = [2.0001, 3.7, 100.]

for ratio in scad_ratios:
    for gam in gam_vals:
        scad_mt_gl2 = MultiTaskSCADnet(scad_ratio=ratio, 
                                gam=gam, 
                                task_sparsity='group-l2')
        try:
            check_estimator(scad_mt_gl2)
            print('\n Test passed with : ')
            print('scad_ratio={}'.format(ratio))
            print('gam={}'.format(gam))
        except ValueError:
            print('\n Issue with : ')
            print('scad_ratio={}'.format(ratio))
            print('gam={}'.format(gam))

scad_mt_gl2 = MultiTaskSCADnet(scad_ratio=1., gam=2.000015, task_sparsity='group-l2')
check_estimator(scad_mt_gl2) # passes
# scad_ratio <= 1.0, => zero division in prox_l2, => nn=||tmp||_2=0.0; why ?
