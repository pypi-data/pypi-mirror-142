#!/bin/bash
EPM=$1
set -e

cd Bu_poly1_mistag_single
$EPM calibrate.py |& tee calibrate.log
# $EPM write.py |& tee write.log
cd ..

cd Bd_poly1_mistag_single
$EPM calibrate.py |& tee calibrate.log
# $EPM write.py |& tee write.log
cd ..

cd Bs_poly1_mistag_single
$EPM calibrate.py |& tee calibrate.log
# $EPM write.py |& tee write.log
cd ..

cd combination_test
$EPM combine.py
cd ..
