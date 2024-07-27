import pandas as pd
import os


all_ids = [x.split('.')[0] for x in os.listdir('images/')]
BASE_URL = "https://raw.githubusercontent.com/0xnakul/PatentDesc-testims/b966911e328f44e16b4e6f6f81b57c4d24cddd4a/images/"

all_urls = [BASE_URL + x + '.png' for x in all_ids]

df = pd.DataFrame({'id': all_ids, 'image_url': all_urls})

df.to_csv('brief_desc_files_gptv/master.tsv', sep='\t', index=False)
df.to_csv('detailed_desc_files_gptv/master.tsv', sep='\t', index=False)
