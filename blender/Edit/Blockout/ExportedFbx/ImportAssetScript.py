#This script was generated with the addons Blender for UnrealEngine : https://github.com/xavier150/Blender-For-UnrealEngine-Addons
#It will import into Unreal Engine all the assets of type StaticMesh, SkeletalMesh, Animation and Pose
#The script must be used in Unreal Engine Editor with UnrealEnginePython : https://github.com/20tab/UnrealEnginePython
#Use this command : unreal_engine.py_exec(r"C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\ImportAssetScript.py")

import os.path
import configparser
import ast
import unreal_engine as ue
from unreal_engine.classes import PyFbxFactory, StaticMesh, Skeleton, SkeletalMeshSocket
from unreal_engine.enums import EFBXImportType, EMaterialSearchLocation
from unreal_engine.structs import StaticMeshSourceModel, MeshBuildSettings
from unreal_engine import FVector, FRotator

#Prepare var and def
UnrealImportLocation = r'/Game/ImportedFbx'
ImportedAsset = []

def GetOptionByIniFile(FileLoc, OptionName, literal = False):
	Config = configparser.ConfigParser()
	Config.read(FileLoc)
	Options = []
	for option in Config.options(OptionName):
		if (literal == True):
			Options.append(ast.literal_eval(Config.get(OptionName, option)))
		else:
			Options.append(Config.get(OptionName, option))
	return Options


#Process import
print('========================= Import started ! =========================')



################[ Import Cube_MaterialTest_1x1x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_MaterialTest_1x1x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_MaterialTest_1x1x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Cube_MaterialTest_1x1x1" ')



################[ Import Platform_Basic_1x1x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Platform_Basic_1x1x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Platform_Basic_1x1x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Platform_Basic_1x1x1" ')



################[ Import Ramp_basic_2x1x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_2x1x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_2x1x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Ramp_basic_2x1x1" ')



################[ Import Ramp_basic_3x1x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_3x1x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_3x1x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Ramp_basic_3x1x1" ')



################[ Import Ramp_basic_1x1x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_1x1x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_1x1x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Ramp_basic_1x1x1" ')



################[ Import Ramp_basic_4x1x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_4x1x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_4x1x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Ramp_basic_4x1x1" ')



################[ Import Ramp_basic_2x1x2 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_2x1x2.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_2x1x2_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Ramp_basic_2x1x2" ')



################[ Import Ramp_basic_3x1x2 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_3x1x2.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_3x1x2_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Ramp_basic_3x1x2" ')



################[ Import Ramp_basic_1x1x2 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_1x1x2.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_1x1x2_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Ramp_basic_1x1x2" ')



################[ Import Ramp_basic_4x1x2 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_4x1x2.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Ramp_basic_4x1x2_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Ramp_basic_4x1x2" ')



################[ Import Cube_Basic_1x1x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_Basic_1x1x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_Basic_1x1x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Cube_Basic_1x1x1" ')



################[ Import Cube_Basic_3x3x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_Basic_3x3x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_Basic_3x3x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Cube_Basic_3x3x1" ')



################[ Import Cube_Basic_4x2x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_Basic_4x2x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_Basic_4x2x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Cube_Basic_4x2x1" ')



################[ Import Cube_CornerRound_Basic_1x1x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_CornerRound_Basic_1x1x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_CornerRound_Basic_1x1x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Cube_CornerRound_Basic_1x1x1" ')



################[ Import Platform_Basic_3x1x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Platform_Basic_3x1x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Platform_Basic_3x1x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Platform_Basic_3x1x1" ')



################[ Import Cube_CornerRound_Basic_2x2x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_CornerRound_Basic_2x2x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Cube_CornerRound_Basic_2x2x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Cube_CornerRound_Basic_2x2x1" ')



################[ Import Platform_CornerRound_Basic_1x1x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Platform_CornerRound_Basic_1x1x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Platform_CornerRound_Basic_1x1x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Platform_CornerRound_Basic_1x1x1" ')



################[ Import Platform_Basic_2x2x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Platform_Basic_2x2x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Platform_Basic_2x2x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Platform_Basic_2x2x1" ')



################[ Import Platform_CornerSharp_Basic_1x1x1 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Platform_CornerSharp_Basic_1x1x1.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Platform_CornerSharp_Basic_1x1x1_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Platform_CornerSharp_Basic_1x1x1" ')



################[ Import Basic_StairCase_Special as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Basic_StairCase_Special.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Basic_StairCase_Special_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Basic_StairCase_Special" ')



################[ Import Character_Pig_01 as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Character_Pig_01.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Character_Pig_01_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Character_Pig_01" ')



################[ Import Coin_M as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Coin_M.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Coin_M_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Coin_M" ')



################[ Import Coin_XS as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Coin_XS.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Coin_XS_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Coin_XS" ')



################[ Import Coin_L as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Coin_L.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Coin_L_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Coin_L" ')



################[ Import Coin_S as StaticMesh type ]################
fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = True
fbx_factory.ImportUI.bImportTextures = False
fbx_factory.ImportUI.TextureImportData.MaterialSearchLocation = EMaterialSearchLocation.Local
fbx_factory.ImportUI.StaticMeshImportData.bCombineMeshes = True
fbx_factory.ImportUI.StaticMeshImportData.bAutoGenerateCollision = True
FbxLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Coin_S.fbx')
AdditionalParameterLoc = os.path.join(r'C:\Users\jssou\Documents\Gay Jam\LudumDare44\blender\Edit\Blockout\ExportedFbx\StaticMesh\SM_Coin_S_AdditionalParameter.ini')
AssetImportLocation = (os.path.join(UnrealImportLocation, r'').replace('\\','/')).rstrip('/')
try:
	asset = fbx_factory.factory_import_object(FbxLoc, AssetImportLocation)
	lods_to_add = GetOptionByIniFile(AdditionalParameterLoc, 'LevelOfDetail')
	for x, lod in enumerate(lods_to_add):
		asset.static_mesh_import_lod(lod, x+1)
	asset.save_package()
	asset.post_edit_change()
	ImportedAsset.append(asset)
except:
	ImportedAsset.append('Import error for asset named "Coin_S" ')



print('========================= Imports completed ! =========================')

for asset in ImportedAsset:
	print(asset)

print('=========================')
