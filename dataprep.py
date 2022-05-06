import pandas as pd
import os

if __name__ == "__main__":
    for r, d, f in os.walk("./exampledata/finetune/"):
        print(r, d, f)
        for filename in f:
            if filename[-4:] == ".csv":
                print(f, filename, filename[:-4])
                df = pd.read_csv("exampledata/finetune/" + filename)
                #print(df.head(2))
                for fract in [0.1, 0.05, 0.01]:
                    for sample in range(5):
                        new_fn = "exampledata/finetune/downsampled/" + filename[:-4] + "_%s_s%s.csv" % (fract, sample)
                        new = df.sample(frac=fract)
                        #if sample == 0:
                            #print(new.head(2))
                        #new.to_csv(new_fn, index=False)
                        print(new.shape)
        break           
