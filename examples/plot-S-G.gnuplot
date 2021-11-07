# Reset all previously set options
reset
set datafile separator " "
set terminal png size 800,600 enhanced font "Helvetica,20"

# Filename of the data
#filename='/home/steven/Project/ns-3/src/lorawan/examples/results.dat'
set output "SGplot.png"

# Set linestyle 1 to blue (#0060ad)
set style line 1 \
    linecolor rgb '#0060ad' \
    linetype 1 linewidth 2 \
    pointtype 7 pointsize 1.5

set xrange [0:2.0]
set yrange [0:0.2]
plot 'results.dat' using 1:2 with lines
# Plot the data
#plot filename using 1:2:3 notitle with points pt 2 palette