#!/bin/bash

dir=$(pwd)
for i in 16.0 16.5 17.0 17.5 18.0 18.5 19.0 19.5 20.0 20.5 21.0 21.5 22.0; do
	cp continue.py submit_data_calc.sh ${i}_ell
	cd ${i}_ell
	sed -i "s/21.0/$i/g" submit_data_calc.sh
	sbatch submit_data_calc.sh
	cd $dir
done	
