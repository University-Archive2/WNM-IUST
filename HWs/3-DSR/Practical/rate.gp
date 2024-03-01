#!/usr/bash
set ylabel 'Avg. Rate'
set xlabel 'Number of Nodes'
set output 'rate.eps'
set yrange [0.6:0.9]
set xtics 10
set term post size 10,8 #8 inches by 6 inches
set term postscript eps enhanced color 'Times-Roman' 11
plot 'results_average' using 1:2:3 title 'Average Rate' with yerrorlines lt rgb '#1F0CA1' lw 5
