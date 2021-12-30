library(phytools)
library(phangorn)

#tree<-pbtree(n=100,scale=1)
#tree <- di2multi(tree)
x<-fastBM(tree, a=500, sig2=10)


X.full<-x
X.missing<-X.full
Nmis <- 2
sample(1:nrow(X.missing),7-Nmis)

xp<-sample(x,5)

fit<-anc.ML(tree,xp)
fit

tips<-sapply(names(fit$missing.x),function(x,y)
    which(y==x),y=tree$tip.label)

parents<-sapply(tips,Ancestors,x=tree,type="parent")
X<-rbind(fit$missing.x,fit$ace[as.character(parents)])
rownames(X)<-c("daughter","parent")
X

x.all<-c(xp,fit$missing.x,fit$ace)
tree<-paintBranches(tree,tips,"2")
phenogram(tree,x.all,fsize=0.3)
nodelabels(node=tips,pie=rep(1,length(fit$missing.x)),
    cex=0.5)   


#Small subtree
tree <- read.tree(text="('Pseudopleuronectes_americanus_AY631036.1_506.00000':0.095216,(('Sebastolobus_altivelis_DQ490124_483.00000':0.064897,('Dissostichus_mawsoni_DQ498794.1_504.00000':0.046174,'Pagothenia_borchgrevinki_DQ498791.1_499.00000':0.027617):0.090443):0.021312,('Cottocomephorus_inermis_U97266.1_494.00000':0.049939,('Batrachocottus_nikolskii_U97268.1_488.00000':0.042368,'Leocottus_kesslerii_L42953.1_516.00000':0.062089):0.038376):0.044061):0.010315);")



    
tree <- read.tree(text="((('Conger_myriaster_AB043817.1_486.00000':0.098867,('Gymnothorax_favagineus_HQ444181.1_488.00000':0.008474,('Rhinomuraena_quaesita_HQ444180.1_498.00000':0.0127,('Gymnothorax_reticularis_HQ444182.1_486.00000':0.019795,'Strophidon_sathete_HQ444183.1_487.00000':0.007619):0.002432):0.004029):2.0E-6):0.047045,('Anguilla_japonica_LC464070.1_479.00000':0.094033,('Amia_calva_AF137208.1_527.00000':0.094452,(('Latimeria_chalumnae_AH007712.2_482.00000':0.127979,('Acipenser_transmontanus_KC250344.1_540.00000':0.013241,'Neoceratodus_forsteri_EF526295.1_540.00000':0.074844):0.014714):0.025934,('Geotria_australis_AY366493.1_499.00000':0.228469,('Anolis_carolinensis_L31503_491.00000':0.147012,('Tachyglossus_aculeatus_JX103830_497.90000':0.048591,('Loxodonta_africana_AY686752.1_496.00000':0.039759,('Tursiops_truncatus_AF055456_488.00000':0.049859,('Bos_taurus_NM_001014890.2_500.00000':.01,'Bos_taurus_NM_001014890.2_498.00000':.01):0.061153):0.020583):0.038506):0.071825):0.021687):0.032219):0.080042):0.050794):0.040846):0.008589,((('Carassius_auratus_L11863.1_521.00000':.01,'Carassius_auratus_L11863.1_522.00000':.01):0.16785,('Astyanax_mexicanus_U12328.1_504.00000':0.092959,('Sardinops_melanostictus_LC007931.1_502.00000':0.020857,('Engraulis_mordax_KT201125.1_498.00000':0.014551,('Engraulis_encrasicolus_KT201123.1_500.00000':.01,'Engraulis_japonicus_AB731902.1_502.00000':0.003355):0.027946):0.085767):0.056064):0.0316):0.013511,((('Lepidopus_fitchi_EU407252.1_507.00000':0.063821,'Lepidopus_fitchi_EU407253.1_486.00000':0.123422):0.116737,(('Aristostomias_scintillans_EU407248.1_526.00000':0.185535,'Chauliodus_macouni_EU407250.1_489.00000':0.139364):0.089337,('Stenobrachius_leucopsarus_EU407251.1_492.00000':0.240941,('Oncorhynchus_keta_AY214141.1_524.00000':0.006644,('Oncorhynchus_kisutch_AY214146.1_531.00000':0.003317,'Oncorhynchus_tshawytscha_AY214136.1_524.00000':.01):2.0E-6):0.067404):0.038129):0.015344):0.039232,('Pomatoschistus_minutus_FN430594.1_508.00000':0.101279,(('Atherina_boyeri_JF309697.1_511.00000':0.046221,'Belone_belone_AY141268.1_509.00000':0.04826):0.025843,((('Myripristis_violacea_U57539.1_499.00000':0.013113,('Myripristis_berndti_U57538.1_495.00000':.01,'Myripristis_berndti_U57538.1_493.00000':.01):0.029878):0.058378,(('Sargocentron_microstoma_U57542.1_494.00000':0.015469,('Sargocentron_diadema_U57537.1_491.00000':0.00367,('Sargocentron_xantherythrum_U57546.1_490.00000':.01,'Sargocentron_xantherythrum_U57546.1_486.00000':.01):0.029034):0.003031):0.016879,(('Sargocentron_punctatissimum_U57543.1_494.00000':0.029133,('Neoniphon_sammara_U57536.1_502.00000':0.014195,'Neoniphon_argenteus_U57540.1_502.00000':3.0E-6):0.029558):0.008541,('Neoniphon_aurolineatus_U57541.1_481.00000':0.044694,('Sargocentron_spiniferum_U57544.1_490.00000':0.004593,'Sargocentron_tiere_U57545.1_490.00000':0.002436):0.047214):0.049226):0.01118):0.020403):0.063832,(('Pseudopleuronectes_americanus_AY631036.1_506.00000':0.095216,(('Sebastolobus_altivelis_DQ490124_483.00000':0.064897,('Dissostichus_mawsoni_DQ498794.1_504.00000':0.046174,'Pagothenia_borchgrevinki_DQ498791.1_499.00000':0.027617):0.090443):0.021312,('Cottocomephorus_inermis_U97266.1_494.00000':0.049939,('Batrachocottus_nikolskii_U97268.1_488.00000':0.042368,'Leocottus_kesslerii_L42953.1_516.00000':0.062089):0.038376):0.044061):0.010315):0.035496,('Ictalurus_punctatus_AF028016.1_542.00000':0.094847,('Acanthopagrus_butcheri_DQ354577.1_509.00000':0.044806,((('Dimidiochromis_compressiceps_AB084931.1_498.00000':.01,'Dimidiochromis_compressiceps_AB084931.1_502.00000':.01):7.27E-4,(('Diplotaxodon_macrops_AB185220.1_500.00000':0.00809,'Pallidochromis_tokolosh_AB185229.1_500.00000':2.0E-6):0.012055,(('Oreochromis_niloticus_AB084938.1_505.00000':0.04036,('Pseudotropheus_acei_GQ422475.1_505.00000':.01,('Pseudotropheus_acei_GQ422475.1_498.00000':0.0,('Melanochromis_vermivorus_GQ422472.1_505.00000':0.0,'Pseudotropheus_sp._GQ422475.1_498.00000':0.0):0.0):.01):3.0E-6):0.003726,('Tropheus_duboisi_AB084946.1_501.00000':2.0E-6,(('Pundamilia_pundamilia_AY673739.1_506.00000':0.003644,'Haplochromis_sp._AB084933.1_501.00000':3.0E-6):0.035297,('Tramitichromis_intermedius_GQ422473.1_505.00000':.01,('Tramitichromis_intermedius_GQ422473.1_506.00000':.01,'Labidochromis_caeruleus_AB084934.1_500.00000':.01):3.0E-6):0.003606):2.0E-6):0.010909):2.0E-6):0.007655):0.006162,(('Spathodus_erythrodon_AB084941.1_502.00000':0.007803,('Xenotilapia_ochrogenys_AB084947.1_503.00000':0.017575,('Altolamprologus_calvus_AB458132.1_498.00000':.01,'Altolamprologus_calvus_AB084924.1_499.00000':.01):0.014538):2.0E-6):0.007501,('Haplotaxodon_microlepis_AB458142.1_504.00000':0.007299,(('Xenotilapia_papilio_AB457996.1_497.00000':0.020937,(('Bathybates_fasciatus_AB185218.1_501.00000':0.006327,('Trematocara_unimaculatum_AB185238.1_484.00000':0.023755,'Trematocara_macrostoma_AB084945.1_488.00000':0.027526):0.025578):0.010252,('Baileychromis_centropomoides_AB185217.1_492.00000':0.016377,('Limnochromis_staneri_AB185225.1_498.00000':3.0E-6,('Gnathochromis_permaxillaris_AB084932.1_497.00000':0.012396,'Hemibates_stenosoma_AB185222.1_496.00000':0.03853):0.007997):0.004033):0.008121):2.37E-4):0.004031,((('Aulonocara_sp._AB185214.1_495.00000':0.012058,'Benthochromis_tricoti_AB084927.1_488.00000':0.016353):0.004115,('Neolamprologus_ventralis_AB458138.1_493.00000':0.017397,('Xenotilapia_nigrolabiata_AB458130.1_488.00000':0.00677,'Xenotilapia_caudafasciata_AB458131.1_491.00000':0.004409):0.022489):0.005134):0.003582,('Perissodus_elaviae_AB185230.1_490.00000':.01,('Greenwoodochromis_bellcrossi_AB185221.1_488.00000':0.012065,('Cyphotilapia_frontosa_AB084929.1_487.00000':.01,(('Paracyprichromis_brieni_AB458120.1_491.00000':0.018772,('Cyprichromis_leptosoma_AB084930.1_498.00000':.01,'Cyprichromis_leptosoma_AB458118.1_500.00000':.01):0.003716):0.010836,('Paracyprichromis_nigripinnis_AB458122.1_492.00000':0.014742,('Paracyprichromis_brieni_AB458121.1_494.00000':0.01093,'Cyprichromis_pavo_AB458119.1_489.00000':0.007175):0.004034):3.0E-6):0.00726):0.007225):0.007324):2.0E-6):0.003563):0.007243):0.007277):0.003663):0.043051):0.008541):0.014204):0.010267):0.006939):0.014206):0.04106):0.037163):0.07015);")
