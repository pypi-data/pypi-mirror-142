#!/bin/bash

function resetFolder {

    for FILETYPE in "*.tex" "*.png" "*.pdf" "*.csv" "*.xml" "EspressoCalibrations.py" "*.root" "output.root" "EspressoHistograms.root" "*.log"; do
        find $1 -name $FILETYPE -type f -exec rm -v {} \;;
    done

}

resetFolder ./Bd_poly1_mistag_single
resetFolder ./Bu_poly1_mistag_single
resetFolder ./Bs_poly1_mistag_single
resetFolder ./combination_test
