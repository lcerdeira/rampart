import sys, os
import glob
import random
import shutil
import time, datetime

if __name__ == '__main__':
    """This file is only temporary.
    Every 1 second it either passes or writes
    a file to data/real_time_reads/<DATE>
    This file is actually simply a copy of a file in read_files
    See the real read_mapping_daemon for actual reads.
    """

    outdir = "./data/real_time_reads/"
    print("Mock read mapping daemon running. Files produced in {}.".format(outdir))

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # remove any previous real-time-mapping files
    files = glob.glob(outdir + "*")
    for f in files:
        os.remove(f)


    i = 0;
    while True:
        # produce a mapped read around 30% of the time
        if random.random() > 0.7:
            i+=1
            new_read_path = outdir + "mapped_" + datetime.datetime.now().isoformat() + '.csv'
            old_read_path = "./data/read_files/reads_1k_{}.csv".format(i)
            shutil.copyfile(old_read_path, new_read_path)
        time.sleep(1)
