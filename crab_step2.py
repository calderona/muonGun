from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'SingleMuFlatP5To2500_mc2017_pythia8_cfi_step2' 
config.General.workArea = 'crab_projects'


config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = 'muonGun_step2_newAlg.py'
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 10000


config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'SingleMuFlatP5To2500_mc2017_pythia8_cfi_step2'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/monoH-2017/muons' 
config.Data.publication = True
config.Data.inputDataset = '/MuonGun_PTOT-5-2500/calderon-SingleMuFlatP5To2500_pythia8_cfi_step1-1e44167951ea00f74cc60d4513a1a5f7/USER'

#'/MuonGun_PTOT-5-2500/calderon-SingleMuFlatP5To2500_pythia8_cfi_step1-1e44167951ea00f74cc60d4513a1a5f7/USER'
#'/SingleMuFlatP5To2500_pythia8_cfi/cprieels-SingleMuFlatP5To2500_pythia8_cfi_step1-1e44167951ea00f74cc60d4513a1a5f7/USER'


config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
config.Site.blacklist = ['T2_ES_IFCA']

#config.Site.storageSite = 'T2_ES_IFCA'
#config.Site.whitelist = ['T2_ES_IFCA'] 

config.section_("User")
#config.User.voGroup = "Spain"
