import os
for root, dirs, files in os.walk("/Users/morrealed/Desktop/BK_seq_run1/prokka"):
    for file in files:
        if file.endswith(".faa"):
             print(os.path.join(root, file))
print "DONE"
