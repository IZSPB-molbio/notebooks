import csv
import os
import glob

# fastq_R1 = sorted(glob.glob(run_folder + "/COVID*_R1*.fastq.gz"))
# fastq_R2 = sorted(glob.glob(run_folder + "/COVID*_R2*.fastq.gz"))
fastq_R1 = sorted(glob.glob("COVID*_R1*.fastq.gz"))
fastq_R2 = sorted(glob.glob("COVID*_R2*.fastq.gz"))

# filenames_file = open(os.path.join(run_folder, "filenames_list.csv"), 'w')
filenames_file_dict = {}
filenames_file = open("filenames_list.csv", 'w')
batch_file = open("batch.csv", 'w')

## Parse Icogen metadata as exported from FMPro with these fields (in this order!)
## and with this filename: sars-cov-2_db_export_icogen.csv
# - "Coronavirus"
# - "Puglia"
# - Comune
# - LabProvenienza_esteso
# - AccettazioneIZSPB_Icogen
# - DataPrelievo
icogen_metadata_handle = open("sars-cov-2_db_export_icogen.csv", 'r')
icogen_metadata = {}

with open("sars-cov-2_db_export_icogen.csv", 'rt') as f:
    icogen_metadata_handle = csv.reader(f)
    for i in icogen_metadata_handle:
#        corona, regione, comune, lab, sample_name, data_prelievo = i.split(",")
        [corona, regione, comune, lab, sample_name, data_prelievo] = i
        try:
            gg, mm, yyyy = data_prelievo.split("/")
            data_prelievo = '-'.join([yyyy, mm, gg])
        except:
            print("Error in parsing data_prelievo for {sample_name}: {data_prelievo}".format(sample_name = sample_name, data_prelievo = data_prelievo))
            data_prelievo = ""
            pass
        icogen_metadata[sample_name] = {'corona' : corona, 
                                        'regione' : regione,
                                        'comune' : comune,
                                        'lab' : lab,
                                        'sample_name' : sample_name,
                                        'data_prelievo' : data_prelievo}

print(list(icogen_metadata.keys())[:10])

for R1, R2 in zip(fastq_R1, fastq_R2):
    #print("R1: ", R1)
    #print("R2: ", R2)
    sample_name = "PT" + os.path.split(R1)[1].split("_")[0].split("-")[1]
    R1 = os.path.split(R1)[1]
    R2 = os.path.split(R2)[1]
    print("Parsing: ", sample_name)
    filenames_file_dict[sample_name] = [R1, R2]
    filenames_file.write(",".join([sample_name, R1, R2])+"\n")
    try:
        batch_file.write("{corona},{regione},{comune},{lab},{sample_name},{data_prelievo},{R1},{R2}\n".format(corona=icogen_metadata[sample_name]['corona'],
                      regione=icogen_metadata[sample_name]['regione'],
                      comune=icogen_metadata[sample_name]['comune'],
                      lab=icogen_metadata[sample_name]['lab'],
                      sample_name=icogen_metadata[sample_name]['sample_name'],
                      data_prelievo=icogen_metadata[sample_name]['data_prelievo'],
                      R1=filenames_file_dict[sample_name][0],
                      R2=filenames_file_dict[sample_name][1]))
    except Exception as e:
        print("Exception:", e)
        print("Error with sample: ", sample_name)
        print(icogen_metadata[sample_name])
        print(filenames_file_dict[sample_name])
        pass

batch_file.close()
filenames_file.close()
