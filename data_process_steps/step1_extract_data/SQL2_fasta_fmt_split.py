import argparse
import mysql.connector
import re


ap = argparse.ArgumentParser(description='Converts a 3-column table to LATEX to format species based on columns')
ap.add_argument("-wd", "--whole_dataset_file", default='wds.txt', 
        help="full dataset output text file")
ap.add_argument("-ni", "--whole_ds_noinverts", default='wds_noinverts.txt', 
        help="full dataset output text file")
ap.add_argument("-swd", "--sws_dataset_file", default='swd.txt', 
        help="sws dataset output text file")   
ap.add_argument("-mwd", "--mws_dataset_file", default='mwd.txt', 
        help="mws/lws dataset output text file")
ap.add_argument("-rod", "--rod_dataset_file", default='rod.txt', 
        help="rhodopsin dataset output text file")    
ap.add_argument("-wmd", "--whole_metadata_file", default='wds_meta.txt', 
        help="output regression metadata file")
ap.add_argument("-smd", "--sws_metadata_file", default='sws_meta.txt', 
        help="output regression metadata file")
ap.add_argument("-mmd", "--mws_metadata_file", default='mws_meta.txt', 
        help="output regression metadata file")
ap.add_argument("-rmd", "--rod_metadata_file", default='rod_meta.txt', 
        help="output regression metadata file")
ap.add_argument("-nim", "--wholeds_noinverts_metadata", default='wds_ni_meta.txt', 
        help="output regression metadata file")
ap.add_argument("-cmd", "--class_metadata_file", default='class_meta.txt', 
        help="output classifier metadata file")
ap.add_argument("-cni", "--class_md_noinverts", default='class_noinverts_meta.txt', 
        help="output classifier metadata file")
args = vars(ap.parse_args())
wd_output = args["whole_dataset_file"]
sws_output = args["sws_dataset_file"]
mws_output = args["mws_dataset_file"]
rod_output = args["rod_dataset_file"]
wh_metadata = args["whole_metadata_file"]
sw_metadata = args["sws_metadata_file"]
mw_metadata = args["mws_metadata_file"]
rh_metadata = args["rod_metadata_file"]
wd_ni_output = args["whole_ds_noinverts"]
wd_ni_metadata = args["wholeds_noinverts_metadata"]
class_ni_metadata = args["class_md_noinverts"]
class_metadata = args["class_metadata_file"]
m = 0
s = 0
l = 0
r = 0
c = 0
acc_list = []
duped = 0

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database=input("Database Name: "),
  password=input("Password: ")
)
mycursor = mydb.cursor()

sql = "select DISTINCT o.genus,o.species,o.genefamily,o.accession,h.lamdamax, o.aa from opsins.opsins o, opsins.heterologous h WHERE (o.accession = h.accession AND o.refid = h.refid); "
mycursor.execute(sql)
myresult = mycursor.fetchall()


