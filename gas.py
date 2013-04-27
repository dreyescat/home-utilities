#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

M3_KWH = 11.763
KWH_EURO = 0.05750871
KWH_FEE = 0.00234
IVA = 0.21 

if len(sys.argv) == 2:
    m3 = float(sys.argv[1])
    kwh = m3 * M3_KWH
    gas_consumption = kwh * KWH_EURO
    hydrocarbon_tax = kwh * KWH_FEE
    iva = (gas_consumption + hydrocarbon_tax) * IVA
    total = gas_consumption + hydrocarbon_tax + iva 
    print 'Gas consumption ' + str(kwh) + '\n' + \
        '\tGas consumption ' + str(gas_consumption) + '\n' + \
        '\tHydrocarbon tax ' + str(hydrocarbon_tax) + '\n' + \
        '\tIVA ' + str(iva) + '\n' + \
        '\tTotal ' + str(total) + '\n'
else:
    print 'Command:\n', sys.argv[0], ' <m3>' 
