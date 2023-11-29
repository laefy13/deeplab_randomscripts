import random

df = []
with open('dataset.txt','r') as f:
    for line in f:
        df.append(line)

print('length:',len(df))
random.shuffle(df)
df_30=df[:int(len(df)*.30)]
print('30% length:',len(df_30))
df_70 = df[int(len(df)*.30):]
print('30% length:',len(df_70))
with open('validation.txt','w') as f:
    for x in df_30:
        f.write(x)
with open('train.txt','w') as f:
    for x in df_70:
        f.write(x)