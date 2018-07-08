import shutil
import fire
import os

def downsize(
            rta = '/Users/eulring/Efile/Dataset/dogcat/train', 
            rtb = None,
            scale = 1000):
    print(rta)
    if rtb == None:
        rtb = rta + '-' + str(scale) + '/'
    rta = rta + '/'
    print(rtb)
    
    if not os.path.exists(rta):
        print("No such Dataset, route may wrong...")
        return 

    if not os.path.exists(rtb):
        os.makedirs(rtb) 

    # files = [os.path.join(rta, fe) for fe in os.listdir(rta)]
    files = [fe for fe in os.listdir(rta)]
    print(len(files))
    print(files[1])
    

    for i, fname in enumerate(files):
        if(i % scale == 0):
            oldname = rta + files[i]
            newname = rtb + files[i]
            shutil.copyfile(oldname, newname)


if __name__ == '__main__':
    fire.Fire()



