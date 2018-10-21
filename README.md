# Engine
Building Positional Inverted Index

DEPENDENCIES
#############

Graphlab- 2.1


INSTALL GRAPHLAB
################

pip install --upgrade --user --no-cache-dir  https://get.graphlab.com/GraphLab-Create/2.1/email-id/LICENSE KEY/GraphLab-Create-License.tar.gz




EXECUTION
#########


Default Arguments

	#############################################################################################

    Execute  python Main.py
    		 Saves all results into Output Folder,  


    ############################################################################################# 		 

   	Execute with arguments

   			python Main.py -h


	   	usage: Main.py [-h] [--db DB] [--query QUERY] [--rank RANK]
	               [--invertedIdx INVERTEDIDX] [--oBQuery OBQUERY]
	               [--oRQuery ORQUERY]

		Mini Search Engine

		optional arguments:
		  -h, --help            show this help message and exit
		  --db DB               Please provide xml data
		  --query QUERY         Please provide file name to execute boolean queries
		  --rank RANK           Please provide file name to execute rank queries
		  --invertedIdx INVERTEDIDX
		                        Please provide an output file for Positional Inverted
		                        Index
		  --oBQuery OBQUERY     Please provide an output file for Boolean queries
		  --oRQuery ORQUERY     Please provice an output file for Rank queries
	##############################################################################################
