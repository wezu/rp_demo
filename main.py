
from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
import sys


class World(ShowBase):

    def __init__(self):


        pipeline_path = "../../"
        # pipeline_path = "../../RenderPipeline/"

        # -- Begin of render pipeline code --
        sys.path.insert(0, pipeline_path)
        from __init__ import RenderPipeline
        from __init__ import PointLight
        
        self.render_pipeline = RenderPipeline(self)
        self.render_pipeline.set_default_loading_screen()

        # Mount the directories, this mounts the base path of the pipeline so
        # we don't have to speficy relative paths all the time
        self.render_pipeline.get_mount_manager().mount()

        # Load the default settings
        self.render_pipeline.load_settings("Config/pipeline.yaml")

        # Create the pipeline
        self.render_pipeline.create()
        #self.render_pipeline.create_default_skybox()

        my_light = PointLight()
        my_light.set_pos(Vec3(1.0, 0.5, 5.0))
        my_light.set_radius(10.0)
        self.render_pipeline.add_light(my_light)

        self.tile=loader.loadModel("tile0") 
        self.tile.reparentTo(render)
        

w = World().run()

