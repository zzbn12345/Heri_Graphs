import json
import flickrapi
import pandas as pd
import numpy as np
from argparse import Namespace
from collections import Counter
import pickle
import os
import urllib

args = Namespace(
    # Data and Path information
    api_key = u'[api_key]',
    api_secret = u'[api_secret]',
    radius = 0.3,
    save_dir = 'data_storage/',
    tags = None,
    len_grid = 20,
    image_dir = 'data_storage/images/grid/'
    #tags = 'landscape,urban,heritage,culture,building,architecture,park,street'
)

def get_photos(flickr, Photos, Ids):
    processed = Photos.keys()
    for id_now in Ids:
        if id_now in processed:
            continue
        else:
            Photos[id_now] = {}
            sizes = json.loads(flickr.photos.getSizes(photo_id = id_now, format='json'))
            try:
                url_c = sizes['sizes']['size'][-2]['source']
                url_q = sizes['sizes']['size'][1]['source']
                can = sizes['sizes']['candownload']
                Photos[id_now]['candownload'] = can
                Photos[id_now]['url_c'] = url_c
                Photos[id_now]['url_q'] = url_q
                Photos[id_now]['others'] = sizes

                if can:
                    urllib.request.urlretrieve(url_q, args.image_dir+'{}.jpg'.format(id_now))

                if len(processed)%20 ==1:
                    print('{}/{} photos collected'.format(len(processed),len(Ids)))
                    with open(args.image_dir+'Photo_sizes_pre_sep.p', 'wb') as fp:
                        pickle.dump(Photos,fp, protocol=pickle.HIGHEST_PROTOCOL)
                    with open(args.image_dir+'Photo_sizes_sep.p', 'wb') as fp:
                        pickle.dump(Photos,fp, protocol=pickle.HIGHEST_PROTOCOL)
                    photo_df = pd.DataFrame(Photos).T.drop('others',axis=1)
                    photo_df.to_csv(args.image_dir+'photos_sizes_sep.csv', sep='\t',encoding='utf-8-sig')
            except:
                print(id_now)
                continue
    
    with open(args.image_dir+'Photo_sizes_pre_sep.p', 'wb') as fp:
        pickle.dump(Photos,fp, protocol=pickle.HIGHEST_PROTOCOL)

    with open(args.image_dir+'Photo_sizes_sep.p', 'wb') as fp:
        pickle.dump(Photos,fp, protocol=pickle.HIGHEST_PROTOCOL)
    photo_df = pd.DataFrame(Photos).T.drop('others',axis=1)
    photo_df.to_csv(args.image_dir+'photos_sizes_sep.csv', sep='\t',encoding='utf-8-sig')
    return Photos

def main():

    flickr = flickrapi.FlickrAPI(args.api_key, args.api_secret)

    df=pd.read_csv(args.save_dir+'grid/photos_sep.csv',sep='\t').rename(columns={'Unnamed: 0':'num'})
    Ids = df['ids']

    if 'Photo_sizes_sep.p' in [files for root, dirs, files in os.walk(args.image_dir)][0]:
        with open(args.image_dir+'Photo_sizes_sep.p', 'rb') as fp:
            Photos = pickle.load(fp)
    else:
        Photos = {}

    Photos = get_photos(flickr, Photos, Ids)

if __name__ == "__main__":
    main()
"""## END"""