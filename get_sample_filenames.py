import os
import glob

# fastq_R1 = sorted(glob.glob(run_folder + "/COVID*_R1*.fastq.gz"))
# fastq_R2 = sorted(glob.glob(run_folder + "/COVID*_R2*.fastq.gz"))
fastq_R1 = sorted(glob.glob("COVID*_R1*.fastq.gz"))
fastq_R2 = sorted(glob.glob("COVID*_R2*.fastq.gz"))

# filenames_file = open(os.path.join(run_folder, "filenames_list.csv"), 'w')
filenames_file = open("filenames_list.csv"), 'w')

for R1, R2 in zip(fastq_R1, fastq_R2):
    #print("R1: ", R1)
    #print("R2: ", R2)
    sample_name = "PT" + os.path.split(R1)[1].split("_")[0].split("-")[1]
    R1 = os.path.split(R1)[1]
    R2 = os.path.split(R2)[1]
    print(sample_name)
    filenames_file.write(",".join([sample_name, R1, R2])+"\n")

filenames_file.close()
