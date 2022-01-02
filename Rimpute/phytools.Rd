library(phytools)
library(phangorn)

setwd("~/Documents/GitHub/vizphiz/Rimpute/")
read.csv(file="rh1_ymax.csv", row.names=1, header=FALSE) -> ymax

x <-svl<-as.matrix(ymax)[,1]

leaveout <- 10
all <- c() # initialize for imputed results
for(i in 1:20) {
    xp <- as.matrix(x)
    xp[cbind(sample(1:nrow(as.matrix(xp)), leaveout), sample(1,leaveout,replace=TRUE))]<-NA
    xp
    xpt <- as.matrix(xp)[,1]
    xpt

    fit<-anc.ML(tree,na.omit(xpt))
    fit

    impute <- as.matrix(fit$missing.x)
    #find row for missing data to obtain actual data
    as.matrix(x[which(is.na(xp))]) -> actual
    cbind(actual[,1], impute[,1])->rep
    print(rep)
    all <- rbind(all,rep)
}


plot(all[,1], all[,2], ,pch=21,bg="grey",cex=1.5,
    xlab="true values of rod lambda max",ylab="imputed values using phylo.impute",asp=1)



phenogram(tree,x,fsize=0.3)
nodelabels(node=tips,pie=rep(1,length(fit$missing.x)),
    cex=0.5)   

contMap(tree,x,plot=TRUE, plot.tip.labels=FALSE,fsize=.5)


