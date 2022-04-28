# Heri-Graphs: A Workflow of Creating Datasets for Multi-modal Machine Learning on Graphs of Heritage Values and Attributes with Social Media

This is the Code and Dataset for the Paper '*Heri-Graphs: A Workflow of Creating Datasets for Multi-modal Machine Learning on Graphs of Heritage Values and Attributes with Social Media*' submitted to ArXiv preprint server showing the collection, preprocessing, and rearrangement of data related to Heritage values and attributes in three cities that have canal-related UNESCO World Heritage properties: Venice, Suzhou, and Amsterdam.

## Cite as

(to be continued)

## Requirment and Dependency
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

## Raw Data Collection
### Flickr API Requirements
Apply for your own API key from [Flickr APP Garden](https://www.flickr.com/services/apps/create/), and save the ```[api_key]``` and ```[api_secret]``` for later usage of API whenever requested.

### Small Datasets
A restriction of maximum ```5000``` IDs has been given to the API to keep datasets comparable to each other.