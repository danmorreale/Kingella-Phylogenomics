#!/usr/bin/env bash
mkdir /Users/morrealed/Desktop/hiprokka
cd /Users/morrealed/Desktop/hifna
for file in *; do
  echo ""
  echo "Running PROKKA for $file."
  echo ""
  prokka --outdir  /Users/morrealed/Desktop/hiprokka/$file --addgenes --genus Haemophilus --species influenzae --kingdom Bacteria /Users/morrealed/Desktop/hifna/$file
  echo ""
  echo "Finished running PROKKA for $file."
  echo ""

done
