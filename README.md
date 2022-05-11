# Heri-Graphs: A Workflow of Creating Datasets for Multi-modal Machine Learning on Graphs of Heritage Values and Attributes with Social Media

This is the Code and Dataset for the Paper '*Heri-Graphs: A Workflow of Creating Datasets for Multi-modal Machine Learning on Graphs of Heritage Values and Attributes with Social Media*' submitted to ArXiv preprint server showing the collection, preprocessing, and rearrangement of data related to Heritage values and attributes in three cities that have canal-related [UNESCO World Heritage](http://whc.unesco.org/en/about/) properties: Venice, Suzhou, and Amsterdam.

## Cite as

(to be continued)

## Table of Content
#### [Requirement and Dependency](#requirement)
#### [Workflow and Dataset](#workflow)
#### [Case Studies](#case)
#### [Dataset Summary](#dataset)

The following sections about the workflow can be skipped for those who only intend to use the provided datasets.
#### [Raw Data Collection](#raw)
#### [Multi-modal Feature Generation](#feature)
#### [Label Generation](#label)
#### [Multi-graph Construction](#graph)
#### [Acknowledgements and License](#license)

## Requirement and Dependency<a name="requirement"></a>
deep_translator == 1.7.0

facenet_pytorch == 2.5.2

fastai == 2.5.3

flickrapi == 2.4.0

[GIT Large File Storage](https://docs.github.com/en/repositories/working-with-files/managing-large-files) (please install the GIT LFS before cloning the repository for storage of large datasets)

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

## Workflow and Dataset<a name="workflow"></a>
This project provides a workflow to to construct graph-based multi-modal datasets HeriGraph concerning heritage values and attributes using data from social media platform Flickr.
The workflow is illustrated as follows:

![Workflow of Data](/Diagrams/HeriGraph-DataFlow_1.png)

To protect the privacy and copyright of Flickr users, only [the final processed (stored) datasets](../tree/main/dataset) (thus no raw images) will be provided in this repository.
The users are invited to collect and construct datasets of the provided case study cities or any other new ```[city]``` for their own interests.

## Case Studies<a name="case"></a>
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

## Dataset Summary (skip the next parts of project workflow)<a name="dataset"></a>
As the final outcome of this project, datasets for multi-modal machine learning on multi-graphs are provided for each ```[city]```.
The components of the datasets are respectively saved in [```./dataset/[city]/```](https://github.com/zzbn12345/Heri_Graphs/tree/main/dataset), ready to be used for multiple tasks.

The merging and saving of datasets could be found following [```./Dataset_Saving.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Dataset_Saving.ipynb).

| File Name | Column Size | Description | Notation |
| ------------- | ------------- | ------------- | ------------- |
| [Visual_Features.csv](https://github.com/zzbn12345/Heri_Graphs/blob/main/dataset/Venice/Visual_Features.csv) | 984 | Visual Features extracted | ***X***<sup>vis</sup>
| [Textual_Features.csv](https://github.com/zzbn12345/Heri_Graphs/blob/main/dataset/Venice/Textual_Features.csv) | 776 | Textual Features extracted | ***X***<sup>tex</sup>
| [Value_Labels.csv]() | 26 | Soft and Hard Labels for Heritage Values together with confidence scores | ***Y***<sup>HV</sup>\|***K***<sup>HV</sup>
| [Attribute_Labels.csv]() | 19 | Soft and Hard Labels for Heritage Attributes together with confidence scores | ***Y***<sup>HA</sup>\|***K***<sup>HA</sup>
| [Edge_List.csv]() | 18 | Adjacency information of Multi-graphs with three types of links | ***A***, ***A***<sup>TEM</sup>, ***A***<sup>SOC</sup>, ***A***<sup>SPA</sup>

## Raw Data Collection<a name="raw"></a>
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

## Multi-modal Feature Generation<a name="feature"></a>
### Visual Features
The 512-dimensional vector of hidden visual features, 365-dimensional [scene category](https://github.com/CSAILVision/places365) predictions, and 102-dimensional [scene attribute](https://cs.brown.edu/~gmpatter/sunattributes.html) predictions could be obtained following [```./Places_Prediction.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Places_prediction.ipynb).
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
| 1 | text_bool | Whether the original post has a valid textual data (as a filter) | Boolean | - 
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

## Label Generation<a name="label"></a>
### Heritage Values

This project applied the heritage value definition in UNESCO WHL with regard to ten [Outstanding Universal Value selection criteria](https://whc.unesco.org/en/criteria/) plus one additional "other" class, which is introduced and trained in [WHOSe_Heritage](https://github.com/zzbn12345/WHOSe_Heritage).

The predicted labels on heritage values by BERT could be obtained following [```./bert_inference_HeriGraph.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/bert_inference_HeriGraph.ipynb).
The results will be saved as ```./[city]/data_storage/metadata_bert.csv``` in post level and ```./[city]/data_storage/sentences_bert.csv``` in sentence level.

The predicted labels on heritage values by ULMFiT could be obtained following [```./ulmfit_inference_HeriGraph.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/ulmfit_inference_HeriGraph.ipynb).
The results will be saved as ```./[city]/data_storage/metadata_ulmfit.csv``` in post level and ```./[city]/data_storage/sentences_ulmfit.csv``` in sentence level.

The comparison of the both models for performance, coherence, and consistency on both post level and sentence level could be obtained following [```./Diagram_Values.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Diagram_Values.ipynb).

The final merged **heritage value label data** (11-dimensional) are provided in [```./dataset/[city]/Value_Labels.csv```](https://github.com/zzbn12345/Heri_Graphs/blob/main/dataset/Venice/Value_Labels.csv), which is effectively a 26-column table.
A sample is considered as ```labelled``` if the average top-3 confidence of both BERT and UMLFiT models is larger than ```0.75``` and the [Jaccard Index](https://en.wikipedia.org/wiki/Jaccard_index) of such top-3 predictions is larger than ```0.5```.
This leads to around ```40-50%``` texual samples as labelled (thus around ```10-35%``` of all data samples in each city).
Users are invited to adjust the thresholds of labelled data to experiment on the effects.

| Column Index | Name | Description | Data Type | Notation |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 0 | index | Unique Image Index from Flickr | String | -
| 1 | text_bool | Whether the original post has a valid textual data (as a filter) | Boolean | - 
| 2-12 | Criteria_[i]/ Others | The average predicted soft label of post text concerning heritage values in terms of [OUV](https://aclanthology.org/2021.findings-emnlp.34/). | Float | ***Y***<sup>HV</sup>
| 13-18 | max_[i]\_val/ max_[i]\_col | The predicted hard top-3 labels of heritage values | Float/ String | - 
| 19-20 | max_[i] | The top-k confidence of averaged soft label prediction | Float | -
| 21-22 | conf_[i] | The average model confidence of BERT and ULMFiT for their top-k predictions | Float | ***&kappa;***<sup>HV(0)</sup>
| 23-24 | same_[i] | The model agreement/consistency of BERT and ULMFiT for their top-k predictions in terms of Jaccard Index | Float/ Boolean | ***&kappa;***<sup>HV(1)</sup>
| 25 | labelled | Whether the sample should be considered as "pseudo-labelled" data | Boolean | -

A demo of labelled heritage values can be seen with the following diagram:

![Heritage Values](/Diagrams/Value_labels.jpg)

### Heritage Attributes

This project applied the heritage definition by [Veldpaus (2015)](https://pure.tue.nl/ws/files/3914913/798291.pdf) and [Ginzarly et al. (2019)](http://dx.doi.org/10.1016/j.culher.2018.10.002), keeping a nine-class category of depicted scenery of an image.

A few models have been trained on the data presented by [Ginzarly et al. (2019)](http://dx.doi.org/10.1016/j.culher.2018.10.002) in Tripoli, Lebanon.
The training process together with hyper-parameter tuning with grid search cross validation with [scikit-learn library](https://scikit-learn.org/stable/modules/classes.html) could be found in [```./Machine_Learning_Models_on_Heritage_Attributes_Tripoli.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Machine_Learning_Models_on_Heritage_Attributes_Tripoli.ipynb).

![Model_Training](/Diagrams/ML_models.png)

The trained ensemble VOTE and STACK classification models are saved in the folder [```./Tripoli/model_storage/```](https://github.com/zzbn12345/Heri_Graphs/tree/main/Tripoli/model_storage) respectively under [```./Tripoli/model_storage/vote_classifier.joblib```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Tripoli/model_storage/vote_classifier.joblib) and [```./Tripoli/model_storage/stack_classifier.joblib```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Tripoli/model_storage/stack_classifier.joblib).

The predicted labels on heritage attributes by both classifiers could be obtained following [```./Machine_Learning_Models_on_Heritage_Attributes_Tripoli.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Machine_Learning_Models_on_Heritage_Attributes_Tripoli.ipynb).
The results will be saved as ```./[city]/data_storage/IMG_pred_150_cat.csv```.

The comparison of the both models for performance, coherence, and consistency could be obtained following [```./Diagram_Attributes.ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/Diagram_Attributes.ipynb).

The final merged **heritage attribute label data** (9-dimensional) are provided in [```./dataset/[city]/Attribute_Labels.csv```](https://github.com/zzbn12345/Heri_Graphs/blob/main/dataset/Venice/Attribute_Labels.csv), which is effectively a 19-column table.
A sample is considered as ```labelled``` if the average top-1 confidence of both VOTE and STACK models is larger than ```0.7``` and the top-1 predictions is ```same```.
This leads to around ```35-50%``` samples as labelled.
Users are invited to adjust the thresholds of labelled data to experiment on the effects.

| Column Index | Name | Description | Data Type | Notation |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 0 | ID | Unique Image Index from Flickr | String | -
| 1-9 | [various names] | The average predicted soft label of post image concerning heritage attributes in terms of [depicted scenes](http://dx.doi.org/10.1016/j.culher.2018.10.002). | Float | ***Y***<sup>HA</sup>
| 10-11 | category[-/_id] | The predicted hard top-1 labels of heritage attributes | String | - 
| 12-15 | category/ cat_id_[model] | The top-1 hard label prediction of VOTE and STACK models | String | -
| 16 | conf | The average model confidence of VOTE and STACK for their top-1 predictions | Float | ***&kappa;***<sup>HA(0)</sup>
| 17 | category_same | The model agreement/consistency of VOTE and STACK for their top-1 predictions | Boolean | ***&kappa;***<sup>HA(1)</sup>
| 18 | labelled | Whether the sample should be considered as "pseudo-labelled" data | Boolean | -

A demo of labelled heritage attributes can be seen with the following diagram:

![Heritage Attributes](/Diagrams/Categories.jpg)

## Multi-graph Construction<a name="graph"></a>

The graph construction process for the Multi-Graphs, the three subgraphs with Temporal, Social, and Spatial links, as well as the simple composed graphs could be obtained following [```./HeriGraph_Construction_[city].ipynb```](https://github.com/zzbn12345/Heri_Graphs/blob/main/HeriGraph_Construction_Venezia.ipynb).

The [Edge Lists](https://en.wikipedia.org/wiki/Edge_list) that could be directly used [by NetworkX](https://networkx.org/documentation/stable/reference/generated/networkx.convert_matrix.from_pandas_edgelist.html) or other softwares to construct graphs are provided in [```./dataset/[city]/Edge_List.csv```](https://github.com/zzbn12345/Heri_Graphs/blob/main/dataset/Venice/Edge_List.csv), which is effectively a 16-column table.
The columns of ```[Temporal/Social/Spatial]_Similarity``` are the edge weight for each type of subgraphs, and the column ```One_Edge``` is the adjacency indicator for the composed simple graph.

| Column Index | Name | Description | Data Type | Notation |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 0 | 0 | Unique Image Index from Flickr for Node 0 | String | *v*<sub>0</sub>
| 1 | 1 | Unique Image Index from Flickr for Node 1 | String | *v*<sub>1</sub>
| 2-3 | Week_[i] | The timestamp ID in week level | String | *t*<sub>i</sub>
| 4 | dist | The temporal distance of two nodes | String | -
| 5 | Temporal_Similarity | The edge weight of temporal links | Float | ***A***<sup>TEM</sup>
| 6-7 | User_[i] | The user ID in Flickr | String | *u*<sub>i</sub>
| 8 | relationship | The strength level of relationship of two users | Integer | -
| 9 | Social_Similarity | The edge weight of social links | Float | ***A***<sup>SOC</sup>
| 10-11 | GEO_[i] | The GEO-location ID in the spatial network | String | &upsilon;<sub>i</sub>
| 12 | geo_distance | The spatial distance of two nodes in terms of travel time | Float | *w*<sub>e</sub>
| 13 | Spatial_Similarity | The edge weight of spatial links | Float | ***A***<sup>SPA</sup>
| 14 | One_Edege | The adjacency indicator for the composed simple graph | Boolean | ***A***
| 15 | Same_Node | Whether the two nodes are the same one | Boolean | -

The statistics of generated graphs following [the standard of PyTorch-Geometric](https://pytorch-geometric.readthedocs.io/en/latest/notes/data_cheatsheet.html) could be found in the following table:

| Name | #graphs/ subgraphs | #nodes | #edges | #features | #classes/ tasks |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| HeriGraph | 3 | ~3271.7 | ~907,393.3 | - | -
| └─Amsterdam | 3+1 | 3727 | 1,271,171 | 1753 | 11+9
| └─Suzhou | 3+1 | 3137 | 916,496 | 1753 | 11+9
| └─Venice | 3+1 | 2951 | 534,513 | 1753 | 11+9

## Acknowledgements and License<a name="license"></a>
This project applied the pretrained models of the following projects which are openly released on GitHub or published as python packages. Part of the codes are adpated from the original codes.

[Places365-CNNs](https://github.com/CSAILVision/places365)

[Face Recognition Using Pytorch](https://github.com/timesler/facenet-pytorch)

[WHOSe_Heritage](https://github.com/zzbn12345/WHOSe_Heritage)

The workflows and datasets of this paper can be used under the Creative Common License (Attribution [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)). 
Please give appropriate credit, such as providing a link to our paper or to [this github repository](https://github.com/zzbn12345/Heri_Graphs).
The copyright of all the downloaded and processed images belongs to the image owners.
