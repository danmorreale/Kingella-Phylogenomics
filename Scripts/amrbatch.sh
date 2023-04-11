for file in *
do
  amrfinder -n $file -o /Users/morrealed/Desktop/AMR/AMRfinder/prot_out/$file
  echo "Finished:$file"


print "DONE"

done