for x in myresult:       

  if (x[4] in range(340, 380)):
    opclass = 0
  
  elif (x[4] in range(380, 420)):
    opclass = 1 

  elif (x[4] in range(420, 460)):
    opclass = 2

  elif (x[4] in range(460, 500)):
    opclass = 3 

  elif (x[4] in range(500, 540)):
    opclass = 4  
  else:
    opclass = 5

  #Keep all accessions in a list -- don't print 
  if (x[3] in acc_list):
    #print ("\n\n\n****Accession Exists" + x[2] + "\n\n" )
    duped=1
  #First 2 of if statements ignore ancestral (pigment named) or mutated genes
  if (duped==1) :
    duped=0
  #do not print if contains the word "pigment" which is an ancestral sequence

  else :
       with open(wd_output, 'a') as f:
        m += 1 
        #This makes the fasta format file
        seq = ">S" + str(m)
        f.write(seq)
        seq2 = str('\n' + x[5] + '\n')
        f.write(seq2)

       with open(wd_ni_output, 'a') as f:
        p = re.compile('^Rtc|^BRh[0-3]|Pr[A-Z]')
        if p.match(x[2]):
          pass
        else:        
          c += 1 
          #This makes the fasta format file
          seq = ">S" + str(c)
          f.write(seq)
          seq2 = str('\n' + x[5] + '\n')
          f.write(seq2)

       with open(sws_output, 'a') as f:
        p = re.compile('^SWS|^UVS')
        if p.match(x[2]):
          s+=1
          if s == 1:
            f.write(">Bovine\nMNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAAYMFLLIMLGFPINFLTLYVTVQHKKLRTPLNYILLNLAVADLFMVFGGFTTTLYTSLHGYFVFGPTGCNLEGFFATLGGEIALWSLVVLAIERYVVVCKPMSNFRFGENHAIMGVAFTWVMALACAAPPLVGWSRYIPEGMQCSCGIDYYTPHEETNNESFVIYMFVVHFIIPLIVIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWLPYAGVAFYIFTHQGSDFGPIFMTIPAFFAKTSAVYNPVIYIMMNKQFRNCMVTTLCCGKNPLGDDEASTTVSKTETSQVAPA\n")  
        #This makes the fasta format file
          seq = ">S" + str(s)
          f.write(seq)
          seq2 = str('\n' + x[5] + '\n')
          f.write(seq2)

       with open(mws_output, 'a') as f:
        p = re.compile('^MWS|^LWS')
        if p.match(x[2]):
          l+=1
          if l == 1:
            f.write(">Bovine\nMNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAAYMFLLIMLGFPINFLTLYVTVQHKKLRTPLNYILLNLAVADLFMVFGGFTTTLYTSLHGYFVFGPTGCNLEGFFATLGGEIALWSLVVLAIERYVVVCKPMSNFRFGENHAIMGVAFTWVMALACAAPPLVGWSRYIPEGMQCSCGIDYYTPHEETNNESFVIYMFVVHFIIPLIVIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWLPYAGVAFYIFTHQGSDFGPIFMTIPAFFAKTSAVYNPVIYIMMNKQFRNCMVTTLCCGKNPLGDDEASTTVSKTETSQVAPA\n")
          #This makes the fasta format file
          seq = ">S" + str(l)
          f.write(seq)
          seq2 = str('\n' + x[5] + '\n')
          f.write(seq2)

       with open(rod_output, 'a') as f:
        p = re.compile('Rh[0-2]|exoRh')
        if p.match(x[2]):
          r+=1
          #This makes the fasta format file
          seq = ">S" + str(r)
          f.write(seq)
          seq2 = str('\n' + x[5] + '\n')
          f.write(seq2)


       with open(wh_metadata, 'a') as g:
        #This makes the metadata formatted for a linear regression model.
        if m == 1:
          g.write("\tLambda_Max\tSpecies\tOpsin_Family\tAccession\n")  
        md =  str("S" + str(m) + "\t" + str(x[4]).strip()) + "\t" + str(x[0]).strip().replace(' ','') + "_" + str(x[1]).strip().replace(' ','') + "\t" + str(x[2]).strip() + "\t" + x[3].strip() + "\n"
        g.write(md)

       with open(wd_ni_metadata, 'a') as g:
        p = re.compile('^Rtc|^BRh[0-3]|Pr[A-Z]')
        if p.match(x[2]):
          pass
        #This makes the metadata formatted for a linear regression model.
        else:
          if c == 1:
            g.write("\tLambda_Max\tSpecies\tOpsin_Family\tAccession\n")  
          md =  str("S" + str(c) + "\t" + str(x[4]).strip()) + "\t" + str(x[0]).strip().replace(' ','') + "_" + str(x[1]).strip().replace(' ','') + "\t" + str(x[2]).strip() + "\t" + x[3].strip() + "\n"
          g.write(md)

       with open(sw_metadata, 'a') as g:
        #This makes the metadata formatted for a linear regression model.
        p = re.compile('^SWS|^UVS')
        if p.match(x[2]):
          if s == 1:
            g.write("\tLambda_Max\tSpecies\tOpsin_Family\tAccession\n")
            g.write("Bovine\t500\tBos_tarus\tRh1\tNM_001014890\n")  
          md =  str("S" + str(s) + "\t" + str(x[4]).strip()) + "\t" + str(x[0]).strip().replace(' ','') + "_" + str(x[1]).strip().replace(' ','') + "\t" + str(x[2]).strip() + "\t" + x[3].strip() + "\n"
          g.write(md)

       with open(mw_metadata, 'a') as g:
        #This makes the metadata formatted for a linear regression model.
        p = re.compile('^MWS|^LWS')
        if p.match(x[2]):
          if l == 1:
            g.write("\tLambda_Max\tSpecies\tOpsin_Family\tAccession\n")  
            g.write("Bovine\t500\tBos_tarus\tRh1\tNM_001014890\n")  
          md =  str("S" + str(l) + "\t" + str(x[4]).strip()) + "\t" + str(x[0]).strip().replace(' ','') + "_" + str(x[1]).strip().replace(' ','') + "\t" + str(x[2]).strip() + "\t" + x[3].strip() + "\n"
          g.write(md)

       with open(rh_metadata, 'a') as g:
        #This makes the metadata formatted for a linear regression model.
        p = re.compile('Rh[0-3]|exoRh')
        if p.match(x[2]):
          if r == 1:
            g.write("\tLambda_Max\tSpecies\tOpsin_Family\tAccession\n")  
          md =  str("S" + str(r) + "\t" + str(x[4]).strip()) + "\t" + str(x[0]).strip().replace(' ','') + "_" + str(x[1]).strip().replace(' ','') + "\t" + str(x[2]).strip() + "\t" + x[3].strip() + "\n"
          g.write(md)

       with open(class_metadata, 'a') as h:
          #This makes the metadata formatted for a classification model. 
        if m == 1:
          h.write("\tOpsin_Class\n")  
        md = "S" + str(m) + "\t" + str(opclass) + "\n"
        h.write(md)

       with open(class_ni_metadata, 'a') as h:
        p = re.compile('^Rtc|^BRh[0-3]|Pr[A-Z]')
        if p.match(x[2]):
          pass
          #This makes the metadata formatted for a classification model. 
        else:
          if c == 1:
            h.write("\tOpsin_Class\n")  
          md = "S" + str(c) + "\t" + str(opclass) + "\n"
          h.write(md)