from class_data_preparation import *
from class_additif import *

dataset_df = pd.read_csv(r'.\vente_maillots_de_bain(1).csv', encoding='ISO-8859-1')
data_preparation_object = DataPreparation(dataset_df)
Additif_object = Additif(data_preparation_object)
