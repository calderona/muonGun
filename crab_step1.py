from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'SingleMuFlatP5To2500_pythia8_cfi_step1' 
config.General.workArea = 'crab_projects'



config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = 'muonGun_step1.py'
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 5000


config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'SingleMuFlatP5To2500_pythia8_cfi_step1'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/monoH-2017/muons' 
config.Data.publication = True
config.Data.inputDataset = '/MuonGun_PTOT-5-2500/abbiendi-crab_MuonGun_step1_mem25-c2f8040234c0cadd94e4b6dadcde8031/USER'
#'/SingleMuFlatP5To2500_pythia8_cfi/cprieels-SingleMuFlatP5To2500_pythia8_cfi-cede80ba020c227dbe5094019354f986/USER'


config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
config.Site.blacklist = ['T2_ES_IFCA']

#config.section_("User")
#config.User.voGroup = "Spain"
