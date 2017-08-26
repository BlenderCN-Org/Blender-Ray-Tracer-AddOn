import bpy
from extensions_framework import Addon

bl_info = {
	"name" : "SPT",
	"description" : "A toy path tracing physically based render",
	"author" : "alianpaul",
	"version" : (0, 0, 1),
	"category" : "Render"
}

#Addon has a addon_register_class(self, cls), this will work as a decorator
#to keep track of the registered classes of this SPT addon.
#
SPTAddon = Addon(bl_info)
addon_register, addon_unregister = SPTAddon.init_functions()


#Class registration(loading its classes into Blender), setting up data for our addon.
#this will not rerun when a new blend file is loaded.

#Class registration:
#Class definition being loaded into Blender, where it becomes available alongside 
#existing functionality,Once this class is loaded you can access it from bpy.types, 
#using the bl_idname rather than the classes original name.

#When there are many classes or a packages submodule has its own classes it can be tedious
#to list them all for registration.
#For more convenient loading/unloading bpy.utils.register_module (module) and bpy.utils.unregister_module (module) functions exist.

#?if bpy.utils.register_module can register all the registerable classs in the module
#Why do we need SPTAddon.

def register():
	addon_register()

	bpy.utils.register_module(__name__)


def unregister():
	addon_unregister()

	bpy.utils.register_module(__name__)


