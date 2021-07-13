## BERT PRE-TRAINING USING NEMO

This module covers the various steps to run bert-pretraining on the IndicCorp Dataset: https://indicnlp.ai4bharat.org/corpora/ . The various steps are :

* The first step of the process is to generate the hdf5 files required for the training. 

* In the line **380** of the *data_gen.py*, specify the path to the folder containing the txt files of the dataset, or simply specify the path to a single file of the dataset. Note that you can also pass this file using argument parser while running the file.

* In the line **384** of the *data_gen.py*, specify the name that you want to give to the output hdf5 file. Again, this can be passed using argument parser.

* Please note that you have to run *data_gen.py* to generate both the train and the validation *hdf5* files. Therefore, If your dataset is a single file( like the English dataset of IndicCorp), you can use a script to split the dataset. A sample script( demo.py ) is attached.Now  you can run the files to generate the hd5 files like this - 

      python data_gen.py

* Once you have the required hd5 files ( both train and val), specify the path to these files in the *bert_pretraining_from_preprocessed_config.yaml* file, in lines 46 and 56

* Once the above step is done, specify the path to the above config file in the *bert_pretraining.py* file, and run the file. The model training will start and you will be able to see the logs. The command to start the pretraining is 
  
      python bert_pretraining.py
