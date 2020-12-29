import flickrapi
import json
import pandas as pd
import numpy as np
from argparse import Namespace
from collections import Counter
import pickle
import os

args = Namespace(
    # Data and Path information
    api_key = u'9e32e17383e134335b5cabf2eb186b7a',
    api_secret = u'781aa9cac0a656c9',
    radius = 0.3,
    save_dir = 'data_storage/',
    tags = None,
    len_grid = 20,
    #tags = 'landscape,urban,heritage,culture,building,architecture,park,street'
)

def get_latlon(id_x, id_y, num = args.len_grid):
    lat_min = 45.420855
    lon_min = 12.291054

    lat_max = 45.448286
    lon_max = 12.369234
    
    lat_d = (lat_max - lat_min)/(num-1)
    lon_d = (lon_max - lon_min)/(num-1)

    lat = lat_min + id_x * lat_d
    lon = lon_min + id_y * lon_d

    #lat = 45.438759
    #lon = 12.327145
    return lat,lon

def collect_ids(flickr, lat, lon, radius, x,y, tags = None):

    if 'photo_ids_{}_{}.csv'.format(x,y) in [files for root, dirs, files in os.walk(args.save_dir)][0]:
            Ids = pd.read_csv(args.save_dir+'photo_ids_{}_{}.csv'.format(x,y),sep='\t')['ids'].tolist()
    else:
        Ids = []

    walk = flickr.walk(has_geo = 1, lat = lat, lon = lon, radius = args.radius, tags=tags)
    for photo in walk:
        id_now = photo.get('id')
        if id_now in Ids:
            continue
        Ids.append(id_now)
        if len(Ids)%200 == 0:
            print('{} photo ids collected'.format(len(Ids)))
            pd.Series(Ids, name = 'ids').to_csv(args.save_dir + 'photo_ids_{}_{}.csv'.format(x,y), index=False)
    pd.Series(Ids, name = 'ids').to_csv(args.save_dir + 'photo_ids_{}_{}.csv'.format(x,y), index=False)
    return Ids

def update_df(Photos):
    return Photos

def get_photos(flickr, Photos, Ids):
    processed = Photos.keys()
    for id_now in Ids:
        if str(id_now) in processed:
            continue

        Photos[id_now] = {}
        info = json.loads(flickr.photos.getInfo(photo_id = id_now, format='json'))
        Photos[id_now]['info'] = info
        Photos[id_now]['owner'] = info['photo']['owner']['nsid']
        Photos[id_now]['owner_loc'] = info['photo']['owner']['location']
        Photos[id_now]['title'] = info['photo']['title']['_content']
        Photos[id_now]['description'] = info['photo']['description']['_content']
        Photos[id_now]['comments'] = info['photo']['comments']['_content']
        Photos[id_now]['taken'] = info['photo']['dates']['taken']
        Photos[id_now]['views'] = info['photo']['views']
        Photos[id_now]['people'] = info['photo']['people']['haspeople']
        Photos[id_now]['tags'] = info['photo']['tags']['tag']
        Photos[id_now]['lat'] = info['photo']['location']['latitude']
        Photos[id_now]['lon'] = info['photo']['location']['longitude']
        Photos[id_now]['neighbourhood'] = info['photo']['location']['neighbourhood']['_content']
        Photos[id_now]['url'] = info['photo']['urls']['url'][0]['_content']

        if len(processed)%20 ==1:
            print('{}/{} photos collected'.format(len(processed),len(Ids)))
            with open(args.save_dir+'Photo_info.p', 'wb') as fp:
                pickle.dump(Photos,fp, protocol=pickle.HIGHEST_PROTOCOL)
            photo_df = pd.DataFrame(Photos).T.drop('info',axis=1)
            photo_df.to_csv(args.save_dir+'photos.csv', sep='\t',encoding='utf-8-sig')
    
    with open(args.save_dir+'Photo_info_pre.p', 'wb') as fp:
        pickle.dump(Photos,fp, protocol=pickle.HIGHEST_PROTOCOL)

    with open(args.save_dir+'Photo_info.p', 'wb') as fp:
        pickle.dump(Photos,fp, protocol=pickle.HIGHEST_PROTOCOL)
    photo_df = pd.DataFrame(Photos).T.drop('info',axis=1)
    photo_df.to_csv(args.save_dir+'photos.csv', sep='\t',encoding='utf-8-sig')
    return Photos

def main():

    flickr = flickrapi.FlickrAPI(args.api_key, args.api_secret)

    if 'completed.p' in [files for root, dirs, files in os.walk(args.save_dir)][0]:
        with open(args.save_dir+'completed.p', 'rb') as fp:
                completed = pickle.load(fp)
    else:
        completed = {}

    for x in range(args.len_grid):
        for y in range(args.len_grid):
            if (x,y) in completed.keys():
                continue

            lat,lon = get_latlon(x,y)
    
            if 'photo_ids_{}_{}.csv'.format(x,y) in [files for root, dirs, files in os.walk(args.save_dir)][0]:
                Ids = pd.read_csv(args.save_dir+'photo_ids_{}_{}.csv'.format(x,y),sep='\t')['ids'].tolist()
            else:
                Ids = collect_ids(flickr, lat,lon, args.radius, tags=args.tags, x=x,y=y)

            if 'Photo_info.p' in [files for root, dirs, files in os.walk(args.save_dir)][0]:
                with open(args.save_dir+'Photo_info.p', 'rb') as fp:
                        Photos = pickle.load(fp)
            else:
                Photos = {}

            Photos = get_photos(flickr, Photos, Ids)

            completed[(x,y)] = {}
            completed[(x,y)]['lat'] = lat
            completed[(x,y)]['lon'] = lon
            completed[(x,y)]['collected'] = len(Ids)
            completed[(x,y)]['total'] = len(Photos)

            with open(args.save_dir+'completed.p', 'wb') as fp:
                pickle.dump(completed,fp, protocol=pickle.HIGHEST_PROTOCOL)
            
            completed_df = pd.DataFrame(completed).T
            completed_df.to_csv(args.save_dir+'completed.csv')


if __name__ == "__main__":
    main()
"""## END"""