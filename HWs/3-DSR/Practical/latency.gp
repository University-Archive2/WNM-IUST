#!/usr/bash
set ylabel 'Avg. Latency (msec)'
set xlabel 'Number of Nodes'
set output 'latency.eps'
set xrange [10:50]
set xtics 10
set yrange [0:]
set term post size 10,8 #8 inches by 6 inches
set term postscript eps enhanced color 'Times-Roman' 11
plot 'results_average' using 1:4:5 title 'Average Latency' with yerrorlines lt rgb '#1F0CA1' lw 5
