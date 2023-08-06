import makana

# Get Framworks
modelFramworks = makana.MakanaModel.getModelFramworks()

# # Register MakanaModel
makanaModel = makana.MakanaModel.registerModel("Test Model Dev1","Test Model Dev1", modelFramworks[0]['id'],
                                 modelFramworks[0]['name'], 1.0 ,"sentiment.h5","Y:\Working\Makana\Models\sentiment.h5")

# Get All MakanaModels
makanaModels = makana.MakanaModel.getMakanaModel()

# Get MakanaModel By Id
# makanaModel = makana.MakanaModel.getMakanaModel(model['id'])


makanaService = makana.MakanaService.registerModelService("Test Service Dev1","Test Service Dev1",makanaModel['id'],
                                 "main.py","requirements.txt","Y:\Working\Makana\Models\main.py","Y:\Working\Makana\Models\requirements.txt")

# Get All MakanaServices
makanaServices = makana.MakanaService.getMakanaServices()

# Get MakanaService By Id
# makanaModel = makana.MakanaService.getMakanaService(makanaService['id'])
