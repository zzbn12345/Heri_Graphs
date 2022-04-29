# Heri-Graphs: A Workflow of Creating Datasets for Multi-modal Machine Learning on Graphs of Heritage Values and Attributes with Social Media

This is the Code and Dataset for the Paper '*Heri-Graphs: A Workflow of Creating Datasets for Multi-modal Machine Learning on Graphs of Heritage Values and Attributes with Social Media*' submitted to ArXiv preprint server showing the collection, preprocessing, and rearrangement of data related to Heritage values and attributes in three cities that have canal-related [UNESCO World Heritage](http://whc.unesco.org/en/about/) properties: Venice, Suzhou, and Amsterdam.

## Cite as

(to be continued)

## Requirment and Dependency
deep_translator == 1.7.0

facenet_pytorch == 2.5.2

fastai == 2.5.3

flickrapi == 2.4.0

matplotlib == 3.5.1

networkx == 2.6.3

numpy == 1.22.2

opencv-python == 4.5.5.62

osmnx == 1.1.2

pandas == 1.4.0

pillow == 9.0.1

[places365](https://github.com/CSAILVision/places365) (please download the repository ```places365``` and put under the root as ```./places365```)

scipy == 1.8.0

scikit-learn == 1.0.2

torch == 1.10.2+cu113

torchvision == 0.11.3+cu113

transformers == 4.16.2

[WHOSe_Heritage](https://github.com/zzbn12345/WHOSe_Heritage) (please download the repository ```WHOSe_Heritage``` and put under the root as ```./WHOSe_Heritage```)

## Workflow and Dataset
This project provides a workflow to to construct graph-based multi-modal datasets HeriGraph concerning heritage values and attributes using data from social media platform Flickr.
The workflow is illustrated as follows:

![Workflow of Data](/Diagrams/HeriGraph-DataFlow_1.png)

To protect the privacy and copyright of Flickr users, only [the final processed (stored) datasets](https://github.com/zzbn12345/Heri_Graphs/tree/main/dataset) (thus no raw images) will be provided in this repository.
The users are invited to collect and construct datasets of the provided case study cities or any other new ```[city]``` for their own interests.

## Case Studies
Three cities related to UNESCO World Heritage and Historic Urban Landscape were selected as case studies: Amsterdam, the Netherlands ([Seventeenth-Century Canal Ring Area of Amsterdam inside the Singelgracht](https://whc.unesco.org/en/list/1349/)), Suzhou, China ([Classical Gardens of Suzhou](http://whc.unesco.org/en/list/813)), and Venice, Italy ([Venice and its Lagoon](https://whc.unesco.org/en/list/394)).

The data of each case study has been put in a different folder, such as: ```./Amsterdam```, ```./Suzhou```, and ```./Venezia```.
Without further explanation, all the codes and data introduced below will be coresponding to and stored in the respetive folder.

For constructing your ```own dataset``` with any other ```[city]```, build an individual folder ```./[city]```, and record the GEO-locations ```[city_lat]```, ```[city_lon]``` and diameter ```[city_radius]``` of the demanded area.

| Case Study City | World Heritage Name | Latitude | Longitude | Diameter |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Amsterdam (AMS) | Seventeenth-Century Canal Ring Area of Amsterdam inside the Singelgracht | 52.365000N | 4.887778E | 2 km
| Suzhou (SUZ) | Classical Gardens of Suzhou | 31.302300N | 120.631300E | 5 km
| Venice (VEN) | Venice and its Lagoon | 45.438759N | 12.327145E | 5 km
| [city] | World Heritage status of [city] | [city_lat] | [city_lon] | [city_radius]

## Dataset Summary (skip the next parts of project workflow)
As the final outcome of this project, datasets for multi-modal machine learning on multi-graphs are provided for each ```[city]```.
The components of the datasets are respectively saved in [```./dataset/[city]/```](https://github.com/zzbn12345/Heri_Graphs/tree/main/dataset), ready to be used for multiple tasks.

| File Name | Column Size | Description | Notation |
| ------------- | ------------- | ------------- | ------------- |
| [Visual_Features.csv](https://github.com/zzbn12345/Heri_Graphs/blob/main/dataset/Venice/Visual_Features.csv) | 984 | Visual Features extracted | ***X***<sup>vis</sup>
| [Textual_Features.csv](https://github.com/zzbn12345/Heri_Graphs/blob/main/dataset/Venice/Textual_Features.csv) | 776 | Textual Features extracted | ***X***<sup>tex</sup>
| [Value_Labels.csv]() | 18 | Soft and Hard Labels for Heritage Values together with confidence scores | ***Y***<sup>HV</sup>\|***K***<sup>HV</sup>
| [Attribute_Labels.csv]() | 16 | Soft and Hard Labels for Heritage Attributes together with confidence scores | ***Y***<sup>HA</sup>\|***K***<sup>HA</sup>
| [Edge_List.csv]() | 18 | Adjacency information of Multi-graphs with three types of links | ***A***

## Raw Data Collection
### Flickr API Requirements
Apply for your own API key from [Flickr APP Garden](https://www.flickr.com/services/apps/create/), and save the ```[api_key]``` and ```[api_secret]``` for later usage of API whenever requested.

### Small Datasets (*Recommended*)
The code to download raw data as IDs of Flickr posts and to save images are given in [```./[city]/save_image.py```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Venezia/save_image.py).

Input the respective ```[api_key]```, ```[api_secret]``` ,```[city_lat]```, ```[city_lon]```, and ```[city_radius]``` to run the code.
A restriction of maximum ```5000``` IDs has been given to the API to keep datasets comparable to each other.

The downloaded metadata will be saved as ```./[city]/data_storage/images/photos_sizes.csv```, and the images of which the owner allowed to download with ```candownload==True``` flag will be saved in ```./[city]/data_storage/images/150/``` and ```./[city]/data_storage/images/320/```, respectively, for the ```Large Square - url_q``` (150&times;150 px) and ```Small 320 - url_n``` (320&times;240 px) versions of the original image.

### Large Datasets
To collect large datasets without the restriction of ```5000``` IDs, follow [```./Venezia/collect_data.py```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Venezia/collect_data.py) to save all the IDs and metadata, and follow [```./Venezia/save_image_all.py```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Venezia/save_image_all.py) to download the images in the folder.

Input the respective ```[api_key]```, ```[api_secret]``` , the range of minumum and maximum
```[city_lat]``` and ```[city_lon]``` as bounding box of the region, the size of the grid (default ```20```), and radius of inquiry in the grid (default ```0.3```) to run the code.

The IDs will be collected in a 20 by 20 grid with the name of ```./[city]/data_storage/photo_ids_{}_{}.csv```, while the summarized metadata will be saved in ```./[city]/data_storage/photos_last.csv```.
All the saved images will be stored in the folder ```./[city]/data_storage/images/grid/``` with the ```Large Square - url_q``` (150&times;150 px) version of the original image.

Note that Flickr API might return an error code during the data inquiry. Run the both codes interatively to continue collecting data until the total amount is satisfied.

## Multi-modal Feature Generation
### Visual Features
The 512-dimensional vector of hidden visual features, 365-dimensional [scene category](https://github.com/CSAILVision/places365) predictions, and 102-dimensional [scene attribute](https://cs.brown.edu/~gmpatter/sunattributes.html) predictions could be obtained following [```./Places_pred.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Places_pred.ipynb).
The results will be saved as ```./[city]/data_storage/IMG_pred_150.csv``` (150&times;150 px small images only), and ```./[city]/data_storage/IMG_pred.csv``` (images of both sizes for comparison of confidence and/or consistency).

The 3-dimensional vector of [face prediction](https://github.com/timesler/facenet-pytorch) in images could be obtained following [```./Face_Detection_in_Images.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Face_Detection_in_Images.ipynb).
The results will be saved as ```./[city]/data_storage/Face_preds.csv```.

The final merged **visual features data** (982-dimensional) are provided in [```./dataset/[city]/Visual_Features.csv```](https://github.com/zzbn12345/Heri_Graphs/blob/main/dataset/Venice/Visual_Features.csv), which is effectively a 984-column table.

| Column Index | Name | Description | Data Type | Notation |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 0 | ID | Unique Image Index from Flickr | String | -
| 1 | IO_Type | Indoor/Outdoor Scene | String | - 
| 2-513 | Vis_Feat_[i] | Last 512-dimensional Hidden Layer of ResNet-18 pretrained on PlacesCNN as Visual Feature | Float | ***H***<sup>v</sup>
| 514-516 | Face_[*] | Number of faces, confidence of face prediction, proportion of faces in the image | Float | ***F*** 
| 517-881 | SCE_[*] | Smoothened/Filtered 365-dimensional scene category prediction Logit | Float | **&sigma;**<sup>(5)</sup>(***L***<sup>s</sup>)
| 882-983 | ATT_[*] | Smoothened/Filtered 102-dimensional scene attribute prediction Logit | Float | **&sigma;**<sup>(10)</sup>(***L***<sup>a</sup>)

### Textual Features
The data cleaning of textual data, and the 3-dimensional vector of original language of posts could be obtained following [```./Dataset_Cleaning_and_Merging_[city].ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Dataset_Cleaning_and_Merging_Venice.ipynb).
The results will be saved as ```./[city]/data_storage/metadata.csv``` in post level and ```./[city]/data_storage/sentences.csv``` in sentence level.

The 768-dimensional vector of BERT [CLS] token could be obtained following [```./bert_inference_HeriGraph.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/bert_inference_HeriGraph.ipynb).
The results will be saved as ```./[city]/data_storage/metadata_bert.csv``` in post level and ```./[city]/data_storage/sentences_bert.csv``` in sentence level.

The final merged **textual features data** (771-dimensional) are provided in [```./dataset/[city]/Textual_Features.csv```](https://github.com/zzbn12345/Heri_Graphs/blob/main/dataset/Venice/Textual_Features.csv), which is effectively a 776-column table.

| Column Index | Name | Description | Data Type | Notation |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 0 | index | Unique Image Index from Flickr | String | -
| 1 | text_bool | If the original post has a valid textual data (as a filter) | Boolean | - 
| 2 | revised_text | The processed and filtered textual data of the post as combination of description, title, and tags. | String | *S*
| 3-4 | num_sent/ text_len | Number of sentences and number of words in the revised text | Integer | - 
| 5-772 | BERT_[i] | The 768-dimensional output vector of [CLS] token | Float | ***H***<sup>B</sup>
| 773-775 | English/ Local_Lang/ Other_Lang | Detected original language in the posts | Boolean | ***O***

### Contextual Features

The **temporal features** about the timestamps of the posts in their unique week counts could be obtained following [```./Dataset_Cleaning_and_Merging_[city].ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Dataset_Cleaning_and_Merging_Venice.ipynb).
The results will be saved in ```./[city]/data_storage/metadata.csv```.

The **social features** about the social relations of the post owners could be obtained following [```./Social_Links_of_Interests.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Social_Links_of_Interests.ipynb).
Input the ```[api_key]``` and ```[api_secret]``` to activate the queries of the public contacts and public groups of the Flickr users.
The information will be respectively saved as ```./[city]/data_storage/contacts.csv```, ```./[city]/data_storage/interest.csv```, and ```./[city]/data_storage/friendship.csv```, while the final merged social information is saved as ```./[city]/data_storage/social_links.csv```.

The **spatial features** about the locations of the posts and their connectivity in geographical network could be obtained following [```./Geographical_Graph_Construction.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Geographical_Graph_Construction.ipynb).
Input the respective ```[city_lat]```, ```[city_lon]```, and ```[city_radius]``` to run the code.
The spatial network information will be saved respectively as ```./[city]/data_storage/GEO_nodes.csv``` showing the intersections in spatial network, ```./[city]/data_storage/GEO_edges.csv``` showing the connectivity of spatial nodes with travel time information, and ```./[city]/data_storage/GEO_node_dist.csv``` showing the travel time between any two nodes.
The geo-node assigned to each post will be recorded in ```./[city]/data_storage/GEO_metadata.csv```.

## Label Generation
### Heritage Values
### Heritage Attributes

## Multi-graph Construction

## Acknowledgements and License
This project applied the pretrained models of the following projects which are openly released on GitHub or published as python packages. Part of the codes are adpated from the original codes.

[Places365-CNNs](https://github.com/CSAILVision/places365)

[Face Recognition Using Pytorch](https://github.com/timesler/facenet-pytorch)

[WHOSe_Heritage](https://github.com/zzbn12345/WHOSe_Heritage)

The copyright of all the downloaded and processed images belongs to the image owners.