tree <- read.tree(text="(('Anolis_carolinensis_L31503_491.00000':0.147541,('Tachyglossus_aculeatus_JX103830_497.90000':0.048767,('Loxodonta_africana_AY686752.1_496.00000':0.039911,('Bos_taurus_NM_001014890.2_500.00000':0.061422,'Tursiops_truncatus_AF055456_488.00000':0.050037):0.020666):0.038656):0.072194):0.010872,('Geotria_australis_AY366493.1_499.00000':0.229272,(('Latimeria_chalumnae_AH007712.2_482.00000':0.128562,('Acipenser_transmontanus_KC250344.1_540.00000':0.01333,'Neoceratodus_forsteri_EF526295.1_540.00000':0.075123):0.014794):0.026042,('Amia_calva_AF137208.1_527.00000':0.095183,('Anguilla_japonica_LC464070.1_479.00000':0.09439,(('Conger_myriaster_AB043817.1_486.00000':0.099299,('Gymnothorax_favagineus_HQ444181.1_488.00000':0.008511,('Rhinomuraena_quaesita_HQ444180.1_498.00000':0.012763,('Gymnothorax_reticularis_HQ444182.1_486.00000':0.019894,'Strophidon_sathete_HQ444183.1_487.00000':0.007655):0.002442):0.00405):2.0E-6):0.047261,(('Carassius_auratus_L11863.1_521.00000':0.168531,('Astyanax_mexicanus_U12328.1_504.00000':0.093314,('Sardinops_melanostictus_LC007931.1_502.00000':0.020955,('Engraulis_mordax_KT201125.1_498.00000':0.014638,('Engraulis_encrasicolus_KT201123.1_500.00000':1.0E-6,'Engraulis_japonicus_AB731902.1_502.00000':0.003368):0.028054):0.086102):0.056387):0.031694):0.013538,((('Lepidopus_fitchi_EU407252.1_507.00000':0.064089,'Lepidopus_fitchi_EU407253.1_486.00000':0.123909):0.117159,(('Aristostomias_scintillans_EU407248.1_526.00000':0.186114,'Chauliodus_macouni_EU407250.1_489.00000':0.139895):0.089621,('Stenobrachius_leucopsarus_EU407251.1_492.00000':0.241699,('Oncorhynchus_keta_AY214141.1_524.00000':0.006672,('Oncorhynchus_kisutch_AY214146.1_531.00000':0.00333,'Oncorhynchus_tshawytscha_AY214136.1_524.00000':1.0E-6):2.0E-6):0.067584):0.038426):0.015441):0.039348,('Pomatoschistus_minutus_FN430594.1_508.00000':0.101607,(('Atherina_boyeri_JF309697.1_511.00000':0.046482,'Belone_belone_AY141268.1_509.00000':0.048519):0.025992,((('Myripristis_berndti_U57538.1_495.00000':0.029988,'Myripristis_violacea_U57539.1_499.00000':0.013169):0.058559,(('Sargocentron_microstoma_U57542.1_494.00000':0.01553,('Sargocentron_xantherythrum_U57546.1_490.00000':0.029146,'Sargocentron_diadema_U57537.1_491.00000':0.003685):0.003041):0.016926,(('Sargocentron_punctatissimum_U57543.1_494.00000':0.029227,('Neoniphon_sammara_U57536.1_502.00000':0.014249,'Neoniphon_argenteus_U57540.1_502.00000':2.0E-6):0.029682):0.008566,('Neoniphon_aurolineatus_U57541.1_481.00000':0.044759,('Sargocentron_spiniferum_U57544.1_490.00000':0.004702,'Sargocentron_tiere_U57545.1_490.00000':0.002374):0.047397):0.04954):0.01123):0.02056):0.064,(('Pseudopleuronectes_americanus_AY631036.1_506.00000':0.095569,(('Sebastolobus_altivelis_DQ490124_483.00000':0.065171,('Dissostichus_mawsoni_DQ498794.1_504.00000':0.046482,'Pagothenia_borchgrevinki_DQ498791.1_499.00000':0.027728):0.091037):0.021362,('Cottocomephorus_inermis_U97266.1_494.00000':0.050187,('Batrachocottus_nikolskii_U97268.1_488.00000':0.042544,'Leocottus_kesslerii_L42953.1_516.00000':0.062362):0.038524):0.044221):0.010358):0.035619,('Ictalurus_punctatus_AF028016.1_542.00000':0.095235,('Acanthopagrus_butcheri_DQ354577.1_509.00000':0.045117,(('Dimidiochromis_compressiceps_AB084931.1_498.00000':7.3E-4,(('Diplotaxodon_macrops_AB185220.1_500.00000':0.008119,'Pallidochromis_tokolosh_AB185229.1_500.00000':2.0E-6):0.012099,(('Oreochromis_niloticus_AB084938.1_505.00000':0.040502,('Melanochromis_vermivorus_GQ422472.1_505.00000':1.0E-6,'Pseudotropheus_acei_GQ422475.1_505.00000':3.0E-6):3.0E-6):0.003741,('Tropheus_duboisi_AB084946.1_501.00000':3.0E-6,(('Pundamilia_pundamilia_AY673739.1_506.00000':0.003659,'Haplochromis_sp._AB084933.1_501.00000':2.0E-6):0.035444,('Tramitichromis_intermedius_GQ422473.1_505.00000':1.0E-6,'Labidochromis_caeruleus_AB084934.1_500.00000':1.0E-6):0.003621):3.0E-6):0.010953):2.0E-6):0.007684):0.006184,(('Spathodus_erythrodon_AB084941.1_502.00000':0.007831,('Xenotilapia_ochrogenys_AB084947.1_503.00000':0.017639,('Altolamprologus_calvus_AB458132.1_498.00000':1.0E-6,'Altolamprologus_calvus_AB084924.1_499.00000':1.0E-6):0.014598):1.0E-6):0.007531,('Haplotaxodon_microlepis_AB458142.1_504.00000':0.007328,((('Aulonocara_sp._AB185214.1_495.00000':0.012195,('Xenotilapia_papilio_AB457996.1_497.00000':3.0E-6,('Xenotilapia_nigrolabiata_AB458130.1_488.00000':3.0E-6,'Xenotilapia_caudafasciata_AB458131.1_491.00000':0.011319):0.026596):0.015162):2.0E-6,(('Bathybates_fasciatus_AB185218.1_501.00000':0.006347,('Trematocara_unimaculatum_AB185238.1_484.00000':0.02382,'Trematocara_macrostoma_AB084945.1_488.00000':0.027628):0.025672):0.010313,('Baileychromis_centropomoides_AB185217.1_492.00000':0.016438,('Limnochromis_staneri_AB185225.1_498.00000':1.0E-6,('Gnathochromis_permaxillaris_AB084932.1_497.00000':0.01244,'Hemibates_stenosoma_AB185222.1_496.00000':0.038673):0.008029):0.004047):0.008227):0.003985):0.00367,('Perissodus_elaviae_AB185230.1_490.00000':1.0E-6,(('Benthochromis_tricoti_AB084927.1_488.00000':0.021199,'Neolamprologus_ventralis_AB458138.1_493.00000':0.023361):0.003031,('Greenwoodochromis_bellcrossi_AB185221.1_488.00000':0.012108,('Cyphotilapia_frontosa_AB084929.1_487.00000':3.0E-6,(('Paracyprichromis_brieni_AB458120.1_491.00000':0.018846,('Cyprichromis_leptosoma_AB084930.1_498.00000':1.0E-6,'Cyprichromis_leptosoma_AB458118.1_500.00000':1.0E-6):0.00373):0.01088,('Paracyprichromis_nigripinnis_AB458122.1_492.00000':0.014802,('Paracyprichromis_brieni_AB458121.1_494.00000':0.010972,'Cyprichromis_pavo_AB458119.1_489.00000':0.007206):0.004047):2.0E-6):0.007288):0.007253):0.007353):2.0E-6):0.003587):0.007275):0.007305):0.003684):0.043194):0.008562):0.014295):0.010303):0.006971):0.01423):0.041213):0.037287):0.079127):0.040986):0.050898):0.080333):0.032287):0.010872);")
